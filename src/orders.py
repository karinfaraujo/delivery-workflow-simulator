"""
Order module.

This module handles order creation,
retrieval, and cancellation.
"""

from constants import (
    ORDER_STATUS_PREPARING,
    ORDER_STATUS_CANCELED,
)

# ==========================
# In-Memory Storage
# ==========================

orders = {}
next_order_id = 1


def create_order(item: str) -> dict:
    """
    Create a new order.

    Args:
        item (str):
            The selected menu item.

    Returns:
        dict:
            The newly created order.
    """
    global next_order_id

    order = {
        "order_id": next_order_id,
        "item": item,
        "status": ORDER_STATUS_PREPARING,
    }

    orders[next_order_id] = order
    next_order_id += 1

    return order


def get_order(order_id: int) -> dict | None:
    """
    Return an order by its ID.

    Args:
        order_id (int):
            The order identifier.

    Returns:
        dict | None:
            The order if found, otherwise None.
    """
    return orders.get(order_id)


def cancel_order(order_id: int) -> bool:
    """
    Cancel an existing order.

    Args:
        order_id (int):
            The order identifier.

    Returns:
        bool:
            True if the order was canceled,
            otherwise False.
    """
    order = get_order(order_id)

    if order is None:
        return False

    order["status"] = ORDER_STATUS_CANCELED

    return True
