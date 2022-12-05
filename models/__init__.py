<<<<<<< HEAD
#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
=======
#!/usr/bin/env python3

"""
    module to create a generic storage object
"""

>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
