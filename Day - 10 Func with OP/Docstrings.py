formatted_name = "Harsh Turakhiha"

length = len(formatted_name)


def format_name(fname, lname):

    # Documentation or Dosctring
    """ 
        -> Takes 6 qoutation marks to make docstring 
        -> Takes first name and last name and convert it to title case version 
    """

    if fname == "" or lname == "":
        return "You didnt provide any inputs"

    formatted_fname = fname.title()
    formatted_lname = lname.title()

    return f" Result : {formatted_fname} {formatted_lname}"


format_name("harsH", "turakHIA")
