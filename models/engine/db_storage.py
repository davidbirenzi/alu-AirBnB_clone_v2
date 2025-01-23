#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State


class DBStorage:
    """This class manages storage for hbnb clone"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        result = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(City, State).all()
        for obj in objs:
            key = f"{obj.__class__.__name__}.{obj.id}"
            result[key] = obj
        return result

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
