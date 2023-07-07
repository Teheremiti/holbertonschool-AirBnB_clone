#!/usr/bin/python3
"""City class module"""


from models.base_model import BaseModel


class City(BaseModel):
    """Defines the City class which inherits from BaseModel

    Attributes:
        state_id (str): Will be the State.id (id of a State instance)
        name (str): City name
    """

    state_id = ""
    name = ""
