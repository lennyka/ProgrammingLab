valori=[]
contatore=0

def funzione_somma(array1):
    print("La somma è: {:.2f}".format(sum(array1)))
    
my_file = open('shampoo_sales.txt', 'r')

for line in my_file:
    
    if(contatore<=3):
        elemento = line.split(',')
        contatore = contatore + 1

        if elemento[0]!='Date':
            dat=elemento[0]
            num=float(elemento[1])
            valori.append(num)
    
    else: break

my_file.close()

funzione_somma(valori)


''' 
valori=[]

def funzione_somma():
    my_file = open('shampoo_sales.txt', 'r')

    for line in my_file:
        elemento = line.split(',')
        if elemento[0]!='Date':
            dat=elemento[0]
            num=float(elemento[1])
            valori.append(num)
    my_file.close()
    print("La somma è: {:.2f}".format(sum(valori)))
    
funzione_somma()
'''