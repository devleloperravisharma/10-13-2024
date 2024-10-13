import pgzrun
#to change in your code
#the width of the timer box should be larger
#Skip box should be horizontal

WIDTH = 870
HEIGHT = 650 
TITLE = "Test Your Knowledge!"
score = 0
time_left = 10
question_file_name = "question.txt"
is_game_over = False

#boxes
marquee_box = Rect(0,0, 880, 80)
question_box = Rect(0, 0, 650,150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)
#numbers and lists
marquee_message = ""
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0
question_index = 0
question = []
#box positions
marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700, 270)


#functions

def draw():
    global marquee_message
    screen.clear()
    screen.fill("pink")
    screen.draw.filled_rect(marquee_box, "white")
    screen.draw.filled_rect(question_box, "white")
    screen.draw.filled_rect(timer_box, "white")
    screen.draw.filled_rect(skip_box, "white")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "sky blue")

    
    marquee_message = f"Welcome to the quiz game! You are at Question {question_index} of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color = "pink")

    screen.draw.textbox(str(time_left), timer_box, color = "pink", shadow = (0.5, 0.5), scolor = "dim grey")

    screen.draw.textbox("skip", skip_box, color = "pink")

    screen.draw.textbox(question[0].strip(), question_box, color = "pink")

    index = 1
    for answerbox in answer_boxes:
        screen.draw.textbox(question[index].strip(), answerbox, color = "white")
        index += 1

def update():
    move_marquee()

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name, "r")
    for row in q_file:
        questions.append(row)
        question_count += 1
    q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def on_mouse_down(pos):
    index = 1
    for answer_box in answer_boxes:
        if answer_box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global time_left, score, question, questions

    score += 1

    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def game_over():
    global question, time_left, is_game_over
    #add message to marquee_box
    message = f"You finished the game! \nYour score is {score}/{question_count}"
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0
    is_game_over = True

def skip_question():
    global question, time_left

    if questions and not is_game_over:
        question = read_next_question()
        time_left = 10

    else:
        game_over()

def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()

read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left, 1)
pgzrun.go()