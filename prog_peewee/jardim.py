from peewee import *
import os

db = SqliteDatabase("jardim.db")

class BaseModel(Model):
    class Meta:
        database = db

class Planta(BaseModel):

    nome_popular = CharField()
    nome_cientif = CharField()
    tamanhofolha = CharField()
    
    def __str__(self):
        return "Planta "+self.nome_popular+" de nome científico "+self.nome_cientif+" com folha do tamanho "+self.tamanhofolha

class Jardim(BaseModel):

    proprie = CharField()

    def __str__(self):
        return "Jardim pertencente (à/ao) "+self.proprie


class PlantaDoJardim(BaseModel):

    planta = ForeignKeyField(Planta)
    jardim = ForeignKeyField(Jardim)
    data_plantio = DateField()
    periodo_poda = IntegerField()

    def __str__(self):
        return str(self.planta)+" plantada no dia "+str(self.data_plantio)+" no "+str(self.jardim)+" e deverá ser podada novamente daqui a "\
            +str(self.periodo_poda)+" dias."


if __name__=="__main__":
    arq = "jardim.db"
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Planta, Jardim, PlantaDoJardim])
    except OperationalError as e:
        print(e)

    rosa = Planta.create(nome_popular = 'Rosa', nome_cientif = 'Rosaceae', tamanhofolha = 'pequena')
    orquidea = Planta.create(nome_popular = 'Orquídea', nome_cientif = 'Orchidaceae', tamanhofolha = 'média')
    jardim = Jardim.create(proprie = 'Naielly')
    pdj = PlantaDoJardim.create(planta = rosa, jardim = jardim, data_plantio = '08-08-2019', periodo_poda = 90)

    print(rosa)
    print(orquidea)
    print(jardim)
    print(pdj)