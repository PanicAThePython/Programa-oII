from peewee import *
import os

db = SqliteDatabase("receita.db")

class BaseModel(Model):

    class Meta:

        database = db

class Ingrediente(BaseModel):

    nome = CharField()
    qtd  = FloatField()

    def __str__(self):

        return  str(self.qtd) + " unidades de medida do ingrediente "+str(self.nome)

class Receita(BaseModel):

    nome = CharField()
    porcao = IntegerField()
    ingredientes = ManyToManyField(Ingrediente)

    def __str__(self):

        l=[]
        for i in self.ingredientes:
            l.append(i)

        return "Receita de "+str(self.nome)+" para "+str(self.porcao)+" pessoas, com os ingredientes: " +str(l)


if __name__=="__main__":

    arq = 'receita.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Ingrediente, Receita, Receita.ingredientes.get_through_model()])
    except OperationalError as e:
        print("Erro: "+str(e))

    ing1 = Ingrediente.create(nome = 'cenoura', qtd = 3)
    ing2 = Ingrediente.create(nome = 'trigo', qtd = 0.5)
    ing3 = Ingrediente.create(nome = "ovo", qtd = 2)
    receita = Receita.create(nome = 'bolo de cenoura', porcao = 5)
    receita.ingredientes.add([ing1, ing2, ing3])
    
    print(ing1)
    print(ing2)
    print(ing3)
    print(receita)