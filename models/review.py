#!/usr/bin/python3
"""Review class module"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the Review class which inherits from BaseModel

    Attributes:
        place_id (str): Will be the Place.id
        user.id (str): Will be the User.id
        text (str): Content of the review
    """

    place_id = ""
    user.id = ""
    text = ""
