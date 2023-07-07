#!/usr/bin/python3
"""Place class module"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the Place class which inherits from BaseModel

    Attributes:
        city_id (str): Will be the City.id (id of a City instance)
        user_id (str): will be the User.id
        name (str): Place name
        description (str): Description on the Place
        number_rooms (int): Number of room at said Place
        number_bathrooms (int): Number of bathrooms at said place
        max_guest (int): Max number of guests
        price_by_night (int): The price of a night
        latitude (float): GPS location on latitude
        longitude (float): GPS location on longitude
        amenity_ids (list): List of strings containing all Amenity.ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
