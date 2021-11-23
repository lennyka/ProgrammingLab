class CSVFile:
    def __init__(self,name):
        self.name = name

    def getdata(self):
        lista=[]
        my_file = open(self.name, 'r')

        for line in my_file:
            elemento = line.split(',')
            
            if elemento[0]!='Date':
                elemento[1] = elemento[1][0:-1]
                lista.append(elemento)

        my_file.close()
        return lista
        
shampo = CSVFile('shampoo_sales.txt')
print(shampo.getdata())

        
