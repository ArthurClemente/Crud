#-*-coding:utf-8-*
from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
from BancoDados import BancoDados

class Janela(Frame):
    def __init__(self, master=None):
        self.__master = master
        Frame.__init__(self, master)
        self.janelaPrincipal()

    def janelaPrincipal(self):
        self.master.title("Sistema Acadêmico")
        self.master.geometry("600x400")
        
        titulo= Label(
            text="Menu Principal",
            font=("Arial Bold",16),
            bg="grey",
            fg="white",
            width="600",
            height="1")
        titulo.pack()

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff = 0)
        
        self.menubar.add_cascade(label = "Cadastro", menu=menu)
        
        menu.add_command(label = "Aluno", command=JanelaAluno.cadAluno)
        menu.add_command(label = "Professor", command=JanelaProfessor.cadProfessor)
        menu.add_command(label = "Disciplina")#, command=self.__janelaDisciplina
        menu.add_separator()
        menu.add_command(label = "Sair", command=root.quit)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = "Relatório", menu=menu)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = "Notas", menu=menu)

        self.master.config(menu = self.menubar)

class JanelaAluno(Janela):
    @staticmethod
    def __init__(self, master):
        super().__init__(master)
    
    @staticmethod
    def cadAluno():
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
            font=("Arial Bold", 16),
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

        def atualizarDados():
            dados = BancoDados.listarDados("academico.bd", "alunos")
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
                fldSexo2 = Entry(janelaFilhaAtualiza, textvariable=getSexo, width=5)
                fldSexo2.place(x=380,y=90)

                lblDataNasc2 = Label(janelaFilhaAtualiza, text="Data Nascimento: ")
                lblDataNasc2.place(x=20,y=120)
                fldDataNasc2 = Entry(janelaFilhaAtualiza, textvariable=getDataNasc, width=15)
                fldDataNasc2.place(x=130,y=120)

                lblRg2 = Label(janelaFilhaAtualiza, text="RG: ")
                lblRg2.place(x=260,y=120)
                fldRg2 = Entry(janelaFilhaAtualiza, textvariable=getRg)
                fldRg2.place(x=290,y=120)

            btnOk = Button(janelaFilhaAtualiza, text=' OK ', command=pesquisaDados)
            btnOk.place(x=330, y=40)

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

        def salvaDados():
            nome = fldNome.get()
            nasc = fldDataNasc.get()
            sexo = listaSexo.get()
            rg = fldRg.get()
            if nome == "":
                messagebox.showinfo("Erro", "Informe um nome!")
            elif sexo == "":
                messagebox.showinfo("Erro", "Informe um sexo!")
            elif nasc == "":
                messagebox.showinfo("Erro", "Informe uma data de nascimento!")
            elif rg == "":
                messagebox.showinfo("Erro", "Informe um número de RG!")
            else:
                BancoDados.inserirAluno("academico.db", contaID, nome, sexo, nasc, rg)
                messagebox.showinfo("Aviso", "Dados inseridos no banco!")

        btnOk = Button(janelaFilhaAluno, text=' Salvar ', command=salvaDados)
        btnOk.place(x=150, y=330)

        btnAtualiza = Button(janelaFilhaAluno, text=' Atualizar/Excluir ', command=atualizaDados)
        btnAtualiza.place(x=230, y=330)

        btnSair = Button(janelaFilhaAluno, text=' Fechar ', command=janelaFilhaAluno.destroy)
        btnSair.place(x=360, y=330)
