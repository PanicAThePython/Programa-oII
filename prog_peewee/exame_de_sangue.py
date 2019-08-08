from peewee import *
import os

db = SqliteDatabase("exame.db")

class BaseModel(Model):

    class Meta:
        database = db

class Exame (BaseModel):
    
    nome = CharField()
    preco = FloatField()
    prazo = IntegerField()

    def __str__(self):
        return "Exame "+self.nome+" que custa "+str(self.preco)+" que será entregue daqui a "+str(self.prazo)+" dias."

class Requisicao (BaseModel):

    data = DateField()
    paciente = CharField()
    medico = CharField()
    exames = ManyToManyField(Exame)

    def __str__(self):
        l=[]
        for i in self.exames:
            l.append(i)

        return "Requisição feita no dia "+str(self.data)+" dos exames "+str(l)+" pela(o) médica(o) "+self.medico+" da(o) paciente "+self.paciente

if __name__ == "__main__":
    arq = "jardim.db"
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Exame, Requisicao, Requisicao.exames.get_through_model()])
    except OperationalError as e:
        print(e)

    exame1 = Exame.create(nome="de Urina", preco = 10.0, prazo = 7)
    exame2 = Exame.create(nome="de Fezes", preco = 10.0, prazo = 7)
    requisicao = Requisicao.create(data='08-08-2019', paciente = "Ronald Weasley", medico = "Madame Pomfrey")
    requisicao.exames.add([exame1, exame2])
    print(exame1)
    print(exame2)
    print(requisicao)