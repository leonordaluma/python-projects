from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 14, "italic")
class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(150,125, 
                                         text="Amazon acquired Twitch in August 2014 for $970 million dollars.", 
                                         font=QUESTION_FONT,
                                         fill=THEME_COLOR,
                                         width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.score_text = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1, padx=50)
        
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.answer_true)
        self.true_button.grid(row=2, column=0)
        
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, command=self.answer_false)
        self.false_button.grid(row=2, column=1)
        
        self.get_question()
        
        
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(self.score_text, text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=question)
        else:
            self.canvas.itemconfig(self.q_text, text=f"You've completed the game!\n Your final score is {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.get_feedback(self.quiz.check_answer("True"))
        
    def answer_false(self):
        self.get_feedback(self.quiz.check_answer("False"))
    
    
    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_question)