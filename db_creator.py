from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Time  
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///appt.db', echo=True)
Base = declarative_base()


class Appointments(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True) # Customer ID
    FirstName = Column(String) # Customer First Name
    LastName = Column(String)# Customer Last Name
    TimeIN = Column(Time) #Time of Appointment

    def __repr__(self):
        return "{}".format(self.name)


Base.metadata.create_all(engine)