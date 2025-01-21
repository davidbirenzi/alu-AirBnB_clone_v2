#!/usr/bin/python3
""" Class Place Module for HBNB project """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ test place class """

    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test city id functionality """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ test user id functionality """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test name functionality """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test description functionality """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test number rooms functionality """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test number bathrooms functionality """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test max guest functionality """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test price by night functionality """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test latitude functionality """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test longitude functionality """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test amenity ids functionality """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
