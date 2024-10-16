import sqlite3

class SessaoFotografica:
    def conexao(self):
        conexao = sqlite3.connect("estudioFotografico_db")
        consulta = conexao.cursor()
        tabela = """
        CREATE TABLE IF NOT EXISTS sessoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100),
            data DATE,
            tipo VARCHAR(100),
            preco FLOAT
        );
        """

        consulta.execute(tabela)
        return conexao
    
    def cadastrarSessao(self, cliente, data, tipo, preco):
        conexao = self.conexao() 

        sql = " INSERT INTO sessoes VALUES (?,?,?,?,?)"
        campos = (None, cliente, data, tipo, preco)

        consulta = conexao.cursor()
        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "linha(s) atualizada(s) com sucesso")

        conexao.close()

    def consultarsessao(self):
        conexao= self.conexao()
        consulta = conexao.cursor()

        sql = " SELECT * FROM sessoes"
        consulta.execute(sql)

        resultado = consulta.fetchall()

        for itens in resultado:
            print(f"ID: {itens[0]}")
            print(f"Cliente: {itens[1]}")
            print(f"Data: {itens[2]}")
            print(f"Tipo: {itens[3]}")
            print(f"Preço: {itens[4]}")
            print(f"-"*40)

        conexao.close()    

    def deletarsessao(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        
        id = int(input("Informe o código da sessão que deseja deletar: "))

        sql = "DELETE FROM sessoes WHERE id = ?"

        campos = (id,) 

        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "linha(s) deletadas(s) com sucesso")

        conexao.close()

    def atualizarsessao(self):
        conexao = self.conexao()
        consulta = conexao.cursor()

        print("1-Cliente\n2-Data\n3-Tipo\n4-Preço\n")
        esc = input("O que você deseja atualizar?")

        if esc == "cliente" or "Cliente":

            cliente = input("Informe o novo nome do cliente: ")
            id = int(input("Informe o ID da sessão: "))

            sql = "UPDATE sessoes SET nome = ? WHERE id = ?"

            campos = (cliente, id)

            consulta.execute(sql, campos)

            conexao.commit()

            print(consulta.rowcount, "linha atualizada com sucesso")

            conexao.close()

        
            data = input("Informe a nova data: ")
            id = int(input("Informe o ID da sessão: "))

            sql = "UPDATE sessoes SET data = ? WHERE id = ?"

            campos = (data, id)

            consulta.execute(sql, campos)

            conexao.commit()

            print(consulta.rowcount, "linha atualizada com sucesso")

            conexao.close()

    
    