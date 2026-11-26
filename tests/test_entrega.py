import re
import shutil
import tempfile
import unittest
from pathlib import Path

import nbformat
import pandas as pd
from nbclient import NotebookClient
from scipy import stats


ROOT = Path(__file__).resolve().parents[1]


class EntregaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="correlacion_m15_")
        cls.workdir = Path(cls.temp.name)
        shutil.copytree(ROOT / "data", cls.workdir / "data")
        cls.notebook = nbformat.read(ROOT / "pre-entregamd15.ipynb", as_version=4)
        NotebookClient(
            cls.notebook,
            timeout=180,
            kernel_name="python3",
            resources={"metadata": {"path": str(cls.workdir)}},
        ).execute()
        cls.outputs = [
            output
            for cell in cls.notebook.cells
            if cell.cell_type == "code"
            for output in cell.outputs
        ]
        cls.text = "\n".join(
            "".join(output.get("text", ""))
            for output in cls.outputs
            if output.output_type == "stream"
        )

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_three_coefficients_match_independent_scipy_calculations(self):
        frame = pd.read_csv(ROOT / "data" / "dashboard_ventas.csv")
        pairs = frame[["Discount", "Profit"]].dropna()
        self.assertIn(f"Pares analizados: {len(pairs)}", self.text)
        for name, function in (
            ("Pearson", stats.pearsonr),
            ("Spearman", stats.spearmanr),
            ("Kendall", stats.kendalltau),
        ):
            result = re.search(rf"{name}: (-?\d+\.\d+)", self.text)
            self.assertIsNotNone(result, name)
            expected = function(pairs["Discount"], pairs["Profit"]).statistic
            self.assertAlmostEqual(float(result.group(1)), expected, places=5)

    def test_visualizations_are_rendered(self):
        images = [
            output for output in self.outputs
            if output.output_type in ("display_data", "execute_result")
            and "image/png" in output.get("data", {})
        ]
        self.assertGreaterEqual(len(images), 2)

    def test_saved_notebook_contains_executed_cells_without_errors(self):
        saved = nbformat.read(ROOT / "pre-entregamd15.ipynb", as_version=4)
        code = [cell for cell in saved.cells if cell.cell_type == "code"]
        self.assertTrue(code)
        self.assertTrue(all(cell.execution_count is not None for cell in code))
        self.assertTrue(any(cell.outputs for cell in code))
        self.assertFalse(any(
            output.output_type == "error"
            for cell in code
            for output in cell.outputs
        ))
        saved_outputs = [output for cell in code for output in cell.outputs]
        saved_text = "\n".join(
            "".join(output.get("text", ""))
            for output in saved_outputs
            if output.output_type == "stream"
        )
        for name in ("Pearson", "Spearman", "Kendall"):
            result = re.search(rf"{name}: (-?\d+\.\d+)", self.text)
            self.assertIn(result.group(0), saved_text)
        self.assertGreaterEqual(sum(
            "image/png" in output.get("data", {}) for output in saved_outputs
        ), 2)

    def test_explanation_addresses_causality_and_method_choice(self):
        markdown = "\n".join(
            cell.source.lower()
            for cell in self.notebook.cells
            if cell.cell_type == "markdown"
        )
        for term in ("pearson", "spearman", "kendall", "causalidad", "atípicos"):
            self.assertIn(term, markdown)


if __name__ == "__main__":
    unittest.main()
