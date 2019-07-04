from peewee import *
import os

db = SqliteDatabase("vendas.db")

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):

    nome = CharField()
    email = CharField()

    def __str__(self):

        return "Cliente "+str(self.nome)+" de e-mail "+str(self.email)

class Produto(BaseModel):

    descricao = CharField()
    preco = FloatField()

    def __str__(self):

        return str(self.descricao)+" que custa "+str(self.preco)

class Venda(BaseModel):

    data_hora = DateTimeField()
    produtos = ManyToManyField(Produto)
    clientes = ForeignKeyField(Cliente)

    def __str__(self):

        l=[]
        for i in self.produtos:
            l.append(i)

        return "Venda do(s) produto(s)"+str(l)+" para o(s) cliente(s) "+str(self.clientes)+" na data e hora "+str(self.data_hora)


if __name__=="__main__":
    arq = 'vendas.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Cliente, Produto, Venda, Venda.produtos.get_through_model()])
    except OperationalError as e:
        print(e)
    
    na = Cliente.create(nome = 'Natália', email = 'nataliaweise@gmail.com')
    nay = Cliente.create(nome = 'Naielly', email = 'naiellyrc10@gmail.com')
    prod1 = Produto.create(descricao = "Fone de ouvido branco da Oex", preco = 39.90)
    prod2 = Produto.create(descricao = 'XBox', preco = 2099)
    prod3 = Produto.create(descricao = 'Notebook Acer 1TB', preco = 1600)
    venda1 = Venda.create(data_hora = '2018-04-02 19:30:17', clientes = na)
    venda2 = Venda.create(data_hora = '2018-12-02 09:30:17', clientes = nay)
    venda2.produtos.add(prod2)
    venda1.produtos.add([prod1, prod3])

    print(venda1)
    print(venda2)
