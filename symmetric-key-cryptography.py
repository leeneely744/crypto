# -*- coding: utf-8 -*-

class SymmetricKeyCryptography:
    """
    Rijndael
    """
    def __init__(self):
        self.key_size = 128  # bits
        self.round_num = 10  # For 128-bit key size
        self.block_size = 128
    
    def encrypto(self, round_index: int):
        for i in range(round_index):
            self.sub_bytes()
            self.shift_rows()
            self.mix_columns()
            self.add_round_key()
    
    def decrypto(self, round_index: int):
        for i in range(round_index):
            self.add_round_key()
            self.inv_mix_columns()
            self.inv_shift_rows()
            self.inv_sub_bytes()

    def sub_bytes(self):
        # Perform the SubBytes step
        pass

    def shift_rows(self):
        # Perform the ShiftRows step
        pass

    def mix_columns(self):
        # Perform the MixColumns step
        pass

    def add_round_key(self):
        # Perform the AddRoundKey step
        pass

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
