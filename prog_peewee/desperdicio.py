from peewee import *

db = SqliteDatabase("restaurante.db")

class BaseModel(Model):
    class Meta:
        database = db

class Desperdicio(BaseModel):

    item_cons = CharField()
    sobra = FloatField()
    qtd_pes_mesa = IntegerField()

    def __str__(self):

        return str(self.item_cons) + " por "+ str(self.qtd_pes_mesa) +" pessoas e sobrou "+str(self.sobra)+"'%' do que foi consumido"

class Item(BaseModel):

    qtd_item = IntegerField()
    nom_item = CharField()

    def __str__(self):

        return str(self.qtd_item) + " pratos de " + str(self.nom_item)

class Atendimento(BaseModel):

    num_mesa = IntegerField()
    itens = ManyToManyField(Item)

    def __str__(self):

        l = []

        for i in self.itens:
            l.append(i)
        
        return str(l) + " da mesa " + str(self.num_mesa)


if __name__=="__main__":


    item1 = Item.create(qtd_item=5, nom_item="Macarrão ao molho de camarão")
    item2 = Item.create(qtd_item=7, nom_item="Pudim")
    at1 = Atendimento.create(num_mesa=9)
    at1.itens.add([item1, item2])
    des = Desperdicio.create(item_cons=item1, sobra=3.9, qtd_pes_mesa=2)

    print(item1)
    print(item2)
    print(at1)
    print(des)


