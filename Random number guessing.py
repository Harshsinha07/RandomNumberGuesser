import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("300x180")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess the Number:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=5)

        self.attempts_label = tk.Label(root, text="")
        self.attempts_label.pack(pady=10)

    def make_guess(self):
        user_guess = self.entry.get()
        self.attempts += 1

        try:
            user_guess = int(user_guess)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        if user_guess < self.target_number:
            result = "Too low! Try again."
        elif user_guess > self.target_number:
            result = "Too high! Try again."
        else:
            result = f"Congratulations! You guessed the number in {self.attempts} attempts."
            self.reset_game()

        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        messagebox.showinfo("Result", result)

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label.config(text="Guess the Number:")
        self.attempts_label.config(text="")
        self.entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
