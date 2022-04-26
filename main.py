from banco import criacao_banco
from controle import cadastrar_acolhido, verCadastro, excluirDado
import sqlite3
from PyQt5 import uic, QtWidgets

criacao_banco()

banco = sqlite3.connect('pvn_banco.bd')

"""
app = QtWidgets.QApplication([])

acolhido = uic.loadUi("formAcolhido.ui")
cadastrado = uic.loadUi("formCadastrado.ui")

acolhido.btnCadastrar.clicked.connect(cadastrar)
acolhido.btnVer.clicked.connect(verCadastro)
cadastrado.btnExcluir.clicked.connect(excluirDado)

acolhido.show()
app.exec()
"""
