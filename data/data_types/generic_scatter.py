from contracts.data_types import DataCore
from implementations.utils.file_readers.read_table_csv import read_csv
from utils.logging import with_logging, DEBUG_DATA_TYPE

class GenericScatterData(DataCore):
    """
    GenericScatterData
    ==================

    A lightweight data container class for simple two-column scatter-type datasets.
    This class derives from `DataCore` and provides a minimal implementation for
    reading CSV or Excel files containing paired *independent* (x) and *dependent*
    (y) variables.

    Overview
    --------
    `GenericScatterData` is intended for plotters or processors that work with
    generic x–y data without prescribing specific physical quantities. The class:

    - Stores all raw observable data
    - Exposes four possible observables:
        - ``label``: A string passed during construction.
        - ``independent``: X-axis data (units: "Independent var (a.u.)").
        - ``dependent``: Y-axis data (units: "Dependent var (a.u.)").
        - ``datetime``: Extracted from the filename

    Attributes
    ----------
    label_format : str
        Datetime formatting string used for timestamp extraction from filenames.

    dt_pattern : str
        Regular expression pattern for detecting the encoded timestamp in filenames.

    _allowed_observables : KeysView
        Set internally based on ``raw_data`` keys. Used by :meth:`DataCore.get_data`.

    Usage Notes
    -----------
    This class is commonly paired with :class:`DataProcessor` subclasses and may be
    used by scatter-based plotters. It is intentionally generic: units and semantic
    meaning of variables are left to the user or to processing layers.

    """
    def __init__(self, label):
        super().__init__(file_reader=read_csv)
        self.raw_data = {
            "label": {"units": "N/A", "data": label},
            "independent": None,
            "dependent": None,
            "datetime": None,
        }
        self._allowed_observables = self.raw_data.keys()
        self.label_format = "%Y_%m_%d_%H_%M_%S"
        self.dt_pattern = '\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}'

    @with_logging
    def read_file(self, filepath: str):
        data = self.file_reader(filepath)
        # Assume first two columns are independent and dependent variables
        if self.raw_data['independent'] is None:
            self.raw_data['independent'] = {"units": "Independent var (a.u.)", "data": data['0']}
        if self.raw_data['dependent'] is None:
            self.raw_data['dependent'] = {"units": "Dependent var (a.u.)", "data": data['1']}
