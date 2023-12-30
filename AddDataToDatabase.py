import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})


ref = db.reference('Students')

data = {
    "B2005090000": {
        "name": "Emly Blunt",
        "major": "Computer Engineering",
        "starting_year": 2020,
        "total_attendance": 7,
        "Course": "IOT",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "B1905090007": {
        "name": "Sara Meitani",
        "major": "Software Engineering",
        "starting_year": 2020,
        "total_attendance": 8,
        "Course": "SRS",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "B2005090130": {
        "name": "Ghada Sarakbi",
        "major": "Software Engineering",
        "starting_year": 2020,
        "total_attendance": 7,
        "Course": "SRS",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "B1905090096": {
        "name": "Dorsa Fadaei Arasi",
        "major": "Software Engineering",
        "starting_year": 2019,
        "total_attendance": 2,
        "Course": "SRS",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "B2005010000": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "Course": "IOT",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
