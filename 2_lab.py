import unittest
def find_three_numbers(arr, P):
    num_set = set(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            required = P - (arr[i] + arr[j])
            if required in num_set and required != arr[i] and required != arr[j]:
                return True
    return False


class TestFindThreeNumbers(unittest.TestCase):

    def test_example(self):
        arr = [1, 2, 3]
        P = 6
        self.assertTrue(find_three_numbers(arr, P))

    def test_no_solution(self):
        arr = [1, 2, 3]
        P = 7
        self.assertFalse(find_three_numbers(arr, P))

    def test_large_input(self):
        arr = [100001, 200002, 300003]
        P = 600006
        self.assertTrue(find_three_numbers(arr, P))


if __name__ == '__main__':
    unittest.main()

