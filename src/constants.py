"""
Application constants.
"""

# ==========================
# Intent Constants
# ==========================

SHOW_MENU = "SHOW_MENU"
CREATE_ORDER = "CREATE_ORDER"
CHECK_ORDER = "CHECK_ORDER"
CANCEL_ORDER = "CANCEL_ORDER"
GREETING = "GREETING"
EXIT = "EXIT"
UNKNOWN = "UNKNOWN"


# ==========================
# Order Status Constants
# ==========================

ORDER_STATUS_PREPARING = "Preparing"
ORDER_STATUS_CANCELED = "Canceled"
ORDER_STATUS_DELIVERED = "Delivered"


# ==========================
# Application Messages
# ==========================

WELCOME_MESSAGE = (
    "Hello! 👋\n"
    "Welcome to the Delivery Workflow Simulator.\n"
    "How can I help you today?"
)

GOODBYE_MESSAGE = "Goodbye! Have a great day!"

EMPTY_MESSAGE = "Please type a message."

UNKNOWN_MESSAGE = (
    "Sorry, I didn't understand your request.\n"
    "Please try again."
)

ORDER_NOT_FOUND_MESSAGE = "Order not found."

ORDER_CANCELED_MESSAGE = "Order canceled successfully."

MENU_ITEM_NOT_FOUND_MESSAGE = (
    "I couldn't identify the menu item.\n"
    "Please choose an item from the menu."
)
