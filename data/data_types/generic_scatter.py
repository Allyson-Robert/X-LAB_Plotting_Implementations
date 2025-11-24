from contracts.data_types import DataCore
from utils.file_readers.read_table_csv import read_csv
import pandas as pd


class GenericScatterData(DataCore):
    def __init__(self, label):
        super().__init__()
        self.raw_data = {
            "label": {"units": "N/A", "data": label},
            "independent": None,
            "dependent": None,
            "datetime": None,
        }
        self._allowed_observables = self.raw_data.keys()
        self.label_format = "%Y_%m_%d_%H_%M_%S"
        self.dt_pattern = '\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}'

    def read_file(self, filepath: str):
        # Check whether this is an excel file or a csv
        if 'xls' in filepath.split('.')[-1]:
            data = pd.read_excel(filepath)
            x_data = data[data.keys()[0]]
            y_data = data[data.keys()[1]]
        else:
            data = read_csv(filepath)
            x_data = data[0][1:]
            y_data = data[1][1:]

        if self.raw_data['independent'] is None:
            self.raw_data['independent'] = {"units": "Independent var (a.u.)", "data": x_data}
        if self.raw_data['dependent'] is None:
            self.raw_data['dependent'] = {"units": "Dependent var (a.u.)", "data": y_data}
