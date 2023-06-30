from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Medecin(Base):
    __tablename__ = "medecins"

    id = Column(Integer, primary_key=True, index=True)
    lastname = Column(String)
    firsname=Column(String)
    title = Column(String)
    speciality_id = Column(Integer, ForeignKey("specialities.id"))
    description=Column(String)
    phone=Column(String)
    address=Column(String)
    speciality=relationship('Speciality', back_populates='medecins')
    cabinets = relationship('Cabinet', secondary='cabinet_medecin', back_populates='medecins')



class Speciality(Base):
    __tablename__ = "specialities"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    medecins=relationship("Medecin", back_populates="speciality")

class Ville(Base):
    __tablename__ = "villes"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    cabinets=relationship("Cabinet", back_populates="ville")

class Cabinet(Base):
    __tablename__ = "cabinets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description=Column(String)
    phone=Column(String)
    address=Column(String)
    ville_id=Column(Integer, ForeignKey("villes.id"))
    ville=relationship("Ville", back_populates="cabinets")
    medecins = relationship('Medecin', secondary='cabinet_medecin', back_populates='cabinets')


class CabinetMedecin(Base):
    __tablename__ = "cabinet_medecin"

    id = Column(Integer, primary_key=True)

    cabinet_id = Column(Integer, ForeignKey('cabinets.id'))
    medecin_id = Column(Integer, ForeignKey('medecins.id'))

    