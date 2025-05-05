import os
import hashlib

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
        # K XOR ipad, text
        k_xor_ipad = bytes([a ^ b for a, b in zip(self.key, self.ipad)])
        inner_message = k_xor_ipad + message.encode('utf-8')

        # H(K XOR ipad, text)
        inner_hash = hashlib.sha256(inner_message).digest()

        # K XOR opad
        k_xor_opad = bytes([a ^ b for a, b in zip(self.key, self.opad)])
        # K XOR opad, H(K XOR ipad, text)
        outer_message = k_xor_opad + inner_hash
        # H(K XOR opad, H(K XOR ipad, text))
        outer_hash = hashlib.sha256(outer_message).hexdigest()
        return outer_hash


def main():
    print("This is a HMAC-SHA-256 example.")
    print("Please enter a message:", end=" ")
    message = input()
    mac = MessageAuthCode()
    mac_value = mac.execute(message)
    print(f"MAC: {mac_value}")

if __name__ == "__main__":
    main()