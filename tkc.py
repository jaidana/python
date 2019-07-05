import tkinter as tk

class ModeleConvertisseur:
    def __init__(self, taux=1.14, dev1='EUR', dev2='USD'):
        self.taux = taux
        self.dev1 = dev1
        self.dev2 = dev2

    def convertir(self,montant):
        return self.taux*montant

    def calculer(self):

class VueConvertisseur(tk.Frame):
    def __init__(self, parent, controleur=None, model=None):
        tk.Frame.__init__(self,parent)
        self.controleur = controleur
        self.create_widgets

    def create_widgets(self):
        self.labelDev1 = tk.Label(self, text ='Devise1')
        self.varDev1 = tk.Stringvar(self,'xxx', 'Devise1')
        self.entryDev1 =tk.Entry(self,textVariable= self.varDev1)
        self.taux
        self.varTaux=tk.DoubleVar(self, value=0.0, name='taux')
        self.entryTaux=tk.Entry(self,textvariable=self.varTaux)
        self.calculer = tk.Button(self, text='calculer',
                                  command=self.controleur.calule())
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
class Controleur:
    def __init__(self):
        self.root = tk.Tk()
        self.model =ModelConvertisseur(self.root, model=self.model,

    def run(self):
        self.root.mainloop()
                                       
    
    
    
