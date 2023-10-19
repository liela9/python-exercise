from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#B1DDC6"
SCORE_FONT = ("Arial", 15, "bold")
QUESTION_FONT = ("Arial", 30, "italic")
IMG = "tkinter-GUI/REST-API/trivia/card.png"
TRUE_BTN = "tkinter-GUI/REST-API/trivia/true.png"
FALSE_BTN = "tkinter-GUI/REST-API/trivia/false.png"

class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=40, pady=40)

        self.canvas = Canvas(width=800, height=526, bg=THEME_COLOR, highlightthickness=0)
        img = PhotoImage(file=IMG)
        self.canvas.create_image(400, 263, image=img)
        self.q_text = self.canvas.create_text(400, 263, text="", font=QUESTION_FONT, width=700)
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file=TRUE_BTN)
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.is_true)
        self.true_btn.grid(row=2, column=1)

        false_img = PhotoImage(file=FALSE_BTN)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.is_false)
        self.false_btn.grid(row=2, column=0, )

        self.score_label = Label(text="score: 0", width=10, bg=THEME_COLOR, font=SCORE_FONT)
        self.score_label.grid(row=0, column=0)

        self.get_next_question()
        self.window.mainloop()

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def update_score_label(self):
        self.score_label.config(text=f"score: {self.quiz.score}")

    def get_next_question(self):
        self.score_label.config(fg="black")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've completed the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.update_score_label()
            self.score_label.config(fg="green")
        else:
            self.score_label.config(fg="red")
        self.window.after(1000, self.get_next_question)