"""
O proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o codigo cliente 
gostaria de usar.
O proxy receberá as solicitações e tera controle
sobre como e quando repassar tais solicitações ao 
objeto real

Com base no modo como o proxies são usados,
nós os classificamos como:

-Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.

-Proxy Remoto: controla acesso a recursos que
estão em servidores remotos.

-Proxy de proteção: controla acesso a recursos que possam 
necessotar autenticação ou permissão.
 
 -Proxy inteligente: além de controlar acesso ao
 objeto real, também executa tarefas adicionais para
 saber quando e como executar determinadas ações.

Proxies podem fazer varias coisas diferentes:
criar logs, autenticar usuarios, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List


class IUser(ABC):
    """ Subject Interface """
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    """ Real Subject """

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # Simulando Requisição
        return [
            {'rua': 'Av.Brasil', 'numero': 500}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # Simulando Requisição
        return {
            'cpf': '111.111.111-11',
            'rg': 'AB111222444'}


class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser

        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cachedd_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    luiz = UserProxy('Luiz', 'Otavio')

    print(luiz.firstname)
    print(luiz.lastname)

    # 6 segundos
    print(luiz.get_all_user_data())
    print(luiz.get_addresses())

    # Responde instantaneamente
    print('CACHED DATA:')
    for i in range(10):
        print(luiz.get_addresses())
