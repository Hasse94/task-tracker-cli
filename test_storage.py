"""Tests for storage.py. They use a temporary folder and never touch tasks.json."""

import tempfile
import unittest
from pathlib import Path

import storage


class TestStorage(unittest.TestCase):
    def test_save_then_load_returns_the_same_tasks(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "tasks.json"
            saved = [{"id": 1, "description": "Learn Python", "status": "todo"}]
            storage.save_tasks(saved, path)
            self.assertEqual(storage.load_tasks(path), saved)

    def test_missing_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "missing.json"
            self.assertEqual(storage.load_tasks(path), [])

    def test_empty_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "tasks.json"
            path.write_text("")
            self.assertEqual(storage.load_tasks(path), [])


if __name__ == "__main__":
    unittest.main()