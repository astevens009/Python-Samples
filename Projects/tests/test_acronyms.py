import unittest
from acronyms_demo.acronym import get_acronym


class TestAcronyms(unittest.TestCase):

    def test_it_should_properly_seperate_phrase_initials_with_periods(self):
        test_cases = [
            {
                'given': ["laughing", "out", "loud"],
                'expected': "L.O.L."
            },
            {
                'given': ["N*****", "With", "Attitude"],
                'expected': "N.W.A."
            },
            {
                'given': ["Black", "American", "Princesses"],
                'expected': "B.A.P."
            },
            {
                'given': ["North", "American", "Treaty", "Organization"],
                'expected': "N.A.T.O."
            },
        ]

        for tc in test_cases:
            phrase = tc['given']
            expected = tc['expected']

            actual = get_acronym(phrase)
            self.assertEqual(expected, actual, "acronym(s) should match")

