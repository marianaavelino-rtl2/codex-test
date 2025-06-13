"""Simple greeting script with an optional name argument."""

import argparse


def greet(name: str) -> str:
    """Return a greeting for the provided name."""
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> None:
    """Parse arguments and print the greeting."""
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument(
        "--name",
        default="world",
        help="Name to greet",
    )
    args = parser.parse_args(argv)
    print(greet(args.name))


if __name__ == "__main__":
    main()
