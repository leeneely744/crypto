# -*- coding: utf-8 -*-

class PublicKeyCryptography:
    def __init__(self, key: str):
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        pass

    def execute(self, message: str) -> str:
        if not message:
            print("Please enter a message. Do nothing.")
            return ""
        
        encrypted_message = self.encrypt(message)
        return encrypted_message


def main():
    print("This is a public-key cryptography example.")
    print("Please enter a message:", end=" ")
    message = input()
    crypto = PublicKeyCryptography()
    output = crypto.execute(message)
    print(f"Encrypted message: {output}")

if __name__ == "__main__":
    main()
