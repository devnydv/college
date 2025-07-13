from model import db, Subject
from tempdata import departments
dep = departments()
data = {
  "Computer Science Engineering": {
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

  "Electronics Engineering": {
    "First Semester": [
      "Engineering Mathematics I",
      "Physics",
      "Basic Electrical & Electronics Engineering",
      "Engineering Mechanics",
      "Communication Skills",
      "Physics Lab",
      "Basic Engineering Lab",
      "Workshop Practice"
    ],
    "Second Semester": [
      "Engineering Mathematics II",
      "Chemistry",
      "Basic Electronics Engineering",
      "Network Theory",
      "Environmental Science",
      "Basic Electronics Lab",
      "Network Lab"
    ],
    "Third Semester": [
      "Engineering Mathematics III",
      "Analog Electronics",
      "Digital Electronics",
      "Signals and Systems",
      "Electronic Measurement and Instrumentation",
      "Analog Electronics Lab",
      "Digital Electronics Lab"
    ],
    "Fourth Semester": [
      "Electromagnetic Fields",
      "Microprocessors and Microcontrollers",
      "Analog Communication",
      "Control Systems",
      "Microprocessor Lab",
      "Communication Lab",
      "Mini Project I"
    ],
    "Fifth Semester": [
      "Digital Communication",
      "VLSI Design",
      "Embedded Systems",
      "Antenna and Wave Propagation",
      "VLSI Lab",
      "Digital Communication Lab",
      "Minor Project II"
    ],
    "Sixth Semester": [
      "Microwave Engineering",
      "Digital Signal Processing",
      "Industrial Automation and Robotics",
      "IoT and Embedded Systems",
      "DSP Lab",
      "Microwave Lab",
      "Technical Seminar"
    ],
    "Seventh Semester": [
      "Wireless and Mobile Communication",
      "Optical Communication",
      "Machine Learning",
      "Major Project Phase I",
      "Internship and Technical Seminar"
    ],
    "Eighth Semester": [
      "Satellite Communication and Advanced VLSI",
      "Major Project Final Phase",
      "Viva Voce",
      "Internship Report",
      "Emerging Technologies in Electronics"
    ]
  },

  "Mechanical Engineering": {
    "First Semester": [
      "Engineering Mathematics I",
      "Physics",
      "Basic Electrical & Electronics Engineering",
      "Engineering Mechanics",
      "Communication Skills",
      "Physics Lab",
      "Basic Engineering Lab",
      "Workshop Practice"
    ],
    "Second Semester": [
      "Engineering Mathematics II",
      "Chemistry",
      "Engineering Thermodynamics",
      "Computer Programming",
      "Engineering Graphics",
      "Programming Lab",
      "Thermodynamics Lab"
    ],
    "Third Semester": [
      "Engineering Mathematics III",
      "Fluid Mechanics",
      "Material Science",
      "Manufacturing Processes",
      "Machine Drawing",
      "Fluid Mechanics Lab",
      "Manufacturing Lab"
    ],
    "Fourth Semester": [
      "Applied Thermodynamics",
      "Strength of Materials",
      "Kinematics of Machines",
      "Electrical Machines & Controls",
      "Measurement & Metrology",
      "Mechanics of Solids Lab",
      "Thermal Lab",
      "Mini Project I"
    ],
    "Fifth Semester": [
      "Dynamics of Machines",
      "Heat & Mass Transfer",
      "Design of Machine Elements",
      "CNC & Automation",
      "HMT Lab",
      "Dynamics Lab",
      "Minor Project II"
    ],
    "Sixth Semester": [
      "Internal Combustion Engines",
      "Refrigeration & Air Conditioning",
      "Finite Element Method (FEM)",
      "Operations Research",
      "IC Engine Lab",
      "CAD Lab",
      "Technical Seminar"
    ],
    "Seventh Semester": [
      "Power Plant Engineering",
      "Industrial Engineering & Management",
      "Additive Manufacturing ",
      "Major Project Phase I",
      "Industry Interaction"
    ],
    "Eighth Semester": [
      "Renewable Energy Systems ",
      "Project Phase II & Final Report",
      "Comprehensive Viva",
      "Internship Presentation",
      "Emerging Trends in Mechanical Engineering"
    ]
  },

  "Civil Engineering": {
    "First Semester": [
      "Engineering Mathematics I",
      "Physics",
      "Basic Electrical & Electronics Engineering",
      "Engineering Mechanics",
      "Communication Skills",
      "Physics Lab",
      "Basic Engineering Lab",
      "Workshop Practice"
    ],
    "Second Semester": [
      "Engineering Mathematics II",
      "Chemistry",
      "Programming for Problem Solving",
      "Engineering Graphics",
      "Environmental Science",
      "Programming Lab",
      "Engineering Graphics Lab"
    ],
    "Third Semester": [
      "Engineering Mathematics III",
      "Building Materials & Construction",
      "Strength of Materials",
      "Surveying I",
      "Fluid Mechanics",
      "Materials Testing Lab",
      "Surveying Lab"
    ],
    "Fourth Semester": [
      "Structural Analysis I",
      "Concrete Technology",
      "Transportation Engineering I",
      "Geotechnical Engineering I",
      "Surveying II",
      "Concrete Lab",
      "Soil Mechanics Lab",
      "Mini Project I"
    ],
    "Fifth Semester": [
      "Structural Analysis II",
      "Design of Reinforced Concrete Structures",
      "Geotechnical Engineering II",
      "Transportation Engineering II",
      "Construction Planning & Management",
      "Geotech Lab II",
      "Structural Design Lab",
      "Minor Project II"
    ],
    "Sixth Semester": [
      "Design of Steel Structures",
      "Water Supply & Wastewater Engineering",
      "Environmental Engineering",
      "Estimation, Costing & Valuation",
      "Open Channel Flow ",
      "Environmental Engg. Lab",
      "CAD in Civil Lab",
      "Industrial Training"
    ],
    "Seventh Semester": [
      "Irrigation & Hydraulic Structures",
      "Advanced Foundation Engineering ",
      "Remote Sensing & GIS",
      "Ethics",
      "Major Project Phase I",
      "Technical Seminar"
    ],
    "Eighth Semester": [
      "Green Building Technologies",
      "Major Project Final Submission",
      "Viva Voce",
      "Internship Report",
      "Emerging Trends in Civil Engineering"
    ]
  }
}


def insert_subjects():
    
  for dept in dep :
      for semester, subjects in data[dept].items():
          for subject in subjects:
              new_subject = Subject(
                  name=subject,
                  semester=semester,
                  dep_id= dep.index(dept) + 1  # Assuming department IDs start from 1
                )
              db.session.add(new_subject)
          db.session.commit()
  return "Subjects inserted successfully"
