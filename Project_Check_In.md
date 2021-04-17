## Main Components

Class Coordinates:
 """ A class to match enetered coordinates with coordinates in the list in file. 
 
 Attributes:
    grid (float or int) a number entered by user to match designated bird coordinates.
 """
 
 def __init__ (self, grid): 
     """
     Initializes coordinate object. 
     
     Args:
         grid (float or int of coordinate):
         
     Raises:
         ValueError: If coordinates entered are not a match.
     """
 
Class Collection_Birds:
 """ A class to make a new captured bird entry. 
 
 Attributes:
    new_bird (obj:'list') information about new recorded/captured bird.
    new_coordinates(int or float) to assign new ccordinate to bird. 
 """
 
 def __init__ (self, new_bird, new_coordinate):
     """
     Initializes new_bird and new_cooridnate objects. 
     
     Args:
         new_bird (obj:'list'): information about new recorded/captured bird.
         new_coordinates(int or float): to assign new ccordinate to bird. 
         
     Raises:
         ValueError: If duplicate.
     """

if __name__ == "__main__":
    main()





