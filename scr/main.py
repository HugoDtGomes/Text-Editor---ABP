from files import open_file, save_file_as, new_file, save_file
from text import find_text, replace_text
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox


def on_closing(window, text_edit):
    """Verifica se há alterações não salvas antes de fechar"""
    if text_edit.edit_modified():
        response = messagebox.askyesnocancel(
            "Sair", "O arquivo tem alterações não salvas. Deseja salvar antes de sair?"
        )
        if response is None:  
            return
        if response:
            save_file_as(window, text_edit)
    window.quit()
    window.destroy()


def main():
    window = tk.Tk()
    window.title("Text Editor ABP - Untitled")
    window.geometry("700x500")  # Tamanho inicial
    window.minsize(400, 300)    # Tamanho mínimo

    # Configure grid weights
    window.rowconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    # Create text widget with scrollbar
    text_frame = tk.Frame(window)
    text_frame.grid(row=0, column=1, sticky="nsew")
    text_frame.rowconfigure(0, weight=1)
    text_frame.columnconfigure(0, weight=1)

    text_edit = tk.Text(text_frame, font="Helvetica 10", wrap=tk.WORD)
    scrollbar = tk.Scrollbar(text_frame, command=text_edit.yview)
    text_edit.configure(yscrollcommand=scrollbar.set)

    text_edit.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Create button frame
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    frame.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

    # Create Buttons
    new_file_button = tk.Button(
        frame,
        text="📄 New File",
        command=lambda: new_file(window, text_edit),
        width=10,
    )

    open_button = tk.Button(
        frame,
        text="📂 Open",
        command=lambda: open_file(window, text_edit),
        width=10,
    )

    save_button = tk.Button(
        frame,
        text="💾 Save",
        command=lambda: save_file(window, text_edit),
        width=10,
    )

    save_file_as_button = tk.Button(
        frame,
        text="💿 Save As",
        command=lambda: save_file_as(window, text_edit),
        width=10,
    )
    # find text
    find_text_button = tk.Button(
        frame,
        text="Find text",
        command=lambda: find_text(window, text_edit),
        width=10,
    )
    replace_text_button = tk.Button(
        frame,
        text="Substituir",
        command=lambda: replace_text(window, text_edit),
        width=10,
    )


    exit_button = tk.Button(
        frame, text="🚪 Exit", command=lambda: on_closing(window, text_edit), width=10
    )

    # Grid Buttons
    new_file_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    save_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    save_file_as_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    find_text_button.grid(row=4, column=0, padx=5,pady=5, sticky="ew")#<=====
    replace_text_button.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
    exit_button.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

    # configure shortcuts
    window.bind("<Control-n>", lambda x: new_file(window, text_edit))
    window.bind("<Control-s>", lambda x: save_file_as(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.bind("<Control-w>", lambda x: window.quit())

    window.mainloop()


if __name__ == "__main__":
    main()
