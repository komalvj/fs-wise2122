class Places:
    """
    class that defines a Places entity, which can be ordered
    """

    def __init__(self, _id: str, _place: str = "", _day: str = "", _category: str = ""):
        """
        Constructor of class
        :param _id: place keeping unit (SKU) (private, final, cannot be altered)
        :param _place: location in Berlin
        :param _day: day of the trip
        :param _category: place category
        """
        self.__sku = _id  # private, final, cannot be altered
        self.place = _place
        self.day = _day
        self.category = _category

    def get_sku(self):
        return self.__sku

    def set_sku(self, sku: str):
        self.__sku = sku

    def get_place(self):
        return self.place

    def set_place(self, place: str):
        self.place = place

    def get_day(self):
        return self.day

    def set_day(self, day: str):
        self.day = day

    def get_category(self):
        return self.category

    def set_category(self, category: str):
        self.category = category
