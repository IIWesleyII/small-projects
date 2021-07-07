import unittest
import add
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add.add([1,2,3]), 6 ,"Should equal 6.")
    def test_types(self):
        self.assertRaises(TypeError, add.add, True)
        self.assertRaises(TypeError, add.add, "hlornk")
        self.assertRaises(TypeError, add.add, -5j)
if __name__ == '__main__':
    unittest.main()