from peewee import *
import os

db = SqliteDatabase("doacao.db")

class BaseModel(Model):
    class Meta:
        database = db

class Objeto(BaseModel):

    nome = CharField()
    qtd = FloatField()

    def __str__(self):
        return str(self.qtd)+" unidades de "+str(self.nome)

class Doador(BaseModel):

    nome = CharField()
    objeto = ForeignKeyField(Objeto)

    def __str__(self):
        return str(self.nome)+ " doou "+str(self.objeto)

class Instituicao(BaseModel):

    nome = CharField()
    doador = ForeignKeyField(Doador)

    def __str__(self):
        return "Instituição de nome "+str(self.nome)+" recebeu doação de "+str(self.doador)

if __name__=="__main__":

    arq = 'doacao.db'
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Objeto, Doador, Instituicao])
    except OperationalError as e:
        print(e)

    obj1 = Objeto.create(nome = 'Dinheiro', qtd = 50)
    na = Doador.create(nome = 'Natália', objeto = obj1)
    inst = Instituicao.create(nome = 'Criança Esperança', doador = na)

    print(inst)