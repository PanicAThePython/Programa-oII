from peewee import *

db = SqliteDatabase("marcenaria.db")

class BaseModel(Model):

    class Meta:

        database =db
    
class Estoque(BaseModel):

    tip_material = CharField()

    def __str__(self):
        return str(self.tip_material)

class Mobilia(BaseModel):

    status = CharField()
    materiais = ManyToManyField(Estoque)

    def __str__(self):
        l = []

        for i in self.materiais:
            l.append(i)

        return str(self.status) + " e " + str(l)

class Pedido(BaseModel):

    mobilias = ManyToManyField(Mobilia)

    def __str__(self):
        l = []

        for i in self.mobilias:
            l.append(i)

        return str(l)

if __name__=="__main__":

    db.connect()
    db.create_tables([Estoque, Mobilia, Pedido, Mobilia.materiais.get_through_model(),
    Pedido.mobilias.get_through_model()])


    madeira = Estoque.create(tip_material="madeira")
    ferro = Estoque.create(tip_material="ferro")
    mob1 = Mobilia.create(status="pronta")
    mob1.materiais.add( [madeira, ferro] )
    mob2 = Mobilia.create(status="sob medida") 
    mob2.materiais.add(madeira)
    ped1 = Pedido.create()
    ped1.mobilias.add([mob1, mob2])

    print(madeira)
    print(ferro)
    print(mob1)
    print(mob2)
    print(ped1)






