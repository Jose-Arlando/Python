cont_total = 0
acm = 0
cont_total_pares = 0
acm_pares = 0
media_pares = 0
par = 0
impar = 0

op= int(input("deseja adicionar valor? \nPositivo-sim\nNegativo-não\n"))
while op > 0:
    n1 = float(input("qual o valor: "))
    acm = acm + n1
    cont_total = cont_total + 1
    media = acm/cont_total

    if n1 % 2 == 0:
        par+=1
        acm_pares = acm_pares + n1
        media_pares = acm_pares/par
    elif n1 % 2 == 1:
        impar+=1
    op= int(input("deseja adicionar valor? \nPositivo-sim\nNegativo-não\n"))
print("FIM...\nPAR: ",par,"\nIMPAR: ",impar,"\nMEDIA PAR: ",float(media_pares),"\nMEDIA GERAL: ", media_pares)
