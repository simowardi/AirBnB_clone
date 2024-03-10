#!/usr/bin/python3
"""This initializes the package"""
"""Create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage

strg = FileStorage()
strg.reload()
