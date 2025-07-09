import sqlite3

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


def data_insert(Data):
    Cursor.execute(f"""INSERT INTO Clientes_PET VALUES('{Data["date"]}',
                    '{Data["position"]}', '{Data["client"]}', '{Data["number"]}',
                    '{Data["pet"]}', '{Data["process"]}') """)
    banco.commit()
