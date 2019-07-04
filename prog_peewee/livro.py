from peewee import *
import os

db = SqliteDatabase("livro.db")

class BaseModel(Model):
    class Meta:
        database = db

class Autor(BaseModel):

    nome = CharField()

    def __str__(self):
       
        return str(self.nome) 

class Livro(BaseModel):

    titulo = CharField()
    ano = IntegerField()
    genero = CharField()
    autors = ManyToManyField(Autor)

    def __str__(self):

        l=[]
        for a in self.autors:
            l.append(a)

        return "Livro "+str(self.titulo)+", do ano de "+str(self.ano) + ", do genero " + str(self.genero) + " do(s) autor(es): " +str(l)

if __name__ == "__main__":

    arq = 'livro.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Autor, Livro, Livro.autors.get_through_model()])
    except OperationalError as e:
        print("ERROOOOOOOOOOOO: "+str(e))

    livro1 = Livro.create(titulo = "Teoria da Vida", ano = 2035, genero = "Literatura Brasileira")
    livro2 = Livro.create(titulo = "Socorro", ano = 1978, genero = "Autoajuda")
    autor1 = Autor.create(nome = "Jusselina Pereira")
    autor2 = Autor.create(nome = "Micael Antônio")
    livro1.autors.add([autor1, autor2])

    print(autor1)
    print(autor2)
    print(livro1)
