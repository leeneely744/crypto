# -*- coding: utf-8 -*-

from bitarray import bitarray, util as bitutil
import os

class SymmetricKeyCryptography:
    """
    Rijndael
    """
    def __init__(self):
        self.key_size = 128  # bits
        self.block_size = 16 # bytes (128 bits)
        self.state = [[0] * 4 for _ in range(4)]  # 4x4 matrix for AES state
        self.S_BOX = [
            # y=0  1     2     3     4     5     6     7     8     9     a     b     c     d     e     f
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,  # x=0
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,  # x=1
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,  # x=2
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,  # x=3
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,  # x=4
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,  # x=5
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,  # x=6
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,  # x=7
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,  # x=8
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,  # x=9
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,  # x=a
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,  # x=b
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,  # x=c
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,  # x=d
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,  # x=e
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16   # x=f
        ]
        self.constant_matrix = [
            [2, 3, 1, 1],
            [1, 2, 3, 1],
            [1, 1, 2, 3],
            [3, 1, 1, 2]
        ]
        self.Nr = 10  # round num for 128-bit key size
        self.Nk = 4  # Number of original key words(4 hexadecimals)
        self.Nb = 4  # block size in words(4 hexadecimals)
        # for test key
        self.key = b"\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c"
        self.key_expansion = self.generate_key_expansion()
  
    def generate_key_expansion(self) -> list[int]:
        k = self.key  # for short
        w = []
        for i in range(self.Nk):
            w.append(k[4*i] << 24 | k[4*i+1] << 16 | k[4*i+2] << 8 | k[4*i+3])
        
        i = self.Nk
        while i < self.Nb * (self.Nr + 1):
            temp = w[i-1]
            if i % self.Nk == 0:
                temp = self.sub_word(self.rot_word(temp)) ^ self.rcon[i // self.Nk]
            elif self.Nk > 6 and i % self.Nk == 4:
                temp = self.sub_word(temp)
            w.append(w[i - self.Nk] ^ temp)
            i += 1
        return w

    def sub_word(self, word: int) -> int:
        b0 = self.S_BOX[word >> 24 & 0xFF]
        b1 = self.S_BOX[word >> 16 & 0xFF]
        b2 = self.S_BOX[word >> 8 & 0xFF]
        b3 = self.S_BOX[word & 0xFF]
        return (b0 << 24) | (b1 << 16) | (b2 << 8) | b3
    
    def rot_word(self, word: int) -> int:
        b0 = word >> 24 & 0xFF
        b1 = word >> 16 & 0xFF
        b2 = word >> 8 & 0xFF
        b3 = word & 0xFF
        return (b1 << 24) | (b2 << 16) | (b3 << 8) | b0

    def generate_rcon(self, n: int) -> list[int]:
        rcon = [0x00] * n
        rcon[0] = 0x01
        for i in range(1, n):
            rcon[i] = self.xtime(rcon[i-1])
        return rcon
    
    def xtime(self, x: int) -> int:
        return ((x << 1) ^ 0x1b) & 0xff if (x & 0x80) else (x << 1) & 0xff

    def round(self, round_count: int):
        for i in range(round_count):
            self.sub_bytes()
            self.shift_rows()
            self.mix_columns()
            self.add_round_key()
    
    def decrypto(self, round_count: int):
        for i in range(round_count):
            self.add_round_key()
            self.inv_mix_columns()
            self.inv_shift_rows()
            self.inv_sub_bytes()

    def sub_bytes(self):
        for col in range(4):
            for row in range(4):
                index = self.state[row][col]  # 0~255
                self.state[row][col] = self.S_BOX[index]

    def shift_rows(self):
        for row in range(1, 4):
            self.state[row] = self.state[row][row:] + self.state[row][:row]

    def mul(self, a: int, b: int) -> int:
        res = 0
        for i in range(8):
            if b & 1:
                res ^= a
            high = a & 0x80
            a = (a << 1) & 0xFF
            if high:
                a ^= 0x1b
            b >>= 1
        return res

    def my_dot(self, x: int, y, int) -> int:
        return self.mul(self.constant_matrix[x][0], self.state[0][y]) ^ \
                self.mul(self.constant_matrix[x][1], self.state[1][y]) ^ \
                self.mul(self.constant_matrix[x][2], self.state[2][y]) ^ \
                self.mul(self.constant_matrix[x][3], self.state[3][y])

    def mix_columns(self):
        for col in range(4):
            for row in range(4):
                self.state[row][col] = self.my_dot(row, col)

    def add_round_key(self):
        # Perform the AddRoundKey step
        pass

    def pkcs7_pad(self, data: bytes) -> bytes:
        pad = self.block_size - len(data) % self.block_size
        return data + bytes([pad]) * pad

    def input_block_to_state(self, block: bytes):
        # state is a 4x4 matrix, block is a 16 bytes array
        # filling order is column-major: state[0][0] → state[1][0]...
        for col in range(4):
            for row in range(4):
                self.state[row][col] = block[col * 4 + row]

    def execute(self, message: str) -> str:
        if not message:
            return ""
        data = message.encode('utf-8')
        message_bytes = self.pkcs7_pad(data)
        prev = os.urandom(self.block_size)
        round_count = 0
        for offset in range(0, len(message_bytes), self.block_size):
            # block xor prev, and insert it to state
            block = message_bytes[offset: offset + self.block_size]
            block = bytes(a ^ b for a, b in zip(message_bytes[offset: offset+self.block_size], prev))
            self.input_block_to_state(block)

            crypto = self.round(round_count)

            prev = crypto
            round_count += 1
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
