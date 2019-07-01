class Animal():
    def __init__(self, nome, raca, especie, idade):
        self.nome = nome
        self.raca = raca
        self.especie = especie
        self.idade = idade

    def __str__(self):
        return "Animal da raca " + self.raca +' de espécie '+self.especie+','+" de nome "+self.nome+' com '+str(self.idade)+" anos de idade"

class Dono():
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal

    def __str__(self):
        return "Dono de "+str(self.animal)+" de nome "+self.nome
    
class Consulta():
    def __init__(self, data, hora, veterinario, animal):
        self.data = data
        self.hora = hora 
        self.veterinario = veterinario
        self.animal = animal
    
    def __str__(self):
        return "Consulta do "+str(self.animal)+" em "+self.data+" às "+str(self.hora)+" com "+str(self.veterinario)

class Veterinario():
    def __init__(self, nome, especializacao):
        self.nome = nome
        self.especializacao = especializacao

    def __str__(self):
        return "Doutor(a) "+self.nome+" de especialização "+self.especializacao

if __name__ =="__main__":

    ani = Animal("Lady", "Beagle", "Cão", 9)
    don = Dono("Natália", ani)
    vet = Veterinario("Tibúrsio", "caccioro")
    con = Consulta("02/12/2020", 12, vet, ani)

    print(ani)
    print(don)
    print(con)
    print(vet)