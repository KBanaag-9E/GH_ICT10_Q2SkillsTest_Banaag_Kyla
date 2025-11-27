from pyscript import display, document

# reference: https://www.w3schools.com/tags/ev_onchange.asp

# dict for math club
math = {
        "Description": "club for math competition training",
        "Meeting_Time": "Every Tuesday 2:30-3:30",
        "Location": "Room 701",
        "Club Moderator": "Mr. Mendoza",
        "Number of Members": 36
}

# dict for science club
science = {
    "Description": "club for science competition training and lab experiments",
    "Meeting_Time": "Every Thursday 2:30-3:30",
    "Location": "Room 510",
    "Club Moderator": "Mr. Bautista",
    "Number of Members": 28
}

# dict for robotics club
robotics = {
    "Description": "club for robotics",
    "Meeting_Time": "Every Wednesday 2:30-4:30",
    "Location": "Room 704",
    "Club Moderator": "Ms. Torres",
    "Number of Members": 32
}

# display math club info
def m_club(e):
    display(math, target='output')

# display science club info
def s_club(e):
    display(science, target='output')

# display robotics club info
def r_club(e):
    display(robotics, target='output')