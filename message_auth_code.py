

class MessageAuthCode:
    def __init__(self):
        pass

    def execute(self, message: str) -> str:
        return "test: " + message

def main():
    mac = MessageAuthCode()
    message = "Hello, World!"
    mac_value = mac.execute(message)
    print(f"Message: {mac_value}")

if __name__ == "__main__":
    main()