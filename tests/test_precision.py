import ast
from pathlib import Path
import unittest

import mpmath as mp


class PrecisionTests(unittest.TestCase):
    def test_recorded_precision_assignments_configure_the_active_context(self):
        source_dir = Path(__file__).resolve().parents[1] / "Non-Hermitian-Critical-Edge"
        checked = 0
        previous = mp.mp.dps
        try:
            for source in source_dir.glob("*.py"):
                tree = ast.parse(source.read_text(encoding="utf-8"))
                if not any(isinstance(node, ast.Import) and any(
                        alias.name == "mpmath" and alias.asname == "mp" for alias in node.names)
                           for node in tree.body):
                    continue
                for node in tree.body:
                    if not isinstance(node, ast.Assign):
                        continue
                    for target in node.targets:
                        if isinstance(target, ast.Attribute) and target.attr == "dps":
                            self.assertEqual(ast.unparse(target), "mp.mp.dps")
                            expected = ast.literal_eval(node.value)
                            mp.mp.dps = 15
                            exec(compile(ast.Module(body=[node], type_ignores=[]), str(source), "exec"), {"mp": mp})
                            self.assertEqual(mp.mp.dps, expected)
                            checked += 1
            self.assertEqual(checked, 7)
        finally:
            mp.mp.dps = previous


if __name__ == "__main__":
    unittest.main()
