from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Non-Hermitian-Critical-Edge"))
from data_io import parse_complex_string


class ComplexParsingTests(unittest.TestCase):
    def test_real_imaginary_and_scientific_notation(self):
        examples = {"1": 1 + 0j, "-2.5": -2.5 + 0j, "j": 1j,
                    "-i": -1j, "1+2j": 1 + 2j,
                    "( 1e-3 - 2e+4j )": 0.001 - 20000j,
                    "-3E-4+2E-6i": -0.0003 + 0.000002j}
        for value, expected in examples.items():
            with self.subTest(value=value):
                self.assertEqual(parse_complex_string(value), expected)

    def test_invalid_suffix_is_not_silently_ignored(self):
        for value in ["", "1+2j trailing", "1e-", "abc", "(1+2j"]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_complex_string(value)


if __name__ == "__main__":
    unittest.main()
