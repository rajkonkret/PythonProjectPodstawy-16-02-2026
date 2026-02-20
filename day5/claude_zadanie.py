from enum import Enum


class SystemType(Enum):
    CONSOLE = "console"
    EMAIL = "email"


class ErrorLevel(Enum):
    ERROR = "error"
    MEDIUM = "medium"
    UNKNOWN = "unknown"

    @classmethod
    def from_string(cls, value: str) -> "ErrorLevel":
        try:
            return cls(value)
        except ValueError:
            return cls.UNKNOWN


ERROR_LEVEL_TRANSLATIONS = {
    ErrorLevel.ERROR: "Krytyczny",
    ErrorLevel.MEDIUM: "Średni",
    ErrorLevel.UNKNOWN: "Nieznany",
}


class LogEntry:
    def __init__(self, level: ErrorLevel, message: str):
        self.level = level
        self.message = message
        self.translated_level = ERROR_LEVEL_TRANSLATIONS[level]

    def __repr__(self) -> str:
        return f"LogEntry(level={self.translated_level}, message={self.message!r})"


class LogCollector:
    def __init__(self):
        self.entries: list[LogEntry] = []

    def process(self, system_type: SystemType, level: str = None, message: str = None) -> None:
        match system_type:
            case SystemType.CONSOLE:
                print("Stało się coś strasznego")
            case SystemType.EMAIL:
                self._handle_email(level, message)
            case _:
                print(f"Unknown system type: {system_type}")

    def _handle_email(self, level: str | None, message: str | None) -> None:
        print("System email")
        if level and message:
            error_level = ErrorLevel.from_string(level)
            entry = LogEntry(level=error_level, message=message)
            self.entries.append(entry)
            print(f"Added log entry: {entry}")

    def summary(self) -> None:
        if not self.entries:
            print("No log entries collected.")
            return
        for i, entry in enumerate(self.entries, 1):
            print(f"{i}. Level: {entry.translated_level}, Message: {entry.message}")


def main():
    print("=== Log Collection System Simulation ===\n")

    collector = LogCollector()

    print("1. Console system test:")
    collector.process(SystemType.CONSOLE)

    print("\n2. Email system — error level:")
    collector.process(SystemType.EMAIL, "error", "Database connection failed")

    print("\n3. Email system — medium level:")
    collector.process(SystemType.EMAIL, "medium", "Slow API queries")

    print("\n4. Email system — unknown level:")
    collector.process(SystemType.EMAIL, "warning", "Unexpected system behaviour")

    print("\n=== Collected log entries ===")
    collector.summary()


if __name__ == "__main__":
    main()
