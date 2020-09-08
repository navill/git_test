from __future__ import annotations
import abc
from typing import Any

"""test complete"""
"""git_test-10: test issue"""
diaskldfjjaser
class Builder(metaclass=abc.ABCMeta):
    def product(self):
        pass

    @abc.abstractmethod
    def product_part_a(self) -> None:
        pass

    @abc.abstractmethod
    def product_part_b(self) -> None:
        pass

    @abc.abstractmethod
    def product_part_c(self) -> None:
        pass

    @abc.abstractmethod
    def product_part_d(self) -> None:
        pass

    @abc.abstractmethod
    def product_part_e(self) -> None:
        pass


class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        def reset(self) -> None:
            self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()

    def product_part_a(self) -> None:
        self._product.add('part_A')

    def product_part_b(self) -> None:
        def product_part_c(self) -> None:
            pass

        def product_part_d(self) -> None:
            pass

        def product_part_e(self) -> None:
            self._product.add('part_E')


class Product:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"product parts:{', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimum_product(self) -> None:
        self.builder.product_part_a()

    def build_full_product(self) -> None:
        self.builder.product_part_b()
        self.builder.product_part_c()
        self.builder.product_part_d()


if __name__ == '__main__':
    director = Director()
    concrete_builder = ConcreteBuilder()
    director.builder = concrete_builder
    director.build_minimum_product()
    director.builder.product.list_parts()
    print('\n')
    # product
    director.builder.product.list_parts()
