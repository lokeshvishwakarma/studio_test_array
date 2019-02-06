import unittest
import flatten_array


class TestFlatten(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(flatten_array.flatten([]), [])

    def test_flatten(self):
        flat_list = flatten_array.flatten([1, [2, 3, [4], 5, [6]]])
        for item in flat_list:
            if isinstance(item, list):
                flag = False
            else:
                flag = True

        self.assertEqual(flag, True)

    def test_diff_dataset(self):
        self.assertEqual(flatten_array.flatten(
            [2, 'loki', [3, 10]]), [2, 'loki', 3, 10])

if __name__=='__main__':
    unittest.main()