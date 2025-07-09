from tkcalendar import DateEntry
import customtkinter as ctk
from Commands.Database import filter_date
from tkinter.ttk import Treeview
from Commands.Database import today_data


def open_daily_table(notebook):
    notebook.add("Diario")

    date_filter_entry = DateEntry(notebook.tab("Diario"), date_pattern="d/m/y", cursor="hand2", fg_color="white",
                                  border_color="black", border_width=2, corner_radius=8, font=("Times", 13, "bold"))
    date_filter_entry.grid(row=0, column=0, pady=6, padx=1)

    date_filter_submit = ctk.CTkButton(notebook.tab("Diario"), width=120, corner_radius=10, border_width=2,
                                       font=("Times", 17, "bold"), text="Filtrar por data",
                                       command=lambda: filter_date(date_filter_entry.get(), pets_table))
    date_filter_submit.grid(row=0, column=1, padx=3, pady=6)

    pets_table = Treeview(notebook.tab("Diario"), columns=["Posição", "Dono", "Telefone", "Pet", "Procedimento"],
                          show="headings")
    pets_table.grid(row=1, column=0, columnspan=2, pady=4)

    pets_table.column("Posição", width=25)
    pets_table.heading("Posição", text="nº")

    pets_table.column("Dono", width=60)
    pets_table.heading("Dono", text="Dono")

    pets_table.column("Telefone", width=75)
    pets_table.heading("Telefone", text="Celular")

    pets_table.column("Pet", width=70)
    pets_table.heading("Pet", text="Pet")

    pets_table.column("Procedimento", width=100)
    pets_table.heading("Procedimento", text="Procedimento")

    today_data(pets_table)
