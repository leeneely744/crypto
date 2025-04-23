# -*- coding: utf-8 -*-


class Keccak:
    def __init__(self, c: int, r: int):
        self.c = c  # capacity
        self.r = r  # bit rate
        self.round_num = 24  # If b=1600, round num is 24
        self.RC = [
            0x0000000000000001, 0x0000000000008082,
            0x800000000000808A, 0x8000000080008000,
            0x000000000000808B, 0x0000000080000001,
            0x8000000080008081, 0x8000000000008009,
            0x000000000000008A, 0x0000000000000088,
            0x0000000080008009, 0x000000008000000A,
            0x000000008000808B, 0x800000000000008B,
            0x8000000000008089, 0x8000000000008003,
            0x8000000000008002, 0x8000000000000080,
            0x000000000000800A, 0x800000008000000A,
            0x8000000080008081, 0x8000000000008080,
            0x0000000080000001, 0x8000000080008008,
        ]
        self.processed_blocks = []  # list to store processed blocks
    
    def round(self, block: str) -> str:
        # repeat 24 times from theta to iota
        for i in range(self.round_num):
            # theta step
            # rho step
            # pi step
            # chi step
            # iota step
            pass
        return ''
    
    def input_to_bits(self, input: str) -> str:
        bits = ''.join(format(ord(c), 'b') for c in input)
        # multi-rate padding
        bits += '1' + '0' * (self.r - len(bits) % self.r - 1) + '1'
        return bits
    
    def execute(self, input: str) -> str:
        # absorb phase
        input_bits = self.input_to_bits(input)
        return input_bits

        # squeeze phase
        result = ''
        return result

def main():
    print("This is a one-way hash function example.")
    print("Using keccak!")
    print("Please enter a string to hash:", end=" ")
    input_str = input()
    
    keccak = Keccak(c=512, r=1088)
    hashed_str = keccak.execute(input_str)
    print(f"Hashed string: {hashed_str}")

if __name__ == "__main__":
    main()
