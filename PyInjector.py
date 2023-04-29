import tkinter as tk
from tkinter import filedialog
import pymem

class InjectorGUI(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Python Injector')
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        # Label and entry for process name
        self.lebel = tk.Label(self, text = "Process name: ")
        self.label.pack(side ="left")

        self.process_entry = tk.Entry(self)
        self.process_entry.pack(side="left")

        # Button to select DLL file
        self.select_button = tk.Button(self, text="Select DLL", command=self.select_file)
        self.select_button.pack(side="left")

        # Button to inject DLL
        self.inject_button = tk.Button(self, text = "Inject DLL", command=self.inject)
        self.inject_button.pack(side="left")

        # Button to quit app
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side="left")
    

    def select_file(self):
        # use filedialog to open file selection dialog and store filename
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select DLL file", filetypes=(("DLL files", "*.dll"), ("All files", "*.*")))


    def inject(self):
        # Get process name and DLL filename
        process_name = self.process_entry.get()

        # Check that process name and DLL filename are not empty
        if not process_name:
            tk.messagebox.showerror("Error", "Please enter a process name")
            return
        if not self.filename:
            tk.messagebox.showerror("Error", "Please select a DLL file")
            return
        
        # use Pymem to automate process handling
        try:
            pm = pymem.Pymem()
            process_id = pm.process_by_name(process_name).pid
            pm.inject_dll(process_id, self.filename)
            tk.messagebox.showinfo("Success", "DLL injected successfully")

        except:
            tk.messagebox.showerror("Error", "Error injecting DLL")