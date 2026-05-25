"""Intentionally vulnerable example for CodeQL training.

This file is isolated from the main application and exists only to
demonstrate how CodeQL detects command-injection risks in Python.
Do not reuse this pattern in production code.
"""

import subprocess


def run_demo_command(user_supplied_text: str) -> str:
    """Run a deliberately unsafe shell command for security training."""
    completed = subprocess.run(
        f"echo Demo output: {user_supplied_text}",
        shell=True,
        check=False,
        capture_output=True,
        text=True,
    )
    return completed.stdout


if __name__ == "__main__":
    payload = input("Enter demo text: ")
    print(run_demo_command(payload))
