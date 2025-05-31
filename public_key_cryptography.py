# -*- coding: utf-8 -*-

class PublicKeyCryptography:
    """ECDSA public-key cryptography example."""
    def __init__(self, key: str):
        # p = 2^256 - 2^32 - 977
        self.p = 115792089237316195423570985008687907852837564279074904382605163141518161494337
        self.a = 0
        self.b = 7
        # G = (x, y) is the generator point
        self.x = 55066263022277343669578718895168534326250603453777594175500187360389116729240
        self.y = 32670510020758816978083085130507043184471273380659243275938904335757337482424
        self.n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

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
