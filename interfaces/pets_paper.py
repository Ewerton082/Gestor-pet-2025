import customtkinter as ctk
from Commands.paper_printed import print_pet_paper
from datetime import datetime
from Commands.constants import FONT_BASE


POSITION_LIST = [
    '1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º',
    '10º', '11º', '12º', '13º', '14º', '15º', '16º', '17º',
    '18º', '19º', '20º', '21º', '22º', '23º', '24º', '25º']

PROCEDIMENT_LIST = [
    'Banho e Higiênica', 'Tosa Padrão 7', 'Tosa Padrão 10',
    'Tosa Completa 7', 'Tosa Completa 10', 'Tosa Bebê']


def open_pet_table(notebook):
    notebook.add("Pets")

    client_text = ctk.CTkLabel(notebook.tab("Pets"), width=150, font=(FONT_BASE, 23, "bold"), text="Dono:")
    client_text.grid(row=0, column=0, pady=3)
    client_entry = ctk.CTkEntry(notebook.tab("Pets"), width=170, placeholder_text="Nome do Dono", fg_color="white",
                                border_color="black", border_width=2, corner_radius=8, font=(FONT_BASE, 18))
    client_entry.grid(row=0, column=1, pady=3)

    number_text = ctk.CTkLabel(notebook.tab("Pets"), width=150, font=(FONT_BASE, 23, "bold"), text="Telefone:")
    number_text.grid(row=1, column=0, pady=3)
    number_entry = ctk.CTkEntry(notebook.tab("Pets"), width=170, placeholder_text="Num. telefone", fg_color="white",
                                border_color="black", border_width=2, corner_radius=8, font=(FONT_BASE, 18))
    number_entry.grid(row=1, column=1, pady=3)

    pet_text = ctk.CTkLabel(notebook.tab("Pets"), width=150, font=(FONT_BASE, 23, "bold"), text="Pet:")
    pet_text.grid(row=2, column=0, pady=3)
    pet_entry = ctk.CTkEntry(notebook.tab("Pets"), width=170, placeholder_text="Nome do Pet", fg_color="white",
                             border_color="black", border_width=2, corner_radius=8, font=(FONT_BASE, 18))
    pet_entry.grid(row=2, column=1, pady=3)

    position_text = ctk.CTkLabel(notebook.tab("Pets"), width=150, font=(FONT_BASE, 23, "bold"), text="Ordem:")
    position_text.grid(row=3, column=0, pady=3)
    position_entry = ctk.CTkComboBox(notebook.tab("Pets"), width=170, fg_color="white", border_color="black",
                                     border_width=2, corner_radius=8, values=POSITION_LIST, font=(FONT_BASE, 18),
                                     button_color="#44acf5", button_hover_color="#318bc6", justify="center",
                                     dropdown_hover_color="#7bc2f2", dropdown_font=(FONT_BASE, 10, "bold"))
    position_entry.grid(row=3, column=1, pady=3)

    procediment_text = ctk.CTkLabel(notebook.tab("Pets"), width=150, font=(FONT_BASE, 23, "bold"), text="Processo:")
    procediment_text.grid(row=4, column=0, pady=3)
    procediment_entry = ctk.CTkComboBox(notebook.tab("Pets"), width=170, fg_color="white", border_color="black",
                                        border_width=2, corner_radius=8, values=PROCEDIMENT_LIST, font=(FONT_BASE, 14),
                                        button_color="#44acf5", button_hover_color="#318bc6", justify="center",
                                        dropdown_hover_color="#7bc2f2", dropdown_font=(FONT_BASE, 14, "bold"))
    procediment_entry.grid(row=4, column=1, pady=3)

    obs_text = ctk.CTkLabel(notebook.tab("Pets"), width=250, font=(FONT_BASE, 23, "bold"), text="Observações Gerais:")
    obs_text.grid(row=5, column=0, pady=7, columnspan=2, padx=25)
    obs_entry = ctk.CTkTextbox(notebook.tab("Pets"), width=300, height=55, fg_color="white", border_color="black",
                               border_width=2, corner_radius=8, font=(FONT_BASE, 16))
    obs_entry.grid(row=6, column=0, pady=3, columnspan=2)

    submit_buttom = ctk.CTkButton(notebook.tab("Pets"), width=300, corner_radius=10, border_width=2,
                                  font=(FONT_BASE, 24, "bold"), text="Imprimir Comanda",
                                  command=lambda: ((print_pet_paper(
                                      {
                                          "client": client_entry.get(),
                                          "number": number_entry.get(),
                                          "pet": pet_entry.get(),
                                          "position": position_entry.get(),
                                          "process": procediment_entry.get(),
                                          "obs": obs_entry.get('0.0', 'end'),
                                          "date": datetime.now().strftime("%d/%m/%Y"),
                                          "hour": datetime.now().strftime("%H:%M")
                                      }),),

                                                   client_entry.delete(0, 50),
                                                   client_entry.focus(),
                                                   number_entry.delete(0, 50),
                                                   pet_entry.delete(0, 50),
                                                   obs_entry.delete("0.0", "end")
                                  )
                                  )
    submit_buttom.grid(row=7, column=0, columnspan=2, pady=7)

