from peewee import *
from os import *

arq = "compra.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Produto(BaseModel):

    nome = CharField()
    obs = CharField()

    def __str__(self):
        return "de "+self.nome+" "+self.obs

class Item(BaseModel):

    qtd = FloatField()
    unid = CharField()
    produto = ForeignKeyField(Produto)

    def __str__(self):
        return str(self.qtd)+" "+self.unid+" "+str(self.produto)

class ListaDeCompra(BaseModel):

    titulo = CharField()
    itens = ManyToManyField(Item)

    def __str__(self):

        res = self.titulo
        for i in self.itens:
            res+=" "+str(i)

        return res

if __name__=="__main__":

    if path.exists(arq):
        remove(arq)
    try:
        db.connect()
        db.create_tables([Produto, Item, ListaDeCompra, ListaDeCompra.itens.get_through_model()])
    except OperationalError as e:
        print(e)

    arroz = Produto.create(nome = "arroz", obs = "branco")
    feijao = Produto.create(nome = "feijão", obs = "branco")
    uni1 = Item.create(qtd = 3.0, unid = "pacotes", produto = arroz)
    uni2 = Item.create(qtd = 3.0, unid = "pacotes", produto = feijao)
    lista = ListaDeCompra.create(titulo = "Compra básica")
    lista.itens.add([uni1, uni2])

    print(lista)
