from abc import ABC, abstractmethod
from utils.logging import decorate_abc_with_debug_logging, DEBUG_DATA_TYPE


# Abstract class for all data types
class AbstractData(ABC):
    # This automatically wraps all of the abstract methods when implemented
    # CHECK: This leads to a lot of messages at the DEBUG level, maybe I can define custom levels between DEBUG and INFO to manage the depth
    def __init_subclass__(cls):
        methods_to_decorate = [method_name for method_name in AbstractData.__abstractmethods__ if method_name in cls.__dict__]
        decorate_abc_with_debug_logging(cls, methods_to_decorate, log_level=DEBUG_DATA_TYPE)

    @abstractmethod
    def read_file(self, filepath: str) -> None:
        pass

    @abstractmethod
    def get_data(self, observable: str) -> list:
        pass

    @abstractmethod
    def get_units(self, observable: str) -> str:
        pass

    @abstractmethod
    def get_allowed_observables(self):
        pass


# Master class with implementation of 1) get_data, 2) get_units and 3) get_allowed_observables
class DataModel(AbstractData):
    def __init__(self):
        self.raw_data = {}
        self._allowed_observables = {}

    @abstractmethod
    def read_file(self, filepath: str) -> None:
        pass

    def get_data(self, observable: str):
        if observable in self._allowed_observables:
            return self.raw_data[observable]['data']
        else:
            raise ValueError(f"{self.__class__.__name__} does not contain {observable} data")

    def get_units(self, observable: str) -> str:
        self.get_data(observable)
        return self.raw_data[observable]["units"]

    def get_allowed_observables(self):
        return self._allowed_observables
