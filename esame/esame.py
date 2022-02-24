import datetime 

# Classe per le eccezioni
class ExamException(Exception):
    pass

# Classe principale 
class CSVTimeSeriesFile():

    # Inizializzazione della classe
    def __init__(self, name):

        self.name = name

        # Verifico che il nome sia una stringa
        if not isinstance(name, str):
            raise ExamException("Non è una stringa")
        pass

    # Funzione per verificare la data
    def is_date(self,stringa): 
        # Definisco il formato da utilizzare
        formato="%Y-%m"
        try:
            # Verifico se la stringa è una data
            datetime.datetime.strptime(stringa,formato) 
            return True

        except ValueError: 
            return False

    # Funzione che restituisce una liste di liste
    def get_data(self):

        # Provo ad aprire il file in lettura
        # Se non ci riesco alzo una eccezione
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            raise ExamException("Errore nella lettura del file {}".format(e)) 

        # Inizializzo una lista vuota per salvare tutti i dati
        listaDiListe = []

        # Leggo il file linea per linea
        for line in my_file:

            # Faccio lo split di ogni linea sulla virgola
            riga = line.split(",")

            
            # Salto la prima riga perchè non la sto processando
            if riga[0] != 'date':

                try:
                    # Assegno a date il valore della prima parte della riga
                    # Faccio il casting e lo converto in stringa
                    date = str(riga[0])
    
                    # Assegno a date il valore della seconda parte della riga
                    # Faccio il casting e lo converto in intero
                    value = int(riga[1])

                    # Se è minore di 0 non lo consiedero e vado avanti
                    if value < 0 or value == '':
                        value = 'Mancante'

                    # Verifico se c'è un duplicato 
                    if len(listaDiListe) > 0: 
                        # Loop sulla lista
                        for item in listaDiListe:  
                            # Salvo la data precedente
                            dataPrec = item[0] 
    
                            # Verifico se la data viene ripetuta
                            if date == dataPrec:
                                raise ExamException("La data è ripetuta") 
    
                            # Verifico se la data non è in ordine
                            dataPrec = listaDiListe[-1][0] 
                            if date < dataPrec:
                                raise ExamException("La data non è in ordine")
                            # Aggiungo i valori alla lista
                    listaDiListe.append([date,value])
                    
                except:
                    continue

                

        # Chiudo il file
        my_file.close()

        # Ritorno il file
        return listaDiListe

def detect_similar_monthly_variations(time_series, years):

    lAnni = []
    for i,item in enumerate(time_series):
        lAnni.append(int(time_series[i][0][0:4]))

    # Verifico se la lista degli anni è vuota
    if len(years) == 0:
        raise ExamException("Errore, lista vuota")
    # Verifico se la lista contiene più o meno di 2 anni
    elif len(years) != 2:
        raise ExamException("Errore, la lista non contiene 2 anni")

    # Verifico che gli anni siano presenti nella lista
    if not years[0] in lAnni:
        raise ExamException("Errore, il primo anno non è presente nella lista")

    if not years[1] in lAnni:
        raise ExamException("Errore, il secondo anno non è presente nella lista")

    # Verifico che i 2 elementi della lista non siano uguali
    if years[0] == years[1]:
        raise ExamException("Errore, gli anni sono gli stessi")

    # Verifico che il primo anno sia precdente al secondo
    if years[0] > years[1]:
        raise ExamException("Errore, gli anni non sono in ordine")
        
    # Verifico che gli anni siano consecutivi
    if years[0] + 1 != years[1]:
        raise ExamException("Errore, gli anni non sono consecutivi")

    # Inizializzo la lista vuota
    lista=[]

    # Funzione che mi ritorna una lista con le differenze tra i mesi
    def differenzaMesi(mese):

        # Inizializzo lista vuota che conterrà i valori delle differenze dei mesi
        arrayofValues = []

        # Inizializzo contatore
        i=0

        # Iterazione su 11 mesi, non 12 pervhè altriment va fuori range
        while i < (len(mese)-1):

            # Se un valore è mancante 
            if(mese[i]=='Mancante' or mese[i + 1]=='Mancante'):
                arrayofValues.append('Mancante')
            else:
                # Calcolo la differenza tra i 2 mesi con il valore assoluto
                diff = abs(mese[i] - mese[i + 1])  
                
                # Aggiungo alla lista il valore della differneza
                arrayofValues.append(diff) 

            # Aggiorno il contatore
            i = i + 1

        # Ritorno la lista con i valori
        return arrayofValues

    # Differenza tra gli anni
    def differenzaAnni(primoAnno, secondoAnno):
        i = 0
        while i < 11:
            # Se mancante lo mette in automatico false
            if(primoAnno[i]=='Mancante' or secondoAnno[i]=='Mancante'):
                lista.append(False)
            else:
                difference = abs(primoAnno[i] - secondoAnno[i]) 
                print("{}".format(difference))
                if (difference <= 2):  
                    lista.append(True)
                else:
                    lista.append(False)
            i = i + 1
                
        return lista

    # Selezione l'anno
    def selezioneanno(anno):
        
        l = []
        tmp = []
        i = 0

        while(i<len(time_series)):
            
            tmp.append(time_series[i][0]) 
            if(tmp[i][0:4] == str(anno)):
                l.append(time_series[i][1])
            
            i=i+1

        
        return l

    anno1 = differenzaMesi(selezioneanno(years[0]))
    anno2 = differenzaMesi(selezioneanno(years[1]))

    # Verifico che siano presenti tutti i mesi di quell'anno
    if len(selezioneanno(years[0])) != 12:
        raise ExamException("Errore, non tutti i mesi sono presenti nel primo anno")
    
    # Verifico che siano presenti tutti i mesi di quell'anno
    if len(selezioneanno(years[1])) != 12:
        raise ExamException("Errore, non tutti i mesi sono presenti nel secondo anno")

    lista = differenzaAnni(anno1, anno2)
    return lista