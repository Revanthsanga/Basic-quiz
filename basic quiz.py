import time

# Quiz Data
quiz_data = {
    "What is the capital of India?": {
        "A": "Chennai",
        "B": "Delhi",
        "C": "Hyderabad",
        "D": "Mumbai",
        "Answer": "B"
    },
    "Who is the founder of Apple": {
        "A": "Elon Musk",
        "B": "Steve Jobs",
        "C": "Jeff Bezos",
        "D": "Mark Zuckerberg",
        "Answer": "B"
    },
    "Which team won the Icc t20 world cup 2024?": {
        "A": "India",
        "B": "South Africa",
        "C": "Australia",
        "D": "England",
        "Answer": "A"
    },
    "Which ammunition does AK-47 use?": {
        "A": "7.62mm",
        "B": "5.56mm",
        "C": "45Acp",
        "D": "9mm",
        "Answer": "A"
    },
    "What is the mascot of Pokemon": {
        "A": "Rhydon",
        "B": "Charizard",
        "C": "Pikachu",
        "D": "Greninja",
        "Answer": "C"
    }
}

def display_question(question, options):
    """Displays a question with its options."""
    print(f"\n** Question: {question} **")
    for option, value in options.items():
        if option != "Answer":
            print(f"{option}: {value}")

def quiz_game():
    """Simple Quiz Game Function"""
    score = 0
    total_questions = len(quiz_data)
    print("** Welcome to the Quiz Game! **")
    print("-----------------------------------")
    time.sleep(1)  
    for question, data in quiz_data.items():
        display_question(question, data)
        
        user_answer = input("\nEnter your answer (A, B, C, D): ").upper()
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid input. Please enter A, B, C, or D: ").upper()
        
        if user_answer == data["Answer"]:
            print("Correct Answer! You earn 2 points.")
            score += 2
        else:
            print(f"Incorrect Answer. The correct answer is {data['Answer']}. You lose 1 point.")
            score -= 1
        
        print(f"** Current Score: {score} **")
        print("-----------------------------------")
    
    print(f"\n** Quiz Completed! Your Final Score out of {total_questions*2} is: {score} **")
    if score <= 3 :
        print("** Better luck next time! You scored below average. **")
    elif score <= 5 :
        print("** You scored Average. **")
    elif score <=7:
        print("** Well done you scored Good. **")
    else:
        print("** Congratulations! You scored Excellent.  **")

if __name__ == "__main__":
    quiz_game()