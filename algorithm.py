x=int(input("total_no_of_pages: "))

def is_even(k):
    if k%2 == 0:
        return(True)
    else:
        return(False)


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







