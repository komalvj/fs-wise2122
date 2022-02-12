from collections.abc import Iterable
from datastore import PlacesDataStore, DataFactory
import datamodel as dm


class DataFactory:
    """
    class that defines a factory to create objects from imported data
    """

    def __init__(self, _places_ds: PlacesDataStore):
        """
        Constructor
        :param _places_ds: dependency injected for PlacesDataStore instance
        """
        # print(f'DataFactory singleton instantiated')
        self.__places_ds = _places_ds   # private, final, cannot be altered

    def import_places(self, _places: []) -> DataFactory:
        if isinstance(_places, Iterable):
            # iterate over tuple lists in 'list comprehension' style
            [self.__add_places_from_tuple(_t) for _t in _places]
        return self

    def __add_places_from_tuple(self, _t: ()):
        # sample tuple: ("1", "Brandenburg Tor", 1, "Landmarks")
        if len(_t) >= 3:
            _places_id = str(_t[0])
            _place = str(_t[1])
            _day = str(_t[2])
            _category = str(_t[3])
            _places_entity = dm.Places(_places_id, _place, _day, _category)
            self.__places_ds.add_place(_places_entity)
