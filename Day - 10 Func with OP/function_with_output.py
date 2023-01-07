# Capitalizing first character

# def format_name(fname, lname):
#     print(fname.title())
#     print(lname.title())


# print("Capitalizing first character via printing the answer...")
# format_name("hshhhJDHSH", "HHdHhSJ")


# def format_name(fname2, lname2):
#     formatted_fname2 = fname2.title()
#     formatted_lname2 = lname2.title()
#     return f"{formatted_fname2} {formatted_lname2}"


# print("Capitalizing first character via returning the answer...")
# print(format_name("harsH", "turakHIA"))


def format_name(fname, lname):

    if fname == "" or lname == "":
        return "You didnt provide any inputs"

    formatted_fname = fname.title()
    formatted_lname = lname.title()
    return f"{formatted_fname} {formatted_lname}"


print("Capitalizing first character via returning the answer with if statement...")
print(format_name(input("What is your first name ? "),
      input("What is your last name ? ")))
