from fastapi import HTTPException,APIRouter
from database.query import query_get, query_create, query_update
from .models import CustomerModel,GuideModel,CompanyModel,ProgramTourModel,ReservationModel
# ProductModel
# def get_all_product():
#     products = query_get("""
#         SELECT  
#             *
#         FROM product
#         """, ())
#     return products

# def get_product_by_id(id: int):
#     product = query_get("""
#         SELECT
#         *
#         FROM product
#         WHERE id = %s
#         """, (id))
#     return product

# def add_product(product: ProductModel):
#     last_row_id = query_create("""
#                 INSERT INTO product (
#                     product_name,
#                     description,
#                     price
#                 ) VALUES (%s, %s, %s)
#                 """,
#                 (
#                     product.product_name,
#                     product.description,
#                     product.price
#                 )
#                 )
#     return last_row_id

# def update_product(id: int,product: ProductModel):
#     is_update = query_update("""
#             UPDATE product
#                 SET product_name = %s,
#                     description = %s,
#                     price = %s
#                 WHERE id = %s;
#             """,
#             (
#             product.product_name,
#             product.description,
#             product.price,
#             id
#             )
#             )
#     if is_update:
#         product_update_data = product.dict()
#         product_update_data.update({"id": id})
#         return product_update_data
#     else:
#         return None

# def delete_product(id: int):
#     is_deleted = query_update("""
#             DELETE FROM product
#                 WHERE id = %s;
#             """,
#             (id)
#     )
#     return is_deleted
#-------------------------------------------------------CustomerModel-----------------------------------------------------------#
#get_all_Customer---------------
def get_all_Customer():
    Customers = query_get("""
        SELECT  
            *
        FROM Customer
        """, ())
    return Customers
#get_Customer_by_Customer_id---------------
def get_Customer_by_Customer_id(Customer_id: str):
    Customer = query_get("""
        SELECT
        *
        FROM Customer
        WHERE Customer_id = %s
        """, (Customer_id,))
    return Customer
#add_Customer---------------
def add_Customer(Customer: CustomerModel):
    last_row_id = query_create("""
                INSERT INTO Customer (
                    Customer_id,
                    Customer_name,
                    Phonenumber,
                    Email
                ) VALUES (%s, %s, %s, %s)
                """,
                (
                    Customer.Customer_id,
                    Customer.Customer_name,
                    Customer.Phonenumber,
                    Customer.Email
                )
                )
    return last_row_id
#update_Customer--------------------
def update_Customer(Customer_id: str, Customer: CustomerModel):
    is_update = query_update("""
            UPDATE Customer
                SET Customer_name = %s,
                    Phonenumber = %s,
                    Email = %s
                WHERE Customer_id = %s;
            """,
            (
            Customer.Customer_name,
            Customer.Phonenumber,
            Customer.Email,
            Customer.Customer_id  # แก้เป็น Customer_id
            )
            )
    if is_update:
        Customer_update_data = Customer.dict()
        Customer_update_data.update({"Customer_id": Customer_id})  # แก้เป็น Customer_id
        return Customer_update_data
    else:
        return None
#delete_Customer------------------------------
def delete_Customer(Customer_id: str):
    is_deleted = query_update("""
            DELETE FROM Customer
                WHERE Customer_id = %s;
            """,
            (Customer_id)
    )
    return is_deleted
#-------------------------------------------------------GuideModel-----------------------------------------------------------#
#get_all_Guide---------------
def get_all_Guide():
    Guides = query_get("""
        SELECT  
            *
        FROM Guide
        """, ())
    return Guides
#get_Guide_by_Guide_id---------------
def get_Guide_by_Guide_id(Guide_id: str):
    Guide = query_get("""
        SELECT
        *
        FROM Guide
        WHERE Guide_id = %s
        """, (Guide_id,))
    return Guide
#add_Guide---------------
def add_Guide(Guide: GuideModel):
    last_row_id = query_create("""
                INSERT INTO Guide (
                    Guide_id,
                    Email,
                    Languages
                ) VALUES (%s, %s, %s)
                """,
                (
                    Guide.Guide_id,
                    Guide.Email,
                    Guide.Languages
                )
                )
    return last_row_id
#update_Guide--------------------
def update_Guide(Guide_id: str, Guide: GuideModel):
    is_update = query_update("""
            UPDATE Guide
                SET Email = %s,
                    Languages = %s
                WHERE Guide_id = %s;
            """,
            (
            Guide.Email,
            Guide.Languages,
            Guide.Guide_id 
            )
            )
    if is_update:
        Guide_update_data = Guide.dict()
        Guide_update_data.update({"Guide_id": Guide_id})  
        return Guide_update_data
    else:
        return None
#delete_Guide------------------------------
def delete_Guide(Guide_id: str):
    is_deleted = query_update("""
            DELETE FROM Guide
                WHERE Guide_id = %s;
            """,
            (Guide_id)
    )
    return is_deleted
#-------------------------------------------------------CompanyModel-----------------------------------------------------------#
#get_all_Company---------------
def get_all_Company():
    Companys = query_get("""
        SELECT  
            *
        FROM Company
        """, ())
    return Companys
