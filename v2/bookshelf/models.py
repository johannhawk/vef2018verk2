# -*- coding: utf-8 -*-

# Model - the business logic of the application

# The model is all to do with the data that's to be handled by the application
# and nothing to do with how it's presented / wired into the view
# functions that work with data (files, database, api etc.)

# very simple class
class Book:

    def __init__(self, name):
        self.name = name

# data
booklist = [
    Book("Fools Errand"), Book("Data and goliath"), Book("Mistur")
]

class year:
    def __init__(self, name):
        self.name = name

yearcount = [
    Book("2014"), Book("2016"), Book("2017")
]

comp = [
    Book("fyr1"), Book("fyr2"), Book("fyr3")
]

# Ath þarf að útfæra betur.
