# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Hurdle 3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
    
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     if wall_in_front():
#         jump()

# Hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
    
#     turn_right()
#     move()
#     turn_right()
#     move()
    
    
# while not at_goal():
#     if wall_in_front():
#         turn_left()
#     if front_is_clear():
#         move()
#     if right_is_clear():
#         jump()
        
# day project
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
    
#     turn_right()
#     move()
#     turn_right()
#     move()
    
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#     else:
#         turn_left()
#     if front_is_clear():
#         move()
    
# course solution to day exercise:
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
      
# debug course solution to day exercise:
# while front_is_clear():
#   move()
# turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()