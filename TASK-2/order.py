from pizza import Pizza
from pasta import Pasta

class Food(Pizza,Pasta):
    def __init__(self,category,foodtype,num):
        self.category = category
        self.type = foodtype
        self.num = num
        
    @property
    def determine_category(self):
        if self.category.lower() == 'pizza':
            return super(Food,self).customize_pizza()
            
        elif self.category.lower() == 'pasta':
            return super(Food,self).customize_pasta()
        
        
food_category = input("What would you like to have: Pizza or Pasta?")
food_type = input("Veg or NonVeg?")
food_num = int(input(f'Enter the number of {food_category.capitalize()}: '))

obj = Food(food_category,food_type,food_num)
details = obj.determine_category
print(f'Ingredients: {details[0]}')
print(f'Price: {food_num*int(details[1])}')












