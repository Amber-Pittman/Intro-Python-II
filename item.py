class Item:
  def __init__(self, description):
    self.name = name
    self.description = description

  def __str__(self):
    return f"\n Item: {self.name} \n Description: {self.description} \n"

items = {
  "Rubies": Item("Rubies", "A handful of rubies are quite valuable."),
  "Emeralds": Item("Emeralds", "These emeralds, I'll keep for myself."),
  "Gold Coins": Item("Gold Coins", "Score! These will be great to use back at the marketplace later."),
  "Torch": Item("Torch", "This torch illuminates the area."),
  "Dragon": Item("Dragon", "A baby dragon? Where's the mother?! It looks orphaned. Perhaps I can raise it like the Targaryen woman?")
}