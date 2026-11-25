"""Entrypoint: print the one-line Solana wallet agent slogan."""

from pathlib import Path


def load_slogan() -> str:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    lines = entry_path.read_text(encoding="utf-8").splitlines()
    cleaned = [line.strip() for line in lines if line.strip()]
    return " ".join(cleaned)


def deliver(slogan: str) -> None:
    print(slogan)


def main() -> None:
    deliver(load_slogan())


if __name__ == "__main__":
    main()
