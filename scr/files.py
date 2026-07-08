import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def open_file(window, text_edit):
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    try:
        with open(filepath, "r",encoding='utf-8') as f:
            content = f.read()
            text_edit.insert(tk.END, content)
        window.title(f"Text Editor ABP - {os.path.basename(filepath)}")
    except Exception as e:
        text_edit.insert(tk.END, f"Error opening file: {e}")


def save_file_as(window, text_edit):
    filepath = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        defaultextension=".txt",
        title="Salvar Como"
    )

    if not filepath:
        return

    try:
        with open(filepath, "w") as f:
            content = text_edit.get(1.0, tk.END)
            f.write(content)
        window.title(f"Open File: {filepath}")
    except Exception as e:
        text_edit.insert(tk.END, f"Error saving file: {e}")


def new_file(window, text_edit):
    text_edit.delete(1.0, tk.END)
    window.title("Text Editor ABP - Untiled")


def save_file(window, text_edit):
    pass
