<<<<<<< HEAD
#!/usr/bin/python3
""" Review module for the HBNB project """
=======
#!/usr/bin/env python3
""" Review class Module """
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
=======
    """ The Review class """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ The review class constructor """
        super().__init__(*args, **kwargs)
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
