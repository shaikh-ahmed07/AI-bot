from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime

app = Flask(__name__, template_folder="templates")
CORS(app)

qa_pairs = {
    "college history": (
        "Lords Institute of Engineering and Technology Hyderabad was founded in 1995 "
        "to offer quality technical education with a vision to foster innovation and research."
    ),
    "library timings": (
        "The college library operates from 8 AM to 6 PM on weekdays and 9 AM to 2 PM on Saturdays. "
        "It houses over 50,000 books and subscribes to numerous journals and e-resources."
    ),
    "principal office": "The principal’s office is located in the main administrative block near the entrance.",
    "courses offered": (
        "We offer undergraduate (B.Tech) programs in Computer Science, Electrical, Mechanical, Civil, and ECE. "
        "Postgraduate (M.Tech) and MBA programs are also available."
    ),
    "coding competitions": (
        "The Computer Science department organizes monthly coding contests and an annual hackathon called 'CodeLords'."
    ),
    "cultural fest": (
        "Lords Fiesta is our flagship annual cultural festival held every December, attracting over 2000 participants."
    ),
    "sports day": (
        "The Annual Sports Day is celebrated in February featuring cricket, football, athletics, and indoor games."
    ),
    "career fairs": (
        "Career fairs happen every March and September, with participation from top IT, manufacturing, and finance companies."
    ),
    "canteen menu": (
        "The canteen offers a variety of cuisines including South Indian, North Indian, Chinese, and Continental dishes."
    ),
    "sports facilities": (
        "We have well-equipped facilities for cricket, basketball, volleyball, badminton, and table tennis."
    ),
    "scholarships": (
        "Scholarships are available for top-ranking students and economically disadvantaged candidates. "
        "Applications are accepted at the student affairs office."
    ),
    "exam schedule": (
        "Semester exams are conducted in November and April, with supplementary exams in July."
    ),
    "admission forms": (
        "Admission forms can be downloaded from the official website or collected at the admissions office."
    ),
    "location": (
        "Lords Institute is located in Himayatnagar, Hyderabad, easily accessible by public transport."
    ),
    "departments": (
        "Departments include Computer Science, Electrical Engineering, Mechanical Engineering, Civil Engineering, "
        "Electronics & Communication, and Management."
    ),
    "contact info": (
        "Contact us at +91-40-12345678 or email info@lordsiet.ac.in for any queries."
    ),
    "hostel facilities": (
        "Separate hostels for boys and girls with hygienic mess and recreational facilities."
    ),
    "transport": (
        "College buses run daily connecting major Hyderabad localities including Secunderabad, Koti, and Kukatpally."
    ),
    "placements": (
        "The placement cell boasts a 90% placement record with companies like TCS, Infosys, Wipro, and Deloitte recruiting annually."
    ),
    "latest news": (
        f"On {datetime.date.today()}: Lords Institute recently launched a new AI research lab with industry partners."
    ),
    "events upcoming": (
        "Upcoming events include 'Tech Symposium 2025' on July 10th and 'Alumni Meet 2025' on August 5th."
    ),
    "covid policy": (
        "The college follows strict COVID-19 protocols including mandatory masks, sanitizers, and vaccination proof for campus entry."
    ),
    "placements process": (
        "The placement process includes resume shortlisting, technica        python3 app.pyl tests, group discussions, and HR interviews."
    ),
    "library resources": (
        "Our digital library has subscriptions to IEEE, Springer, Elsevier, and other international journals."
    ),
    "research opportunities": (
        "Students are encouraged to participate in research projects under faculty guidance with funding from DST and AICTE."
    ),
    "student clubs": (
        "We have active clubs for robotics, drama, music, debating, and entrepreneurship."
    ),
    "coding competitions": (
        "The Computer Science department hosts monthly coding contests and an annual hackathon called 'CodeLords'."
    ),
    "library resources": (
        "The library provides access to over 50,000 books, journals, and digital resources including IEEE and Springer."
    ),  
    "research opportunities": (
        "Students can engage in research projects with faculty, supported by grants from DST and AICTE."
    ),
    "event":( "Upcoming events include 'Tech Symposium 2025' on July 10th and 'Alumni Meet 2025' on August 5th."

    )

}

default_reply = (
    "Sorry, I didn’t understand. Please ask about Lords Institute of Engineering and Technology Hyderabad."
)

def find_best_answer(user_input):
    user_input = user_input.lower().strip()
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]

    if any(greet in user_input for greet in greetings):
        return (
            "Hello! Welcome to Lords Institute of Engineering and Technology Hyderabad — a premier institution established in 1995, "
            "dedicated to fostering innovation, quality technical education, and research excellence. "
            "Feel free to ask me about our courses, faculty, events, placements, and much more!"
        )

    for key in qa_pairs:
        key_words = key.split()
        if all(word in user_input for word in key_words):
            return qa_pairs[key]

    return default_reply

@app.route("/")
def home():
    return render_template("index.html")  #front-end HTML page in templates/

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    answer = find_best_answer(user_input)

    suggestions = [
        "college history",
        "library timings",
        "courses offered",
        "principal office",
        "coding competitions",
        "sports facilities",
        "exam schedule",
        "location",
        "departments",
        "contact info",
        "hostel facilities",
        "transport",
        "covid policy",
        "library resources",
        "research opportunities",
        "events upcoming",
        "placements process",
        "student clubs",
        "cultural fest",
        "placements",
        "canteen menu",
        "admission forms",
        "sports day",
        "career fairs",
        "latest news"
        "events"
        "event"
        "college"
    ]

    return jsonify({"reply": answer, "suggestions": suggestions})

if __name__ == "__main__":
    app.run(debug=True)
