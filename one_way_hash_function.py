# -*- coding: utf-8 -*-


class Keccak:
    def __init__(self, c: int, r: int):
        self.c = c  # capacity
        self.r = r  # bit rate
        self.processed_blocks = []  # list to store processed blocks
    
    def process(self, block: str) -> str:
        return ''

    def absorb(self, block: str) -> str:
        return ''

    def squeeze(self, block: str) -> str:
        return ''
    
    def input_to_bits(self, input: str) -> str:
        result = ""
        for char in input:
            result += bin(ord(char))[2:]
        return result
    
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
    print("Please enter a string to hash:")
    input_str = input()
    
    keccak = Keccak(c=256, r=512)
    hashed_str = keccak.execute(input_str)
    print(f"Hashed string: {hashed_str}")

if __name__ == "__main__":
    main()
