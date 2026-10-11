from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Non-Hermitian-Critical-Edge"))
try:
    import mpmath as mp
except ImportError:
    mp = None


@unittest.skipIf(mp is None, "mpmath is required for dynamics tests")
class DynamicsTests(unittest.TestCase):
    def test_centered_initial_state_and_zero_hamiltonian(self):
        from dynamics import initial_state, time_evolution_renormalization
        psi = initial_state(4)
        self.assertEqual(list(psi), [0, 0, 1, 0])
        data, moments, final = time_evolution_renormalization(mp.zeros(4), psi, 3, 1)
        self.assertEqual(len(data), 3)
        self.assertEqual(data, [[0, 0, 1, 0]] * 3)
        self.assertEqual(moments, [0, 0, 0])
        self.assertEqual(final, [0, 0, 1, 0])

    def test_no_step_preserves_initial_observation(self):
        from dynamics import initial_state, time_evolution_renormalization
        data, moments, final = time_evolution_renormalization(mp.zeros(4), initial_state(4), 0, 1)
        self.assertEqual(len(data), 1)
        self.assertEqual(moments, [0])
        self.assertEqual(final, [0, 0, 1, 0])


if __name__ == "__main__":
    unittest.main()
