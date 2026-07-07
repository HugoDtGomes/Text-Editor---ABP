import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")
    
    

def save_file_as(window, text_edit):
    filepath =asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    with open(filepath , "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")

def save(window, text_edit):
    pass

def find_text(window, text_edit):
    pass

def replace_text(window, text):
    pass
    

def main():
    window = tk.Tk()
    window.title("Text Editor")
    
    # Configure grid weights
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)
    
    # Create text
    text_edit = tk.Text(window, font="Helvetica 10 ")
    text_edit.grid(row=0, column=1)
    
    # 
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    
    # Create Buttons
    open_button = tk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit))
    save_button = tk.Button(
        frame, text="Save", command=lambda: print(" test : save(window, text_edit)"))
    save_file_as_button = tk.Button(
        frame, text="Save As", command=lambda: save_file_as(window, text_edit))
    exit_button = tk.Button(
        frame, text="Exit", command=window.quit)
    
    # Grid Buttons
    open_button.grid(row=0, column=0, padx=5, pady=5, sticky= "ew")
    save_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    save_file_as_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    exit_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    
    # Configure frame grid
    frame.grid(row=0, column=0, sticky="ns")
    
    # configure shortcuts
    window.bind("<Control-s>", lambda x: save_file_as(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.bind("<Control-w>", lambda x: window.quit())
    
    window.mainloop()


if __name__ == "__main__":
    main()