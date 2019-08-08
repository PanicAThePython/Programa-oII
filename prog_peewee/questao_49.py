from peewee import *
import os

db = SqliteDatabase('questao_49.db')

class BaseModel(Model):
    class Meta:
        databse = db

class Exame(BaseModel):

    nome  = CharField()
    preco = FloatField()
    prazo = IntegerField()

    def __str__(self):
        return "Exame "+self.nome+" que custa "+str(self.preco)+" e estará pronto em "+str(self.prazo)+" dias."
    
class Requisicao(BaseModel):

    exames = ManyToManyField(Exame)
    nom_paciente = CharField()
    nom_medico = CharField()
    data = DateField()

    def __str__(self):
        l=[]
        for i in self.exames:
            l.append(i)

        return "Requisição do dia "+self.data+" feita por "+self.nom_medico+" dos exames "+str(l)+" da(o) paciente "+self.nom_paciente
    
if __name__=="__main__":
    arq = 'questao_49.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Exame, Requisicao, Requisicao.exames.get_through_model()])    
    except OperationalError as e:
        print(e)
    
    exame1 = Exame.create(nome = 'da língua presa', preco = 12.0, prazo = 14)
    exame2 = Exame.create(nome = 'de vista', preco = 25.0, prazo = 30)
    requisicao = Requisicao.create(nom_paciente = "Neville Longbottom", nom_medico = "Madame Pomfrey", data = '06-06-1993')
    requisicao.exames.add([exame1, exame2])
    print(exame1)