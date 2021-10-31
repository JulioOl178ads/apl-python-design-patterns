from __future__ import annotations
from abc import ABC, abstractmethod

#Classe abstrata que será utilizada como base na criação dos outros metododos de criação de produtos
class AbstractFactory(ABC):
    """[summary]
        Classe abstrata da Factory que servirá de consumo para as classes filhas
    Args:
        ABC ([ABC]): [Abstract Class imported from abc.py]
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

#Classe que ao herdar a classe abstrata terá que declarar os métodos que a classe abstrata mãe possui
#O metodo de criacao de produto então irá chamar os métodos que retornarão o que há contido na string quando chamados
class ConcreteFactory1(AbstractFactory):
    """[summary]
        Classe filha que herdará os traços da AbstractFactory e terá de implementar seus métodos
    Args:
        AbstractFactory ([AbstractFactory]): [Abstract Factory Class]
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

#Classe que ao herdar a classe abstrata terá que declarar os métodos que a classe abstrata mãe possui
#O metodo de criacao de produto então irá chamar os métodos que retornarão o que há contido na string quando chamados
class ConcreteFactory2(AbstractFactory):
    """[summary]
        Classe filha que herdará os traços da AbstractFactory e terá de implementar seus métodos
    Args:
        AbstractFactory ([AbstractFactory]): [Abstract Factory Class]
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

#Método abstrato que será utilizado pelos produtos para formarem os objetos do produto
class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


def factory_start():
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())