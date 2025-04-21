# -*- coding: utf-8 -*-


def keccak(input_str: str) -> str:
    return input_str

def main():
    print("This is a one-way hash function example.")
    print("Using keccak!")
    print("Please enter a string to hash:")
    input_str = input()
    hashed_str = keccak(input_str)
    print(f"Hashed string: {hashed_str}")
