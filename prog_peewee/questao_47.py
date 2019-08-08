from peewee import *
import os

db = SqliteDatabase('questao_47.db')

class BaseModel(Model):
    class Meta:
        database = db

class Planta(BaseModel):

    nom_popul = CharField()
    nom_cient = CharField()
    tam_folha = CharField()

    def __str__(self):
        return "Planta "+self.nom_popul+" com nome científico "+self.nom_cient+" e folha de tamanho "+self.tam_folha

class Jardim(BaseModel):

    plantas = ManyToManyField(Planta)
    
    def __str__(self):
        l=[]
        for i in self.plantas:
            l.append(i)

        return str(l)

if __name__=='__main__':
    arq = 'questao_47.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Planta, Jardim, Jardim.plantas.get_through_model()])
    except OperationalError as e:
        print(e)

    planta1 = Planta.create(nom_popul = 'Pranta', nom_cient = 'Plantea', tam_folha = 'So much big')
    planta2 = Planta.create(nom_popul = 'Mandrágora', nom_cient = 'Mandragora officinarum', tam_folha = 'Grandíssimo')
    estufa3 = Jardim.create()
    estufa3.plantas.add([planta1, planta2])
    print(estufa3)