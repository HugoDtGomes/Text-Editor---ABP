import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    try:
        with open(filepath, "r") as f:
            content = f.read()
            text_edit.insert(tk.END, content)
        window.title(f"Open File: {filepath}")
    except Exception as e:
        text_edit.insert(tk.END, f"Error opening file: {e}")
    

def save_file_as(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])
    
    if not filepath:
        return
    
    try:
        with open(filepath , "w") as f:
            content = text_edit.get(1.0, tk.END)
            f.write(content)
        window.title(f"Open File: {filepath}")
    except Exception as e:
        text_edit.insert(tk.END, f"Error saving file: {e}")


def new_file(window, text_edit):
    text_edit.delete(1.0, tk.END)
    window.title("Text Editor ABP - Untiled")
        
    
    
def save(window, text_edit):
    pass

def find_text(window, text_edit):
    pass

def replace_text(window, text):
    pass
    

def main():
    window = tk.Tk()
    window.title("Text Editor ABP - Untiled")
    
    # Configure grid weights
    window.rowconfigure(0, weight= 1,minsize=400)
    window.columnconfigure(1, weight= 1, minsize=500)
    
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
    
    #Create button frame 
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    frame.grid(row=0, column=0, sticky="ns", padx=5, pady=5)
    
    # Create Buttons
    new_file_button = tk.Button(
        frame, text="New File", command= lambda:new_file(window, text_edit))
    open_button = tk.Button(
        frame, text="Open", command= lambda: open_file(window, text_edit))
    save_button = tk.Button(
        frame, text="Save", command= lambda: print(" test : save(window, text_edit)"))
    save_file_as_button = tk.Button(
        frame, text="Save As", command= lambda: save_file_as(window, text_edit))
    exit_button = tk.Button(
        frame, text="Exit", command= window.quit)
    
    # Grid Buttons
    new_file_button.grid(row=0, column=0, padx=5, pady=5, sticky= "ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    save_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    save_file_as_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    exit_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
    
    # Configure frame grid
    frame.grid(row=0, column=0, sticky="ns")
    
    # configure shortcuts
    window.bind("<Control-s>", lambda x: save_file_as(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.bind("<Control-w>", lambda x: window.quit())
    
    window.mainloop()


if __name__ == "__main__":
    main()