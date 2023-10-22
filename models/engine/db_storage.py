#!/usr/bin/python3
"""sqlalchemy module"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ['HBNB_MYSQL_USER'],
            os.environ['HBNB_MYSQL_PWD'],
            os.environ['HBNB_MYSQL_HOST'],
            os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True, echo=False)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        if os.environ['HBNB_ENV'] == 'test':
            metadata = MetaData(bind=self.__engine)
            metadata.drop_all()

    def all(self, cls=None):
        from models import storage
        dic = {}
        if cls is None:
            result = self.__session.query(
                State, User, City, Amenity, Place, Review).all()
            for r in result:
                dic[f"{r.__class__.__name__}.{r.id}"] = r
            return (dic)
        else:
            if (isinstance(cls, str)):
                result = self.__session.query(eval(cls)).all()
            else:
                result = self.__session.query(cls).all()

            for r in result:
                dic[f"{r.__class__.__name__}.{r.id}"] = r
            return (dic)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)

    def close(self):
        (self.__session).remove()
        # Session.close()
