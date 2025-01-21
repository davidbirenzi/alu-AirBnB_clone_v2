#!/usr/bin/python3
"""Class City Module for HBNB project """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ class test_City """

    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test state id functionality """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test name functionality """
        new = self.value()
        self.assertEqual(type(new.name), str)
