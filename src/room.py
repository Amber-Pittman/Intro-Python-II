# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  n_to = None
  s_to = None
  e_to = None
  w_to = None


  def __init__(self, short_description, description):
    self.short_description = short_description 
    self.description = description
