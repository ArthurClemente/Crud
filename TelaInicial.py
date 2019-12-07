# -*- coding:utf-8 -*

from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
from BancoDados import BancoDados


class Janela(Frame): # A classe Janela usa do recurso de herança, pois herda os métodos de Frame.
    def __init__(self, master=None):
        self.__master = master #Usa encapsulamento fazendo com que se torne um atributo privado
        Frame.__init__(self, master)
        self.janelaPrincipal()


    def janelaPrincipal(self): # Polimorfismo, pois alem de herdar métodos de Frame, a classe Janela tem esse método próprio.       
        self.master.title("Sistema Acadêmico")
        self.master.geometry("600x400")

        titulo= Label(
            text="Menu Principal",
            font=("Arial Bold",16),
            bg="grey",
            fg="black",
            width="600",
            height="1")
        titulo.pack()

        self.menubar = Menu(self)
        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Cadastro", menu=menu)

        menu.add_command(label="Aluno", command=JanelaAluno.cadAluno)
        menu.add_command(label="Professor", command=JanelaProfessor.cadProfessor)
        menu.add_command(label="Disciplina", command=JanelaDisciplina.cadDisciplina)
        menu.add_separator()
        menu.add_command(label="Sair", command=root.quit)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Relatório", menu=menu)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Notas", menu=menu)

        self.master.config(menu=self.menubar)

