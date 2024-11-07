from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
#product ต้องเปลี่ยนเป็น reservation
from reservation import (CustomerModel,get_all_Customer,get_Customer_by_Customer_id,add_Customer,update_Customer,delete_Customer,
                    GuideModel,get_all_Guide,get_Guide_by_Guide_id,add_Guide,update_Guide,delete_Guide,
                    CompanyModel,get_all_Company,
                    ProgramTourModel,get_all_ProgramTour,get_ProgramTour_by_location_id,add_ProgramTour,update_ProgramTour,delete_ProgramTour,
                    ReservationModel,get_all_Reservation,get_Reservation_by_Booking_id,add_Reservation,update_Reservation,delete_Reservation)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ProductModel,get_all_product,get_product_by_id,add_product,update_product,delete_product
# #Get param
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/result/{score}")
# async def result_exam(score:int):
#     if(score >= 50):
#         result = "Pass"
#     else:
#         result = "No pass"
#     return {"your result is": result}

# @app.get("/result_by_query/")
# async def result_exam(score:int, name:str):
#     if(score >= 50):
#         result = name + " Pass"
#     else:
#         result = name + " No pass"
#     return {"your result is": result}
# # from pydantic import BaseModel
# # from typing import Optional

# # class ProductModel(BaseModel):
# #     id: Optional[int] = None
# #     product_name: str
# #     description: Optional[str] = None
# #     price: float

# # @app.post('/create_product/', response_model=ProductModel)
# # def create_product_api(product: ProductModel):
# #     item_dict = product.dict()
# #     print(item_dict)
# #     return JSONResponse(status_code=201, content=item_dict)

# # ##GET


# @app.get("/get_all_product/", response_model=list[ProductModel])
# def get_all_product_api():
#     products = get_all_product()
#     print(products)
#     return JSONResponse(status_code=200, content=jsonable_encoder(products))




# @app.get("/get_product/{id}", response_model=ProductModel)
# def get_product_by_id_api(id:int):
#     products = get_product_by_id(id)
#     print(products)
#     return JSONResponse(status_code=200, content=jsonable_encoder(products))

# # ##POST
# ##create
# @app.post('/create_product/', response_model=ProductModel)
# def create_product_api(product: ProductModel):
#     product_id = add_product(product)
#     return JSONResponse(status_code=201, content={'status': 'success', 'product_id': product_id})

# ## UPDATE
# @app.put("/update_product/{id}", response_model=ProductModel)
# def update_product_api(id: int, product: ProductModel):
#     # Check if product exists
#     existing_product = get_product_by_id(id)
#     if len(existing_product) == 0:
#         raise HTTPException(status_code=404, detail="Data not found")
#     updated_product = update_product(id, product)
#     if updated_product:
#         return JSONResponse(status_code=200, content={'status': 'success', 'product_data': updated_product})
#     else:
#         raise HTTPException(status_code=500, detail="Failed to update data")


# #Delete
# @app.delete("/delete_product/{id}", response_model=ProductModel)
# def delte_product_api(id: int):
#     # Check if product exists
#     existing_product = get_product_by_id(id)
#     if len(existing_product) == 0:
#         raise HTTPException(status_code=404, detail="Data not found")
#     is_deleted = delete_product(id)
#     if is_deleted:
#         return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
#     else:
#         raise HTTPException(status_code=500, detail="Failed to delete data")


#-----------------------------------Customer------------------------------------------------------#
#GET
#get_all_Customer----------------------------
@app.get("/get_all_Customer/", response_model=list[CustomerModel])
def get_all_Customer_api():
    Customer = get_all_Customer()
    print(Customer)
    return JSONResponse(status_code=200, content=jsonable_encoder(Customer))
#get_Customer_id-----------------------------
@app.get("/get_Customer/{id}", response_model=CustomerModel)
def get_Customer_by_Customer_id_api(id:str):
    Customer = get_Customer_by_Customer_id(id)
    print(Customer)
    return JSONResponse(status_code=200, content=jsonable_encoder(Customer))
#POST
#create_Customer-------------------------------
# ##create
@app.post('/create_Customer/', response_model=CustomerModel)
def create_Customer_api(Customer: CustomerModel):
    Customer_id = add_Customer(Customer)
    return JSONResponse(status_code=201, content={'status': 'success', 'Customer_id': Customer_id})
#update_Customer-----------------------------
@app.put("/update_Customer/{id}", response_model=CustomerModel)
def update_Customer_api(id: str, Customer: CustomerModel):
    # Check if customer exists
    existing_Customer = get_Customer_by_Customer_id(id)
    if len(existing_Customer) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    updated_Customer = update_Customer(id, Customer) 
    if updated_Customer:
        return JSONResponse(status_code=200, content={'status': 'success', 'Customer_data': updated_Customer})
    else:
        raise HTTPException(status_code=500, detail="Failed to update customer data")
