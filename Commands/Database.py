import sqlite3
from datetime import datetime

banco = sqlite3.connect("database/Clients_pet.Db")
Cursor = banco.cursor()
BD_COMMAND = "SELECT * FROM Clientes_Pet WHERE Data = ?"

banco.execute('''CREATE TABLE IF NOT EXISTS Clientes_PET(
                  Data TEXT,
                  Posicao TEXT,
                  Dono TEXT,
                  Número TEXT,
                  Pet TEXT,
                  Procedimento TEXT
                  )'''
              )


def data_insert(data):
    Cursor.execute(f"""INSERT INTO Clientes_PET VALUES('{data["date"]}',
                    '{data["position"]}', '{data["client"]}', '{data["number"]}',
                    '{data["pet"]}', '{data["process"]}') """)
    banco.commit()


def filter_date(date, treeview):
    for item in treeview.get_children():
        treeview.delete(item)

    date_obj = datetime.strptime(date, "%d/%m/%Y")
    formated_date = date_obj.strftime("%d/%m/%Y")

    for data in Cursor.execute(BD_COMMAND, (formated_date,)):
        treeview.delete()
        real_data = [data[1], data[2], data[3], data[4], data[5], ]
        treeview.insert(parent="", index=0, values=real_data)


def today_data(treeview):

    today_date = datetime.now().strftime("%d/%m/%Y")

    for data in Cursor.execute(BD_COMMAND, (today_date,)):
        treeview.delete()
        real_data = [data[1], data[2], data[3], data[4], data[5], ]
        treeview.insert(parent="", index=0, values=real_data)
