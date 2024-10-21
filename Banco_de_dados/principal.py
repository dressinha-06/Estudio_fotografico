from sessaofotografica import SessaoFotografica


s1 = SessaoFotografica()
while True:
    print(" 1-Cadastrar \n 2-Consultar \n 3-Deletar \n 4-Atualizar \n")
    esp = input("O que você deseja fazer? ")
    
    if esp == "1":
        cliente = input("Informe o nome do cliente: ")
        data = input("Infome a data da sessão: ")
        tipo = input("informe o tipo da sessão: ")
        preco = input("informe o valor da sessão: ")
        s1.cadastrarSessao(cliente, data, tipo, preco)
    
    if esp == "2":
        s1.consultarsessao() 

    if esp == "3":
        s1.deletarsessao()

    if esp == "4":
        s1.atualizarsessao()
