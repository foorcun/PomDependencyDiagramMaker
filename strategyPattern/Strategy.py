

from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def doOperation(self, pomContent):
        pass