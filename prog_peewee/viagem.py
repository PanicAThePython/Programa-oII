from peewee import *
import os

db = SqliteDatabase("viagem.db")

class BaseModel(Model):
    class Meta:
        database = db


class Viajante(BaseModel):

    nome = CharField()
    pais_origem = CharField()
    qtd_malas = IntegerField()
        
    def __str__(self):

        return "Viajante "+str(self.nome)+" do país "+str(self.pais_origem)+" com "+str(self.qtd_malas)+" malas"

class Destino(BaseModel):

    pais = CharField()

    def __str__(self):
        return " indo para "+str(self.pais)

class Viagem(BaseModel):

    viajante = ForeignKeyField(Viajante)
    destino = ForeignKeyField(Destino)

    def __str__(self):
        return str(self.viajante)+str(self.destino)


if __name__ == "__main__":

    arq = 'viagem.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Viajante, Destino, Viagem])
    except OperationalError as e:
        print("Erro: "+str(e))

    na = Viajante.create(nome = "Natália", pais_origem = "Brasil", qtd_malas = 3)
    lu = Viajante.create(nome = "Luiza", pais_origem = "Brasil", qtd_malas = 2)
    ing = Destino.create(pais = "Inglaterra - Londres")
    jap = Destino.create(pais = "Japão - Tokio")
    via1 = Viagem.create(viajante = na, destino = ing)
    via2 = Viagem.create(viajante = lu, destino = jap)

    print(via1)
    print(via2)

