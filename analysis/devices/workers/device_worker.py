from abc import ABC, ABCMeta, abstractmethod
from fileset.fileset import Fileset
from PyQt5 import QtCore
from utils.logging import decorate_abc_with_debug_logging, ConsoleLogging, DEBUG_WORKER


# This custom metaclass is needed to make ABC and QObject multiple inheritance possible
#   Note: QObject provides default thread management tools
class WorkerMeta(type(ABC), type(QtCore.QObject)):
    pass


# Abstract baseclass to define worker objects and the required functions
class DeviceWorker(ABC, QtCore.QObject, metaclass=WorkerMeta):
    # This automatically wraps all of the abstract methods when implemented
    def __init_subclass__(cls):
        # Ensure that all abstract methods and potential plotters are decorated
        methods_to_decorate = [method_name for method_name in DeviceWorker.__abstractmethods__ if method_name in cls.__dict__]
        methods_to_decorate.extend([method_name for method_name in cls.__dict__ if "plot" in method_name])
        decorate_abc_with_debug_logging(cls, methods_to_decorate, log_level=DEBUG_WORKER)

    @abstractmethod
    def set_data(self,  fileset: Fileset):
        pass

    @abstractmethod
    def set_options(self,  *args, **kwargs):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def set_data_type(self, data_type):
        pass

    @abstractmethod
    def set_processor_type(self, processor_type):
        pass


# Default implementation of the DeviceWorker that can provide default functionality, only set_options needs to be implemented
class DeviceWorkerCore(DeviceWorker, ConsoleLogging):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    def __init__(self, device, fileset, plot_type):
        super().__init__()

        self.device = device
        self.fileset = fileset
        self.plot_type = plot_type

        self.data_processors = None

        self.processor_type = None
        self.data_type = None

    def set_data_type(self, data_type):
        self.data_type = data_type

    def set_processor_type(self, processor_type):
        self.processor_type = processor_type

    def set_data(self, fileset: Fileset):
        # CHECK: Check that data and processor types have been set
        # Initialise an empty dict and get the required filepaths
        self.data_processors = {}
        filepaths = fileset.get_filepaths()

        # Progress housekeeping
        nr_of_files = len(filepaths)
        counter = 0

        # Read the data and instantiate a processor for each file
        for key in filepaths:
            data = self.data_type(key)
            data.read_file(filepaths[key])
            self.data_processors[key] = self.processor_type(data)

            # Emit progress signal
            counter += 1
            self.progress.emit(int(100*counter/nr_of_files))

    def run(self):
        # Set the data
        self.set_data(self.fileset)

        # Pass the options
        self.set_options(**self.options)

        # Grab the correct plot and execute it
        plot_type = getattr(self, self.plot_type)
        plot_type(title=self.fileset.get_name())
        self.finished.emit()
