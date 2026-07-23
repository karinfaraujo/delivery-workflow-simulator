"""
Workflow engine.

This module orchestrates the application flow by routing
the user's request to the appropriate module.
"""

from constants import (
    SHOW_MENU,
    CREATE_ORDER,
    CHECK_ORDER,
    CANCEL_ORDER,
    GREETING,
    EXIT,
    WELCOME_MESSAGE,
    GOODBYE_MESSAGE,
    UNKNOWN_MESSAGE,
    ORDER_NOT_FOUND_MESSAGE,
    ORDER_CANCELED_MESSAGE,
    MENU_ITEM_NOT_FOUND_MESSAGE,
)

from intent import detect_intent
from menu import format_menu, find_menu_item
from orders import (
    create_order,
    get_order,
    cancel_order,
)


def process_message(message: str) -> str:
    """
    Process the user's message and return a response.

    Args:
        message (str):
            The user's input.

    Returns:
        str:
            The assistant's response.
    """

    intent = detect_intent(message)

    if intent == GREETING:
        return WELCOME_MESSAGE

    if intent == SHOW_MENU:
        return format_menu()

    if intent == CREATE_ORDER:

        item = find_menu_item(message)

        if item is None:
            return MENU_ITEM_NOT_FOUND_MESSAGE

        order = create_order(item)

        return (
            f"Order #{order['order_id']} created successfully!\n"
            f"Item: {order['item']}\n"
            f"Status: {order['status']}"
        )

    if intent == CHECK_ORDER:

        order = get_order(1)

        if order is None:
            return ORDER_NOT_FOUND_MESSAGE

        return (
            f"Order #{order['order_id']}\n"
            f"Item: {order['item']}\n"
            f"Status: {order['status']}"
        )

    if intent == CANCEL_ORDER:

        success = cancel_order(1)

        if success:
            return ORDER_CANCELED_MESSAGE

        return ORDER_NOT_FOUND_MESSAGE

    if intent == EXIT:
        return GOODBYE_MESSAGE

    return UNKNOWN_MESSAGE
