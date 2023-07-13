import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Whisper GUI")
        self.master.configure(bg="#222")
        self.grid(padx=20, pady=20)

        # Set theme
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#222")
        style.configure("TButton", foreground="white", background="#444")
        style.configure("TRadiobutton", foreground="white", background="#222")
        style.configure("TLabel", foreground="white", background="#222")
        style.configure("TEntry", foreground="black", background="#fff")
        style.configure("TCheckbutton", foreground="white", background="#222")
        style.configure("TCombobox", foreground="black", background="#fff")

        self.create_widgets()

    def create_widgets(self):
        # File selection
        self.file_path_entry = ttk.Entry(self, width=60)
        self.file_path_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.select_button = ttk.Button(self, text="Browse", command=self.select_file)
        self.select_button.grid(row=0, column=1, sticky="ew")

        # Display selected file
        self.selected_file_label = ttk.Label(self, text="No file selected.")
        self.selected_file_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=10)

        # Model selection
        self.model_var = tk.StringVar(value='small')
        for idx, val in enumerate(['small', 'medium', 'large']):
            rb = ttk.Radiobutton(self, text=f'Model: {val}', variable=self.model_var, value=val)
            rb.grid(row=2+idx, column=0, columnspan=2, sticky="w", pady=5)

        # Language selection
        self.language_var = tk.StringVar()
        self.language_combobox = ttk.Combobox(self, textvariable=self.language_var)
        self.language_combobox['values'] = ('English', 'Swedish', 'German', 'French')
        self.language_combobox.grid(row=5, column=0, columnspan=2, sticky="ew", pady=5)

        # Task selection
        self.translate_var = tk.BooleanVar()
        self.translate_checkbutton = ttk.Checkbutton(self, text='Translate to English', variable=self.translate_var)
        self.translate_checkbutton.grid(row=6, column=0, columnspan=2, sticky="w", pady=5)

        # Run button
        self.run_button = ttk.Button(self, text="RUN", command=self.run_command)
        self.run_button.grid(row=7, column=0, columnspan=2, sticky="ew", pady=10)

    def select_file(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav *.ogg *.mp3 *.flac *.m4a *.wma *.aac")])
        if self.filename:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, self.filename)

    def run_command(self):
        self.filename = self.file_path_entry.get()
        if os.path.isfile(self.filename):
            cmd = f'Whisper "{self.filename}" --model {self.model_var.get()}'
            if self.language_var.get():
                cmd += f' --language {self.language_var.get()}'
            if self.translate_var.get():
                cmd += ' --task translate'
            os.chdir(os.path.dirname(os.path.abspath(self.filename)))
            process = subprocess.run(cmd, shell=True)
            if process.returncode == 0:
                messagebox.showinfo("Success", "Whisper operation completed successfully!")
            else:
                messagebox.showinfo("Error", "The command failed")
        else:
            messagebox.showinfo("Error", "Invalid or no file selected")


root = tk.Tk()
root.geometry("800x400")
app = Application(master=root)
app.mainloop()
