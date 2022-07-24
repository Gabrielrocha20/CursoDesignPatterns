"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompativeis trabalhem em conjunto 
através de um "adapta".
"""
from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    def top(self) -> None:
        print('Movendo para Cima...')

    def right(self) -> None:
        print('Movendo para Direita...')

    def down(self) -> None:
        print('Movendo para Baixo...')

    def left(self) -> None:
        print('Movendo para Esquerda...')


class NewControl:
    def move_top(self) -> None:
        print('Movendo para Cima...')

    def move_right(self) -> None:
        print('Movendo para Direita...')

    def move_down(self) -> None:
        print('Movendo para Baixo...')

    def move_left(self) -> None:
        print('Movendo para Esquerda...')


class ControlAdapter:
    def __init__(self, newcontrol: NewControl) -> None:
        self.new_control = newcontrol

    def top(self) -> None:
        self.new_control.move_top()

    def right(self) -> None:
        self.new_control.move_right()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()


class ControlAdapter2(Control, NewControl):
    def top(self) -> None:
        self.move_top()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()


if __name__ == '__main__':
    newcontrol = NewControl()
    control_object = ControlAdapter(newcontrol)

    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    # Control - Adapter Object

    control_class = ControlAdapter2()

    control_class.top()
    control_class.down()
    control_class.left()
    control_class.right()
