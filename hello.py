#!/usr/bin/env python3
"""A simple script that prints a friendly greeting."""

import argparse
import os
import shutil

RESET      = "\033[0m"
BOLD       = "\033[1m"
DARK_BG    = "\033[40m"
LIGHT_TEXT = "\033[97m"
CYAN       = "\033[96m"


def greet(name="there"):
    return f"Hello, {CYAN}{name}{LIGHT_TEXT}! Hope you're having a great day."


def main():
    parser = argparse.ArgumentParser(description="Print a full-screen greeting.")
    parser.add_argument("--name", default="there", help="Name to greet")
    args = parser.parse_args()

    cols, rows = shutil.get_terminal_size()

    # Clear screen and set black background across entire terminal
    print("\033[2J\033[H", end="")          # clear screen, move cursor to top
    print(f"\033[40m\033[97m\033[1m", end="")  # dark bg + bright white bold

    # Fill every line with spaces to paint the background
    blank = " " * cols
    for _ in range(rows):
        print(blank)

    # Print greeting centered vertically and horizontally
    msg = greet(args.name)
    row = rows // 2
    col = (cols - len(msg)) // 2
    print(f"\033[{row};{col}H{msg}", end="", flush=True)

    # Move cursor to bottom after
    print(f"\033[{rows};0H{RESET}", flush=True)


if __name__ == "__main__":
    main()
