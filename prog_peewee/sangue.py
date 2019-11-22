from peewee import *
import os
arq = 'sangue.db'
db= SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Exame(BaseModel):
    nome = CharField()
    preco = FloatField()
    prazo = IntegerField()

    def __str__(self):
        return self.nome +', '+str(self.preco)+', '+str(self.prazo)

class RequisicaoExame(BaseModel):
    data = DateField()
    paciente = CharField()
    medico = CharField()
    exames = ManyToManyField(Exame)

    def __str__(self):
        l=[]
        for i in self.exames:
            l.append(i)

        return self.data+', '+self.paciente+', '+self.medico+str(l)

if __name__=='__main__':
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Exame, RequisicaoExame, RequisicaoExame.exames.get_through_model()])
    ex1 = Exame.create(nome = 'Triglicerideos', preco = 50, prazo = 2)
    ex2 = Exame.create(nome = 'Glicemia', preco = 100, prazo = 3)
    req = RequisicaoExame.create(data = '09/08/2019', paciente = 'Joao da Silva', medico = 'John Hank')
    req.exames.add([ex1, ex2])
    print(req)        