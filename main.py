from tkinter import *
import random
from PIL import Image, ImageTk
score = 0
names = []
global questions_answers
asked = []

questions_answers = { 
    1: ["Who won the 2021 F1 Championship?", 'Max Verstappen', 'Lewis Hamilton','Christiano Ronaldo', 'Fernando Alonso ' ,'Max Verstappen',1],
  
    2: ["Which NBA team won the NBA in 2017?",'Cleveland Caveliers  ','Golden state warriors','Manchester utd', 'Milwaukee Bucks','Golden state warriors',2],
  
    3: ["What material is used to make the outer shell of a cricket ball?", 'Leather','Cork', 'Twine','Rubber','Leather',1],
  
    4: ["How many sports are there in the world?", '5','1000', '20,000','8000','8000',4],
  
    5: ["The olympics are held every how many years?", '10','4', '5','2','4',2],
  
    6: ["What is the national sport of India?", 'Hockey','Cricket', 'Football','Rugby','Hockey',1],

    7: ["How many days is a cricket test match played ?", '2','10', '5','3','5',3],

    8: ["how many weight classes in boxing?", '5','25', '17','1','17',3],

    9: ["Who played for the Chicago bulls?", 'Lebron james','Micheal Jordan', 'Steph curry','Diangelo russel ','Micheal Jordan',2],

    10: ["What is used in tennis to hit the ball?", 'Raquet','Bat', 'Stick','Hand','Raquet',1],

}



def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()
     

class QuizStarter:
  def __init__(self, parent):
    background_color="lightgrey"

    self.heading_label=Label(window, text = "General Knowledge Sports quiz", font =( "Times","18","bold"),bg=background_color)
    self.heading_label.place(x=30, y=10)

    self.var1=IntVar()

    self.user_label=Label(window, text="Please Enter your Username Below: ", font=( "Tw Cen MT","18","bold"),bg=background_color)
    self.user_label.place(x=20 , y= 80)

    self.entry_box=Entry(window)
    self.entry_box.grid(row=1,padx=150, pady=120)

    self.continue_button = Button(window, text="Continue", font=( "Helvetica","13","bold"), bg="darkgrey",command=self.name_collection)
    self.continue_button.grid(row=2,padx=5, pady=5)

    self.Exit_button = Button(window, text="Exit Quiz", font=( "Helvetica","13","bold"), bg="darkgrey",command=self.name_collection)
    self.continue_button.grid(row=2,padx=4, pady=4)






  
  def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        self.heading_label.destroy()
        self.user_label.destroy()
        self.entry_box.destroy()
        self.continue_button.destroy()
        Quiz(window)

class Quiz:

   def __init__(self, parent):
    background_color="lightgrey"
 
 
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomiser()

    self.question_label=Label(window, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.var1=IntVar()

    self.rb1 = Radiobutton(window, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton(window, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.var1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton(window, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.var1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton(window, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.var1, pady=10)
    self.rb4.grid(row=4, sticky=W)

    self.confirm_button = Button(window, text="Confrim",bg="white",command=self.test_progress)
    self.confirm_button.grid(row=6)
    self.score_label  = Label(window, text =
                             'score')
    self.score_label.grid(row= 7)  
     
     
   def questions_setup(self):
     randomiser()
     self.var1.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.rb1.config(text=questions_answers[qnum][1])
     self.rb2.config(text=questions_answers[qnum][2])
     self.rb3.config(text=questions_answers[qnum][3])
     self.rb4.config(text=questions_answers[qnum][4])

 
   def test_progress(self):
      global score
      scr_label=self.score_label
      choice=self.var1.get()
      if len(asked)>9:
        if choice == questions_answers[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
        else:
          score+=0
          scr_label.configure(text="The correct answer was: "+ questions_answers[qnum][5] )
          self.confirm_button.config(text="confirm")
     
      else:
            if choice==0:
              self.confirm_button.config(text="Try Again, you didn't select an option then submit again" )
              choice=self.var1.get()
            else:
              if choice == questions_answers[qnum][6]:
                score+=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup()
 
              else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5])
                  self.confirm_button.config(text="Confirmn")
                  self.questions_setup()
       


if __name__== "__main__":
    window = Tk()
    window.title("12CSC Quiz")
    window.geometry("600x600")
    bg_image = Image.open("Lebron james.jpg")
    bg_image = bg_image.resize((1000,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = QuizStarter(window)

   
  

    window.mainloop()