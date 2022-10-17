from ebanistika.parents import Model
from ebanistika.parents import Serializer

class User(Model):
    model = Model()
    user_id = model.serial(name='user_id', primary=False)
    name = model.varChar(name='gaymaster', length='228')
    age = model.integer(name='age')

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nID: {self.user_id}'

class UserSerializer(Serializer):
    pass

# print(User())