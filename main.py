from tkinter import *
import random # for selection of random questions
from PIL import Image, ImageTk # for images to be imported 
from tkinter import messagebox # for messagebox to be imported




def randomselect(): #selects random questions
    global qnum #In my dictionary, the question number is the key.
    qnum = random.randint(1,10)  # Number of questions
    if qnum not in asked: # asked is a list I declared, so to start of with any number will be added
      asked.append(qnum)
    elif qnum in asked:
      randomselect()
     

class Quizinitiator: # Quiz initiator, main page of the quiz, leads user to questions page.
  def __init__(self, parent):
    background_color="Black" # background colour
    text_color="white" 
    
    self.title_label=Label(window, text = "General Knowledge Sports quiz", font =( "Times","18","bold"),bg=background_color,fg=text_color)
    self.title_label.place(x=30, y=10) # The quiz heading

    self.option_picker=IntVar()

    self.instruction_label=Label(window, text="Please Enter your Username Below: ", font=( "Tw Cen MT","18","bold"),bg=background_color,fg=text_color)
    self.instruction_label.place(x=20 , y= 80) # The name instruction

    self.username_entrybox=Entry(window)
    self.username_entrybox.grid(row=1,padx=150, pady=120) # Name entrybox

    self.proceed_button = Button(window, text="Continue", font=( "Helvetica","13","bold"), bg= background_color,fg=text_color,command=self.username_entry)
    self.proceed_button.grid(row=2,padx=5, pady=5) # Continue button 

   


  def username_entry(self): # Controls the entry of names
      name = self.username_entrybox.get()
       # Start of error handling 
      if name == '':             # To make sure the user has entred a username
            messagebox.showerror('Name is Necessary!', 'Please enter your username!') # To make sure the user has entred a username
      elif len(name) > 15:        
        messagebox.showerror('AN ERROR HAS BEEN MADE!', 'Please enter a name between 1 and 15 Letters')# To make sure the users name is between 1 and 15 letters 
      elif name.isnumeric():
            messagebox.showerror('AN ERROR HAS BEEN MADE!', 'Name should ONLY!! have letters please')# To make sure the user has entred no numbers in their name 
      elif not name.replace(' ','').isalpha(): # .replace to allow spaces 
        messagebox.showerror('AN ERROR HAS BEEN MADE!', 'No Symbols Accepted ,Try Again!')# To make sure the user has no symbols in thier name
      else:

            names.append(name)  
            print (names)
            self.title_label.destroy() #will destroy quiz heading
            self.instruction_label.destroy() #will destroy name instructions
            self.username_entrybox.destroy() #will destroy username enterybox 
            self.proceed_button.destroy() #will destroy continue button
            StartQuiz(window) # This will open the questions page of the quiz







