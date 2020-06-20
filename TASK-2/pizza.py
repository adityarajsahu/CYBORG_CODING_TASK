

class Pizza:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    @classmethod
    def customize_pizza(self):
        custom_pizza = int(input(""" Enter your Pizza choice:
                                 1. Mexican (Pizza crust, cheese, ham, olives)
                                 2. Spice Heaven (Pizza crust, cheese, meatball, bacon)
                                 3. Customized Pizza
                             """))
                             
        if custom_pizza == 1:
            ingredients = ['Pizza crust','Cheese','Ham','Olives']
            self.price = 4.1
            
        elif custom_pizza == 2:
            ingredients = ['Pizza crust','cheese','meatball','bacon']
            self.price = 3.5
            
        elif custom_pizza == 3:
            ingredients = ['Pizza crust','Cheese']
            self.price = 1.8
            print("Pizza crust and Cheese will be present by default.")
            
            if Pizza.type.lower() == 'veg':
                veg_addon = ['Pineapple','Mushroom','Olives']
                for i in range(len(veg_addon)):
                    print(f'{i+1}. {veg_addon[i]}')
                    
                addon_no = int(input('Enter the item number: '))
                
                j=0
                while j<3 and True:
                    if addon_no == 1:
                        ingredients.append('Pineapple')
                        self.price += 0.5
                        j+=1
                        response = input(""" Would you like to add something more?(y/n)
                                         y for Yes
                                         n for No
                                         """).lower()
                        if response == 'y':
                            return True
                        else:
                            return False
                        
                    elif addon_no == 2:
                        ingredients.append('Mushroom')
                        self.price += 1
                        j+=1
                        response = input(""" Would you like to add something more?(y/n)
                                         y for Yes
                                         n for No
                                         """).lower()
                        if response == 'y':
                            return True
                        else:
                            return False
                        
                    elif addon_no == 3:
                        ingredients.append('Olives')
                        self.price += 1.5
                        j+=1
                        response = input(""" Would you like to add something more?(y/n)
                                         y for Yes
                                         n for No
                                         """).lower()
                        if response == 'y':
                            return True
                        else:
                            return False
                        
                    else:
                        print("incorrect choice")
                        
            elif Pizza.type.lower() == 'nonveg':
                nonveg_addon = ['Ham','Meatball','Bacon']
                for i in range(len(nonveg_addon)):
                    print(f'{i+1}. {nonveg_addon[i]}')
                    
                addon_no = int(input('Enter the item number: '))
                
                j=0
                while j<3 and True:
                    if addon_no == 1:
                        ingredients.append('Ham')
                        self.price += 0.8
                        j+=1
                        response = input(""" Would you like to add something more?(y/n)
                                         y for Yes
                                         n for No
                                         """).lower()
                        if response == 'y':
                            return True
                        else:
                            return False
                        
                    elif addon_no == 2:
                        ingredients.append('Meatball')
                        self.price += 1
                        j+=1
                        response = input(""" Would you like to add something more?(y/n)
                                         y for Yes
                                         n for No
                                         """).lower()
                        if response == 'y':
                            return True
                        else:
                            return False
                        
                    elif addon_no == 3:
                        ingredients.append('Bacon')
                        self.price += 0.7
                        j+=1
                        response = input(""" Would you like to add something more?(y/n)
                                         y for Yes
                                         n for No
                                         """).lower()
                        if response == 'y':
                            return True
                        else:
                            return False
                        
                    else:
                        print("incorrect choice")
                        
        return [ingredients,self.price]
