from tkinter import * 
from tkinter import messagebox

root = Tk()

root.title('Page sorter')
root.geometry("200x200")  
Label(root, text = "Enter no. of pages,").place(x = 30,y = 20)  

def is_even(k):
        if k%2 == 0:
            return(True)
        else:
            return(False)

def output_res(a,b):  

    messagebox.askretrycancel("Page sorted","first round :{x},/n second round{y}".format(x = a, y = b))
  


def __main__():
    x = int(input_no.get())
    first_round=[]
    second_round=[]
    if is_even(x):
        print("Total no of pages are even")
        first_round.append(1)
        first_round.append(x)
        mid_page=int(x/2)
        last_page=x
    else:
        print("Total no of pages are odd")
        first_round.append(1)
        first_round.append("skip!!")
        mid_page=int((x+1)/2)
        last_page=x+1
    R1current_page1 = 1
    R1current_page2 = last_page
    while R1current_page1 < (mid_page-1):
        R1current_page1+=2
        first_round.append(R1current_page1)
        R1current_page2-=2
        first_round.append(R1current_page2)     
    R2current_page1 = last_page-1
    R2current_page2 = 2
    while R2current_page2 <= (mid_page):       
        second_round.append(R2current_page1)
        second_round.append(R2current_page2)
        R2current_page1-=2
        R2current_page2+=2
    print(first_round)
    print(second_round)
    output_res(first_round,second_round)

input_no = StringVar()


e = Entry(root,textvariable=input_no).place(x = 34, y = 50)


b1 = Button(root,text = "Next",command=__main__, activeforeground = "red").place(x = 80, y = 100)

root.mainloop() 

