"""
Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the 
courses meet. The dictionary should have the following keyvalue pairs:

Course Number (key) Room Number (value)
CS101               3004
CS102               4501
CS103               6755
NT110               1244
CM241               1411

The program should also create a dictionary containing course numbers and the names of
the instructors that teach each course. The dictionary should have the following key-value
pairs:

Course Number (key) Instructor (value)
CS101               Haynes
CS102               Alvarado
CS103               Rich
NT110               Burke
CM241               Lee

The program should also create a dictionary containing course numbers and the meeting
times of each course. The dictionary should have the following key-value pairs:

Course Number (key) Meeting Time (value)
CS101               8:00 a.m.
CS102               9:00 a.m.
CS103               10:00 a.m.
NT110               11:00 a.m.
CM241               1:00 p.m.

The program should let the user enter a course number, and then it should display the
course’s room number, instructor, and meeting time.
"""
# dictionary containing courses as keys and their respective rooms,
# instructors, and meeting times as keys with their respective values
courses = {
    'CS101' : {
        'room' : 3004,
        'inst' : 'Haynes',
        'time' : '8:00 a.m.'
    },
    'CS102' : {
        'room' : 4501,
        'inst' : 'Alvarado',
        'time' : '9:00 a.m.'
    },
    'CS103' : {
        'room' : 6755,
        'inst' : 'Rich',
        'time' : '10:00 a.m.'
    },
    'NT110' : {
        'room' : 1244,
        'inst' : 'Burke',
        'time' : '11:00 a.m.'
    },
    'CM241' : {
        'room' : 1411,
        'inst' : 'Lee',
        'time' : '1:00 p.m.'
    }
}

# initialize user input
user_input = ''

# get a course number from the user
while user_input not in courses:
    print('Courses: ',str(courses.keys()).lstrip("dict_keys([").rstrip("])"))
    user_input = input('Please enter a course: ')
    if user_input not in courses:
        print('Invalid course number, enter another course')
    
# print out the course number, room number, instructor, and meeting time
print(f"\nCourse {user_input}:"
    f"\n\tRoom: {courses[user_input]['room']}"
    f"\n\tInstructor: {courses[user_input]['inst']}"
    f"\n\tMeeting Time: {courses[user_input]['time']}\n")