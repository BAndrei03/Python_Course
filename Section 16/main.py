# import another_module
# print(another_module.another_variable)
#
# # Turtle este clasa
# from turtle import Turtle, Screen
# timmy = Turtle() # creat nou obiect
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# #  car.speed (obiect.atribut)
# my_screen = Screen()
# print(my_screen.canvheight)
# # metode car.stop()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name",["Pikachu", "Squirtel", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

table.align = "l"

print(table)


