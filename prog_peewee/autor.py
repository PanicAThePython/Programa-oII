from peewee import *
import os

db = SqliteDatabase("autor.db")

class BaseModel(Model):
    class Meta:
        database =db

class Autor(BaseModel):

    nome = CharField()

    def __str__(self):

        return str(self.nome)

class Livro(BaseModel):

    titulo = CharField()
    ano = IntegerField()
    genero = CharField()

    def __str__(self):

        return str(self.titulo)+" do ano de "+str(self.ano)+" do genero "+str(self.genero)       

class Biblioteca(BaseModel):

    autor = ForeignKeyField(Autor)
    livro = ForeignKeyField(Livro)

    def __str__(self):

        return str(self.autor)+" do livro "+str(self.livro)

if __name__=="__main__":

    arq = 'autor.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Autor, Livro, Biblioteca])
    except OperationalError as e:
        print("ERRO: "+str(e))

    livro1 = Livro.create(titulo = "Teoria da Vida", ano = 2035, genero = "Literatura Brasileira")
    livro2 = Livro.create(titulo = "Socorro", ano = 1978, genero = "Autoajuda")
    autor1 = Autor.create(nome = "Jusselina Pereira")
    autor2 = Autor.create(nome = "Micael Antônio")
    a1 = Biblioteca.create(autor = autor1, livro = livro1)    
    a2 = Biblioteca.create(autor = autor2, livro = livro2)

    print(a1)
    print(a2)