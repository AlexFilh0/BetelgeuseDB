from PyQt5 import uic,QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from datetime import date

from banco import criacao_banco

data_atual = date.today()

# executa o metodo de criação do banco que será executado apenas na primeira vez que o programa é aberto no pc
criacao_banco()

# conecta com o banco de dados
banco = sqlite3.connect('pvn_banco.bd')

# Acolhidos --> OK
def cadastrar_acolhido():
    try:
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

        # verifica se algum dado foi preenchido se não foi é atribuido o valor DEFAULT
        if estado_civil == '':
            estado_civil = 'solteiro'

        if qtd_filhos == '':
            qtd_filhos = '0'

        if trabalho == '':
            trabalho = 'desempregado'

        if entrada == 'AAAA-MM-DD' or entrada == '':
            entrada = data_atual

        # muda AAAA-MM-DD se não for apagado no formulário
        if saida == 'AAAA-MM-DD':
            saida = '-'

        cursor = banco.cursor()
        cursor.execute('''INSERT INTO acolhidos (nome, rg, cpf, nascimento, estado_civil,
                        qtd_filhos, trabalho, posto_saude, lazer, substancia_favorita,
                        uso_desde_idade, religiao, responsavel, rg_responsavel, cpf_responsavel,
                        vinculo_responsavel, entrada, saida, obs)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (str(nome), str(rg), str(cpf), str(nascimento),
                                          str(estado_civil), str(qtd_filhos), str(trabalho),
                                          str(posto_saude), str(lazer), str(substancia_favorita),
                                          str(usoAno), str(religiao), str(responsavel), str(rg_responsavel),
                                          str(cpf_responsavel), str(vinculo), str(entrada), str(saida), str(obs)))
        banco.commit()

        acolhido.edtNome.setText('')
        acolhido.edtRG.setText('')
        acolhido.edtCPF.setText('')
        acolhido.edtNascimento.setText('AAAA-MM-DD')
        acolhido.edtECivil.setText('')
        acolhido.edtFilho.setText('')
        acolhido.edtTrabalho.setText('')
        acolhido.edtPSaude.setText('')
        acolhido.edtLazer.setText('')
        acolhido.edtSubst.setText('')
        acolhido.edtTUso.setText('')
        acolhido.edtReligiao.setText('')
        acolhido.edtResponsavel.setText('')
        acolhido.edtReRG.setText('')
        acolhido.edtReCPF.setText('')
        acolhido.edtVinculo.setText('')
        acolhido.edtEntrada.setText('AAAA-MM-DD')
        acolhido.edtSaida.setText('AAAA-MM-DD')
        acolhido.edtObs.setText('')

        aviso_sucesso('INFORMAÇÕES CADASTRADAS COM SUCESSO!')

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

# Ver acolhidos cadastrados -->
def ver_cadastro():
    try:
        cadastrado.show()

        comando_SQL = "SELECT * FROM acolhidos ORDER BY nome"
        cursor = banco.cursor()
        cursor.execute(comando_SQL)
        lidos = cursor.fetchall()


        cadastrado.tabela.setRowCount(len(lidos))
        cadastrado.tabela.setColumnCount(3)

        for i in range(len(lidos)):
            for j in range(3):
                cadastrado.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

def pesquisar_acolhido():
    try:
        pesquisa = cadastrado.edtPesquisa.text()

        c = banco.cursor()

        c.execute("""SELECT * FROM acolhidos WHERE nome LIKE '%""" + pesquisa + """%' ORDER BY nome""")

        lidos = c.fetchall()

        cadastrado.tabela.setRowCount(len(lidos))
        cadastrado.tabela.setColumnCount(3)

        for i in range(len(lidos)):
            for j in range(3):
                cadastrado.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

def excluir_dado_acolhido():
    try:
        confirmacao = confirmacao_excluir()

        if confirmacao == 0:
            excluir = cadastrado.edtExcluir.text()

            cursor = banco.cursor()

            cursor.execute("DELETE FROM acolhidos WHERE id_acolhido=" + str(excluir))
            banco.commit()

            cadastrado.edtExcluir.setText('')

            comando_SQL = "SELECT * FROM acolhidos ORDER BY nome"
            cursor.execute(comando_SQL)
            lidos = cursor.fetchall()

            cadastrado.tabela.setRowCount(len(lidos))
            cadastrado.tabela.setColumnCount(3)

            for i in range(len(lidos)):
                for j in range(3):
                    cadastrado.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
            cursor = banco.cursor()

            aviso_sucesso('DADO EXLCUÍDO COM SUCESSO!')

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

# Ver medicamentos --> OK
def medicamentos_abrir():
    try:
        cadMedicamento.show()

        c = banco.cursor()


        comando_SQL = ("""SELECT * FROM medicamentos ORDER BY nome""")
        c.execute(comando_SQL)
        lidos = c.fetchall()
        cadMedicamento.tabelaCadastro.setRowCount(len(lidos))
        cadMedicamento.tabelaCadastro.setColumnCount(4)

        for i in range(len(lidos)):
            for j in range(4):
                cadMedicamento.tabelaCadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

# Cadastrar medicamentos --> OK
def cadastrar_medicamento():
    try:
        cadMedicamento.show()

        nome = cadMedicamento.edtNomeMed.text()
        espec = cadMedicamento.edtEsp.text()
        obs = cadMedicamento.edtObs.text()

        c = banco.cursor()

        c.execute('''INSERT INTO medicamentos (nome, especificacoes, obs)
                    VALUES (?, ?, ?)''',(str(nome), str(espec), str(obs)))
        banco.commit()

        aviso_sucesso('INFORMAÇÕES CADASTRADAS COM SUCESSO!')

        cadMedicamento.edtNomeMed.setText('')
        cadMedicamento.edtObs.setText('')
        cadMedicamento.edtEsp.setText('')

        comando_SQL = ("""SELECT * FROM medicamentos ORDER BY nome""")
        c.execute(comando_SQL)
        lidos = c.fetchall()
        cadMedicamento.tabelaCadastro.setRowCount(len(lidos))
        cadMedicamento.tabelaCadastro.setColumnCount(4)

        for i in range(len(lidos)):
            for j in range(4):
                cadMedicamento.tabelaCadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

def pesquisar_medicamentos():
    try:
        pesquisa = cadMedicamento.edtPesquisa.text()

        c = banco.cursor()

        c.execute("""SELECT * FROM medicamentos WHERE nome LIKE '%""" + pesquisa + """%' ORDER BY nome""")

        lidos = c.fetchall()

        cadMedicamento.tabelaCadastro.setRowCount(len(lidos))
        cadMedicamento.tabelaCadastro.setColumnCount(4)

        for i in range(len(lidos)):
            for j in range(4):
                cadMedicamento.tabelaCadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

def excluir_medicamento():
    try:
        confirmacao = confirmacao_excluir()

        if confirmacao == 0:
            excluir = cadMedicamento.edtExcluir.text()

            cursor = banco.cursor()

            cursor.execute("DELETE FROM medicamentos WHERE id_medicamento=" + str(excluir))
            banco.commit()

            cadMedicamento.edtExcluir.setText('')

            comando_SQL = "SELECT * FROM medicamentos ORDER BY nome"
            cursor.execute(comando_SQL)
            lidos = cursor.fetchall()

            cadMedicamento.tabelaCadastro.setRowCount(len(lidos))
            cadMedicamento.tabelaCadastro.setColumnCount(4)

            for i in range(len(lidos)):
                for j in range(4):
                    cadMedicamento.tabelaCadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
            cursor = banco.cursor()

            aviso_sucesso('DADO EXLCUÍDO COM SUCESSO!')

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

# Entrada --> OK
def entradas_abrir():
    try:
        cadEntradaMedicamento.show()

        c = banco.cursor()

        comando_SQL = ("""SELECT e.id_entrada, m.nome, m.especificacoes, e.qtd_entrada, e.data_entrada, e.obs FROM medicamentos as m
        JOIN entradas_medicamentos as e ON m.id_medicamento = e.id_medicamento ORDER BY data_entrada DESC;""")
        c.execute(comando_SQL)
        lidos = c.fetchall()
        cadEntradaMedicamento.tabelaEntrada.setRowCount(len(lidos))
        cadEntradaMedicamento.tabelaEntrada.setColumnCount(6)

        for i in range(len(lidos)):
            for j in range(6):
                cadEntradaMedicamento.tabelaEntrada.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

# Cadastrar entrada de medicamento --> Ok
def cadastrar_entrada():
    try:
        id_medicamento = cadEntradaMedicamento.edtIdMed.text()
        qtd_entrada = cadEntradaMedicamento.edtQtdMed.text()
        data_entrada = cadEntradaMedicamento.edtDataMed.text()
        obs = cadEntradaMedicamento.edtObs.text()

        # verifica se algum dado foi preenchido se não foi é atribuido o valor DEFAULT
        if data_entrada == 'AAAA-MM-DD' or data_entrada == '':
            data_entrada = data_atual

        c = banco.cursor()

        c.execute("""INSERT INTO entradas_medicamentos (id_medicamento, qtd_entrada, data_entrada, obs)
                    VALUES (?, ?, ?, ?)""", (str(id_medicamento), str(qtd_entrada), str(data_entrada), str(obs)))

        banco.commit()

        aviso_sucesso('INFORMAÇÕES CADASTRADAS COM SUCESSO!')

        cadEntradaMedicamento.edtIdMed.setText('')
        cadEntradaMedicamento.edtQtdMed.setText('')
        cadEntradaMedicamento.edtDataMed.setText('AAAA-MM-DD')
        cadEntradaMedicamento.edtObs.setText('')

        comando_SQL = ("""SELECT e.id_entrada, m.nome, m.especificacoes, e.qtd_entrada, e.data_entrada, e.obs FROM medicamentos as m
            JOIN entradas_medicamentos as e ON m.id_medicamento = e.id_medicamento ORDER BY data_entrada DESC;""")
        c.execute(comando_SQL)
        lidos = c.fetchall()
        cadEntradaMedicamento.tabelaEntrada.setRowCount(len(lidos))
        cadEntradaMedicamento.tabelaEntrada.setColumnCount(6)

        for i in range(len(lidos)):
            for j in range(6):
                cadEntradaMedicamento.tabelaEntrada.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

def excluir_entrada():
    try:
        confirmacao = confirmacao_excluir()

        if confirmacao == 0:
            excluir = cadEntradaMedicamento.edtExcluir.text()

            cursor = banco.cursor()

            cursor.execute("DELETE FROM entradas_medicamentos WHERE id_entrada=" + str(excluir))
            banco.commit()

            cadEntradaMedicamento.edtExcluir.setText('')

            comando_SQL = """SELECT e.id_entrada, m.nome, m.especificacoes, e.qtd_entrada, e.data_entrada, e.obs FROM medicamentos as m
                JOIN entradas_medicamentos as e ON m.id_medicamento = e.id_medicamento ORDER BY data_entrada DESC;"""
            cursor.execute(comando_SQL)
            lidos = cursor.fetchall()

            cadEntradaMedicamento.tabelaEntrada.setRowCount(len(lidos))
            cadEntradaMedicamento.tabelaEntrada.setColumnCount(6)

            for i in range(len(lidos)):
                for j in range(6):
                    cadEntradaMedicamento.tabelaEntrada.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
            cursor = banco.cursor()

            aviso_sucesso('DADO EXLCUÍDO COM SUCESSO!')

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

# Tratamento
def tratamentos_abrir():
    try:
        tratamento.show()

        c = banco.cursor()

        # deleta tratamentos que já terminaram
        c.execute('''DELETE FROM controle_medicamentos WHERE termino_tratamento < current_date ''')

        comando_SQL = ("""SELECT c.id_tratamento, a.nome, m.nome, m.especificacoes, c.qtd_dose, c.frequencia, c.inicio_tratamento, 
        c.termino_tratamento, c.obs FROM acolhidos as a JOIN controle_medicamentos as c ON a.id_acolhido = c.id_acolhido
        JOIN medicamentos as m on c.id_medicamento = m.id_medicamento ORDER BY c.inicio_tratamento DESC, 
        c.termino_tratamento DESC;""")
        c.execute(comando_SQL)
        lidos = c.fetchall()

        tratamento.tabelaTratamento.setRowCount(len(lidos))
        tratamento.tabelaTratamento.setColumnCount(9)

        for i in range(len(lidos)):
            for j in range(9):
                tratamento.tabelaTratamento.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

def cadastrar_tratamento():
    try:
        id_acolhido = tratamento.edtIAcolhido.text()
        id_medicamento = tratamento.edtIMedicamento.text()
        qtd_dose = tratamento.edtDose.text()
        frequencia = tratamento.edtFrequencia.text()
        inicio = tratamento.edtInicio.text()
        termino = tratamento.edtTermino.text()
        obs = tratamento.edtOBS.text()

        # verifica se algum dado foi preenchido se não foi é atribuido o valor DEFAULT
        if termino == 'AAAA-MM-DD' or termino == '':
            termino = 'indefinido'

        # muda AAAA-MM-DD se não for apagado no formulário
        if inicio == 'AAAA-MM-DD':
            inicio = ''

        c = banco.cursor()

        c.execute('''INSERT INTO controle_medicamentos (id_acolhido, id_medicamento, qtd_dose, frequencia, inicio_tratamento,
                    termino_tratamento, obs) VALUES (?, ?, ?, ?, ?, ?, ?)''', (str(id_acolhido), str(id_medicamento),
                    str(qtd_dose), str(frequencia), str(inicio), str(termino), str(obs)))

        banco.commit()

        comando_SQL = ("""SELECT c.id_tratamento, a.nome, m.nome, m.especificacoes, c.qtd_dose, c.frequencia, c.inicio_tratamento, 
            c.termino_tratamento, c.obs FROM acolhidos as a JOIN controle_medicamentos as c ON a.id_acolhido = c.id_acolhido
            JOIN medicamentos as m on c.id_medicamento = m.id_medicamento ORDER BY c.inicio_tratamento DESC, 
            c.termino_tratamento DESC;""")
        c.execute(comando_SQL)
        lidos = c.fetchall()
        print(lidos)
        tratamento.tabelaTratamento.setRowCount(len(lidos))
        tratamento.tabelaTratamento.setColumnCount(9)

        for i in range(len(lidos)):
            for j in range(9):
                tratamento.tabelaTratamento.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

        aviso_sucesso('INFORMAÇÕES CADASTRADAS COM SUCESSO!')

        tratamento.edtIAcolhido.setText('')
        tratamento.edtIMedicamento.setText('')
        tratamento.edtDose.setText('')
        tratamento.edtFrequencia.setText('')
        tratamento.edtInicio.setText('AAAA-MM-DD')
        tratamento.edtTermino.setText('AAAA-MM-DD')
        tratamento.edtOBS.setText('')

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

def excluir_tratamento():
    try:
        confirmacao = confirmacao_excluir()

        if confirmacao == 0:
            excluir = tratamento.edtExcluir.text()

            cursor = banco.cursor()

            cursor.execute("DELETE FROM controle_medicamentos WHERE id_tratamento=" + str(excluir))
            banco.commit()

            tratamento.edtExcluir.setText('')

            comando_SQL = """SELECT c.id_tratamento, a.nome, m.nome, m.especificacoes, c.qtd_dose, c.frequencia, c.inicio_tratamento, 
                c.termino_tratamento, c.obs FROM acolhidos as a JOIN controle_medicamentos as c ON a.id_acolhido = c.id_acolhido
                JOIN medicamentos as m on c.id_medicamento = m.id_medicamento ORDER BY c.inicio_tratamento DESC,
                c.termino_tratamento DESC;"""
            cursor.execute(comando_SQL)
            lidos = cursor.fetchall()

            tratamento.tabelaTratamento.setRowCount(len(lidos))
            tratamento.tabelaTratamento.setColumnCount(9)

            for i in range(len(lidos)):
                for j in range(9):
                    tratamento.tabelaTratamento.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
            cursor = banco.cursor()

            aviso_sucesso('DADO EXLCUÍDO COM SUCESSO!')

    except:
        aviso_erro()

# Visualizar dados cadastradps -->
def visualizar_dado():
    try:
        visual.show()

        idVer = cadastrado.edtVisualizar.text()
        cursor = banco.cursor()

        cursor.execute("""SELECT nome, rg, cpf, nascimento,
         estado_civil, qtd_filhos, trabalho, posto_saude,
         lazer, substancia_favorita, uso_desde_idade,
         religiao, responsavel, rg_responsavel,
         cpf_responsavel, vinculo_responsavel,
         entrada, saida, obs FROM acolhidos WHERE id_acolhido="""+ (str(idVer)))

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
        #visual.lblSaida.setText(infoGet[17])
        visual.edtSaida.setText(infoGet[17])
        visual.lblOBS.setText(infoGet[18])

        cursor.execute("""SELECT m.nome, m.especificacoes, c.qtd_dose, c.frequencia, c.inicio_tratamento, 
            c.termino_tratamento, c.obs FROM acolhidos as a JOIN controle_medicamentos as c ON a.id_acolhido = c.id_acolhido
            JOIN medicamentos as m on c.id_medicamento = m.id_medicamento WHERE c.id_acolhido ="""+ (str(idVer)) + """
             ORDER BY c.inicio_tratamento DESC, c.termino_tratamento DESC""")

        lidos = cursor.fetchall()

        visual.tabelaTratamento.setRowCount(len(lidos))
        visual.tabelaTratamento.setColumnCount(7)

        for i in range(len(lidos)):
            for j in range(7):
                visual.tabelaTratamento.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))

        visual.btnModificar.clicked.connect(modificar_saida)

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)


def modificar_saida():
    try:
        confirmacao = confirmacao_modificar()
        if confirmacao == 0:
            idVer = cadastrado.edtVisualizar.text()

            saida = visual.edtSaida.text()

            c = banco.cursor()

            c.execute("""UPDATE acolhidos SET saida = '""" + saida + """' WHERE id_acolhido = """ + idVer)

            banco.commit()

            aviso_sucesso('SAÍDA MODIFICADA COM SUCESSO!')

    except Exception as e:
        erro = str(e)
        aviso_erro(erro)

def ajuda_abrir():
    ajuda.show()

# caixas de aviso/mensagem
def confirmacao_excluir():
    janela = QMessageBox()
    janela.setIcon(QMessageBox.Warning)
    janela.setText('Deseja excluir o dado?')
    janela.setWindowTitle('Atenção')
    janela.addButton('Sim', 5)
    janela.addButton('Não', 6)
    janela.setWindowIcon(QtGui.QIcon('imagens/excluir.png'))
    #janela.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

    retorno = janela.exec()
    return retorno

def confirmacao_modificar():
    modAviso = QMessageBox()
    modAviso.setIcon(QMessageBox.Warning)
    modAviso.setText('Deseja modificar o dado?')
    modAviso.setWindowTitle('Atenção')
    modAviso.addButton('Sim', 5)
    modAviso.addButton('Não', 6)
    modAviso.setWindowIcon(QtGui.QIcon('imagens/modificar icon.png'))

    retorno = modAviso.exec()
    return retorno

def aviso_sucesso(op):
    avisoFoi = QMessageBox()
    avisoFoi.setIcon(QMessageBox.Information)
    avisoFoi.setText(op)
    avisoFoi.setWindowTitle('SUCESSO!')
    avisoFoi.addButton('Ok', 0)
    avisoFoi.setWindowIcon(QtGui.QIcon('imagens/sucesso icon.png'))

    avisoFoi.exec()

def aviso_erro(e):
    aviso = QMessageBox()
    aviso.setIcon(QMessageBox.Warning)
    aviso.setText(e)
    aviso.setWindowTitle('ERRO!')
    aviso.addButton('Ok', 0)
    aviso.setWindowIcon(QtGui.QIcon('imagens/erro icon.png'))

    retorno = aviso.exec()
    # ok = 0
    # return retorno

app = QtWidgets.QApplication([])

acolhido = uic.loadUi("formAcolhido.ui")
cadastrado = uic.loadUi("formCadastrado.ui")
visual = uic.loadUi("formVisualizar.ui")
cadMedicamento = uic.loadUi("formCadMedicamento.ui")
cadEntradaMedicamento = uic.loadUi("formEntradaMedicamento.ui")
tratamento = uic.loadUi("formTratamento.ui")
ajuda = uic.loadUi("formAjuda.ui")


acolhido.btnCadastrar.clicked.connect(cadastrar_acolhido)
acolhido.btnVer.clicked.connect(ver_cadastro)
acolhido.btnMedicamento.clicked.connect(medicamentos_abrir)
acolhido.btnEntradaMed.clicked.connect(entradas_abrir)
acolhido.btnTratamento.clicked.connect(tratamentos_abrir)
acolhido.btnAjuda.clicked.connect(ajuda_abrir)

cadastrado.btnExcluir.clicked.connect(excluir_dado_acolhido)
cadastrado.btnVisualizar.clicked.connect(visualizar_dado)
cadastrado.btnPesquisar.clicked.connect(pesquisar_acolhido)

cadMedicamento.btnCadastrarMed.clicked.connect(cadastrar_medicamento)
cadMedicamento.btnPesquisar.clicked.connect(pesquisar_medicamentos)
cadMedicamento.btnExcluir.clicked.connect(excluir_medicamento)

cadEntradaMedicamento.btnCadastrarMed.clicked.connect(cadastrar_entrada)
cadEntradaMedicamento.btnExcluir.clicked.connect(excluir_entrada)

tratamento.btnCadastrarTratamento.clicked.connect(cadastrar_tratamento)
tratamento.btnExcluir.clicked.connect(excluir_tratamento)
#tratamento.btnExcluir.clicked.connect(confirmacao_excluir)


acolhido.show()

app.exec()

banco.close()
