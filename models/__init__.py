#!/usr/bin/env python3

""" 
    module to create a generic storage object
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