class JanelaAluno(Janela): #Uso de herança, JanelaAluno utilizando os métodos de Janela através de super()
    @staticmethod
    def __init__(self,master):
        super().__init__(master)

    @staticmethod
    def cadAluno(): #Polimorfismo, pois tem funcionalidades a mais do que a de sua classe mãe 
        BancoDados.criarTabelas("academico.db")
        dados = BancoDados.listarDados("academico.db","alunos")
        tamanho = len(dados)

        contaID = tamanho+1
        sexo = ["Não informado", "Masculino","Feminino"]

        janelaFilhaAluno = Toplevel(root, width=100, height=100)
        janelaFilhaAluno.geometry("600x400+120+120")

        listaSexo = StringVar(janelaFilhaAluno)
        listaSexo.set(sexo[0])

        titulo = Label(janelaFilhaAluno,
            text="Cadastro de Alunos",
            font=("Arial Bold",16),
            bg="blue",
            fg="white",
            width="600",
            height="1").pack()

        lblId = Label(janelaFilhaAluno, text="Alunos Cadastrados:")
        lblId.place(x=20,y=30)
        exibeDados = Listbox(janelaFilhaAluno, width=80, height=10)
        exibeDados.place(x=20, y=50)

        for i in range(tamanho):
            exibeDados.insert(END, dados[i][1])

        lblId = Label(janelaFilhaAluno, text="ID:")
        lblId.place(x=20, y=230)
        fldId = Label(janelaFilhaAluno, text=contaID)
        fldId.place(x=50, y=230)

        lblNome = Label(janelaFilhaAluno, text="Nome:")
        lblNome.place(x=80, y=230)
        fldNome = Entry(janelaFilhaAluno, width=60)
        fldNome.place(x=130, y=230)

        lblSexo = Label(janelaFilhaAluno, text="Sexo:")
        lblSexo.place(x=20, y=270)
        fldSexo = OptionMenu(janelaFilhaAluno, listaSexo, *sexo)
        fldSexo.place(x=70, y=270)

        lblDataNasc = Label(janelaFilhaAluno, text="Data Nascimento:")
        lblDataNasc.place(x=210, y=270)
        fldDataNasc = Entry(janelaFilhaAluno, width=10)
        fldDataNasc.place(x=320, y=270)

        lblRg = Label(janelaFilhaAluno, text="RG:")
        lblRg.place(x=400, y=270)
        fldRg = Entry(janelaFilhaAluno, width=20)
        fldRg.place(x=440, y=270)
        
        def atualizaDados():
            dados = BancoDados.listarDados("academico.db","alunos")
            tamanho = len(dados)
            alunos = []

            janelaFilhaAtualiza = Toplevel(janelaFilhaAluno, width=100, height=100)
            janelaFilhaAtualiza.geometry("600x400+120+120")

            for i in range(tamanho):
                alunos.append(str(dados[i][0])+" -"+dados[i][1])

            listaAluno = StringVar(janelaFilhaAtualiza)
            listaAluno.set(str(dados[0][0])+"   -"+dados[0][1])

            titulo = Label(janelaFilhaAtualiza,
                text="Alterar Dados/Excluir Alunos",
                font=("Arial Bold",16),
                bg="grey",
                fg="white",
                width="600",
                height="1").pack()

            lblPesquisa = Label(janelaFilhaAtualiza, text="Selecione o(a) Aluno(a):")
            lblPesquisa.place(x=20, y=40)

            fldPesquisa = OptionMenu(janelaFilhaAtualiza, listaAluno, *alunos)
            fldPesquisa.place(x=160, y=40)

            def pesquisaDados():
                getId = listaAluno.get()[:2]
                aluno = BancoDados.listarUmDado("academico.db","alunos", getId)
                getNome = StringVar(janelaFilhaAtualiza, value=aluno[0][1])
                getSexo = StringVar(janelaFilhaAtualiza, value=aluno[0][2])
                getDataNasc = StringVar(janelaFilhaAtualiza, value=aluno[0][3])
                getRg = StringVar(janelaFilhaAtualiza, value=aluno[0][4])

                lblId2 = Label(janelaFilhaAtualiza, text="ID:  "+ str(aluno[0][0]))
                lblId2.place(x=20,y=90)

                lblNome2 = Label(janelaFilhaAtualiza, text="Nome: ")
                lblNome2.place(x=80,y=90)
                fldNome2 = Entry(janelaFilhaAtualiza, textvariable=getNome)
                fldNome2.place(x=130,y=90)

                lblSexo2 = Label(janelaFilhaAtualiza, text="Sexo: ")
                lblSexo2.place(x=330,y=90)
                fldSexo2 = Entry(janelaFilhaAtualiza, textvariable=getSexo, width=15)
                fldSexo2.place(x=380,y=90)

                lblDataNasc2 = Label(janelaFilhaAtualiza, text="Data Nascimento: ")
                lblDataNasc2.place(x=20,y=120)
                fldDataNasc2 = Entry(janelaFilhaAtualiza, textvariable=getDataNasc, width=15)
                fldDataNasc2.place(x=130,y=120)

                lblRg2 = Label(janelaFilhaAtualiza, text="RG: ")
                lblRg2.place(x=260,y=120)
                fldRg2 = Entry(janelaFilhaAtualiza, textvariable=getRg)
                fldRg2.place(x=290,y=120)

                def alteraDados():
                    novoNome = fldNome2.get()
                    novoSexo = fldSexo2.get()
                    novoDataNasc = fldDataNasc2.get()
                    novoRg = fldRg2.get()
                    BancoDados.atualizarAlunos("academico.db", novoNome, novoSexo, novoDataNasc, novoRg, getId)
                    messagebox.showinfo("Aviso", "Dados atualizados no banco!")

                def excluiDados():
                    getId = listaAluno.get()[:2]
                    msg = messagebox.askquestion("Confirmar", "Deseja mesmo excluir estes dados?", icon='warning')
                    if msg == "yes":
                        BancoDados.excluirDados("academico.db", "alunos", getId)
                        messagebox.showinfo("Aviso", "Dados excluidos no banco!")

                btnAtualizaDados = Button(janelaFilhaAtualiza, text=' Atualizar ', command=alteraDados)
                btnAtualizaDados.place(x=100, y=330)

                btnExcluiDados = Button(janelaFilhaAtualiza, text=' Excluir ', command=excluiDados)
                btnExcluiDados.place(x=230, y=330)

                btnSair = Button(janelaFilhaAtualiza, text=' Fechar ', command=janelaFilhaAtualiza.destroy)
                btnSair.place(x=360, y=330)

            btnOk = Button(janelaFilhaAtualiza, text=' OK ', command=pesquisaDados)
            btnOk.place(x=330, y=40)

        def salvaDados():
            nome = fldNome.get()
            nasc = fldDataNasc.get()
            sexo = listaSexo.get()
            rg = fldRg.get()
            if nome == "":
                messagebox.showinfo("Erro", "Informe um nome!")
            if sexo == "":
                messagebox.showinfo("Erro", "Informe um sexo!")
            if nasc == "":
                messagebox.showinfo("Erro", "Informe uma data de nascimento!")
            if rg == "":
                messagebox.showinfo("Erro", "Informe um número de RG!")
            if (nome != "") or (sexo != "") or (nasc != "") or (rg != ""):
                BancoDados.inserirAluno("academico.db", contaID, nome, sexo, nasc, rg)
                messagebox.showinfo("Aviso", "Dados inseridos no banco!")

        btnOk = Button(janelaFilhaAluno, text=' Salvar ', command=salvaDados)
        btnOk.place(x=150, y=330)

        btnAtualiza = Button(janelaFilhaAluno, text=' Atualizar/Excluir ', command=atualizaDados)
        btnAtualiza.place(x=230, y=330)

        btnSair = Button(janelaFilhaAluno, text=' Fechar ', command=janelaFilhaAluno.destroy)
        btnSair.place(x=360, y=330)


