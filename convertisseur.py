class Convertisseur:
    def __init__(self, taux=1.14, devise1='EUR', devise2='USD'):
        self.devise1 = devise1
        self.devise2 = devise2
        self.taux = taux
    
    def change12(self, montant):
        return self.taux*montant
    
    def change21(self, montant):
        return montant/self.taux
    
    def __str__(self):
        return (self.devise1+"/"+self.devise2+" = "+str(self.taux))
        
def main():
    dev1 = input('Devise1: ')
    dev2 = input('Devise2: ')
    try:
        taux = float(input('taux:'))
    except ValueError:
        print('attention au point decimal taux = 1.0')
        taux = 1.0
    convert = Convertisseur(taux, dev1, dev2)
    print(convert)
    while True:
        try:
            m1 = float(input('Montant:'))
        except ValueError:
            print("""attention à l'écriture des nombres 1000 \n
                   0 pour sortir""")
            m1 = 0
        if m1 == 0.0:
            break
        if m1 > 0:
            m2 = convert.change12(m1)
            print('%6.2f %s = %6.2f %s'%(m1, dev1, m2, dev2))
        if m1 < 0:
            m2 = convert.change21(m1)
            print('%6.2f %s = %6.2f %s'%(m1, dev2, m2, dev1))


if __name__ == '__main__':
    main()

##    def main():
##        c = Convertisseur()
##        print(c)
##        print(c.change12(100))
##        assert abs(c.change12(100)-114.00 < 1E-7,)
