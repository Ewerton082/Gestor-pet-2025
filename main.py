import customtkinter as ctk
from datetime import  datetime
from interfaces.notebook_main import create_interface


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("370x515")
    app.resizable(False,False)
    app.title(f"Pets Food   |  {datetime.now().strftime('%d/%m/%Y')}")

    create_interface(app)

    app.mainloop()
