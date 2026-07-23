"""
Intent detection module.

This module identifies the user's intent
based on keywords.
"""

from constants import (
    SHOW_MENU,
    CREATE_ORDER,
    CHECK_ORDER,
    CANCEL_ORDER,
    GREETING,
    EXIT,
    UNKNOWN,
)

# ==========================
# Intent Keywords
# ==========================

INTENT_KEYWORDS = {
    SHOW_MENU: [
        "menu",
        "food",
        "drink",
    ],
    CREATE_ORDER: [
        "buy",
        "want",
        "pizza",
    ],
    CHECK_ORDER: [
        "status",
        "track",
        "where",
    ],
    CANCEL_ORDER: [
        "cancel",
        "remove",
    ],
    GREETING: [
        "hello",
        "hi",
        "good morning",
        "good afternoon",
        "good evening",
    ],
    EXIT: [
        "exit",
        "quit",
        "bye",
    ],
}


def detect_intent(message: str) -> str:
    """
    Detect the user's intent based on keywords.

    Args:
        message (str):
            The user's input.

    Returns:
        str:
            The detected intent.
    """

    message = message.lower()

    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in message:
                return intent

    return UNKNOWN
