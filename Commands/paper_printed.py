import os
from .Database import data_insert


def real_print(qtd):
    print("Imprimir aqui")

def print_pet_paper(data: dict):
    """
    Imprimiremos a comanda dos pets

    Args:
        um dict com as seguintes informações:
        [client, number, pet, position, procediment, obs]

    Returns:
         Uma Comanda impressa na impressora selecionada
    """

    with open("printed_files/template_pet_paper.txt", "r", encoding="utf-8") as file:
        template = file.read()

    formated_text = template.format(**data)
    data_insert(data)
    try:
        os.makedirs("comandas")
    except:
        pass
    finally:
        archive = open("comandas/text_writed.txt", "w")
        archive.write(formated_text)
        archive.close()
        real_print(1)



def print_delivery_paper(data: dict):
    """
    Imprimiremos Aqui os Papeis das Entregas

    Args:
        Um dict com as seguintes informações
        {client, number, adress, items, value, payment, obs}

    Returns:
        Duas Comandas Impressas na Impressora selecionada
    """

    with open("printed_files/template_entrega.txt", "r", encoding="utf-8") as file:
        template = file.read()

    formated_text = template.format(**data)
    try:
        os.makedirs("comandas")
    except:
        pass
    finally:
        archive = open("comandas/text_writed.txt", "w")
        archive.write(formated_text)
        archive.close()
        real_print(2)
