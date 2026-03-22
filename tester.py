"""
tester.py - A tester file for the practice repository.

Runs basic checks to verify the repository files exist and contain
the expected content.
"""

import os
import unittest


class TestRepositoryFiles(unittest.TestCase):
    """Tests for the files present in the practice repository."""

    # ------------------------------------------------------------------
    # README.txt
    # ------------------------------------------------------------------
    def test_readme_exists(self):
        """README.txt should exist in the repository root."""
        self.assertTrue(os.path.isfile("README.txt"), "README.txt not found")

    def test_readme_not_empty(self):
        """README.txt should not be empty."""
        with open("README.txt", "r") as f:
            content = f.read()
        self.assertTrue(len(content.strip()) > 0, "README.txt is empty")

    def test_readme_contains_hello_world(self):
        """README.txt should contain 'Hello World'."""
        with open("README.txt", "r") as f:
            content = f.read()
        self.assertIn("Hello World", content)

    # ------------------------------------------------------------------
    # hello3.txt
    # ------------------------------------------------------------------
    def test_hello3_exists(self):
        """hello3.txt should exist in the repository root."""
        self.assertTrue(os.path.isfile("hello3.txt"), "hello3.txt not found")

    def test_hello3_not_empty(self):
        """hello3.txt should not be empty."""
        with open("hello3.txt", "r") as f:
            content = f.read()
        self.assertTrue(len(content.strip()) > 0, "hello3.txt is empty")

    def test_hello3_contains_hello_world(self):
        """hello3.txt should contain 'Hello World'."""
        with open("hello3.txt", "r") as f:
            content = f.read()
        self.assertIn("Hello World", content)

    # ------------------------------------------------------------------
    # General sanity checks
    # ------------------------------------------------------------------
    def test_tester_file_exists(self):
        """tester.py itself should exist."""
        self.assertTrue(os.path.isfile("tester.py"), "tester.py not found")


if __name__ == "__main__":
    unittest.main(verbosity=2)
