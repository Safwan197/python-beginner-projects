history = [] # To save the History ff Conversions

# Functions for Length Conversion

def length():
        type_of_con =  int(input("\n Select Conversions\n"
              "1. cm to m\n"
              "2. m to cm\n"
              "3. km to m\n"
              "4. m to km\n"
              "5. inch to cm\n"
              "6. cm to inch\n\n"))
       
        if type_of_con == 1 :
           value = float(input("Enter the Value : "))
           converted = value / 100  
           history.append(converted)  # Adding Conversions in List
           print("\n",converted," m")

        elif type_of_con == 2:
            value = float(input("Enter the Value : "))
            converted = value * 100
            history.append(converted)
            print("\n",converted," cm")

        elif type_of_con == 3:
            value = float(input("Enter the Value : "))
            converted = value * 1000
            history.append(converted)
            print("\n",converted," m")

        elif type_of_con == 4:
            value = float(input("Enter the Value : "))
            converted = value / 1000
            history.append(converted)
            print("\n",converted," km")

        elif type_of_con == 5:
            value = float(input("Enter the Value : "))
            converted = value * 2.54
            history.append(converted)
            print("\n",converted," cm")

        elif type_of_con == 6:
            value = float(input("Enter the Value : "))
            converted = value / 2.54
            history.append(converted)
            print("\n",converted," inch")
    
        else:
            condition = False
            print("Out of Range ! Try Again") 




# Functions for Mathematical Conversion

def math():
    type_of_con =  int(input("\n Select Conversions\n"
              "1. Diameter to Radius\n"
              "2. Radius to Diameter\n"
              "3. Area of Circle\n\n"))
    
    if type_of_con == 1:
            value = float(input("Enter the Value : "))
            converted = value / 2
            history.append(converted)
            print("Radius = ",converted)

    elif type_of_con == 2:
            value = float(input("Enter the Value : "))
            converted = value * 2
            history.append(converted)
            print("Diameter = ",converted)

    elif type_of_con == 3:
            pie = 3.14
            radius = float(input("Enter Radius : \n"))

            converted = pie * (radius**2)
            history.append(converted)
            print("Area = ",converted)

    else:
              condition = False
              print("Out of Range ! Try Again") 


# Functions for Weight/Mass Conversion

def mass():
      type_of_con =  int(input("\n Select Conversions\n"
              "1. kg to gram\n"
              "2. gram to kg\n"
              "3. kg to mg\n" \
              "4. ton to kg\n" \
              "5.pound(lb) to kg\n\n"))
      

      if type_of_con == 1:
            value = float(input("Enter the Value : "))
            converted = value * 1000
            history.append(converted)
            print("\n",converted," gm")
    
      elif type_of_con == 2:
            value = float(input("Enter the Value : "))
            converted = value / 1000
            history.append(converted)
            print("\n",converted," kg")

      elif type_of_con == 3:
            value = float(input("Enter the Value : "))
            converted = value * 1000000
            history.append(converted)
            print("\n",converted," mg")

      elif type_of_con == 4:
            value = float(input("Enter the Value : "))
            converted = value * 1000
            history.append(converted)
            print("\n",converted," kg")

      elif type_of_con == 5:
            value = float(input("Enter the Value : "))
            converted = value * 0.4536
            history.append(converted)
            print("\n",converted," kg")

      else:
            condition = False
            print("Out of Range ! Try Again") 


# Functions for Volume Conversion

def volume():
      type_of_con =  int(input("\n Select Conversions\n"
              "1. litre to ml\n"
              "2. ml to litre\n"
              "3. litre to cubic meter\n" \
              "4. cubic meter to litre\n\n"))
      
      if type_of_con == 1:
            value = float(input("Enter the Value : "))
            converted = value * 1000
            history.append(converted)
            print("\n",converted," ml")
    
      elif type_of_con == 2:
            value = float(input("Enter the Value : "))
            converted = value / 1000
            history.append(converted)
            print("\n",converted," litre")
    
      elif type_of_con == 3:
            value = float(input("Enter the Value : "))
            converted = value / 1000
            history.append(converted)
            print("\n",converted," cubic meter")

      elif type_of_con == 1:
            value = float(input("Enter the Value : "))
            converted = value * 1000
            history.append(converted)
            print("\n",converted," litre")

      else:
            condition = False
            print("Out of Range ! Try Again")

      

      
      