#DELETE
#delte_Customer-----------------------------------
@app.delete("/delete_Customer/{id}", response_model=CustomerModel)
def delte_Customer_api(id: str):
    # Check if Customer exists
    existing_Customer = get_Customer_by_Customer_id(id)
    if len(existing_Customer) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    is_deleted = delete_Customer(id)
    if is_deleted:
        return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
    else:
        raise HTTPException(status_code=500, detail="Failed to delete data")

#-----------------------------------Guide------------------------------------------------------#
#GET
#get_all_Guide----------------------------
@app.get("/get_all_Guide/", response_model=list[GuideModel])
def get_all_Guide_api():
    Guide = get_all_Guide()
    print(Guide)
    return JSONResponse(status_code=200, content=jsonable_encoder(Guide))
#get_Guide_id-----------------------------
@app.get("/get_Guide/{id}", response_model=GuideModel)
def get_Guide_by_Guide_id_api(id:str):
    Guide = get_Guide_by_Guide_id(id)
    print(Guide)
    return JSONResponse(status_code=200, content=jsonable_encoder(Guide))
#POST
#create_Guide-------------------------------
@app.post('/create_Guide/', response_model=GuideModel)
def create_Guide_api(Guide: GuideModel):
    Guide_id = add_Guide(Guide)
    return JSONResponse(status_code=201, content={'status': 'success', 'Guide_id': Guide_id})
#update_Guide-----------------------------
@app.put("/update_Guide/{id}", response_model=GuideModel)
def update_Guide_api(id: str, Guide: GuideModel):
    # Check if Guide exists
    existing_Guide = get_Guide_by_Guide_id(id)
    if len(existing_Guide) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    updated_Guide = update_Guide(id, Guide) 
    if updated_Guide:
        return JSONResponse(status_code=200, content={'status': 'success', 'Guide_data': updated_Guide})
    else:
        raise HTTPException(status_code=500, detail="Failed to update Guide data")
#DELETE
#delte_Guide-----------------------------------
@app.delete("/delete_Guide/{id}", response_model=GuideModel)
def delte_Guide_api(id: str):
    # Check if Guide exists
    existing_Guide = get_Guide_by_Guide_id(id)
    if len(existing_Guide) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    is_deleted = delete_Guide(id)
    if is_deleted:
        return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
    else:
        raise HTTPException(status_code=500, detail="Failed to delete data")

#-----------------------------------Company------------------------------------------------------#
#GET
#get_all_Company----------------------------
@app.get("/get_all_Company/", response_model=list[CompanyModel])
def get_all_Company_api():
    Company = get_all_Company()
    print(Company)
    return JSONResponse(status_code=200, content=jsonable_encoder(Company))
#อาจจะไม่ต้องมีในส่วนของ Company*******************************************************************************
# #get_Guide_id-----------------------------
# @app.get("/get_Guide/{id}", response_model=GuideModel)
# def get_Guide_by_Guide_id_api(id:str):
#     Guide = get_Guide_by_Guide_id(id)
#     print(Guide)
#     return JSONResponse(status_code=200, content=jsonable_encoder(Guide))
# #POST
# #create_Guide-------------------------------
# @app.post('/create_Guide/', response_model=GuideModel)
# def create_Guide_api(Guide: GuideModel):
#     Guide_id = add_Guide(Guide)
#     return JSONResponse(status_code=201, content={'status': 'success', 'Guide_id': Guide_id})
# #update_Guide-----------------------------
# @app.put("/update_Guide/{id}", response_model=GuideModel)
# def update_Guide_api(id: str, Guide: GuideModel):
#     # Check if Guide exists
#     existing_Guide = get_Guide_by_Guide_id(id)
#     if len(existing_Guide) == 0:
#         raise HTTPException(status_code=404, detail="data not found")
#     updated_Guide = update_Guide(id, Guide) 
#     if updated_Guide:
#         return JSONResponse(status_code=200, content={'status': 'success', 'Guide_data': updated_Guide})
#     else:
#         raise HTTPException(status_code=500, detail="Failed to update Guide data")
# #DELETE
# #delte_Guide-----------------------------------
# @app.delete("/delete_Guide/{id}", response_model=GuideModel)
# def delte_Guide_api(id: str):
#     # Check if Guide exists
#     existing_Guide = get_Guide_by_Guide_id(id)
#     if len(existing_Guide) == 0:
#         raise HTTPException(status_code=404, detail="Data not found")
#     is_deleted = delete_Guide(id)
#     if is_deleted:
#         return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
#     else:
#         raise HTTPException(status_code=500, detail="Failed to delete data")
#********************************************************************************************************************

