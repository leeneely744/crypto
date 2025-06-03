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
        self.G = (self.x, self.y)
        self.n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

    def generate_keypair(self):
        # For practice, we use a specific secret key
        self.secret_key = 23731619542357098500868790785283
    
    def modinv(self, a: int, p: int) -> int:
        """
        Compute the modular inverse of a modulo p.
        Extended Euclidean Algorithm
        """
        if a == 0:
            raise ValueError("Inverse does not exist for zero.")
        lm, hm = 1, 0  # low multiplier, high multiplier
        low, high = a % p, p
        while low > 1:
            ratio = high // low
            nm = hm - lm * ratio
            new = high - low * ratio
            hm, lm = lm, nm
            high, low = low, new
        return lm % p

    def point_add(self, P: tuple, Q: tuple, a: int, p: int) -> tuple:
        """
        Add two points P and Q on an elliptic curve: y^2 = x^3 + ax + b mod p
        """
        if P is None:
            return Q
        if Q is None:
            return P
        
        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 != y2:
            return None
        
        if P == Q:
            # Multiply point by 2
            m = (3 * x1 * x1 + a) * self.modinv(2 * y1, p) % p
        else:
            # Normal point addition
            m = (y2 - y1) * self.modinv(x2 - x1, p) % p

        x3 = (m * m - x1 - x2) % p
        y3 = (m * (x1 - x3) - y1) % p

        return (x3, y3)

    def scalar_mult(self, d: int, G: tuple) -> tuple:
        """
        Returns d * G using double and add algorithm.
        d: scalar (private key)
        G: base point (x, y)
        """
        N = G
        Q = None # Initially, Q is the point at infinity

        while d > 0:
            if d & 1:
                # If Least Significant Bit is 1, addtion.
                Q = self.point_add(Q, N, self.a, self.p)
            N = self.point_add(N, N, self.a, self.p)
            d >>= 1 # Shift right to decrease one bit in binary
        return Q

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
