import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel

def find_text(window, text_edit):
    find_window = Toplevel(window)
    find_window.title("Buscar texto")
    find_window.geometry("400x120")
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
        
        # Limpar selecao
        text_edit.tag_remove("found", "1.0", tk.END)
        
        # 
        start = "1.0"
        found_count = 0
        while True:
            start = text_edit.search(search_text, start, stopindex= tk.END, nocase=True, exact=False)
            if not start:
                break
            end = f"{start} + {len(search_text)}c"
            text_edit.tag_add("found", start, end)
            found_count +=1
            start = end
        
        # Configurar estilo de destaque
        text_edit.tag_config("found", background="yellow" , foreground="black") 
        
        if found_count > 0 :
            text_edit.mark_set("insert", "1.0")
            text_edit.see("1.0")
            messagebox.showinfo("Busca", f"Encontrado {found_count} no texto") 
        else:
            messagebox.showinfo("Busca", "Texto nao encontrado")
    
    # fechar janela de busca
    def close_find():
        """Fecha a janela de busca e remove os destaques"""
        text_edit.tag_remove("found", "1.0", tk.END)
        find_window.destroy()
    
    # Botoes
    button_frame = tk.Frame(find_window)
    button_frame.grid(row=1, column= 0, columnspan=2, pady=10)
    
    tk.Button(button_frame, text="Buscar", command= do_find, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Fechar", command= close_find, width=10).pack(side=tk.LEFT, padx=5) 
   

def replace_text(window, text):
    pass

def undo():
    pass    