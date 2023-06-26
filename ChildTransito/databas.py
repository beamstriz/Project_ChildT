import sqlite3


class Data_base():

    def __init__(self, name = 'system.db') -> None:
        self.name == name
        self.connection = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)


    def close_connection(self):
        try: 
            self.connection.close()

        except:
            pass

    def table_perguntas(self):
        cursor = self.connection.cursos()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Perguntas(
                                ID INTENGER NOT NULL,
                                pergunta text,
                                nivel text,
                                resposta1 text
                                resposta2 text,
                                resposta3 text,
                                resposta4 text,
                                respostaCerta text,

                                PRIMARY KEY "


                        

                                

                        )
                        """)
    
    def selecionar_pergunta(self, nivel):

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Perguntas")
            perguntas = cursor.fetchall()
            return perguntas
        except Exception as e:
            print(e)
            return e