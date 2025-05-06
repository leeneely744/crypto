# -*- coding: utf-8 -*-

class SymmetricKeyCryptography:
    """
    Rijndael
    """
    def __init__(self):
        self.key_size = 128  # bits
        self.round_num = 10  # For 128-bit key size
        self.block_size = 128

    def execute(self):
        pass


def main():
    print("This is a symmetric-key cryptography example.")
    print("Please enter a message:", end=" ")
    message = input()
    crypto = SymmetricKeyCryptography()
    crypto.execute(message)
    print(f"Encrypted message: {message}")

if __name__ == "__main__":
    main()
