"""
NBP API client (simple)

Provides:
- fetch(endpoint, timeout=5.0)
- get_rate(currency, table='A') -> Decimal
- get_rates_table(table='A') -> dict[str, Decimal]

Falls back to urllib if `requests` is not installed.
"""
from __future__ import annotations

import json
import logging
import sys
import time
from decimal import Decimal, InvalidOperation
from typing import Dict, Optional

BASE = "https://api.nbp.pl"
DEFAULT_TIMEOUT = 5.0

# try to use requests, otherwise fallback to urllib
try:
    import requests  # type: ignore

    _HAS_REQUESTS = True
except Exception:
    _HAS_REQUESTS = False
    import urllib.request as _urllib_request
    import urllib.error as _urllib_error

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class NBPError(Exception):
    pass


def fetch(endpoint: str, timeout: float = DEFAULT_TIMEOUT, retries: int = 1) -> dict:
    """Fetch JSON from NBP API. Endpoint may start with or without leading '/'.

    Raises NBPError on HTTP or parsing problems, TimeoutError on timeouts.
    """
    if not endpoint.startswith("/"):
        endpoint = "/" + endpoint
    url = BASE + endpoint
    headers = {"Accept": "application/json"}

    last_exc: Optional[Exception] = None
    for attempt in range(retries + 1):
        try:
            if _HAS_REQUESTS:
                resp = requests.get(url, headers=headers, timeout=timeout)
                resp.raise_for_status()
                return resp.json()
            else:
                req = _urllib_request.Request(url, headers=headers)
                with _urllib_request.urlopen(req, timeout=timeout) as r:
                    status = getattr(r, "status", None)
                    if status is not None and status >= 400:
                        raise NBPError(f"HTTP {status} for {url}")
                    raw = r.read()
                    return json.loads(raw.decode("utf-8"))
        except Exception as e:
            last_exc = e
            logger.debug("fetch attempt %d failed: %s", attempt + 1, e)
            # simple retry for transient network errors
            if attempt < retries:
                time.sleep(0.2 * (attempt + 1))
                continue
            # different exception translation
            if isinstance(e, TimeoutError) or (hasattr(e, "reason") and isinstance(e.reason, TimeoutError)):
                raise TimeoutError(f"Timeout fetching {url}") from e
            if isinstance(e, _urllib_error.HTTPError) if not _HAS_REQUESTS else False:
                raise NBPError(str(e)) from e
            if _HAS_REQUESTS and isinstance(e, requests.HTTPError):
                raise NBPError(str(e)) from e
            # JSON decode or other
            raise NBPError(f"Failed to fetch {url}: {e}") from e


def _to_decimal(value) -> Decimal:
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise NBPError(f"Invalid numeric value: {value}") from e


def get_rate(currency: str, table: str = "A") -> Decimal:
    """Return the latest 'mid' rate for the currency from the given table.

    Raises NBPError if currency/table not found.
    """
    endpoint = f"/api/exchangerates/rates/{table}/{currency}/"
    data = fetch(endpoint)
    # expected structure: { "table": "A", "currency": "dolar amerykański", "code": "USD", "rates": [ { "no": "...", "effectiveDate": "YYYY-MM-DD", "mid":  ... } ] }
    try:
        rates = data.get("rates")
        if not rates:
            raise NBPError(f"No rates found for {currency} in table {table}")
        rate_entry = rates[0]
        # prefer 'mid' (tables A/B), fallback to 'ask'/'bid' if present
        for key in ("mid", "ask", "bid"):
            if key in rate_entry:
                return _to_decimal(rate_entry[key])
        raise NBPError("No numeric rate field found in response")
    except (KeyError, IndexError, TypeError) as e:
        raise NBPError(f"Unexpected response format: {e}") from e


def get_rates_table(table: str = "A") -> Dict[str, Decimal]:
    """Return a dict mapping currency code -> Decimal(rate) for the given table.

    Uses endpoint /api/exchangerates/tables/{table}/ which returns a list with one table object.
    """
    endpoint = f"/api/exchangerates/tables/{table}/"
    data = fetch(endpoint)
    # response: [ { "table": "A", "no": "...", "tradingDate": "...", "effectiveDate": "...", "rates": [ {"currency":"...","code":"USD","mid":...}, ... ] }]
    try:
        if not isinstance(data, list) or not data:
            raise NBPError("Unexpected table response")
        table_obj = data[0]
        out: Dict[str, Decimal] = {}
        for r in table_obj.get("rates", []):
            code = r.get("code")
            if not code:
                continue
            # prefer mid then ask/bid
            val = r.get("mid") if "mid" in r else (r.get("ask") or r.get("bid"))
            if val is None:
                continue
            out[code] = _to_decimal(val)
        return out
    except (KeyError, TypeError) as e:
        raise NBPError(f"Unexpected response format: {e}") from e


if __name__ == "__main__":
    # quick smoke test when running the module directly
    try:
        print("NBP client smoke test")
        usd = get_rate("USD")
        eur = get_rate("EUR")
        print(f"USD -> {usd} PLN")
        print(f"EUR -> {eur} PLN")
        print("First 5 entries from table A:")
        table = get_rates_table("A")
        count = 0
        for k, v in table.items():
            print(f"  {k}: {v}")
            count += 1
            if count >= 5:
                break
        sys.exit(0)
    except Exception as e:
        logger.error("Error during smoke test: %s", e)
        sys.exit(2)
