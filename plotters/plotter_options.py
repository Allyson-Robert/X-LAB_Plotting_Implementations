class PlotterOptions:
    def __init__(self):
        self.options = {}
        self.handlers = {}

    def add_option(self, label: str, value: Any) -> bool:
        self.options[label] = value
        return True

    def get_option(self, label: str) -> Any:
        # Let the method raise an error if the key does not exist
        return self.options[label]

    def is_instance_valid(self, options_array):
        try:
            for option in options_array:
                self.get_option(label = option)
        except:
            raise ValueError("Invalid Options Object")
        return True

    def add_handler(self, label: str, handler: callable) -> bool:
        """
        Attach a custom handler for a specific option. This corresponds to a delegation of responsability
        """
        if label not in self.options:
            raise KeyError(f"Option '{label}' must be defined before adding a handler.")
        self.handlers[label] = handler
        return True

    def apply_handler(self, label: str, *args, **kwargs):
        """
        Apply the handler for the given option if it exists.
        """
        if label in self.handlers:
            return self.handlers[label](self.options[label], *args, **kwargs)
        return None
