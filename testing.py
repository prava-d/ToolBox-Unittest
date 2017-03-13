""" A program that uses unittest to test a script that orders a list and removes all negative numbers from the list """

import unittest


def sort_list(some_list):
    """ sorts the list
        some_list: a list of numbers that is passed in """
    return sorted(some_list)


def remove_negatives(some_list):
    """ removes the negative numbers from a list
        some_list: a list of numbers that is passed in """
    pos_list = []
    for value in some_list:
        if value >= 0:
            pos_list.append(value)
    return pos_list


def sort_and_remove(some_list):
    """ both sorts a list and removes its negative numbers
        some_list: a list of numbers that is passed in """
    return sort_list(remove_negatives(some_list))


class Test_sort_and_remove(unittest.TestCase):
    """ code that carries out the unit tests """

    def test_sort_list(self):
        """ unittests to determine if the list is sorted """
        self.assertEqual(sort_list([5, 0.5, 1, 0]), [0, 0.5, 1, 5])
        self.assertEqual(sort_list([-4, 2, 3, -5]), [-5, -4, 2, 3])

    def test_text_no_negs(self):
        """ unittests to determine if there are no negatives in list """
        self.assertEqual(remove_negatives([-1, 1, -2, 3]), [1, 3])
        self.assertEqual(remove_negatives([-1, -5, -2, -0.2]), [])
        self.assertEqual(remove_negatives([1, 1, 2, 0.3]), [1, 1, 2, 0.3])

    def test_sort_and_remove(self):
        """ unittests to determine if the list has no negatives and is sorted """
        self.assertEqual(sort_and_remove([3, 5, -2, 1.2]), [1.2, 3, 5])
        self.assertEqual(sort_and_remove([120, -20, 50, 123]), [50, 120, 123])


if __name__ == '__main__':
    """ main to carry out the unittests """
    unittest.main()
