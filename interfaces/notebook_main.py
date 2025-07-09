import customtkinter as ctk
from PIL import Image
from .pets_paper import open_pet_table
from .daily_pets import open_daily_table
from .delivery_paper import open_delivery_table


def create_interface(screen):

    title = ctk.CTkLabel(screen, text="Pets Food", font=("Tahoma", 32, "bold"),
                         width=250, height=35,)
    title.grid(row=1, column=1, pady=10)

    config_image = ctk.CTkImage(Image.open("assets/configs.ico"), size=(35,35))
    config = ctk.CTkButton(screen, image=config_image, width=30, height=35,
                           text="", fg_color="transparent", hover_color="#d9d9d9",
                           command=print("Config"))
    config.grid(row=1, column=2, pady=10)

    notebook = ctk.CTkTabview(screen, width=375, height=400,
                              corner_radius=20, border_width=2,
                              fg_color="#c4c2c2", segmented_button_fg_color="grey")
    notebook.grid(row=2, column=1, columnspan=2, pady=5, padx=2)

    open_pet_table(notebook)
    open_daily_table(notebook)
    open_delivery_table(notebook)


