

class Pasta:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    @classmethod
    def customize_pasta(self):
        custom_pasta = int(input(""" Enter your Pasta choice:
                                 1. Sicilian (Spaghetti, Cheese, Pepperoni, Parsley)
                                 2. Spice Heaven (Spaghetti, Cheese, Meatball, Tomatoes)
                                 3. Customized Pasta
                             """))
                             
        if custom_pasta == 1:
            ingredients = ['Spaghetti','Cheese','Pepperoni','Parsley']
            self.price = 3.3
            
        elif custom_pasta == 2:
            ingredients = ['Spaghetti','Cheese','Meatball','Tomatoes']
            self.price = 3.5
            
        elif custom_pizza == 3:
            ingredients = ['Spaghetti','Cheese']
            self.price = 1.8
            print("Spaghetti and Cheese will be present by default.")
            
            if Pizza.type.lower() == 'veg':
                veg_addon = ['Tomatoes','Mushroom','Parsley']
                for i in range(len(veg_addon)):
                    print(f'{i+1}. {veg_addon[i]}')
                    
                addon_no = int(input('Enter the item number: '))
                
                j=0
                while j<3 and True:
                    if addon_no == 1:
                        ingredients.append('Tomatoes')
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
                        ingredients.append('Parsley')
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
                        
                    else:
                        print("incorrect choice")
                        
            elif Pizza.type.lower() == 'nonveg':
                nonveg_addon = ['Ham','Meatball','Pepperoni']
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
                        ingredients.append('Pepperoni')
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