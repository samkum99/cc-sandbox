#!/usr/bin/env python3
"""A simple script that prints a friendly greeting."""


def greet(name="there"):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Hope you're having a great day."


def main():
    print(greet())


if __name__ == "__main__":
    main()
