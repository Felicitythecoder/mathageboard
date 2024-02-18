from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

# Sample data - replace with database connection later
messages = [
    {"author": "John", "message": "Hello!", "id":1},
    {"author": "Jane", "message": "Nice to meet you!", "id":2},
    {"author": "John", "message": "Hi Jane", "id":3, "reply_id": 2}
]


@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@app.route("/create_message", methods=["POST"])
def create_message():
    author = request.form["author"]
    message = request.form["message"]
    id = str(uuid4())
    # Add to database (not implemented yet)
    messages.append({"author": author, "message": message, "id": id})
    return render_template("index.html", messages=messages)

@app.route("/create_reply", methods=["POST"])
def create_reply():
    id = str(uuid4())
    reply_id = request.form["message_id"]
    author = request.form["author"]
    reply_message = request.form["reply_message"]
    # Add reply to database (not implemented yet)
    messages.append({
        "author": author, 
        "message": reply_message, 
        "id": id,
        "reply_id": reply_id
        })
    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    app.run(debug=True)

questions = [
    {"question": "Which trait resonates most with you?",
     "options": ["Courage and bravery (Gryffindor)", "Wisdom and wit (Ravenclaw)", "Loyalty and friendship (Hufflepuff)", "Ambition and cunning (Slytherin)"],
     "scores": [3, 2, 1, 4]},
    {"question": "How would you handle a difficult situation?",
     "options": ["Face it head-on, even if it's dangerous (Gryffindor)", "Think of a clever plan to overcome it (Ravenclaw)", "Help others involved as a team (Hufflepuff)", "Use your skills to gain an advantage (Slytherin)"],
     "scores": [4, 3, 2, 1]},
    # ... add more questions
]

answers = []

def determine_house(answers):
  house_scores = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}
  for question, answer in zip(questions, answers):
    house_scores[answer.split(" (")[1][:-1]] += question["scores"][answer.split(" (")[0]]
  return max(house_scores, key=house_scores.get)

def determine_house(answers):
  # Store points for each house
  house_scores = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}

  # Check each question and answer
  for question, answer in zip(questions, answers):
    # Give points based on answer choice
    if answer == "Gryffindor":
      house_scores["Gryffindor"] += 2
    elif answer == "Ravenclaw":
      house_scores["Ravenclaw"] += 3
    # ... and so on for other answers

  # Find the house with the most points
  return max(house_scores, key=house_scores.get)

# Get the sorted house
house = determine_house(answers)

# Welcome message with house info
message = f"Welcome to the {house} message board! "

# Show the message board with your house details
print(message)  # In reality, send this to the webpage!
