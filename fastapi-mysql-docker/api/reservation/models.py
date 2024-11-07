from pydantic import BaseModel
from typing import Optional

# class ProductModel(BaseModel):
#     id:  Optional[int] = None
#     product_name: str
#     description: Optional[str] = None
#     price: float


class CustomerModel(BaseModel):
    Customer_id: str
    Customer_name: str
    Phonenumber: str 
    Email: str

class GuideModel(BaseModel):
    Guide_id: str
    Email: str
    Languages: str

class CompanyModel(BaseModel):
    Company_Name: str
    Total: Optional[int] = None

class ProgramTourModel(BaseModel):
    location_id: str
    location_Name: str

class ReservationModel(BaseModel):
    Booking_id: str
    Firstdate: str
    Lastdate: str
