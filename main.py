#!/usr/bin/env python3
"""
Simple greeting application.
Prompts the user for their name and prints a personalized greeting.
"""


def main() -> None:
    """Entry point of the application."""
    print("Welcome to the Greeting App!")
    name = input("Please enter your name: ").strip()
    if not name:
        name = "World"
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()