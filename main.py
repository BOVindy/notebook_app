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


counter = 1
notebook = []
now = date.today()

while counter <= 5:
    content = input("What is the note\n>")
    note_id = counter
    note = (note_id, str(now), content)
    notebook.append(note)
    counter += 1
    print(notebook)
