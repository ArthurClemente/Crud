# -*- coding:utf-8 -*

import sqlite3
from sqlite3 import Error

class BancoDados():
	def __init__(self):
		self.__conectar = conectar
		self.__nomeDb = nomeDb
		self.__cursor = cursor
        # Os argumentos (conectar, nomeDb e cursor) usam encapsulamento, pois estão iniciados por sublinhado, o que os torna privados    
            
	def criarDb(nomeDb):		
		conectar = None
		try:
			conectar = sqlite3.connect(nomeDb)
			print("Criado o banco de dados: "+nomeDb)
		except Error as e:
			print("Erro: "+e)

		return conectar

	def criarTabelas(nomeDb):
		conectar = None
		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)

		else:
			cursor = conectar.cursor()
			cursor.execute(
				"CREATE TABLE IF NOT EXISTS alunos ("
				"id INTEGER PRIMARY KEY, "
				"nome TEXT NOT NULL, "
				"sexo TEXT NOT NULL, "
				"data_nasc TEXT NOT NULL, "
				"rg TEXT NOT NULL);")

			cursor.execute(
				"CREATE TABLE IF NOT EXISTS professores ("
				"id INTEGER PRIMARY KEY, "
				"nome TEXT NOT NULL, "
				"sexo TEXT NOT NULL, "
				"titulacao TEXT NOT NULL, "
				"data_nasc TEXT NOT NULL, "
				"rg TEXT NOT NULL);")

			cursor.execute(
				"CREATE TABLE IF NOT EXISTS notas ("
				"id INTEGER PRIMARY KEY, "
				"id_aluno INTEGER NOT NULL, "
				"id_professor INTEGER NOT NULL, "
				"id_disciplina INTEGER NOT NULL, "
				"nota1 REAL NOT NULL, "
				"nota2 REAL NOT NULL);")

			cursor.execute(
				"CREATE TABLE IF NOT EXISTS disciplinas ("
				"id INTEGER PRIMARY KEY, "
				"nome TEXT NOT NULL, "
				"curso TEXT NOT NULL);")

			conectar.commit()
			print("Criadas as tabelas do banco de dados ")

	def listarDados(nomeDb, nomeTabela):
		conectar = None
		lista = []

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			dados = cursor.execute("SELECT * FROM "+nomeTabela)
			#max_id = cursor.fetchone()[0]
			conectar.commit()
			for item in dados:
				lista.append(item)
		return lista

	def listarUmDado(nomeDb, nomeTabela, ID):
		conectar = None
		lista = []

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			dados = cursor.execute("SELECT * FROM "+nomeTabela+" WHERE ID="+ID)
			conectar.commit()
			for item in dados:
				lista.append(item)
		return lista

	def inserirAluno(nomeDb, ID, NOME, SEXO, DATA_NASC, RG):
		conectar = None
		dados = (ID, NOME, SEXO, DATA_NASC, RG)

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			sql = '''INSERT INTO alunos VALUES (?,?,?,?,?);'''
			cursor.execute(sql, dados)
			conectar.commit()
			cursor.close()
			print("Dados inseridos!")

		return cursor.lastrowid

	def inserirProfessor(nomeDb, ID, NOME, SEXO, TITULACAO, DATA_NASC, RG):
		conectar = None
		dados = (ID, NOME, SEXO, TITULACAO, DATA_NASC, RG)

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			sql = '''INSERT INTO professores VALUES (?,?,?,?,?,?);'''
			cursor.execute(sql, dados)
			conectar.commit()
			cursor.close()
			print("Dados inseridos!")

		return cursor.lastrowid

	def inserirDisciplina(nomeDb, ID, NOME, CURSO):
		conectar = None
		dados = (ID, NOME, CURSO)

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			sql = '''INSERT INTO disciplinas VALUES (?,?,?);'''
			cursor.execute(sql, dados)
			conectar.commit()
			cursor.close()
			print("Dados inseridos!")

		return cursor.lastrowid

	def inserirNotas(nomeDb, ID, ID_ALUNO, ID_PROFESSOR, ID_DISCIPLINA, NOTA1, NOTA2):
		conectar = None
		dados = (ID, ID_ALUNO, ID_PROFESSOR, ID_DISCIPLINA, NOTA1, NOTA2)

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			sql = '''INSERT INTO notas VALUES (?,?,?,?,?,?);'''
			cursor.execute(sql, dados)
			conectar.commit()
			cursor.close()
			print("Dados inseridos!")

		return cursor.lastrowid

	def excluirDados(nomeDb, nomeTabela, ID):
		conectar = None

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			sql = "DELETE FROM "+nomeTabela+" WHERE id="+ID
			cursor.execute(sql)
			conectar.commit()
			cursor.close()
			print("Dados excluídos!")

		return cursor.lastrowid

	def atualizarAlunos(nomeDb, NOME, SEXO, DATA_NASC, RG, ID):
		conectar = None
		dados = (NOME, SEXO, DATA_NASC, RG, ID)

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			sql = '''UPDATE alunos SET nome=?, sexo=?, data_nasc=?, rg=? WHERE id=?;'''
			cursor.execute(sql, dados)
			conectar.commit()
			cursor.close()
			print('Dados Atualizados!')

	def atualizarProfessores(nomeDb, NOME, SEXO, TITULACAO, DATA_NASC, RG, ID):
		conectar = None
		dados = (NOME, SEXO, TITULACAO, DATA_NASC, RG, ID)

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print("Erro: "+e)
		else:
			cursor = conectar.cursor()
			sql = '''UPDATE professores SET nome=?, sexo=?, titulacao=?, data_nasc=?, rg=? WHERE id=?;'''
			cursor.execute(sql, dados)
			conectar.commit()
			cursor.close()
			print('Dados Atualizados!')
	
	def atualizarDisciplinas(nomeDb, NOME, CURSO, ID):
		conectar = None
		dados = (NOME, CURSO, ID)

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print('Erro: '+e)
		else:
			cursor = conectar.cursor()
			sql = '''UPDATE disciplinas SET nome=?, curso=?, WHERE id=?;'''
			cursor.execute(sql, dados)
			conectar.commit()
			cursor.close()
			print('Dados Atualizados!')

	def atualizarNotas(nomeDb, NOTA1, NOTA2, ID_DISCIPLINA):
		conectar = None
		dados = (NOTA1, NOTA2, ID_DISCIPLINA)

		try:
			conectar = sqlite3.connect(nomeDb)
		except Error as e:
			print('Erro: '+e)
		else:
			cursor = conectar.cursor()
			sql = '''UPDATE notas SET nota1=?, nota2=?, WHERE id_disciplina=?;'''
			cursor.execute(sql, dados)
			conectar.commit()
			cursor.close()
			print('Dados Atualizados!')

#BancoDados.criarDb("academico.db")
#BancoDados.criarTabelas("academico.db")
#BancoDados.inserirAluno("academico.db","3","Teste de Aluno","M","02/06/1980","123548-AL")
#BancoDados.inserirAluno("academico.db","4","Maria da Silva","F","11/04/1990","123548-AL")
#BancoDados.listarDados("academico.db", "alunos")
#BancoDados.excluirDados("academico.db", "alunos", "2")
#BancoDados.atualizarAlunos("academico.db","Alexandre Braga","M","13/10/1970","885466-AL","1")
