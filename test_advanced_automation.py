import unittest

from advanced_automation import AdvancedCaptchaSolver, UltraAdvancedAutomationSystem


class AdvancedAutomationTests(unittest.TestCase):
    def test_captcha_solver_initializes_ensemble_components(self) -> None:
        solver = AdvancedCaptchaSolver()
        self.assertEqual(solver.audio_solver, "audio-solver-interface")
        self.assertEqual(solver.visual_solver, "visual-solver-interface")
        self.assertEqual(solver.behavioral_solver, "behavioral-solver-interface")
        self.assertAlmostEqual(sum(solver.ensemble_weights.values()), 1.0)

    def test_system_executes_with_expected_output_shape(self) -> None:
        system = UltraAdvancedAutomationSystem()
        result = system.execute(
            tasks=["scrape", "analyze", "report"],
            challenge={"audio": "clip", "image": "frame", "interaction": {"speed": 1.1}},
        )
        self.assertIn("scheduled_tasks", result)
        self.assertIn("behavior_pattern", result)
        self.assertIn("captcha_result", result)
        self.assertGreater(result["captcha_result"]["confidence"], 0.0)

    def test_captcha_solver_normalizes_non_unit_weights(self) -> None:
        solver = AdvancedCaptchaSolver()
        solver.ensemble_weights = {"audio": 3.0, "visual": 2.0, "behavioral": 5.0}
        result = solver.solve({"audio": "clip", "image": "frame"})
        self.assertLessEqual(result["confidence"], 1.0)
        self.assertAlmostEqual(result["score"], 0.5)


if __name__ == "__main__":
    unittest.main()
