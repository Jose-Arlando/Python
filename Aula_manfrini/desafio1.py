inter1 = 0
inter2 = 0
inter3 = 0
inter4 = 0

op= int(input("deseja adicionar valor? \nPositivo-sim\nNegativo-não\n"))
while op > 0:
    n1 = int(input("qual o valor: "))

    if n1>=0 and n1<=25:
        inter1 = inter1 + 1
    elif n1>=26 and n1<=50:
        inter2 = inter2 + 1
    elif n1>=51 and n1<=75:
        inter3 = inter3 + 1
    elif n1>=76 and n1<=100:
        inter4 = inter4 + 1
    op= int(input("deseja adicionar valor? \nPositivo-sim\nNegativo-não\n"))

print("Fim...\n0-25:",inter1,"\n26-50:",inter2,"\n51-75:",inter3,"\n76-100:",inter4)
    

