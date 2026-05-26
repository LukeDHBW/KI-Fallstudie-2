import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from Words_Hangman import words
from Galgen_Hangman import HANGMAN_ART


class HangmanGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Hangman - Wortratespiel")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")

        # Spielvariablen
        self.answer = ""
        self.hint = []
        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.max_wrong = len(HANGMAN_ART) - 1
        self.game_over = False

        # GUI aufbauen
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        """Erstellt alle GUI-Elemente."""
        
        # Titel
        title_label = tk.Label(
            self.root, 
            text="🎮 HANGMAN", 
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=10)

        # Hangman ASCII-Art (Text-Widget mit fester Breite)
        self.hangman_text = tk.Text(
            self.root,
            height=8,
            width=30,
            font=("Courier", 10),
            bg="white",
            border=2,
            relief="sunken",
            state="disabled"
        )
        self.hangman_text.pack(pady=10, padx=10)

        # Wort-Anzeige (Label mit großer Schrift)
        word_frame = tk.Frame(self.root, bg="#f0f0f0")
        word_frame.pack(pady=10)

        tk.Label(word_frame, text="Gesuchtes Wort:", font=("Arial", 10), bg="#f0f0f0").pack()
        
        self.word_label = tk.Label(
            word_frame,
            text="_ _ _ _",
            font=("Courier", 20, "bold"),
            bg="white",
            fg="#000",
            padx=20,
            pady=10,
            width=20,
            relief="sunken"
        )
        self.word_label.pack(pady=5)

        # Fehlerzahl
        self.error_label = tk.Label(
            self.root,
            text=f"Fehler: 0/{self.max_wrong}",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#d9534f"
        )
        self.error_label.pack()

        # Eingabe-Frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=15)

        tk.Label(input_frame, text="Buchstabe eingeben:", font=("Arial", 10), bg="#f0f0f0").pack()

        self.entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=3,
            justify="center"
        )
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.focus()
        self.entry.bind("<Return>", lambda e: self.guess_button_click())

        # Guess-Button
        guess_button = tk.Button(
            input_frame,
            text="Raten",
            command=self.guess_button_click,
            font=("Arial", 10),
            bg="#5cb85c",
            fg="white",
            padx=15,
            relief="raised"
        )
        guess_button.pack(side=tk.LEFT, padx=5)

        # Geratene Buchstaben
        tk.Label(
            self.root,
            text="Geratene Buchstaben:",
            font=("Arial", 10),
            bg="#f0f0f0"
        ).pack()

        self.guessed_label = tk.Label(
            self.root,
            text="(keine)",
            font=("Arial", 11),
            bg="white",
            fg="#333",
            padx=20,
            pady=8,
            width=40,
            relief="sunken",
            wraplength=300
        )
        self.guessed_label.pack(pady=5, padx=10)

        # Buttons unten
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        new_game_button = tk.Button(
            button_frame,
            text="Neues Spiel",
            command=self.new_game,
            font=("Arial", 11),
            bg="#0275d8",
            fg="white",
            padx=15,
            relief="raised"
        )
        new_game_button.pack(side=tk.LEFT, padx=5)

        exit_button = tk.Button(
            button_frame,
            text="Beenden",
            command=self.root.quit,
            font=("Arial", 11),
            bg="#6c757d",
            fg="white",
            padx=15,
            relief="raised"
        )
        exit_button.pack(side=tk.LEFT, padx=5)

    def update_hangman_display(self):
        """Aktualisiert die Hangman-ASCII-Art Anzeige."""
        hangman_art = HANGMAN_ART[self.wrong_guesses]
        art_string = "\n".join(hangman_art)

        self.hangman_text.config(state="normal")
        self.hangman_text.delete("1.0", tk.END)
        self.hangman_text.insert("1.0", art_string)
        self.hangman_text.config(state="disabled")

    def update_word_display(self):
        """Aktualisiert die Anzeige des gesuchten Wortes."""
        word_display = " ".join(self.hint)
        self.word_label.config(text=word_display)

    def update_error_display(self):
        """Aktualisiert die Fehleranzeige."""
        self.error_label.config(text=f"Fehler: {self.wrong_guesses}/{self.max_wrong}")

    def update_guessed_display(self):
        """Aktualisiert die Anzeige der geratenen Buchstaben."""
        if self.guessed_letters:
            letters_str = " ".join(sorted(self.guessed_letters))
            self.guessed_label.config(text=letters_str)
        else:
            self.guessed_label.config(text="(keine)")

    def guess_button_click(self):
        """Verarbeitet den Buchstaben-Tipp wenn der Button geklickt wird."""
        if self.game_over:
            messagebox.showinfo("Spiel vorbei", "Das Spiel ist vorbei. Starten Sie ein neues Spiel!")
            return

        guess = self.entry.get().upper().strip()
        self.entry.delete(0, tk.END)
        self.entry.focus()

        # Validierung
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie einen einzelnen Buchstaben ein.")
            return

        if guess in self.guessed_letters:
            messagebox.showwarning("Bereits geraten", f"Der Buchstabe {guess} wurde bereits geraten.")
            return

        # Buchstabe zur Liste hinzufügen
        self.guessed_letters.add(guess)
        self.update_guessed_display()

        # Prüfe ob Buchstabe im Wort ist
        if guess in self.answer:
            for i, ch in enumerate(self.answer):
                if ch == guess:
                    self.hint[i] = guess
            messagebox.showinfo("Richtig! ✓", f"Der Buchstabe {guess} ist im Wort!")
        else:
            self.wrong_guesses += 1
            messagebox.showinfo("Falsch! ✗", f"Der Buchstabe {guess} ist nicht im Wort.")

        self.update_hangman_display()
        self.update_word_display()
        self.update_error_display()

        # Prüfe auf Sieg
        if "_" not in self.hint:
            self.game_over = True
            messagebox.showinfo("🎉 GEWONNEN! 🎉", f"Gratuliere! Das Wort war: {self.answer}")
            return

        # Prüfe auf Niederlage
        if self.wrong_guesses >= self.max_wrong:
            self.game_over = True
            messagebox.showinfo("⚰️ VERLOREN! ⚰️", f"Spiel vorbei! Das Wort war: {self.answer}")
            return

    def new_game(self):
        """Startet ein neues Spiel."""
        self.answer = random.choice(words).upper()
        self.hint = ["_"] * len(self.answer)
        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.game_over = False

        self.entry.delete(0, tk.END)
        self.entry.focus()

        self.update_hangman_display()
        self.update_word_display()
        self.update_error_display()
        self.update_guessed_display()


def main():
    """Startet die GUI-Anwendung."""
    try:
        root = tk.Tk()
        app = HangmanGUI(root)
        root.mainloop()
    except Exception as e:
        import traceback
        print(f"FEHLER beim Starten der GUI: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
