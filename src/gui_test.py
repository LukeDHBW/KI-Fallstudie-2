import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import unittest
import tkinter as tk
from gui import HangmanGUI


class TestHangmanGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = HangmanGUI(self.root)
        self.root.update()

    def tearDown(self):
        self.root.destroy()

    def test_window_title(self):
        self.assertEqual(self.root.title(), "🎮 Hangman - Wortratespiel")

    def test_widgets_exist(self):
        self.assertEqual(self.app.entry.winfo_exists(), 1)
        self.assertEqual(self.app.word_label.winfo_exists(), 1)
        self.assertEqual(self.app.error_label.winfo_exists(), 1)
        self.assertEqual(self.app.guessed_label.winfo_exists(), 1)
        self.assertEqual(self.app.hangman_text.winfo_exists(), 1)

    def test_entry_is_empty_at_start(self):
        self.assertEqual(self.app.entry.get(), "")

    def test_new_game_updates_gui_labels(self):
        self.app.new_game()
        self.root.update()

        self.assertEqual(self.app.error_label.cget("text"), f"Fehler: 0/{self.app.max_wrong}")
        self.assertEqual(self.app.guessed_label.cget("text"), "(keine)")
        self.assertIn("_", self.app.word_label.cget("text"))


if __name__ == "__main__":
    unittest.main()
