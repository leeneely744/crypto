# -*- coding: utf-8 -*-

from bitarray import bitarray, util as bitutil

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
        self.lane_num = 64  # b/25
        # State is a 5x5 grid of 64-bit lanes.
        self.state = [[bitarray(self.lane_num) for y in range(5)] for x in range(5)]
        self.rotete_offset = [
            [0, 36, 3, 41, 18],
            [1, 44, 10, 45, 2],
            [62, 6, 43, 15, 61],
            [28, 55, 25, 21, 56],
            [27, 20, 39, 8, 14],
        ]
    
    # In the Keccak theory, the round function needs
    # xoring the state and the round constant RC as argments.
    # But in this implementation,
    # it has in the properties of the Keccak class.
    def round(self):
        # repeat 24 times from theta to iota
        for round_index in range(self.round_num):
            # theta step
            Cs = [bitarray('0' * self.lane_num) for _ in range(5)]
            for x in range(5):
                sheet = self.state[x]
                Cs[x] = sheet[0] ^ sheet[1] ^ sheet[2] ^ sheet[3] ^ sheet[4]
            Ds = [bitarray('0' * self.lane_num) for _ in range(5)]
            for x in range(5):
                Ds[x] = self.rotate(Cs[(x + 4) % 5] ^ Cs[(x + 1)%5], 1).copy()
            for x in range(5):
                D = Ds[x]
                for y in range(5):
                    self.state[x][y] ^= D

            # rho and pi step
            B = [[bitarray('0' * self.lane_num) for y in range(5)] for x in range(5)]
            for x in range(5):
                for y in range(5):
                    B[y][(2*x+3*y)%5] = self.rotate(self.state[x][y], self.rotete_offset[x][y]).copy()

            # chi step
            # 1. B2 = not B[x+1,y]
            # 2. B3 = B2 and B[x+2,y]
            # 3. A[x,y] = B[x,y] xor B3
            for x in range(5):
                for y in range(5):
                    B2 = ~B[(x+1)%5][y]
                    B3 = B2 & B[(x+2)%5][y]
                    self.state[x][y] ^= B3

            # iota step
            # rc is 16 digits hex.
            # 1 digit hex is 4 bits.
            # rc is 64 bits(16 * 4 = 64)
            rc = bitarray(format(self.RC[round_index], '064b'))
            rc.reverse()
            for i in range(64):
                self.state[x][y][i] ^= rc[i]
        return True
    
    def rotate(self, block: bitarray, bit: int) -> bitarray:
        return block[bit:] + block[:bit]
    
    def input_to_bits(self, input: str) -> bitarray:
        bits_str = ''.join(format(ord(c), 'b') for c in input)
        bits = bitarray(bits_str)
        bits.extend('00000110')
        pad_len = (-len(bits) - 1) % self.r
        bits.extend('0' * pad_len)
        bits.extend('1')
        return bits
    
    def execute(self, input: str) -> str:
        # absorb phase
        input_bits = self.input_to_bits(input)
        # pass input_bits per r bits to round function
        for i in range(0, len(input_bits), self.r):
            block = input_bits[i:i + self.r]
            # len(block) == self.r(1088)
            # lane_num = 64
            # xor to first 17 lanes
            for i in range(17):
                x = i % 5
                y = i // 5
                self.state[x][y] ^= block[i * self.lane_num:(i + 1) * self.lane_num]
            self.round()

        # squeeze phase
        # This is SHA3-256, so we need to return the first 256 bits.
        output_bits = bitarray()
        for i in range(4):
            output_bits.extend(self.state[i][0]) 
        return bitutil.ba2hex(output_bits)

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
