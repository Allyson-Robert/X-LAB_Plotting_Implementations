from contracts.data_processors import DataProcessorCore
from implementations.data.data_types.generic_scatter import GenericScatterData
from utils.errors.errors import ObservableNotComputableError


class ScatterDataProcessor(DataProcessorCore):
    """
    ScatterDataProcessor
    ====================

    A lightweight processor for `GenericScatterData` objects. This class extends
    `DataProcessorCore` and provides basic validation of requested observables.
    For more complex data this class would implement some validation or computation
    of derived observables.

    Overview
    --------
    `ScatterDataProcessor` delegates observable access and unit retrieval to the
    underlying `GenericScatterData` instance. It does not compute additional
    derived quantities as it is not needed; it simply ensures that requested
    observables can be retrieved.

    - Wraps a `GenericScatterData` object
    - Validates observable names before use
    - Raises `ObservableNotComputableError` if a requested observable cannot be obtained

    Usage Notes
    -----------
    This processor is intended for simple scatter-type datasets where only raw
    observables (e.g., *independent*, *dependent*, *label*, *datetime*) are
    required. Derived or computed observables should be implemented in dedicated
    processor subclasses.
    """

    def __init__(self, scatter_data: GenericScatterData):
        super().__init__(scatter_data)

    def validate_observables(self, *args):
        print(*args)
        # Checks whether all desired observables can be obtained for this data
        try:
            for observable in args:
                self.get_data(observable)
        # FIXME: Catchall try-except
        except:
            raise ObservableNotComputableError
