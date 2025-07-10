import customtkinter as ctk
from Commands.constants import FONT_BASE
from Commands.paper_printed import print_delivery_paper


def open_delivery_table(notebook):
    notebook.add("Entregas")

    clientdelivery_text = ctk.CTkLabel(notebook.tab("Entregas"), width=150, font=(FONT_BASE, 20, "bold"),
                                       text="Cliente:")
    clientdelivery_text.grid(row=0, column=0, pady=2)
    clientdelivery_entry = ctk.CTkEntry(notebook.tab("Entregas"), width=150, placeholder_text="Cliente",
                                        fg_color="white",
                                        border_color="black", border_width=2, corner_radius=8, font=(FONT_BASE, 15))
    clientdelivery_entry.grid(row=0, column=1, pady=2)

    numberdelivery_text = ctk.CTkLabel(notebook.tab("Entregas"), width=120, font=(FONT_BASE, 20, "bold"),
                                       text="Telefone:")
    numberdelivery_text.grid(row=1, column=0, pady=2)
    numberdelivery_entry = ctk.CTkEntry(notebook.tab("Entregas"), width=150, placeholder_text="Num. telefone",
                                        fg_color="white", border_color="black",
                                        border_width=2, corner_radius=8, font=(FONT_BASE, 15))
    numberdelivery_entry.grid(row=1, column=1, pady=2)

    adress_text = ctk.CTkLabel(notebook.tab("Entregas"), width=270, font=(FONT_BASE, 20, "bold"), text="Endereço:")
    adress_text.grid(row=2, column=0, pady=3, columnspan=2)
    adress_entry = ctk.CTkEntry(notebook.tab("Entregas"), width=290, height=25, fg_color="white", border_color="black",
                                border_width=2, corner_radius=8, font=(FONT_BASE, 12, "bold"), placeholder_text="Endereço do Cliente")
    adress_entry.grid(row=3, column=0, pady=2, columnspan=2)

    items_text = ctk.CTkLabel(notebook.tab("Entregas"), width=270, font=(FONT_BASE, 20, "bold"), text="Produtos Comprados:")
    items_text.grid(row=4, column=0, pady=3, columnspan=2)
    items_entry = ctk.CTkEntry(notebook.tab("Entregas"), width=290, height=25, fg_color="white", border_color="black",
                               border_width=2, corner_radius=8, font=(FONT_BASE, 10, "bold"),
                               placeholder_text="Recomendo usar / ou | para quebrar a linha")
    items_entry.grid(row=5, column=0, pady=6, columnspan=2)

    value_text = ctk.CTkLabel(notebook.tab("Entregas"), width=120, font=(FONT_BASE, 20, "bold"), text="Valor Total:")
    value_text.grid(row=6, column=0, pady=2)
    value_entry = ctk.CTkEntry(notebook.tab("Entregas"), width=150, placeholder_text="R$:---,--", fg_color="white",
                               border_color="black", border_width=2, corner_radius=8, font=(FONT_BASE, 15))
    value_entry.grid(row=6, column=1, pady=2)

    pag_var = ctk.StringVar(value="----")
    din_radio = ctk.CTkRadioButton(notebook.tab("Entregas"), text="Dinheiro", variable=pag_var, value="Dinheiro",
                                   width=50)
    din_radio.grid(row=7, column=0, pady=7)
    pix_radio = ctk.CTkRadioButton(notebook.tab("Entregas"), text="Pix", variable=pag_var, value="Pix", width=50)
    pix_radio.grid(row=7, column=0, pady=7, columnspan=2)
    din_radio = ctk.CTkRadioButton(notebook.tab("Entregas"), text="Cartão", variable=pag_var, value="Cartão", width=50)
    din_radio.grid(row=7, column=1, pady=7)

    obsdelivery_text = ctk.CTkLabel(notebook.tab("Entregas"), width=120, font=(FONT_BASE, 20, "bold"),
                                    text="Observações:")
    obsdelivery_text.grid(row=8, column=0, columnspan=2)
    obsdelivery_entry = ctk.CTkEntry(notebook.tab("Entregas"), width=290,
                                     placeholder_text="Tem alguma informação a mais?",
                                     fg_color="white", border_color="black", border_width=2, corner_radius=8,
                                     font=(FONT_BASE, 11, "bold"))
    obsdelivery_entry.grid(row=9, column=0, columnspan=2)

    submitdelivery_buttom = ctk.CTkButton(notebook.tab("Entregas"), width=290, corner_radius=10, border_width=2,
                                          font=(FONT_BASE, 21, "bold"),
                                          text="Realizar Entrega", command=lambda: print_delivery_paper(
            {
                "client": clientdelivery_entry.get(),
                "number": numberdelivery_entry.get(),
                "adress": adress_entry.get(),
                "items": items_entry.get(),
                "value": value_entry.get(),
                "payment": pag_var.get(),
                "obs": obsdelivery_entry.get()
            }))
    submitdelivery_buttom.grid(row=10, column=0, columnspan=2, pady=14)

