# # def my_decorator(func):
# #     def wrapper():
# #         print("Something is happening before the function is called.")
# #         func()
# #         print("Something is happening after the function is called.")
# #     return wrapper
# #
# # def say_whee():
# #     print("Whee!")
# #
# #
# # say_whee = my_decorator(say_whee)
#
# from datetime import datetime
#
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = not_during_the_night(say_whee)

# Python program to illustrate reflection
def reverse(sequence):
    sequence_type = type(sequence)
    empty_sequence = sequence_type()

    if sequence == empty_sequence:
        return empty_sequence

    rest = reverse(sequence[1:])
    first_sequence = sequence[0:1]

    # Combine the result
    final_result = rest + first_sequence

    return final_result


# Driver code
print(reverse([10, 20, 30, 40]))
print(reverse("GeeksForGeeks"))