import functions

condition = True

while condition:
    choice = int(input("\nSelect Option :\n"
                        " 1. Length Conversions :\n"
                        " 2. Circle (Geometry) :\n"
                        " 3. Weight / Mass Conversions :\n"
                        " 4. Volume Conversions :\n "
                        "5. Exit :\n "
                        "6. View History :\n"))
    
    if choice == 1:
        functions.length()

    elif choice == 2:
        functions.math()

    elif choice == 3 : 
        functions.mass()
          
    elif choice == 3 : 
        functions.mass()
     
    elif choice == 4 : 
        functions.volume()

    elif choice == 5 :
        condition =  False
        print("Exit Successful ! ") 

    elif choice == 6 :
          print(functions.history)   

     
         
  
            
            
           
           
           
           