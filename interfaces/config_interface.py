import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from Commands.constants import PRINTERS, FONT_BASE
from config.settings import set_settings


def select_dir(label, screen):
    file_dir = filedialog.askdirectory()
    if file_dir:
        label.configure(text=file_dir)
    screen.focus_set()


def open_screen(master):
    pass
    config_screen = tk.Toplevel(master, width=380, height=300, takefocus=True, bg="white")
    config_screen.iconbitmap("assets/configs.ico")
    config_screen.title("Ajustar Configurações")
    config_screen.focus_set()

    printers_label = ctk.CTkLabel(config_screen, width=140, font=(FONT_BASE, 14, "bold"), text="Escolha a Impressora:")
    printers_label.grid(row=0, column=0, pady=7, padx=7)

    printers_choice = ctk.CTkComboBox(config_screen, width=200, fg_color="white", border_color="black",
                                      border_width=2, corner_radius=8, values=PRINTERS, font=(FONT_BASE, 12),
                                      button_color="#44acf5", button_hover_color="#318bc6", justify="center",
                                      dropdown_hover_color="#7bc2f2", dropdown_font=(FONT_BASE, 12))
    printers_choice.grid(row=0, column=1, pady=7, padx=7)

    print_dir_label = ctk.CTkLabel(config_screen, width=200, font=(FONT_BASE, 10), bg_color="#afb8ba",
                                   corner_radius=20, text="")
    print_dir_label.grid(row=1, column=1, pady=7, padx=7)

    print_dir_buttom = ctk.CTkButton(config_screen, width=140, corner_radius=10, border_width=1, font=(FONT_BASE, 16),
                                     text="Selecionar Diretorio",
                                     command=lambda: select_dir(print_dir_label, config_screen))
    print_dir_buttom.grid(row=1, column=0, pady=7, padx=7)

    confirm_changes = ctk.CTkButton(config_screen, width=300, corner_radius=10, border_width=2,
                                    text="Salvar Mudanças", font=(FONT_BASE, 20, "bold"),
                                    command=lambda: (set_settings(printers_choice.get(), print_dir_label.cget("text")), config_screen.destroy()))
    confirm_changes.grid(row=2, column=0, columnspan=2, padx=5, pady=15)
