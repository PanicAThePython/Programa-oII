from peewee import *
import os

db = SqliteDatabase('questao_45.db')

class BaseModel(Model):
    class Meta:
        database = db

class Item(BaseModel):

    nome = CharField()

    def __str__(self):
        return self.nome

class Atendimento(BaseModel):

    itens = ManyToManyField(Item)
    num_mesa = IntegerField()
    qtd_pessoas = IntegerField()
    data = DateField()

    def __str__(self):
        l=[]
        for i in self.itens:
            l.append(i)

        return "Pedido no dia "+str(self.data)+" na mesa "+str(self.num_mesa)+" de "+str(l)+" para "+str(self.qtd_pessoas)+" pessoas;"

class Desperdicio(BaseModel):

    atendimento = ForeignKeyField(Atendimento)
    sobra = FloatField()

    def __str__(self):
        return str(self.atendimento)+" teve sobra de "+str(self.sobra)+'%'

if __name__=="__main__":

    arq = 'questao_45.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Item, Atendimento, Atendimento.itens.get_through_model(), Desperdicio])
    except OperationalError as e:
        print(e)

    camarao = Item.create(nome = 'Camarão ao molho')
    lagosta = Item.create(nome = 'Lagosta ao molho branco com salada')
    atendimento = Atendimento.create(num_mesa = 8, qtd_pessoas = 2, data = '31-07-2019')
    atendimento.itens.add([camarao, lagosta])
    desp = Desperdicio.create(atendimento=atendimento, sobra = 6.8 )

    print(desp)