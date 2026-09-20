alunos = []
alunos_aprovados = []

aluno_nome = ""
aluno_nota = 0
i = 0

op = int(input("1 - Cadastrar \n2 - Listar \n3 - Pesquisar \n4 - Mostrar aprovados \n5 - Sair"))
while op != 5:
    match op:
        case 1:
            aluno_nome = input("Nome: ")
            aluno_nota = float(input("Nota: "))
            if aluno_nota > 6:
                alunos_aprovados.append([aluno_nome, aluno_nota])
            alunos.append([aluno_nome, aluno_nota])
            print(f"{aluno_nome} cadastrado")
            op = int(input("1 - Cadastrar \n2 - Listar \n3 - Pesquisar \n4 - Mostrar aprovados \n5 - Sair\n"))

        case 2:
            while i < len(alunos):
                print(f"\nnome:{alunos[i][0]}\nNota: {alunos[i][1]}")
                i = i + 1
            i = 0
            op = int(input("1 - Cadastrar \n2 - Listar \n3 - Pesquisar \n4 - Mostrar aprovados \n5 - Sair\n"))
        case 3:
            aluno_bus = input("Qual nome deseja buscar: ")
            for aluno in alunos:
                if aluno_bus == aluno[0]:
                    print(f"{aluno_bus} encontrado! nota: {aluno[1]} ")
            op = int(input("1 - Cadastrar \n2 - Listar \n3 - Pesquisar \n4 - Mostrar aprovados \n5 - Sair\n"))

            
        


        
