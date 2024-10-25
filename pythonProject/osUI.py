import customtkinter as ctk
from PIL import Image, ImageTk
import threading
from osService import run_program  # Import service function

# Pencereyi ekranın ortasına konumlandıran fonksiyon
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

# Buton oluşturan fonksiyon
def create_button(app, image, command, x, y, hover_color, text):
    button = ctk.CTkButton(
        app,
        image=image,
        text="",
        command=command,
        width=400,
        height=600,
        fg_color="transparent",
        hover_color=hover_color
    )
    button.place(relx=x, rely=y, anchor='center')

    # Metin etiketi oluşturma
    text_label = ctk.CTkLabel(
        app,
        text=text,
        font=("Segoe UI", 25, "bold"),
        text_color=hover_color,
        bg_color="transparent"
    )
    text_label.place(relx=x, rely=y + 0.3, anchor='center')

    # Hover efektleri
    def on_enter(event):
        button.configure(fg_color=hover_color)
        text_label.configure(text_color="black", bg_color=hover_color)

    def on_leave(event):
        button.configure(fg_color="transparent")
        text_label.configure(text_color=hover_color, bg_color="transparent")

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button, text_label


def create_ui():
    app = ctk.CTk()
    app.title("İşletim Sistemi Seçimi")
    app.geometry("800x500")
    center_window(app, 800, 500)

    windows_image = Image.open("windows.png")
    ubuntu_image = Image.open("ubu.png")

    windows_image = windows_image.resize((200, 200))
    ubuntu_image = ubuntu_image.resize((200, 200))

    windows_photo = ImageTk.PhotoImage(windows_image)
    ubuntu_photo = ImageTk.PhotoImage(ubuntu_image)

    windows_bg = ctk.CTkLabel(app, image=windows_photo, text="", bg_color="transparent")
    windows_bg.place(relx=0.25, rely=0.4, anchor='center')

    ubuntu_bg = ctk.CTkLabel(app, image=ubuntu_photo, text="", bg_color="transparent")
    ubuntu_bg.place(relx=0.75, rely=0.4, anchor='center')

    def on_windows_click():
        threading.Thread(target=lambda: run_program(app, "Windows")).start()

    def on_ubuntu_click():
        threading.Thread(target=lambda: run_program(app, "Ubuntu")).start()

    windows_button, windows_text_label = create_button(app, windows_photo, on_windows_click, 0.25, 0.4, "#0078D4",
                                                       "Windows®")
    ubuntu_button, ubuntu_text_label = create_button(app, ubuntu_photo, on_ubuntu_click, 0.75, 0.4, "#F37C22",
                                                     "Ubuntu®")

    return app