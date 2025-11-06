# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
    # States
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata",

    # Union Territories
    "Andaman and Nicobar Islands": "Port Blair",
    "Chandigarh": "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu": "Daman",
    "Delhi": "New Delhi",
    "Jammu and Kashmir": "Srinagar (Summer), Jammu (Winter)",
    "Ladakh": "Leh",
    "Lakshadweep": "Kavaratti",
    "Puducherry": "Puducherry"
}


# Generate 2 quiz files.
for quiz_num in range(2):
    # TODO: Create the quiz and answer key files.
    quiz_file = open(f'Capitalsquiz{quiz_num + 1}.txt', 'w', encoding='UTF-8')
    answer_file = open(f'Capitalsquiz_answers{quiz_num + 1}.txt', 'w', encoding='UTF-8')

    # TODO: Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})')
    quiz_file.write('\n\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # TODO: Loop through all 50 states, making a question for each.
    for num in range(35):

        # Get right and wrong answers.
        correct_answer = capitals[states[num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # TODO: Write the question and answer options to the quiz file.
        quiz_file.write(f'{num + 1}. Capital of {states[num]}:\n')
        for i in range(4):
             quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n") 
        quiz_file.write('\n')
        # TODO: Write the answer key to a file.
        quiz_file.write(f'{num + 1}. Capital of {states[num]}:\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n") 
        quiz_file.write('\n')