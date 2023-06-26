from PySide6.QtWidgets import *
from ui_main import Ui_MainWindow
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base , Questionarios


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ChildTransito")
        engine = create_engine('mysql+mysqlconnector://root:12345@localhost/bancochild', echo=True)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        questionario = Questionarios(
        pergunta='QUAL O ORGÃO BRASILEIRO É RESPONSÁVEL NACIONALMENTE PELO TRÂNSITO?',
        nivel='FACIL',
        alternativa1='IBGE',
        alternativa2='SEMUTRAN',
        alternativa3='DENATRAN',
        alternativa4='INSS',
        resposta='3'
    )
        

        # Adiciona o questionario à sessão
        session.add(questionario)

        # Commit para salvar o registro no banco de dados
        session.commit()

        resultado = session.query(Questionarios).filter_by(nivel='FACIL').first()

        print(str(resultado.pergunta) + " teste")

        # Fechar a sessão
        session.close()
        # appIcons == QIcon()


        ###############################################
        #Páginas do sistema
        self.btn_inicio.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_inicio))
        self.btn_play.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_game))

        self.btn_resp_1 = QLabel("Olá",self)

    # def jogar(self):



if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
