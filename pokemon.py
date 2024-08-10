# Codédex: Pokédex

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
   self.entry = entry
   self.name = name 
   self.types = types
   self.description = description
   self.is_caught = is_caught

  def speak(self):
    print(f'{self.name} '*2)
  
  def display_details(self):
    if self.is_caught:
      print(f'Entry Number: {self.entry} \nName: {self.name} \nType: {self.types} \nDescription: {self.description} \n{self.name} has already been caught!')
    else: 
      print(f'Entry Number: {self.entry} \nName: {self.name} \nType: {self.types} \nDescription: {self.description} \n{self.name} hasn\'t  been caught!')


p1 = Pokemon(12, 'Butterfree', ['bug','flying'], 'It loves the nectar of flowers and can locate flower patches that have even tiny amounts of pollen.', True)
p2 = Pokemon(15, 'Beedrill', ['bug', 'poison'], 'It has three poisonous stingers on its forelegs and its tail. They are used to jab its enemy repeatedly.', False)
p3 = Pokemon(38, 'Ninetales', ['fire'], 'Some legends claim that each of its nine tails has its own unique type of special mystical power.', True)

print('Call a pokemon and see its details:\n 1)Butterfree\n 2)Beedrill\n 3)Ninetales')
choice = int(input('Enter the number: '))
if choice == 1:
  p1.speak()
  p1.display_details()
elif choice == 2:
  p2.speak()
  p2.display_details()
else:
  p3.speak()
  p3.display_details()
