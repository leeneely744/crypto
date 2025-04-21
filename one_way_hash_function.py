# -*- coding: utf-8 -*-


class Keccak:
    def __init__(self, c: int, r: int):
        self.c = c  # capacity
        self.r = r  # bit rate
        # 2^l = b / 25
        # round_num = 12 + 2^l
        self.b = 1600  # band?
        self.round_num = 12 + self.b / 25
        self.processed_blocks = []  # list to store processed blocks
    
    def process(self, block: str) -> str:
        return ''
    
    def input_to_bits(self, input: str) -> str:
        return ''.join(format(ord(c), 'b') for c in input)
    
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
