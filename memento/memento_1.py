"""
GoF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que voce salve e restaure
um estado anterior de um objeto originator sem revelar os detalhes
da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar momento]=s.
caretaker tambem e usado com o Padrão Command.
"""
from __future__ import annotations
from typing import Dict, List
from copy import deepcopy


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        object.__setattr__(self, "_state", state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name, value):
        raise AttributeError('Sorry, I am immutable')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    img = ImageEditor('FOTO_1.jpg', 111, 111)
    cartaker = Caretaker(img)

    cartaker.backup()

    img.name = 'Foto_2.jgp'
    img.width = 222
    img.height = 222

    cartaker.backup()

    img.name = 'Foto_3.jgp'
    img.width = 333
    img.height = 333

    cartaker.backup()

    img.name = 'Foto_4.jgp'
    img.width = 444
    img.height = 444

    cartaker.restore()

    print(img)
