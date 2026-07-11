import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel

def find_text(window, text_edit):
    find_window = Toplevel(window)
    find_window.title("Buscar texto")
    find_window.geometry("400x60")
    find_window.resizable(False, False)
    find_window.transient(window)  # Ficar acima da janela principal
    find_window.grab_set() 
    
    #Widgets
    tk.Label(find_window, text="Buscar").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    
    search_entry = tk.Entry(find_window, width=50)
    search_entry.grid(row=0, column=1, padx=5, pady=5)
    search_entry.focus()
    
    # Fazer busca
    def do_find():
        search_text = search_entry.get()
        if not search_entry:
            messagebox.showwarning("Digite o texto a ser buscado")
            return
        
        text_edit.tag_remove("found",)
        pass
    pass

def replace_text(window, text):
    pass

def undo():
    pass    