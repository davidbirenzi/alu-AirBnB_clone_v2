#!/usr/bin/python3
""" Class Review Module for HBNB project """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Class Review Module for HBNB project """

    def __init__(self, *args, **kwargs):
        """ Init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test place id functionality """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test user id functionality """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test text functionality """
        new = self.value()
        self.assertEqual(type(new.text), str)
