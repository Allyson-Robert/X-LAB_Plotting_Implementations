class PlotterOptions:
    def __init__(self):
        self.options = {}

    def add_option(self, label: str, value: Any) -> bool:
        self.options[label] = value
        return True

    def get_option(self, label: str) -> Any:
        # Let the method raise an error if the key does not exist
        return self.options[label]

