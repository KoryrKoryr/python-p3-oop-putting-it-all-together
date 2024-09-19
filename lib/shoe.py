#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Use a private attribute for size to control access via the setter
        self.size = size  # This will call the setter to ensure validation
        self.condition = "Used"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Ensure size is a valid number (int or float)
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
            self._size = 0  # Default to 0 if invalid

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

