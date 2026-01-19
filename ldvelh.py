import tkinter as tk
from tkinter import ttk
import threading
import time
from pathlib import Path


class SharedFiles:
    def __init__(self):
        self.folder = Path("txt_files")
        self.folder.mkdir(exist_ok=True)
    
    def read(self, key):
        filepath = self.folder / f"{key}.txt"
        if filepath.exists():
            return filepath.read_text(encoding='utf-8').strip()
        return ""
    
    def write(self, key, value):
        filepath = self.folder / f"{key}.txt"
        filepath.write_text(str(value), encoding='utf-8')


class FieldEntry:
    def __init__(self, parent, row, key, label, shared):
        self.key = key
        self.shared = shared
        self.editing = False
        self.value_before_edit = ""
        
        ttk.Label(parent, text=label).grid(row=row, column=0, padx=10, pady=8, sticky='w')
        
        self.var = tk.StringVar(value=shared.read(key))
        self.entry = ttk.Entry(parent, textvariable=self.var, width=20)
        self.entry.grid(row=row, column=1, padx=10, pady=8)
        
        self.entry.bind('<FocusIn>', self.on_focus_in)
        self.entry.bind('<FocusOut>', self.on_focus_out)
        self.entry.bind('<Return>', self.on_validate)
        self.entry.bind('<Escape>', self.on_cancel)
    
    def on_focus_in(self, e):
        self.editing = True
        self.value_before_edit = self.var.get()
    
    def on_focus_out(self, e):
        self.editing = False
        self.shared.write(self.key, self.var.get())
    
    def on_validate(self, e):
        self.editing = False
        self.shared.write(self.key, self.var.get())
        self.entry.master.focus_set()
    
    def on_cancel(self, e):
        self.var.set(self.value_before_edit)
        self.editing = False
        self.entry.master.focus_set()
    
    def refresh(self):
        if not self.editing:
            file_value = self.shared.read(self.key)
            if self.var.get() != file_value:
                self.var.set(file_value)


class TextFieldEntry:
    def __init__(self, parent, row, key, label, shared, height=8):
        self.key = key
        self.shared = shared
        self.editing = False
        self.value_before_edit = ""
        
        ttk.Label(parent, text=label).grid(row=row, column=0, padx=10, pady=8, sticky='nw')
        
        self.text = tk.Text(parent, width=30, height=height)
        self.text.grid(row=row, column=1, padx=10, pady=8)
        self.text.insert('1.0', shared.read(key))
        
        self.text.bind('<FocusIn>', self.on_focus_in)
        self.text.bind('<FocusOut>', self.on_focus_out)
        self.text.bind('<Escape>', self.on_cancel)
    
    def on_focus_in(self, e):
        self.editing = True
        self.value_before_edit = self.text.get('1.0', 'end-1c')
    
    def on_focus_out(self, e):
        self.editing = False
        self.shared.write(self.key, self.text.get('1.0', 'end-1c'))
    
    def on_cancel(self, e):
        self.text.delete('1.0', 'end')
        self.text.insert('1.0', self.value_before_edit)
        self.editing = False
        self.text.master.focus_set()
    
    def refresh(self):
        if not self.editing:
            file_value = self.shared.read(self.key)
            current_value = self.text.get('1.0', 'end-1c')
            if current_value != file_value:
                self.text.delete('1.0', 'end')
                self.text.insert('1.0', file_value)


def add_help_label(parent):
    help_text = "Entrée = valider  |  Échap = annuler"
    label = ttk.Label(parent, text=help_text, foreground="gray", font=("Arial", 9, "italic"))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 15), sticky='w')


class InventaireInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("LDVELH - Inventaire")
        self.root.geometry("450x750+100+100")
        
        self.shared = SharedFiles()
        self.fields = []
        
        # Aide en haut
        add_help_label(root)
        
        field_defs = [
            ("endurance_depart", "Endurance départ"),
            ("endurance", "Endurance"),
            ("habilete_depart", "Habileté départ"),
            ("habilete", "Habileté"),
            ("chance_depart", "Chance départ"),
            ("chance", "Chance"),
            ("provisions", "Provisions"),
        ]
        
        # Row 0 = aide, donc on commence à row 1
        for i, (key, label) in enumerate(field_defs):
            field = FieldEntry(root, i + 1, key, label, self.shared)
            self.fields.append(field)
        
        # Objets
        row = len(field_defs) + 1
        objets_field = TextFieldEntry(root, row, "objets", "Objets", self.shared, height=10)
        self.fields.append(objets_field)
        
        # Notes
        row += 1
        notes_field = TextFieldEntry(root, row, "notes", "Notes", self.shared, height=10)
        self.fields.append(notes_field)
        
        self.start_refresh()
    
    def start_refresh(self):
        def loop():
            while True:
                for field in self.fields:
                    self.root.after(0, field.refresh)
                time.sleep(0.5)
        threading.Thread(target=loop, daemon=True).start()


class CombatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("LDVELH - Combat")
        self.root.geometry("400x350+600+100")
        
        self.shared = SharedFiles()
        self.fields = []
        
        # Aide en haut
        add_help_label(root)
        
        field_defs = [
            ("endurance", "Endurance"),
            ("habilete", "Habileté"),
            ("nom_ennemi", "Nom ennemi"),
            ("endurance_ennemi", "Endurance ennemi"),
            ("habilete_ennemi", "Habileté ennemi"),
        ]
        
        # Row 0 = aide, donc on commence à row 1
        for i, (key, label) in enumerate(field_defs):
            field = FieldEntry(root, i + 1, key, label, self.shared)
            self.fields.append(field)
        
        self.start_refresh()
    
    def start_refresh(self):
        def loop():
            while True:
                for field in self.fields:
                    self.root.after(0, field.refresh)
                time.sleep(0.5)
        threading.Thread(target=loop, daemon=True).start()


if __name__ == "__main__":
    root1 = tk.Tk()
    root2 = tk.Toplevel(root1)
    
    InventaireInterface(root1)
    CombatInterface(root2)
    
    root1.mainloop()