class JanelaProfessor(Janela): #Uso de herança assim como JanelaAlunos, utilizando os metodos de Janela através de super()
    @staticmethod
    def __init__(self,master):
        super().__init__(master)

    @staticmethod
    def cadProfessor(): # Polimorfismo, pois assim como em JanelaAluno, tem funcionalidades extras do que as de sua classe mãe.
        BancoDados.criarTabelas("academico.db")
        dados = BancoDados.listarDados("academico.db","professores")
        tamanho = len(dados)

        contaID = tamanho+1
        sexo = ["Não informado", "Masculino","Feminino"]
        titulacao = ["Não informado", "Especialista","Mestre","Doutor"]

        janelaFilhaProfessor = Toplevel(root, width=100, height=100)
        janelaFilhaProfessor.geometry("600x400+120+120")

        listaSexo = StringVar(janelaFilhaProfessor)
        listaSexo.set(sexo[0])

        listaTitulacao = StringVar(janelaFilhaProfessor)
        listaTitulacao.set(titulacao[0])

        titulo = Label(janelaFilhaProfessor,
            text="Cadastro de Professores",
            font=("Arial Bold",16),
            bg="green",
            fg="white",
            width="600",
            height="1").pack()

        lblId = Label(janelaFilhaProfessor, text="Professores Cadastrados:")
        lblId.place(x=20,y=30)
        exibeDados = Listbox(janelaFilhaProfessor, width=80, height=10)
        exibeDados.place(x=20, y=50)

        for i in range(tamanho):
            exibeDados.insert(END, dados[i][1])

        lblId = Label(janelaFilhaProfessor, text="ID:")
        lblId.place(x=20, y=230)
        fldId = Label(janelaFilhaProfessor, text=contaID)
        fldId.place(x=50, y=230)

        lblNome = Label(janelaFilhaProfessor, text="Nome:")
        lblNome.place(x=80, y=230)
        fldNome = Entry(janelaFilhaProfessor, width=60)
        fldNome.place(x=130, y=230)

        lblSexo = Label(janelaFilhaProfessor, text="Sexo:")
        lblSexo.place(x=20, y=260)
        fldSexo = OptionMenu(janelaFilhaProfessor, listaSexo, *sexo)
        fldSexo.place(x=60, y=260)

        lblTitulacao = Label(janelaFilhaProfessor, text="Titulação:")
        lblTitulacao.place(x=210, y=260)
        fldTitulacao = OptionMenu(janelaFilhaProfessor, listaTitulacao, *titulacao)
        fldTitulacao.place(x=270, y=260)

        lblDataNasc = Label(janelaFilhaProfessor, text="Data Nascimento:")
        lblDataNasc.place(x=20, y=300)
        fldDataNasc = Entry(janelaFilhaProfessor, width=10)
        fldDataNasc.place(x=140, y=300)

        lblRg = Label(janelaFilhaProfessor, text="RG:")
        lblRg.place(x=260, y=300)
        fldRg = Entry(janelaFilhaProfessor, width=20)
        fldRg.place(x=300, y=300)

        def atualizaDados(JanelaAluno):
            dados = BancoDados.listarDados("academico.db","professores")
            tamanho = len(dados)
            professores = []

            janelaFilhaAtualizaProf = Toplevel(janelaFilhaProfessor, width=100, height=100)
            janelaFilhaAtualizaProf.geometry("600x400+120+120")

            for i in range(tamanho):
                professores.append(str(dados[i][0])+" -"+dados[i][1])

            listaProfessor = StringVar(janelaFilhaAtualizaProf)
            listaProfessor.set(str(dados[0][0])+"   -"+dados[0][1])
            
            titulo = Label(janelaFilhaAtualizaProf,
                text="Alterar Dados/Excluir Professores",
                font=("Arial Bold",16),
                bg="grey",
                fg="white",
                width="600",
                height="1").pack()

            lblPesquisa = Label(janelaFilhaAtualizaProf, text="Selecione o(a) Professor(a):")
            lblPesquisa.place(x=20, y=40)

            fldPesquisa = OptionMenu(janelaFilhaAtualizaProf, listaProfessor, *professores)
            fldPesquisa.place(x=170, y=40)

            def pesquisaDados():
                getId = listaProfessor.get()[:2]
                professor = BancoDados.listarUmDado("academico.db","professores", getId)
                getNome = StringVar(janelaFilhaAtualizaProf, value=professor[0][1])
                getSexo = StringVar(janelaFilhaAtualizaProf, value=professor[0][2])
                getTitulacao = StringVar(janelaFilhaAtualizaProf, value=professor[0][3])
                getDataNasc = StringVar(janelaFilhaAtualizaProf, value=professor[0][4])
                getRg = StringVar(janelaFilhaAtualizaProf, value=professor[0][5])

                lblId2 = Label(janelaFilhaAtualizaProf, text="ID:  "+ str(professor[0][0]))
                lblId2.place(x=20,y=90)

                lblNome2 = Label(janelaFilhaAtualizaProf, text="Nome: ")
                lblNome2.place(x=80,y=90)
                fldNome2 = Entry(janelaFilhaAtualizaProf, textvariable=getNome)
                fldNome2.place(x=130,y=90)

                lblSexo2 = Label(janelaFilhaAtualizaProf, text="Sexo: ")
                lblSexo2.place(x=330,y=90)
                fldSexo2 = Entry(janelaFilhaAtualizaProf, textvariable=getSexo, width=5)
                fldSexo2.place(x=380,y=90)

                lblTitulacao2 = Label(janelaFilhaAtualizaProf, text="Titulação: ")
                lblTitulacao2.place(x=315,y=90)
                fldTitulacao2 = Entry(janelaFilhaAtualizaProf, textvariable=getTitulacao, width=10)
                fldTitulacao2.place(x=380,y=90)

                lblDataNasc2 = Label(janelaFilhaAtualizaProf, text="Data Nascimento: ")
                lblDataNasc2.place(x=20,y=120)
                fldDataNasc2 = Entry(janelaFilhaAtualizaProf, textvariable=getDataNasc, width=15)
                fldDataNasc2.place(x=130,y=120)

                lblRg2 = Label(janelaFilhaAtualizaProf, text="RG: ")
                lblRg2.place(x=260,y=120)
                fldRg2 = Entry(janelaFilhaAtualizaProf, textvariable=getRg)
                fldRg2.place(x=290,y=120)

                btnOk = Button(janelaFilhaAtualizaProf, text=' OK ', command=pesquisaDados)
                btnOk.place(x=330, y=40)

                def alteraDados():
                    novoNome = fldNome2.get()
                    novoSexo = fldSexo2.get()
                    novoTitulacao = fldTitulacao2.get()
                    novoDataNasc = fldDataNasc2.get()
                    novoRg = fldRg2.get()
                    BancoDados.atualizarProfessores("academico.db", novoNome, novoSexo, novoTitulacao, novoDataNasc, novoRg, getId)
                    messagebox.showinfo("Aviso", "Dados atualizados no banco!")

                def excluiDados():
                    getId = listaProfessor.get()[:2]
                    msg = messagebox.askquestion("Confirmar", "Deseja mesmo excluir estes dados?", icon='warning')
                    if msg == "yes":
                        BancoDados.excluirDados("academico.db", "professores", getId)
                        messagebox.showinfo("Aviso", "Dados excluidos no banco!")

                btnAtualizaDados = Button(janelaFilhaAtualizaProf, text=' Atualizar ', command=alteraDados)
                btnAtualizaDados.place(x=100, y=330)

                btnExcluiDados = Button(janelaFilhaAtualizaProf, text=' Excluir ', command=excluiDados)
                btnExcluiDados.place(x=230, y=330)

                btnSair = Button(janelaFilhaAtualizaProf, text=' Fechar ', command=janelaFilhaAtualizaProf.destroy)
                btnSair.place(x=360, y=330)

            btnOk = Button(janelaFilhaAtualizaProf, text=' OK ', command=pesquisaDados)
            btnOk.place(x=330, y=40)

        def salvaDados():
            nome = fldNome.get()
            nasc = fldDataNasc.get()
            titu = listaTitulacao.get()
            sexo = listaSexo.get()
            rg = fldRg.get()
            if nome == "":
                messagebox.showinfo("Erro", "Informe um nome!")
            if sexo == "":
                messagebox.showinfo("Erro", "Informe um sexo!")
            if titu == "":
                messagebox.showinfo("Erro", "Informe uma titulação!")
            if nasc == "":
                messagebox.showinfo("Erro", "Informe uma data de nascimento!")
            if rg == "":
                messagebox.showinfo("Erro", "Informe um número de RG!")
            if (nome != "") or (sexo != "") or (titu != "") or (nasc != "") or (rg != ""):
                BancoDados.inserirProfessor("academico.db", contaID, nome, sexo, titu, nasc, rg)
                messagebox.showinfo("Aviso", "Dados inseridos no banco!")

        btnOk = Button(janelaFilhaProfessor, text=' Salvar ', command=salvaDados)
        btnOk.place(x=150, y=330)

        btnAtualiza = Button(janelaFilhaProfessor, text=' Atualizar/Excluir ', command=atualizaDados)
        btnAtualiza.place(x=230, y=330)

        btnSair = Button(janelaFilhaProfessor, text=' Fechar ', command=janelaFilhaProfessor.destroy)
        btnSair.place(x=360, y=330)

