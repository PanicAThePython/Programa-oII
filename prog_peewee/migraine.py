from peewee import *
import os

db = SqliteDatabase('migraine.db')

class BaseModel(Model):
    class Meta:
        database = db

class Ocorrencia(BaseModel):
    ocorrencia = CharField()
    intensidade = IntegerField()
    observacoes = CharField()

    def __str__(self):
        if self.intensidade==0:
            return self.ocorrencia+" leve pois "+self.observacoes
        elif self.intensidade==1:
            return self.ocorrencia+" média(o) pois "+self.observacoes
        elif self.intensidade==2:
            return self.ocorrencia+" forte pois "+self.observacoes

class Registro(BaseModel):
    data = DateField()
    ocorrencia = ForeignKeyField(Ocorrencia)

    def __str__(self):
        return str(self.ocorrencia)+" no dia "+self.data


if __name__=='__main__':
    arq = 'migraine.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Ocorrencia, Registro])
    except OperationalError as e:
        print(e)

    oco1 = Ocorrencia.create(ocorrencia = 'headache', intensidade = 0, observacoes = 'comi muito')
    reg1 = Registro.create(data = '07-08-2019', ocorrencia = oco1)
    print(reg1)
    


