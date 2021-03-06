from datamodel import Places


class PlacesDataStore:
    """
    class that defines a container to hold Places objects and
    provide functions to access, filter and query data
    """

    def __init__(self):
        """
        Constructor
        """
        self.__data = {}

    def add_place(self, _place: Places):
        self.__data[_place.get_sku()] = _place

    def remove_place(self, _place_id: str):
        self.__data.pop(_place_id, None)  # remove key from dict, return object if key existed or None otherwise

    def size(self) -> int:
        return len(self.__data)

    def find_place_by_id(self, _id: str) -> Places:
        return self.__data.get(_id)  # get(key) returns None if key is not found

    def find_places_by_day(self, _day: str) -> []:
        places = []
        for p in self.__data.values():
            if p.get_day() == _day:
                places.append(p)
        return places

    def find_all_places(self) -> []:
        return list(self.__data.values())

