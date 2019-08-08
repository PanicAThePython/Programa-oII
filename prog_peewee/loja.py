from peewee import *
import os

db = SqliteDatabase('loja.db')

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):

    nome = CharField()
    email = CharField()

    def __str__(self):
        return "Cliente "+self.nome+" de e-mail "+self.email

class Produto(BaseModel):

    descricao = CharField()
    preco = FloatField()

    def __str__(self):
        return self.descricao+" que custa R$"+str(self.preco)

class Venda(BaseModel):

    produtos = ManyToManyField(Produto)
    cliente = ForeignKeyField(Cliente)
    data_hora = DateTimeField()

    def __str__(self):
        l=[]
        for i in self.produtos:
            l.append(i)

        return "Venda do(s) produto(s) "+str(l)+" para a(o) "+str(self.cliente)+" no dia e hora: "+str(self.data_hora)

if __name__=='__main__':
    arq = 'loja.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Cliente, Produto, Venda, Venda.produtos.get_through_model()])
    except OperationalError as e:
        print(e)

    cliente = Cliente.create(nome = "Fred Weasley", email = 'fred.wsly@hogsmail.com')
    produt1 = Produto.create(descricao = "Bomba de bosta da Zonko's", preco = 5)
    produt2 = Produto.create(descricao = "Bisbilhômetro", preco = 8.60)
    venda = Venda.create(cliente = cliente, data_hora = '30-10-1995 15:12:07')
    venda.produtos.add([produt1, produt2])

    print(venda)