n = int(input("1 - Adicionar nome \n2 - Listar nomes \n3 - Remover nome \n4 - Pesquisar nome \n5 - Sair"))
nome = ""
nomes = []
while (n!=5):
    match (n):
        case 1:
            print(">>Cadastrar")
            nome = input("qual o nome: ")
            nomes.append(nome)
            print("Cadastrado")
            n = int(input("1 - Adicionar nome \n2 - Listar nomes \n3 - Remover nome \n4 - Pesquisar nome \n5 - Sair"))
        case 2:
            for nome in nomes:
                print(f"{nome}") 
            n = int(input("1 - Adicionar nome \n2 - Listar nomes \n3 - Remover nome \n4 - Pesquisar nome \n5 - Sair"))
        case 3:
            nome_rem = input("Qual o nome? ")
            if nome_rem in nomes:
                nomes.remove(nome_rem)
            n = int(input("1 - Adicionar nome \n2 - Listar nomes \n3 - Remover nome \n4 - Pesquisar nome \n5 - Sair"))
        case 4:
            nome_bus = input("Qual o nome? ")
            if nome_bus in nomes:
                print(f"{nome_bus} encontrado")
            n = int(input("1 - Adicionar nome \n2 - Listar nomes \n3 - Remover nome \n4 - Pesquisar nome \n5 - Sair"))

