import pytest

from day5.claude_zadanie import ErrorLevel, LogCollector, SystemType


def test_error_level_from_string_known_value():
    assert ErrorLevel.from_string("error") is ErrorLevel.ERROR
    assert ErrorLevel.from_string("medium") is ErrorLevel.MEDIUM


def test_error_level_from_string_unknown_value():
    assert ErrorLevel.from_string("warning") is ErrorLevel.UNKNOWN


def test_log_collector_console_does_not_store_entries(capsys: pytest.CaptureFixture[str]):
    collector = LogCollector()
    collector.process(SystemType.CONSOLE)
    captured = capsys.readouterr()
    assert "Stało się coś strasznego" in captured.out
    assert collector.entries == []


def test_log_collector_email_adds_entry_and_translates_level(capsys: pytest.CaptureFixture[str]):
    collector = LogCollector()
    collector.process(SystemType.EMAIL, "error", "Database connection failed")
    captured = capsys.readouterr()
    assert "System email" in captured.out
    assert len(collector.entries) == 1
    entry = collector.entries[0]
    assert entry.level is ErrorLevel.ERROR
    assert entry.translated_level == "Krytyczny"
    assert entry.message == "Database connection failed"


def test_log_collector_email_unknown_level_marked_unknown(capsys: pytest.CaptureFixture[str]):
    collector = LogCollector()
    collector.process(SystemType.EMAIL, "warning", "Unexpected system behaviour")
    capsys.readouterr()  # clear prints
    assert len(collector.entries) == 1
    entry = collector.entries[0]
    assert entry.level is ErrorLevel.UNKNOWN
    assert entry.translated_level == "Nieznany"
    assert entry.message == "Unexpected system behaviour"
