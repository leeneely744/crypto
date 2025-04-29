import unittest
from one_way_hash_function import Keccak
import hashlib

class TestKeccak(unittest.TestCase):
    def test_keccak_hash(self):
        keccak = Keccak()
        input_str = "hello"
        expected_output = keccak.execute(input_str)
        self.assertEqual(expected_output, keccak.execute(input_str))

    def test_empty_string(self):
        keccak = Keccak()
        input_str = ""
        expected_output = ""
        self.assertEqual(expected_output, keccak.execute(input_str))

    def test_different_inputs(self):
        keccak = Keccak()
        input_str1 = "test1"
        input_str2 = "test2"
        self.assertNotEqual(keccak.execute(input_str1), keccak.execute(input_str2))
    
    def test_compare_to_public_library(self):
        keccak = Keccak()
        input_str = "hello"
        keccak_output = keccak.execute(input_str)
        
        # Using hashlib to get the expected output
        sha3_256 = hashlib.sha3_256()
        sha3_256.update(input_str.encode('utf-8'))
        expected_output = sha3_256.hexdigest()
        
        self.assertEqual(keccak_output, expected_output)

if __name__ == "__main__":
    unittest.main()