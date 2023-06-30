from pydantic import BaseModel

class MedecinBase(BaseModel):
    id: int|None=None
    lastname: str 
    firsname:str
    title :str|None=None
    speciality_id:int
    description:str|None=None
    phone:str|None=None
    address:str|None=None

    class Config:
        orm_mode = True


class CabinetBase(BaseModel):
    id:int
    name:str|None=None
    firsname:str|None=None
    title :str|None=None
    description:str|None=None
    phone:str|None=None
    address:str|None=None
    ville_id:int|None=None

    class Config:
        orm_mode = True


class SpecialityBase(BaseModel):
    label:str
    class Config:
        orm_mode = True

class VilleBase(BaseModel):
    label:str
    class Config:
        orm_mode = True
       

class Speciality(SpecialityBase):
    medecins:list[MedecinBase]
    

class Medecin(MedecinBase):
    cabinets:list[CabinetBase]
    speciality:SpecialityBase=None


class Cabinet(CabinetBase):
    medecins:list[MedecinBase] 
    ville:VilleBase=None 

class Ville(VilleBase):
    cabinets:list[CabinetBase]
    