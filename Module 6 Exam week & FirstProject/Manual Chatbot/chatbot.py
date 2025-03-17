from utils import load_responses, log_conversation
from errors import InvalidInputError

class ChatBot:
    def __init__(self):
        self.responses = load_responses()

    def get_response(self, user_input):
        """Fetch a response based on user input."""
        user_input = user_input.lower().strip()
        if not user_input:
            raise InvalidInputError()
        
        return self.responses.get(user_input, self.responses["default"])

    def chat(self):
        """Main chatbot loop."""
        print("🤖 ChatBot: Hello! Type 'exit' to end the chat.")

        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == "exit":
                    print("🤖 ChatBot: Goodbye! Have a great day!")
                    break

                response = self.get_response(user_input)
                print(f"🤖 ChatBot: {response}")

                log_conversation(user_input, response)

            except InvalidInputError as e:
                print(f"⚠️ {e}")
            except Exception as e:
                print(f"⚠️ Unexpected error: {e}")

