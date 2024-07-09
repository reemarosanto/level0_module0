from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question = simpledialog.askstring(title='Greeter', prompt="How many states are in America?")
    #      // 3.  Use an if statement to check if their answer is correct
    if question == "50":
    #      // 4.  if the user's answer was correct, add one to their score 
        score = score + 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    question_2 = simpledialog.askstring(title='Greeter', prompt="How many new emotions in Inside Out 2?")
    if question_2 == "4":
        score = score + 1
    question_3 = simpledialog.askstring(title='Greeter', prompt="What was Jane Austen's most popular book?")
    if question_3 == "Pride and Prejudice":
        score = score + 1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(message="Your score is " + str(score))
    # Run the window's .mainloop() method
    window.mainloop()