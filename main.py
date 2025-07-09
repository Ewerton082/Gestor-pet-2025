import customtkinter as ctk
from datetime import datetime
from interfaces.notebook_main import create_interface


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("380x530")
    app.resizable(False, False)
    app.title(f"Pets Food   |  {datetime.now().strftime('%d/%m/%Y')}")
    app.iconbitmap("assets/icon.ico")

    create_interface(app)

    app.mainloop()
