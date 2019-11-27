from peewee import *
import os

arq = 'evento.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Musica(BaseModel):

    nome = CharField()
    album = CharField()

    def __str__(self):
        return "Música "+self.nome+" do álbum "+self.album

class Instrumento(BaseModel):

    nome = CharField()
    modelo = CharField()
    cor = CharField()

    def __str__(self):
        return "Instrumento "+self.nome+" de cor "+self.cor+", modelo "+self.modelo

class Integrante(BaseModel):

    nome = CharField()
    cargo = CharField()

    def __str__(self):
        return self.cargo+" "+self.nome

class Banda(BaseModel):

    nome = CharField()
    genero = CharField()
    integrantes = ManyToManyField(Integrante)
    instrumentos = ManyToManyField(Instrumento)

    def __str__(self):

        lista_intg = []
        lista_intm = []

        for integrante in self.integrantes:
            lista_intg.append(integrante)
        
        for instrumento in self.instrumentos:
            lista_intm.append(instrumento)

        return self.nome +", que é uma banda do gênero "+self.genero+" composta pelos integrantes "+str(lista_intg)+". A banda usa os instrumentos"+\
            str(lista_intm)

class Palco(BaseModel):

    nome = CharField()

    def __str__(self):
        return self.nome

class Show(BaseModel):

    data_hora = DateTimeField()
    banda = ForeignKeyField(Banda)
    palco = ForeignKeyField(Palco)
    musicas = ManyToManyField(Musica)

    def __str__(self):
        lista_musi = []
        for musica in self.musicas:
            lista_musi.append(musica)

        return "O show da banda "+str(self.banda)+" trará o seguinte setlist: "+str(lista_musi)+"; e ocorrerá no palco "+\
            str(self.palco)+" na seguinte data e hora: "+self.data_hora

class Espaco(BaseModel):

    nome = CharField()
    obs = CharField()

    def __str__(self):
        return self.nome+": "+self.obs

class Patrocinador(BaseModel):

    nome = CharField()
    status = CharField()

    def __str__(self):
        return self.nome+", "+self.status

class Festival(BaseModel):

    nome = CharField()
    local = CharField()
    data_inicio = DateField()
    data_final = DateField()
    palcos = ManyToManyField(Palco)
    shows = ManyToManyField(Show)
    espacos = ManyToManyField(Espaco)
    patrocinadores = ManyToManyField(Patrocinador)

    def __str__(self):
        lista_palcos = []
        lista_shows = []
        lista_espacos = []
        lista_patro = []

        for palco in self.palcos:
            lista_palcos.append(palco)

        for show in self.shows:
            lista_shows.append(show)

        for espaco in self.espacos:
            lista_espacos.append(espaco)

        for patrocinador in self.patrocinadores:
            lista_patro.append(patrocinador)

        return self.nome+", que ocorrerá no/na "+self.local+". Começará no dia "+self.data_inicio+\
            " e terminará no dia "+self.data_final+". O festival terá os seguintes shows: "+str(lista_shows)+", que ocorrerão nos palcos: "+\
                str(lista_palcos)+". Ele também tem outros espaços, tais como: "+str(lista_espacos)+". O evento tem os patrocinadores: "+\
                    str(lista_patro)

class Ingresso(BaseModel):

    valor = FloatField()
    tipo = CharField()
    festival = ForeignKeyField(Festival)

    def __str__(self):
        return "Ingresso "+self.tipo+" de valor "+str(self.valor)+" do festival "+str(self.festival)

if __name__=="__main__":

    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Musica, Instrumento, Integrante, Banda, Banda.integrantes.get_through_model(), Banda.instrumentos.get_through_model(), Palco, Show, Show.musicas.get_through_model(), Espaco, Patrocinador, Festival, Festival.palcos.get_through_model(), Festival.shows.get_through_model(), Festival.espacos.get_through_model(), Festival.patrocinadores.get_through_model(), Ingresso])

    iwsnt = Musica.create(nome = "I Write Sins Not Tragedies", album = "A Fever You Can't Sweet Out")
    tboml = Musica.create(nome = 'The Ballad Of Mona Lisa', album = 'Vices & Virtues')
    br = Musica.create(nome = "Bohemian Rhapsody", album = "Suicide Squad")
    guitarra = Instrumento.create(nome = "guitarra", cor = "preta", modelo = "top")
    bateria = Instrumento.create(nome = "bateria", cor = "preta", modelo = "panic")
    piano = Instrumento.create(nome = "piano", cor = "preta", modelo = "Mozart")
    baixo = Instrumento.create(nome = "baixo", cor = "prata", modelo = "chic")
    guitarra_solo = Instrumento.create(nome = "guitarra", cor = "dourada", modelo = "rich")
    nicole = Integrante.create(nome = "Nicole Row", cargo = "Baixista")
    brendon = Integrante.create(nome = "Brendon Urie", cargo = "Vocalista, Pianista e Guitarrista")
    dan = Integrante.create(nome = "Dan Pawlovich", cargo = "Baterista")
    mike = Integrante.create(nome = "Mike Narah", cargo = "Guitarrista")
    patd = Banda.create(nome = "Panic! At The Disco", genero = "Rock Alternativo")
    patd.instrumentos.add([guitarra, bateria, piano, baixo, guitarra_solo])
    patd.integrantes.add([nicole, brendon, dan, mike])
    mundo = Palco.create(nome = "Mundo")
    sunset = Palco.create(nome = "Sunset")
    supernova = Palco.create(nome = "Supernova")
    show = Show.create(data_hora = "10/3/2019 18:00:00", banda = patd, palco = mundo)
    show.musicas.add([iwsnt, tboml, br])
    roda_gigante = Espaco.create(nome = "Roda Gigante", obs = "Ótima vista")
    montanha = Espaco.create(nome = "Montanha Russa", obs = "Radical")
    big_tower = Espaco.create(nome = "Big Tower", obs = "Frio na Barriga")
    itau = Patrocinador.create(nome = "Itaú", status = "Master")
    riotur = Patrocinador.create(nome = "Riotur", status = "Institucional")
    coca = Patrocinador.create(nome="Coca-Cola", status = "Marca")
    rockinrio = Festival.create(nome = "Rock In Rio", local = "Parque Olímpico da Barra", data_inicio = "09/27/2019", data_final = '10/06/2019')
    rockinrio.palcos.add([mundo, sunset, supernova])
    rockinrio.patrocinadores.add([itau, coca, riotur])
    rockinrio.espacos.add([roda_gigante, montanha, big_tower])
    rockinrio.shows.add([show])
    ingresso = Ingresso.create(valor = 1300, tipo = 'inteiro', festival = rockinrio)
    
    print(ingresso)