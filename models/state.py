#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage_type



class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]

