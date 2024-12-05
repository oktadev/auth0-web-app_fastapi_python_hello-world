from typing import TypedDict


class MessageServiceType(TypedDict):
    text: str


class MessageService:

    def public_message(self) -> MessageServiceType:
        return {
            'text': 'This is a public message.'
        }

    def protected_message(self) -> MessageServiceType:
        return {
            'text': 'This is a protected message.'
        }

    def admin_message(self) -> MessageServiceType:
        return {
            'text': 'This is an admin message.'
        }