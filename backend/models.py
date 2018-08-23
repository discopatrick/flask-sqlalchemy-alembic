from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import mapper, relationship

from backend.database import Base


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))

    addresses = relationship(
        "Address", order_by=Address.id, back_populates="user")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


role = Table('role', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)


class Role(object):
    def __init__(self, name):
        self.name = name


mapper(Role, role)


company = Table('company', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)


class Company(object):
    def __init__(self, name):
        self.name = name


mapper(Company, company)
