"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite que subclasses
redefinam certo passos de um algoritmo sem mudar a estrutura do mesmo

também é possivel definir hooks para que as subclasses utilizem caso necessário

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.opderation1()
        self.base_class_method()
        self.opderation2()

    def hook(self): pass

    def base_class_method(self):
        print('Olá Eu sou da classe abstrata e serei executado tambem')

    @abstractmethod
    def opderation1(self): pass

    @abstractmethod
    def opderation2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Olha eu vou utilizar o hook')

    def opderation1(self):
        print('Operaçao 1 concluida')

    def opderation2(self):
        print('Operaçao 2 concluida')


class ConcreteClass2(Abstract):
    def opderation1(self):
        print('Operaçao 1 concluida (de maneira diferente)')

    def opderation2(self):
        print('Operaçao 2 concluida (de maneira diferente)')


if __name__ == '__main__':
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()
