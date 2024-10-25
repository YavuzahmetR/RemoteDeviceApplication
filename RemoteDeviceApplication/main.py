import tkinter as tk
from ui import create_ui  # Assuming create_ui is defined in ui.py

def main():
    root = tk.Tk()
    create_ui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
