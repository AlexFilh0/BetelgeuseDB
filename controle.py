from PyQt5 import uic,QtWidgets
import sqlite3

from banco import criacao_banco


numero_id = 0

criacao_banco()

banco = sqlite3.connect('pvn_banco.bd')


def cadastrar_acolhido():
    nome = acolhido.edtNome.text()
    rg = acolhido.edtRG.text()
    cpf = acolhido.edtCPF.text()
    nascimento = acolhido.edtNascimento.text()
    estado_civil = acolhido.edtECivil.text()
    qtd_filhos = acolhido.edtFilho.text()
    trabalho = acolhido.edtTrabalho.text()
    posto_saude = acolhido.edtPSaude.text()
    lazer = acolhido.edtLazer.text()
    substancia_favorita = acolhido.edtSubst.text()
    usoAno = acolhido.edtTUso.text()
    religiao = acolhido.edtReligiao.text()
    responsavel = acolhido.edtResponsavel.text()
    rg_responsavel = acolhido.edtReRG.text()
    cpf_responsavel = acolhido.edtReCPF.text()
    vinculo = acolhido.edtVinculo.text()
    entrada = acolhido.edtEntrada.text()
    saida = acolhido.edtSaida.text()
    obs = acolhido.edtObs.text()

    cursor = banco.cursor()
    cursor.execute('''INSERT INTO acolhidos (nome, rg, cpf, nascimento, estado_civil,
                    qtd_filhos, trabalho, posto_saude, lazer, substancia_favorita,
                    uso_desde_idade, religiao, responsavel, rg_responsavel, cpf_responsavel,
                    vinculo_responsavel, entrada, saida, obs)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (str(nome), str(rg), str(cpf), str(nascimento),
                                      str(estado_civil), int(qtd_filhos), str(trabalho),
                                      str(posto_saude), str(lazer), str(substancia_favorita),
                                      int(usoAno), str(religiao), str(responsavel), str(rg_responsavel),
                                      str(cpf_responsavel), str(vinculo), str(entrada), str(saida), str(obs)))
    banco.commit()


def medicamentos_abrir():
    cadMedicamento.show()
    c = banco.cursor()


    comando_SQL = ("""SELECT * FROM medicamentos""")
    c.execute(comando_SQL)
    lidos = c.fetchall()
    cadMedicamento.tabelaCadastro.setRowCount(len(lidos))
    cadMedicamento.tabelaCadastro.setColumnCount(4)

    for i in range(len(lidos)):
        for j in range(4):
            cadMedicamento.tabelaCadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))


def cadastrar_medicamento():
    cadMedicamento.show()

    nome = cadMedicamento.edtNomeMed.text()
    espec = cadMedicamento.edtEsp.text()
    obs = cadMedicamento.edtObs.text()

    c = banco.cursor()

    c.execute('''INSERT INTO medicamentos (nome, especificacoes, obs)
                VALUES (?, ?, ?)''',(str(nome), str(espec), str(obs)))
    banco.commit()

    comando_SQL = ("""SELECT * FROM medicamentos""")
    c.execute(comando_SQL)
    lidos = c.fetchall()
    cadMedicamento.tabelaCadastro.setRowCount(len(lidos))
    cadMedicamento.tabelaCadastro.setColumnCount(4)

    for i in range(len(lidos)):
        for j in range(4):
            cadMedicamento.tabelaCadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))


def entradas_abrir():
    cadEntradaMedicamento.show()
    c = banco.cursor()

    comando_SQL = ("""SELECT m.id_medicamento, m.nome, m.especificacoes, e.qtd_entrada, e.data_entrada, e.obs FROM medicamentos as m
    JOIN entradas_medicamentos as e ON m.id_medicamento = e.id_medicamento ORDER BY data_entrada DESC;""")
    c.execute(comando_SQL)
    lidos = c.fetchall()
    cadEntradaMedicamento.tabelaEntrada.setRowCount(len(lidos))
    cadEntradaMedicamento.tabelaEntrada.setColumnCount(6)

    for i in range(len(lidos)):
        for j in range(6):
            cadEntradaMedicamento.tabelaEntrada.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

def cadastrar_entrada():
    id_medicamento = cadEntradaMedicamento.edtIdMed.text()
    qtd_entrada = cadEntradaMedicamento.edtQtdMed.text()
    data_entrada = cadEntradaMedicamento.edtDataMed.text()
    obs = cadEntradaMedicamento.edtObs.text()

    c = banco.cursor()

    c.execute("""INSERT INTO entradas_medicamentos (id_medicamento, qtd_entrada, data_entrada, obs)
                VALUES (?, ?, ?, ?)""", (id_medicamento, qtd_entrada, data_entrada, obs))

    comando_SQL = ("""SELECT m.id_medicamento, m.nome, m.especificacoes, e.qtd_entrada, e.data_entrada, e.obs FROM medicamentos as m
        JOIN entradas_medicamentos as e ON m.id_medicamento = e.id_medicamento ORDER BY data_entrada DESC;""")
    c.execute(comando_SQL)
    lidos = c.fetchall()
    cadEntradaMedicamento.tabelaEntrada.setRowCount(len(lidos))
    cadEntradaMedicamento.tabelaEntrada.setColumnCount(6)

    for i in range(len(lidos)):
        for j in range(6):
            cadEntradaMedicamento.tabelaEntrada.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))


def tratamentos_abrir():
    tratamento.show()

def cadastrar_tratamento():

    print('erros aqui não')

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
    excluir = cadastrado.edtExcluir.text()
    cadastrado.tabela.removeRow(int(excluir)-1)

    cursor = banco.cursor()

    cursor.execute("DELETE FROM acolhidos WHERE id_acolhido="+ str(excluir))
    banco.commit()

    #Colocar label para atualizar

def visualizarDado():
    visual.show()

    idVer = cadastrado.edtVisualizar.text()
    cursor = banco.cursor()

    cursor.execute("""SELECT nome, rg, cpf, nascimento,
     estado_civil, qtd_filhos, trabalho, posto_saude,
     lazer, substancia_favorita, uso_desde_idade,
     religiao, responsavel, rg_responsavel,
     cpf_responsavel, vinculo_responsavel,
     entrada, saida, obs FROM acolhidos WHERE id_acolhido=?""", (str(idVer)))

    infoGet = cursor.fetchone()
    visual.lblNome.setText(infoGet[0])
    visual.lblRG.setText(infoGet[1])
    visual.lblCPF.setText(infoGet[2])
    visual.lblNascimento.setText(infoGet[3])
    visual.lblECivil.setText(infoGet[4])
    visual.lblFilhos.setText(str(infoGet[5]))
    visual.lblTrabalho.setText(infoGet[6])
    visual.lblPSaude.setText(infoGet[7])
    visual.lblLazer.setText(infoGet[8])
    visual.lblSubst.setText(infoGet[9])
    visual.lblIdade.setText(str(infoGet[10]))
    visual.lblReligiao.setText(infoGet[11])
    visual.lblResponsavel.setText(infoGet[12])
    visual.lblReRG.setText(infoGet[13])
    visual.lblReCPF.setText(infoGet[14])
    visual.lblVinculo.setText(infoGet[15])
    visual.lblEntrada.setText(infoGet[16])
    visual.lblSaida.setText(infoGet[17])
    visual.lblOBS.setText(infoGet[18])

app = QtWidgets.QApplication([])

acolhido = uic.loadUi("formAcolhido.ui")
cadastrado = uic.loadUi("formCadastrado.ui")
visual = uic.loadUi("formVisualizar.ui")
cadMedicamento = uic.loadUi("formCadMedicamento.ui")
cadEntradaMedicamento = uic.loadUi("formEntradaMedicamento.ui")
tratamento = uic.loadUi("formTratamento.ui")


acolhido.btnCadastrar.clicked.connect(cadastrar_acolhido)
acolhido.btnVer.clicked.connect(verCadastro)
acolhido.btnMedicamento.clicked.connect(medicamentos_abrir)
acolhido.btnEntradaMed.clicked.connect(entradas_abrir)
acolhido.btnTratamento.clicked.connect(tratamentos_abrir)

cadastrado.btnExcluir.clicked.connect(excluirDado)
cadastrado.btnVisualizar.clicked.connect(visualizarDado)

cadMedicamento.btnCadastrarMed.clicked.connect(cadastrar_medicamento)

cadEntradaMedicamento.btnCadastrarMed.clicked.connect(cadastrar_entrada)

tratamento.btnCadastrarTratamento.clicked.connect(cadastrar_tratamento)


acolhido.show()

app.exec()
