"""Tests for tasks.py. They use their own lists and never touch tasks.json."""

import unittest

import tasks


class TestAddTask(unittest.TestCase):
    def test_first_task_gets_id_1_and_status_todo(self):
        task_list = []
        task = tasks.add_task(task_list, "Buy milk")
        self.assertEqual(task["id"], 1)
        self.assertEqual(task["status"], "todo")

    def test_id_is_not_reused_after_a_delete(self):
        task_list = []
        for name in ("a", "b", "c"):
            tasks.add_task(task_list, name)
        tasks.delete_task(task_list, 2)
        new_task = tasks.add_task(task_list, "d")
        self.assertEqual(new_task["id"], 4)


class TestMarkStatus(unittest.TestCase):
    def setUp(self):
        self.task_list = []
        tasks.add_task(self.task_list, "Buy milk")

    def test_changes_the_status(self):
        task = tasks.mark_status(self.task_list, 1, "done")
        self.assertEqual(task["status"], "done")

    def test_unknown_id_returns_none(self):
        self.assertIsNone(tasks.mark_status(self.task_list, 99, "done"))

    def test_invalid_status_raises_value_error(self):
        with self.assertRaises(ValueError):
            tasks.mark_status(self.task_list, 1, "finished")


class TestDeleteAndList(unittest.TestCase):
    def setUp(self):
        self.task_list = []
        tasks.add_task(self.task_list, "a")
        tasks.add_task(self.task_list, "b")
        tasks.mark_status(self.task_list, 2, "done")

    def test_delete_removes_the_task(self):
        self.assertTrue(tasks.delete_task(self.task_list, 1))
        self.assertIsNone(tasks.find_task(self.task_list, 1))

    def test_delete_unknown_id_returns_false(self):
        self.assertFalse(tasks.delete_task(self.task_list, 99))

    def test_list_without_status_returns_everything(self):
        self.assertEqual(len(tasks.list_tasks(self.task_list)), 2)

    def test_list_filters_by_status(self):
        done = tasks.list_tasks(self.task_list, "done")
        self.assertEqual([task["id"] for task in done], [2])

    def test_list_invalid_status_raises_value_error(self):
        with self.assertRaises(ValueError):
            tasks.list_tasks(self.task_list, "finished")


if __name__ == "__main__":
    unittest.main()