class JanelaDisciplina(): #Uso de herança, utilizando os metodos de Janela através de super()
    @staticmethod
    def __init__(self,master):
        super().__init__(master)

    @staticmethod
    def cadDisciplina(): #Polimorfismo, assim como cadAluno e cadProfessor 
        BancoDados.criarTabelas("academico.db")
        dados = BancoDados.listarDados("academico.db","disciplinas")
        tamanho = len(dados)

        contaID = tamanho+1
        curso = ["Não informado", "Técnico","Superior"]

        janelaFilhaDisciplina = Toplevel(root, width=100, height=100)
        janelaFilhaDisciplina.geometry("600x400+120+120")

        listaCurso = StringVar(janelaFilhaDisciplina)
        listaCurso.set(curso[0])

        titulo = Label(janelaFilhaDisciplina,
            text="Cadastro de Disciplinas",
            font=("Arial Bold",16),
            bg="red",
            fg="white",
            width="600",
            height="1").pack()

        lblId = Label(janelaFilhaDisciplina, text="Disciplinas Cadastradas:")
        lblId.place(x=20,y=30)
        exibeDados = Listbox(janelaFilhaDisciplina, width=80, height=10)
        exibeDados.place(x=20, y=50)

        for i in range(tamanho):
            exibeDados.insert(END, dados[i][1])

        lblId = Label(janelaFilhaDisciplina, text="ID:")
        lblId.place(x=20, y=230)
        fldId = Label(janelaFilhaDisciplina, text=contaID)
        fldId.place(x=50, y=230)

        lblNome = Label(janelaFilhaDisciplina, text="Nome:")
        lblNome.place(x=80, y=230)
        fldNome = Entry(janelaFilhaDisciplina, width=60)
        fldNome.place(x=130, y=230)

        lblCurso = Label(janelaFilhaDisciplina, text="Curso:")
        lblCurso.place(x=20, y=270)
        fldCurso = OptionMenu(janelaFilhaDisciplina, listaCurso, *curso)
        fldCurso.place(x=70, y=270)
        
        
        def atualizaDados():
            dados = BancoDados.listarDados("academico.db","disciplinas")
            tamanho = len(dados)
            disciplinas = []

            janelaFilhaAtualizaDisci = Toplevel(janelaFilhaDisciplina, width=100, height=100)
            janelaFilhaAtualizaDisci.geometry("600x400+120+120")

            for i in range(tamanho):
                disciplinas.append(str(dados[i][0])+" -"+dados[i][1])

            listaDisciplina = StringVar(janelaFilhaAtualizaDisci)
            listaDisciplina.set(str(dados[0][0])+"   -"+dados[0][1])

            titulo = Label(janelaFilhaAtualizaDisci,
                text="Alterar Dados/Excluir Disciplinas",
                font=("Arial Bold",16),
                bg="grey",
                fg="white",
                width="600",
                height="1").pack()

            lblPesquisa = Label(janelaFilhaAtualizaDisci, text="Selecione a Disciplina:")
            lblPesquisa.place(x=20, y=40)

            fldPesquisa = OptionMenu(janelaFilhaAtualizaDisci, listaDisciplina, *disciplinas)
            fldPesquisa.place(x=160, y=40)

            def pesquisaDados():
                getId = listaDisciplina.get()[:2]
                disciplina = BancoDados.listarUmDado("academico.db","disciplinas", getId)
                getNome = StringVar(janelaFilhaAtualizaDisci, value=disciplina[0][1])
                getCurso = StringVar(janelaFilhaAtualizaDisci, value=disciplina[0][2])

                lblId2 = Label(janelaFilhaAtualizaDisci, text="ID:  "+ str(disciplina[0][0]))
                lblId2.place(x=20,y=90)

                lblNome2 = Label(janelaFilhaAtualizaDisci, text="Nome: ")
                lblNome2.place(x=80,y=90)
                fldNome2 = Entry(janelaFilhaAtualizaDisci, textvariable=getNome)
                fldNome2.place(x=130,y=90)

                lblCurso2 = Label(janelaFilhaAtualizaDisci, text="Curso: ")
                lblCurso2.place(x=330,y=90)
                fldCurso2 = Entry(janelaFilhaAtualizaDisci, textvariable=getCurso, width=9)
                fldCurso2.place(x=380,y=90)

                def alteraDados():
                    novoNome = fldNome2.get()
                    novoCurso = fldCurso2.get()
                    BancoDados.atualizarDisciplinas("academico.db", novoNome, novoCurso, getId)
                    messagebox.showinfo("Aviso", "Dados atualizados no banco!")

                def excluiDados():
                    getId = listaDisciplina.get()[:2]
                    msg = messagebox.askquestion("Confirmar", "Deseja mesmo excluir estes dados?", icon='warning')
                    if msg == "yes":
                        BancoDados.excluirDados("academico.db", "disciplinas", getId)
                        messagebox.showinfo("Aviso", "Dados excluidos no banco!")

                btnAtualizaDados = Button(janelaFilhaAtualizaDisci, text=' Atualizar ', command=alteraDados)
                btnAtualizaDados.place(x=100, y=330)

                btnExcluiDados = Button(janelaFilhaAtualizaDisci, text=' Excluir ', command=excluiDados)
                btnExcluiDados.place(x=230, y=330)

                btnSair = Button(janelaFilhaAtualizaDisci, text=' Fechar ', command=janelaFilhaAtualizaDisci.destroy)
                btnSair.place(x=360, y=330)

            btnOk = Button(janelaFilhaAtualizaDisci, text=' OK ', command=pesquisaDados)
            btnOk.place(x=330, y=40)

        def salvaDados():
            nome = fldNome.get()
            curso = listaCurso.get()
            if nome == "":
                messagebox.showinfo("Erro", "Informe um nome!")
            if curso == "":
                messagebox.showinfo("Erro", "Informe um curso!")
            if (nome != "") or (curso != ""):
                BancoDados.inserirDisciplina("academico.db", contaID, nome, curso)
                messagebox.showinfo("Aviso", "Dados inseridos no banco!")

        btnOk = Button(janelaFilhaDisciplina, text=' Salvar ', command=salvaDados)
        btnOk.place(x=150, y=330)

        btnAtualiza = Button(janelaFilhaDisciplina, text=' Atualizar/Excluir ', command=atualizaDados)
        btnAtualiza.place(x=230, y=330)

        btnSair = Button(janelaFilhaDisciplina, text=' Fechar ', command=janelaFilhaDisciplina.destroy)
        btnSair.place(x=360, y=330)

root = Tk()
app = Janela(root)
root.mainloop()