#functions with outputs

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
#
# format_name("andrei", "ANDREI")

def format_name(f_name, l_name):
    """Numele apare cu litera mare la inceput."""
    if f_name == "" or l_name == "":
        return "You didnt provide vlaid inputs."
    formate_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formate_f_name} {formated_l_name}"

print(format_name(input("First name"), input("Last name")))