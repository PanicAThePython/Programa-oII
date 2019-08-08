from peewee import *
import os

arq = 'receita.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Receita(BaseModel):
    titulo = CharField()

    def __str__(self):
        return self.titulo

class Ingrediente(BaseModel):
    nome = CharField()

    def __str__(self):
        return self.nome

class IngredienteDaReceita(BaseModel):

    receita = ForeignKeyField(Receita)
    ingrediente = ForeignKeyField(Ingrediente)
    qtd = FloatField()

    def __str__(self):
        return str(self.qtd)+' unidade de medida do ingrediente '+str(self.ingrediente)+' para a receita de '+str(self.receita)



if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Receita, Ingrediente, IngredienteDaReceita])
    except OperationalError as e:
        print(e)

    
    brigadeiro = Receita.create(titulo = 'Brigadeiro, o doce que mais briga')
    leite_cond = Ingrediente.create(nome = 'Leite Condensado')
    nescau_rad = Ingrediente.create(nome = 'Achocolatado')
    indrec = IngredienteDaReceita.create(receita = brigadeiro, ingrediente = leite_cond,qtd = 100)


    print(brigadeiro)
    print(leite_cond)
    print(nescau_rad)
    print(indrec)


