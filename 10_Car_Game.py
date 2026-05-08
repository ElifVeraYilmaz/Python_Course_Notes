######## Car Game ##########

command = "" # Empty string.
started = False
while True : # If it is true, the program will continue; but if it is false, the program stops.
     command = input("> ").lower() # Instead of converting every condition to lower case, we made the input lower case to prevent errors.
     if command == "start":
          if started:
               print("Car is already started!")
          else:
               started = True 
               print("Car started...")     
     elif command == "stop":
          if not started:
               print("Car is already stopped!")
          else:
               started = False     
               print("Car stopped.") 
     elif command == "help":
          print(""" 
start- to start the car
stop - to stop the car
quit - to quit
          """)
     elif command == "quit":
          break     
     else:
          print("Sorry, I dont understand that!")    
