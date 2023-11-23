"""""
Develop a program for library management. Ensure
to create a "book" class encompassing all the
fundamental properties and methods.

"""

class Book:
    def __init__(self,nrpages,author,genre,available=True,beholder="Library"):
        self.nrpages = nrpages
        self.author =author
        self.genre = genre
        self.available = available
        self.beholder = beholder
        
    def borrow(self,client):
        self.beholder = client
        self.available = False
        
    def back(self):
        self.beholder = "Library"
        self.available = True
        
    def __str__(self):
        print(self.nrpages , self.author,self.genre,self.available,self.beholder)
        
        
    