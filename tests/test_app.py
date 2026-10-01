import unittest

from app import accepted
from data import build_demo_data


class ApplicantTestCase(unittest.TestCase):
    def test_accepted_filters_by_score(self) -> None:
        result = accepted(build_demo_data(), 260)
        self.assertEqual(
            [item.full_name for item in result],
            ["Анна Петрова", "Мария Волкова"],
        )


if __name__ == "__main__":
    unittest.main()
