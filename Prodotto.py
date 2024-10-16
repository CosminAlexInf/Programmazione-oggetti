class Prodotto:
    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def get_quantita(self):
        return self.quantita

    def set_quantita(self, quantita):
        self.quantita = quantita

    def calcola_valore(self):
        return self.prezzo * self.quantita

    def toString(self):
        return "Nome: " + self.nome + "\n" "Prezzo: " + str(self.prezzo) + "\n" "Quantità: " + str(self.quantita)


Mobile = Prodotto("Armadio di legno", 25, 7 )


print(Mobile.tostring())
Mobile.calcola_valore()
print("Il valore è:", Mobile.calcola_valore())