# class Meta(type):
#     def __call__(self, *args, **kwargs):
#         print('CALL é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('New é executado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('INIT é executado')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('Call Chamado', self.nome, x + y)


# p1 = Pessoa('Gabriel')
# print(p1.nome)
from typing import Dict


class Singleton(type):
    _instance: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'Tema escuro'
        self.font = '18 px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = "Qualquer outra coisa"
    print(as1.tema)
    as2 = AppSettings()
    as3 = AppSettings()

    print(as3.tema)
