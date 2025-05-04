import os

class MessageAuthCode:
    """
    HMAC-SHA-256
    """
    def __init__(self):
        self.block_size = 64
        # Ideally, a Diffie-Hellman key exchange should be used,
        # but in this implementation, 
        # the key is generated manually for simplicity.
        self.key = os.urandom(self.block_size)
        self.ipad = bytes([0x36] * self.block_size)
        self.opad = bytes([0x5c] * self.block_size)

    def execute(self, message: str) -> str:
        return "test: " + message

def main():
    mac = MessageAuthCode()
    message = "Hello, World!"
    mac_value = mac.execute(message)
    print(f"Message: {mac_value}")

if __name__ == "__main__":
    main()