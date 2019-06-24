from peewee import *
import os 

db = SqliteDatabase("pessoa.db")

class Pessoa(Model):

    cpf = CharField()
    nome = CharField()
    endereco = CharField()
    telefone = CharField()

    class Meta():
        
        database = db

if __name__ == "__main__":
    '''
    arq = "pessoa.db"
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Pessoa])
    
    except OperationalError as err:
        print("ERROU")

    Pessoa.create (cpf = "090.012.919-02", nome = "Sofia Katherine Cimardi", 
    endereco = "Rua Itapema, 562", telefone = "(47) 9 9618-1422")
    '''
