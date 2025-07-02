from model import db, Student, Faculty, Notice, Subject

data = {
    "Computer Science": {
    "First Semester": [
      "Engineering Mathematics I",
      "Physics",
      "Programming for Problem Solving",
      "Basic Electrical and Electronics Engineering",
      "Engineering Graphics and Workshop",
      "Communication Skills",
      "Physics Lab",
      "Programming Lab"
    ],
    "Second Semester": [
      "Engineering Mathematics II",
      "Chemistry",
      "Data Structures",
      "Digital Logic Design",
      "Environmental Studies",
      "Data Structures Lab",
      "Digital Logic Lab"
    ],
    "Third Semester": [
      "Discrete Mathematics",
      "Computer Organization and Architecture",
      "Object Oriented Programming",
      "Operating Systems",
      "Design and Analysis of Algorithms",
      "OOPs Lab",
      "OS Lab and Algorithm Lab"
    ],
    "Fourth Semester": [
      "Theory of Computation",
      "Database Management Systems",
      "Computer Networks",
      "Software Engineering",
      "DBMS Lab",
      "CN Lab",
      "Mini Project I"
    ],
    "Fifth Semester": [
      "Compiler Design",
      "Web Technologies",
      "Artificial Intelligence",
      "Professional Ethics",
      "Web Tech Lab",
      "Compiler Design Lab",
      "Minor Project II"
    ],
    "Sixth Semester": [
      "Cloud Computing and  IoT",
      "Mobile App Development and Big Data",
      "Cybersecurity",
      "Major Project Phase I",
      "Aptitude & Reasoning Skills",
      "Technical Seminar"
    ],
    "Seventh Semester": [
      "Data Science",
      "Research Methodology",
      "Industrial Management",
      "Major Project Phase II",
      "Internship and Field Work"
    ],
    "Eighth Semester": [
      "Major Project Final Submission",
      "Viva Voce",
      "Internship Report",
      "Emerging Technologies",
      "Capstone Project"
    ]
  },
}


for sem, subjects in data["Computer Science"].items():
    print(f"{sem}:")
    for subject in subjects:
        subject = Subject(
            name=subject,
            semester=sem,
            dep_id=1  # Assuming 1 is the ID for Computer Science department
        )
        db.session.add(subject)
        db.session.commit()