"""
Menu module.

This module stores the available menu items and provides
functions to retrieve and search menu items.
"""

MENU_ITEMS = {
    "Margherita Pizza": 35.00,
    "Pepperoni Pizza": 42.00,
    "Chicken Pizza": 40.00,
    "Cheese Pizza": 38.00,
    "Coca-Cola": 8.00,
    "Orange Juice": 10.00,
}

MENU_ALIASES = {
    "pepperoni": "Pepperoni Pizza",
    "margherita": "Margherita Pizza",
    "chicken": "Chicken Pizza",
    "cheese": "Cheese Pizza",
    "coke": "Coca-Cola",
    "cola": "Coca-Cola",
    "juice": "Orange Juice",
}


def get_menu() -> dict:
    """
    Return the available menu items.
    """
    return MENU_ITEMS


def format_menu() -> str:
    """
    Return the menu formatted as a string.
    """

    menu_lines = ["🍕 MENU", "-" * 20]

    for item, price in MENU_ITEMS.items():
        menu_lines.append(f"- {item}: ${price:.2f}")

    return "\n".join(menu_lines)


def find_menu_item(message: str) -> str | None:
    """
    Find a menu item mentioned in the user's message.

    Args:
        message (str):
            User input.

    Returns:
        str | None:
            The menu item if found, otherwise None.
    """

    message = message.lower()

    # Check aliases first
    for alias, item in MENU_ALIASES.items():
        if alias in message:
            return item

    # Check full menu item names
    for item in MENU_ITEMS:
        if item.lower() in message:
            return item

    return None