class StartQuiz: # main questions window, this is where users play the quiz. 

   def __init__(self, parent):
    background_color="Black" # background colour
    text_color="red"  
 
 
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid() # frame of the quiz page 

    randomselect() # Selects random questions

    self.question_label=Label(window, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold"),bg=background_color,fg=text_color )
    self.question_label.grid(row= 0, padx=10, pady=10) # label for questions 

    self.option_picker=IntVar()

    self.possibility1 = Radiobutton(window, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color,fg=text_color, value=1, variable=self.option_picker, pady=10)
    self.possibility1.grid(row=1, sticky=W) # Answer option 1 

    self.possibility2 = Radiobutton(window, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color,fg=text_color, value=2, variable=self.option_picker, pady=10)
    self.possibility2.grid(row=2, sticky=W) # Answer option 2

    self.possibility3 = Radiobutton(window, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color,fg=text_color, value=3, variable=self.option_picker, pady=10)
    self.possibility3.grid(row=3, sticky=W) # Answer option 3

    self.possibility4 = Radiobutton(window, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color,fg=text_color, value=4, variable=self.option_picker, pady=10)
    self.possibility4.grid(row=4, sticky=W) # Answer option 4

    self.confirm_key = Button(window, text="Confrim",bg="white",command=self.test_progression )
    self.confirm_key.grid(row=6) # confirm button which leads you to the next question
    self.score_label  = Label(window, text =
                             'score')
    self.score_label.grid(row= 7)

    self.leave = Button(window, text='Exit Quiz', font=('Helvetica', '13', 'bold'), bg='red', command=self.final_screen) 
    # Exit quiz button which takes you to the final page 
    self.leave.place(x=243, y=300)  
     
     
   def questions_setup(self): #question setup 
     randomselect() # randomises questions 
     self.option_picker.set(0) #sets value to 0 
     self.question_label.config(text=questions_answers[qnum][0]) #displays the questions being asked
     self.possibility1.config(text=questions_answers[qnum][1]) # radiobutton displaying answer possibility 1
     self.possibility2.config(text=questions_answers[qnum][2]) # radiobutton displaying answer possibility 2
     self.possibility3.config(text=questions_answers[qnum][3]) # radiobutton displaying answer possibility 3
     self.possibility4.config(text=questions_answers[qnum][4]) # radiobutton displaying answer possibility 4

 
   def test_progression (self): # Shows the user their score 
      global score # sore needs to be accessed by everyone
      scr_label=self.score_label
      choice=self.option_picker.get() # to store the option the user has chosen 
      if len(asked)>9: # To see if its the last question adn wether to end the quiz or not
        if choice == questions_answers[qnum][6]: #checking if its the right answer in index 6
          score +=1 # adds one point to the tally when answer is correct
          scr_label.configure(text=score) # displays new points gained everytime a question is answered correctly
          self.confirm_key.config(text="Confirm")# will change the button name to Confirm
          self.final_screen()# to open the final screen of the quiz 
        else:
          score+=0 # score stays the same 
          scr_label.configure(text="The correct answer was: "+ questions_answers[qnum][5] ) # if asnwer is incorrect, will display corrrect asnwer
          self.confirm_key.config(text="confirm") #Confirm Button
          self.final_screen() #to open the final screen of the quiz 
      else:
            if choice==0:# score stays the same if user does not select an option
              self.confirm_key.config(text="Try Again, you must select an option please submit again " ) # error message
              choice=self.option_picker.get() #Stil get the answer if they didnt chose it
            else:
              if choice == questions_answers[qnum][6]: # if user answer is correct
                score+=1 # adds 1 point to score tally
                scr_label.configure(text=score)
                self.confirm_key.config(text="confirm")
                self.questions_setup() # moves onto the next question
 
              else:
                  score+=0 # if user answer is incorrect score stays the same
                  scr_label.configure(text="Incorrect!! The correct answer was: " + questions_answers[qnum][5])
                  self.confirm_key.config(text="Confirm")
                  self.questions_setup()# moves onto the next question
       


   def final_screen(self): # Moves to final screen 
    window.destroy()
    name = names[0]
    open_finish_object = finish()



class finish: # Fnal page of the quiz, displays thank you message and asks them to try again later.


  def __init__(self):
        background_color = 'black' #background colour 
        global finish_window
        finish_window = Tk()
        finish_window.title('Exit Box') # Exit window title
        finish_window.geometry('600x600')# Exit window size 

        self.finish_frame = Frame(finish_window, width=700, height=600,bg=background_color)
        self.finish_frame.grid(row=1)

        self.finish_heading = Label(finish_window,text='Thank You For Attempting The Quiz  ',  font=('Tw Cen Mt', 22, 'bold'), bg='black',fg='white') # heading of the end screen 
        self.finish_heading.place(x=15, y=35) # position of heading

        self.exit_button = Button(finish_window,text='Exit',width=10,bg='black',fg='white',font=('Tw Cen Mt', 12, 'bold'),command=self.eliminate_finish,)# for the exit button that eliminates the quiz
        self.exit_button.place(x=260, y=200)# position of final exit button 

        self.invite_label = Label(finish_window, text='Please try again later :)' + str(names),font=('Tw Cen Mt', 12, 'bold'),width=40, bg='black',fg='white') # label to invite the user to try again 
        self.invite_label.place(x=110, y=80) # position of this label
       
        self.final_score = Label(finish_window, text='Your final score is ' + str(score), font=('Tw Cen Mt', 12, 'bold'), width=40, bg='black',fg='white') # label to show the users final score
        self.final_score.place(x=110, y=110) # position of this label
       
 
 
  def eliminate_finish(self): # will destroy all widgets below
      self.finish_frame.destroy()# will destroy finish frame label 
      self.finish_heading.destroy()# will destroy end screen heading 
      self.exit_button.destroy()# will destroy end screen exit button 
      self.invite_label.destroy()# will destroy end screen invite label
      finish_window.destroy()# will destroy finish window

score = 0 
names = [] #list
asked = [] #list

questions_answers = { #questions for the user
    1: ["Who won the 2021 F1 Championship?", 'Max Verstappen', 'Lewis Hamilton','Christiano Ronaldo', 'Fernando Alonso ' ,'Max Verstappen',1],#question 1. options are called index 6 
 
    2: ["Which NBA team won the NBA in 2017?",'Cleveland Caveliers  ','Golden state warriors','Manchester utd', 'Milwaukee Bucks','Golden state warriors',2],#question 2
 
    3: ["What material is used to make the outer shell of a cricket ball?", 'Leather','Cork', 'Twine','Rubber','Leather',1],#question 3
 
    4: ["How many sports are there in the world?", '5','1000', '20,000','8000','8000',4],#question 4
 
    5: ["The Nba happens every how many years?", '10','1', '5','2','1',2],#question 5
 
    6: ["What is the national sport of India?", 'Hockey','Cricket', 'Football','Rugby','Hockey',1],#question 6

    7: ["How many days is a cricket test match played ?", '2','10', '5','3','5',3],#question 7

    8: ["How many weight classes in boxing?", '5','25', '17','1','17',3],#question 8 

    9: ["Who played for the Chicago bulls?", 'Lebron james','Micheal Jordan', 'Steph curry','Diangelo russel ','Micheal Jordan',2], #question 9

    10: ["What is used in tennis to hit the ball?", 'Raquet','Bat', 'Stick','Hand','Raquet',1], #question 10

}

#my programs runs below 
if __name__== "__main__":
    window = Tk()
    window.title("12CSC Quiz Guransh")
    window.geometry("600x600")
    bg_image = Image.open("LebronJames.jpg")# file of background image
    bg_image = bg_image.resize((1000,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image) # imagelabel
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Quizinitiator(window)

   
 

    window.mainloop() # so that the window does not dissaper