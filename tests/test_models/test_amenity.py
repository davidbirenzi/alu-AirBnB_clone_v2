#!/usr/bin/python3
"""Class amenity Module for HBNB project """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """class test Amenity """

    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test name functionality """
        new = self.value()
        self.assertEqual(type(new.name), str)
