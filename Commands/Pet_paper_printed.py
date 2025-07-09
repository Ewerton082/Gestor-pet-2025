from .Database import data_insert


def print_pet_paper(Data):
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

    formated_text = template.format(**Data)
    data_insert(Data)


