# -*- coding: utf-8 -*-


class Keccak:
    def __init__(self, c: int, r: int):
        self.c = c  # capacity
        self.r = r  # bit rate

    def absorb(self, block: str) -> str:
        return ''

    def squeeze(self, block: str) -> str:
        return ''
    
    def execute(self, block: str) -> str:
        # absorb fase

        # squeeze fase
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
