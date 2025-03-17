class ChatbotError(Exception):
    """Base class for chatbot exceptions."""
    pass

class InvalidInputError(ChatbotError):
    """Raised when user input is invalid or empty."""
    def __init__(self, message="Invalid input! Please enter a valid query."):
        self.message = message
        super().__init__(self.message)
