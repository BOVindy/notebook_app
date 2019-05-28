from datetime import date

"""
Notebook app


notes will have 3 parts:
an ID
Content
Date/Time
"""

# we are building it it imperative style. (imperative style is: top to bottom reading)

# notebook = []

# counter = 1
# note_id = counter


# counter += 1

# now = date.today()
# print(now)

# content = "this is content"

# note = (note_id, str(now), content)

# notebook.append(note)
# print(notebook)


# counter = 1
# notebook = []
# now = date.today()

# while True:
#     user_response = input("what would you like to do? \n>"
#                         "1. add a note \n"
#                         "2. print a note \n"
#                         "3. exit\n> "
#         )


#     if user_response == "1":
#         content = input("What is the note\n>")
#         note_id = counter
#         note = (note_id, str(now), content)
#         notebook.append(note)
#         counter += 1
#     if user_response == "2":
#         for note in notebook:
#             print(f"ID: {note[0]}| {note[2]}")
#     elif user_response == "3":
#         exit()
#     else:
#         print("invalid input")

# # while counter <= 5:
# #     content = input("What is the note\n>")
# #     note_id = counter
# #     note = (note_id, str(now), content)
# #     notebook.append(note)
# #     counter += 1
# #     print(notebook)


counter = 1
notebook = []
now = date.today()

def menu():
    user_response = input("what would you like to do? \n>"
                        "1. add a note \n"
                        "2. print a note \n"
                        "3. exit\n> ")
    return user_response

def note_create():
        content = input("What is the note\n>")
        global counter
        note_id = counter
        note = (note_id, str(now), content)
        notebook.append(note)
        counter += 1    

def print_notes():
    for note in notebook:
        print(f"ID: {note[0]}| {note[2]}")

def run():
    while True:
        choice = menu()
        if user_response == "1":
            note_create()
        if user_response == "2":
            print_notes()
        elif user_response == "3":
            exit()
        else:
            print("invalid input")

if __name__ == "__main__":
    run()
