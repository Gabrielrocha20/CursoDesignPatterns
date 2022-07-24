"""
Composite é um padrão de projeto estrutural que permite que 
você utilize a composição para criar objetos em estruturas
de arvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de 
objetos (Composite).

Importante: Só aplique este padrão em uma estrutura que possa
ser representada em formato hierarquico (arvore)

No padrão composite, temos dois tipos de objetos:
composite (que representa nos internos da arvore) e Leaf
(que representa nos externos da arvore).

Objetos Composite são objetos mais complexos e com filhos
Geralmente, eles delegam trabalho para os filhos usando um metodo em comun

Objetos Leaf sçao objetos simples, da ponta e sem filhos.
Geralmente, sao esses objetos que realizam o trabalho
real da aplicação
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    def add(self, child: BoxStructure) -> None:
        pass

    def remove(self, child: BoxStructure) -> None:
        pass


class Box(BoxStructure):
    """ Composite """

    def __init__(self, name) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    # leaf
    camiseta1 = Product('camiseta1', 49.90)
    camiseta2 = Product('camiseta2', 19.90)
    camiseta3 = Product('camiseta3', 10.90)

    # composite
    caixa_camisetas = Box('Caixa de camisetas')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)

    caixa_camisetas.print_content()
