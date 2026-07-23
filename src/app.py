"""
Main application entry point.

This module starts the Delivery Workflow Simulator
and handles user interaction.
"""

from workflow_engine import process_message
from constants import GOODBYE_MESSAGE


def main() -> None:
    """
    Start the Delivery Workflow Simulator.
    """

    print("=" * 50)
    print("Delivery Workflow Simulator")
    print("=" * 50)

    while True:
        user_message = input("\nYou: ").strip()

        if not user_message:
            print("\nAssistant: Please type a message.")
            continue

        response = process_message(user_message)

        print(f"\nAssistant:\n{response}")

        if response == GOODBYE_MESSAGE:
            break


if __name__ == "__main__":
    main()
    