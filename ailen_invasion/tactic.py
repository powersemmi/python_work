from abc import ABC, abstractmethod

"""Вносит в основной цикл игры функции, которые необходимо выполнить"""
class Strategy(ABC):
    @abstractmethod
    def doOperation(self, ):
