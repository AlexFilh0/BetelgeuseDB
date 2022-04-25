from PyQt5 import uic,QtWidgets
import mysql.connector

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="diamond10",
    database="pvn_v2"
)


def cadastrar():
    nome = acolhido.edtNome.text()
    cpf = acolhido.edtCPF.text()

    comando_SQL = "INSERT INTO acolhidos (nome, cpf) VALUES (%s,%s)"
    dados = (str(nome), str(cpf))
    cursor = banco.cursor()
    cursor.execute(comando_SQL, dados)
    banco.commit()

    acolhido.edtNome.setText("")
    acolhido.edtCPF.setText("")
    acolhido.lblAviso.setText(f"{nome} CADASTRADO COM SUCESSO")

def verCadastro():
    cadastrado.show()

    comando_SQL = "SELECT * FROM acolhidos"
    cursor = banco.cursor()
    cursor.execute(comando_SQL)
    lidos = cursor.fetchall()


    cadastrado.tabela.setRowCount(len(lidos))
    cadastrado.tabela.setColumnCount(3)

    for i in range(len(lidos)):
        for j in range(3):
            cadastrado.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

def excluirDado():
    linha = cadastrado.tabela.currentRow()
    cadastrado.tabela.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM acolhidos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM acolhidos WHERE id="+ str(valor_id))


app=QtWidgets.QApplication([])

acolhido=uic.loadUi("formAcolhido.ui")
cadastrado=uic.loadUi("formCadastrado.ui")

acolhido.btnCadastrar.clicked.connect(cadastrar)
acolhido.btnVer.clicked.connect(verCadastro)
cadastrado.btnExcluir.clicked.connect(excluirDado)

acolhido.show()
app.exec()