# #get_Guide_by_Guide_id---------------
# def get_Guide_by_Guide_id(Guide_id: str):
#     Guide = query_get("""
#         SELECT
#         *
#         FROM Guide
#         WHERE Guide_id = %s
#         """, (Guide_id,))
#     return Guide
# #add_Guide---------------
# def add_Guide(Guide: GuideModel):
#     last_row_id = query_create("""
#                 INSERT INTO Guide (
#                     Guide_id,
#                     Email,
#                     Languages
#                 ) VALUES (%s, %s, %s)
#                 """,
#                 (
#                     Guide.Guide_id,
#                     Guide.Email,
#                     Guide.Languages
#                 )
#                 )
#     return last_row_id
# #update_Guide--------------------
# def update_Guide(Guide_id: str, Guide: GuideModel):
#     is_update = query_update("""
#             UPDATE Guide
#                 SET Email = %s,
#                     Languages = %s
#                 WHERE Guide_id = %s;
#             """,
#             (
#             Guide.Email,
#             Guide.Languages,
#             Guide.Guide_id 
#             )
#             )
#     if is_update:
#         Guide_update_data = Guide.dict()
#         Guide_update_data.update({"Guide_id": Guide_id})  
#         return Guide_update_data
#     else:
#         return None
# #delete_Guide------------------------------
# def delete_Guide(Guide_id: str):
#     is_deleted = query_update("""
#             DELETE FROM Guide
#                 WHERE Guide_id = %s;
#             """,
#             (Guide_id)
#     )
#     return is_deleted
#-------------------------------------------------------ProgramTourModel-----------------------------------------------------------#
#get_all_ProgramTour---------------
def get_all_ProgramTour():
    ProgramTours = query_get("""
        SELECT  
            *
        FROM ProgramTour
        """, ())
    return ProgramTours
#get_Guide_by_location_id---------------
def get_ProgramTour_by_location_id(location_id: str):
    ProgramTour = query_get("""
        SELECT
        *
        FROM ProgramTour
        WHERE location_id = %s
        """, ( location_id,))
    return ProgramTour
#add_ProgramTour---------------
def add_ProgramTour(ProgramTour: ProgramTourModel):
    last_row_id = query_create("""
                INSERT INTO ProgramTour (
                    location_id,
                    location_Name
                ) VALUES (%s, %s)
                """,
                (
                    ProgramTour.location_id,
                    ProgramTour.location_Name
                )
                )
    return last_row_id
#update_ProgramTour--------------------
def update_ProgramTour(location_id: str, ProgramTour: ProgramTourModel):
    is_update = query_update("""
            UPDATE ProgramTour
                SET location_Name = %s
                WHERE location_id = %s;
            """,
            (
            ProgramTour.location_Name,
            ProgramTour.location_id 
            )
            )
    if is_update:
        ProgramTour_update_data = ProgramTour.dict()
        ProgramTour_update_data.update({"location_id": location_id})  
        return ProgramTour_update_data
    else:
        return None
#delete_ProgramTour------------------------------
def delete_ProgramTour(location_id: str):
    is_deleted = query_update("""
            DELETE FROM ProgramTour
                WHERE location_id = %s;
            """,
            (location_id)
    )
    return is_deleted

#-------------------------------------------------------ReservationModel-----------------------------------------------------------#
#get_all_Reservation---------------
def get_all_Reservation():
    Reservations = query_get("""
        SELECT  
            *
        FROM Reservation
        """, ())
    return Reservations
#get_Reservation_by_Booking_id---------------
def get_Reservation_by_Booking_id(Booking_id: str):
    Reservation = query_get("""
        SELECT
        *
        FROM Reservation
        WHERE Booking_id = %s
        """, ( Booking_id,))
    return Reservation
#add_Reservation---------------
def add_Reservation(Reservation: ReservationModel):
    last_row_id = query_create("""
                INSERT INTO Reservation (
                    Booking_id,
                    Firstdate,
                    Lastdate,

                ) VALUES (%s, %s, %s)
                """,
                (
                    Reservation.Booking_id,
                    Reservation.Firstdate,
                    Reservation.Lastdate
                )
                )
    return last_row_id
#update_Reservation--------------------
def update_Reservation(Booking_id: str, Reservation: ReservationModel):
    is_update = query_update("""
            UPDATE Reservation
                SET Firstdate = %s,
                Lastdate = %s
                WHERE Booking_id = %s
            """,
            ( 
                Reservation.Firstdate,
                Reservation.Lastdate,
                Booking_id
            )
            )
    if is_update:
        Reservation_update_data = Reservation.dict()
        Reservation_update_data.update({"Booking_id": Booking_id})  
        return Reservation_update_data
    else:
        return None

#delete_Reservation------------------------------
def delete_Reservation(Booking_id: str):
    is_deleted = query_update("""
            DELETE FROM Reservation
                WHERE Booking_id = %s;
            """,
            (Booking_id)
    )
    return is_deleted


