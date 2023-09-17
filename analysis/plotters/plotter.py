from abc import ABC, abstractmethod
from analysis.data.data_processors.data_processors import DataProcessor
from utils.logging import decorate_abc_with_debug_logging, DEBUG_PLOTTER

class Plotter(ABC):
    # This automatically wraps all of the abstract methods when implemented
    def __init_subclass__(cls):
        methods_to_decorate = [method_name for method_name in Plotter.__abstractmethods__ if method_name in cls.__dict__]
        decorate_abc_with_debug_logging(cls, methods_to_decorate, log_level=DEBUG_PLOTTER)

    @abstractmethod
    def ready_plot(self, processors: DataProcessor, options: dict):
        pass

    @abstractmethod
    def draw_plot(self):
        pass