#-----------------------------------ProgramTour------------------------------------------------------#
#GET
#get_all_ProgramTour----------------------------
@app.get("/get_all_ProgramTour/", response_model=list[ProgramTourModel])
def get_all_ProgramTour_api():
    ProgramTour = get_all_ProgramTour()
    print(ProgramTour)
    return JSONResponse(status_code=200, content=jsonable_encoder(ProgramTour))
#get_location_id-----------------------------
@app.get("/get_ProgramTour/{id}", response_model=ProgramTourModel)
def get_ProgramTour_by_location_id_api(id:str):
    ProgramTour = get_ProgramTour_by_location_id(id)
    print(ProgramTour)
    return JSONResponse(status_code=200, content=jsonable_encoder(ProgramTour))
#POST
#create_ProgramTour-------------------------------
@app.post('/create_ProgramTour/', response_model=ProgramTourModel)
def create_ProgramTour_api(ProgramTour: ProgramTourModel):
    location_id = add_ProgramTour(ProgramTour)
    return JSONResponse(status_code=201, content={'status': 'success', 'location_id': location_id})
#update_ProgramTour-----------------------------
@app.put("/update_ProgramTour/{id}", response_model=ProgramTourModel)
def update_ProgramTour_api(id: str, ProgramTour: ProgramTourModel):
    # Check if ProgramTour exists
    existing_ProgramTour = get_ProgramTour_by_location_id(id)
    if len(existing_ProgramTour) == 0:
        raise HTTPException(status_code=404, detail="data not found")
    updated_ProgramTour = update_ProgramTour(id, ProgramTour) 
    if updated_ProgramTour:
        return JSONResponse(status_code=200, content={'status': 'success', 'ProgramTour_data': updated_ProgramTour})
    else:
        raise HTTPException(status_code=500, detail="Failed to update Guide data")
#DELETE
#delte_ProgramTour-----------------------------------
@app.delete("/delete_ProgramTour/{id}", response_model=ProgramTourModel)
def delte_ProgramTour_api(id: str):
    # Check if ProgramTour exists
    existing_ProgramTour = get_ProgramTour_by_location_id(id)
    if len(existing_ProgramTour) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    is_deleted = delete_ProgramTour(id)
    if is_deleted:
        return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
    else:
        raise HTTPException(status_code=500, detail="Failed to delete data")

#-----------------------------------Reservation------------------------------------------------------#
#GET
#get_all_Reservation----------------------------
@app.get("/get_all_Reservation/", response_model=list[ReservationModel])
def get_all_Reservation_api():
    Reservation = get_all_Reservation()
    print(Reservation)
    return JSONResponse(status_code=200, content=jsonable_encoder(Reservation))
#get_Reservation_id-----------------------------
@app.get("/get_Reservation/{id}", response_model=ReservationModel)
def get_Reservation_by_Booking_id_api(id:str):
    Reservation = get_Reservation_by_Booking_id(id)
    print(Reservation)
    return JSONResponse(status_code=200, content=jsonable_encoder(Reservation))
#POST
#create_Reservation-------------------------------
@app.post('/create_Reservation/', response_model=ReservationModel)
def create_Reservation_api(Reservation: ReservationModel):
    Booking_id = add_Reservation(Reservation)
    return JSONResponse(status_code=201, content={'status': 'success', 'Booking_id': Booking_id})
#update_Reservation-----------------------------
@app.put("/update_Reservation/{id}", response_model=ReservationModel)
def update_Reservation_api(id: str, Reservation: ReservationModel):
    # Check if Reservation exists
    existing_Reservation = get_Reservation_by_Booking_id(id)
    if len(existing_Reservation) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    updated_Reservation = update_Reservation(id, Reservation) 
    if updated_Reservation:
        return JSONResponse(status_code=200, content={'status': 'success', 'Reservation_data': updated_Reservation})
    else:
        raise HTTPException(status_code=500, detail="Failed to update Guide data")
#DELETE
#delete_Reservation-----------------------------------
@app.delete("/delete_Reservation/{id}", response_model=ReservationModel)
def delte_Reservation_api(id: str):
    # Check if Reservation exists
    existing_Reservation = get_Reservation_by_Booking_id(id)
    if len(existing_Reservation) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    is_deleted = delete_Reservation(id)
    if is_deleted:
        return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
    else:
        raise HTTPException(status_code=500, detail="Failed to delete data")

