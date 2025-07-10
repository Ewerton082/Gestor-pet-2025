import tkinter as tk
import customtkinter as ctk
from Commands.constants import PRINTERS, FONT_BASE


def open_screen(master):
    pass
    config_screen = tk.Toplevel(master,width=380, height=300,takefocus=True, bg="white",)
    config_screen.iconbitmap("assets/configs.ico")
    config_screen.title("Ajustar Configurações")

    printers_label = ctk.CTkLabel(config_screen, width=140, font=(FONT_BASE,23, "bold"), text=)



