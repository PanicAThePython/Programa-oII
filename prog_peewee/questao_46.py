from peewee import *
import os

db = SqliteDatabase('saude.db')

class BaseModel(Model):
    class Meta:
        database = db

class Ocorrencia(BaseModel):

    nome = CharField()
    intensidade = IntegerField()
    motivo = CharField()

    def __str__(self):
        if str(self.intensidade) == "0":
            return str(self.nome)+" com intensidade leve pois "+str(self.motivo)
        elif str(self.intensidade) == "1":
            return str(self.nome)+" com intensidade média pois "+str(self.motivo)
        elif str(self.intensidade) == "2":
            return str(self.nome)+" com intensidade alta pois "+str(self.motivo)
    
class Registro(BaseModel):

    data = DateField()
    ocorrencia = ForeignKeyField(Ocorrencia)

    def __str__(self):

        return str(self.data)+": "+str(self.ocorrencia)

if __name__=="__main__":
    arq = 'saude.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Ocorrencia, Registro])
    except OperationalError as e:
        print(e)

    oc1 = Ocorrencia.create(nome = 'dor de cabeça', intensidade = 0, motivo = 'jantei muito na noite anterior(resto de marmita do almoço)')
    r1 = Registro.create(data = '2019-06-29', ocorrencia = oc1)
    print(r1)