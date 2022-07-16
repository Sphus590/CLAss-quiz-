from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

score = 0
names = []
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



def randomselect():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomselect()
     

class Quizinitiator:
  def __init__(self, parent):
    background_color="lightgrey"

    self.heading_label=Label(window, text = "General Knowledge Sports quiz", font =( "Times","18","bold"),bg=background_color)
    self.heading_label.place(x=30, y=10)

    self.var1=IntVar()

    self.user_label=Label(window, text="Please Enter your Username Below: ", font=( "Tw Cen MT","18","bold"),bg=background_color)
    self.user_label.place(x=20 , y= 80)

    self.entry_box=Entry(window)
    self.entry_box.grid(row=1,padx=150, pady=120)

    self.continue_button = Button(window, text="Continue", font=( "Helvetica","13","bold"), bg="darkgrey",command=self.username_entry)
    self.continue_button.grid(row=2,padx=5, pady=5)

   


  def username_entry(self):
      name = self.entry_box.get()
       
      if name == '':
            messagebox.showerror('Name is Necessary!', 'Please enter your username!')
      elif len(name) > 15:
        messagebox.showerror('AN ERROR HAS BEEN MADE!', 'Please enter a name between 1 and 15 Letters')
      elif name.isnumeric():
            messagebox.showerror('AN ERROR HAS BEEN MADE!', 'Name should ONLY!! have letters please')
      elif not name.isalpha():
        messagebox.showerror('AN ERROR HAS BEEN MADE!', 'No Symbols Accepted ,Try Again!')
      else:

            names.append(name)  
            print (names)
            self.heading_label.destroy()
            self.user_label.destroy()
            self.entry_box.destroy()
            self.continue_button.destroy()
            StartQuiz(window)







class StartQuiz:

   def __init__(self, parent):
    background_color="lightgrey"
 
 
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomselect()

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

    self.leave = Button(window, text='Exit Quiz', font=('Helvetica', '13', 'bold'), bg='darkgrey', command=self.final_screen) 
     
    self.leave.place(x=0, y=300)  
     
     
   def questions_setup(self):
     randomselect()
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
          self.final_screen()
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
       


   def final_screen(self):
    window.destroy()
    name = names[0]
    open_finish_object = finish()



class finish:


  def __init__(self):
        background_color = 'black'
        global finish_window
        finish_window = Tk()
        finish_window.title('Exit Box')
        finish_window.geometry('600x600')

        self.finish_frame = Frame(finish_window, width=700, height=600,bg=background_color)
        self.finish_frame.grid(row=1)

        self.finish_heading = Label(finish_window,text='Thank You For Attempting The Quiz  ',  font=('Tw Cen Mt', 22, 'bold'), bg='white')
        self.finish_heading.place(x=15, y=35)

        self.exit_button = Button(finish_window,text='Exit',width=10,bg='white',font=('Tw Cen Mt', 12, 'bold'),command=self.eliminate_finish,)
        self.exit_button.place(x=260, y=200)

        self.list_label = Label(finish_window, text='Please try again later :)' + str(names),font=('Tw Cen Mt', 12, 'bold'),width=40, bg='white')
        self.list_label.place(x=110, y=80)
       
        self.final_score = Label(finish_window, text='Your final score is ' + str(score), font=('Tw Cen Mt', 12, 'bold'), width=40, bg='white')
        self.final_score.place(x=110, y=110)
       
 
 
  def eliminate_finish(self):
      self.finish_frame.destroy()
      self.finish_heading.destroy()
      self.exit_button.destroy()
      self.list_label.destroy()
      finish_window.destroy()








if __name__== "__main__":
    window = Tk()
    window.title("12CSC Quiz")
    window.geometry("600x600")
    bg_image = Image.open("Lebron james.jpg")
    bg_image = bg_image.resize((1000,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Quizinitiator(window)

   
 

    window.mainloop()