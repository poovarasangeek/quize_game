print("Quize game")
plyr=input("Do you want to play?\n")
if plyr.lower() == "yes":
    print("ok lets play")
else:
     quit()  
scr=0
      
q1=input("Q1.how many days are in a week?\n")     
if q1.lower()=="seven":
    print("you are correct")
    scr+=1
else:
    print("you are wrong!") 
       
q2=input("Q2.which city is capital of india?\n")    
if q2.lower()=="delhi":
    print("you are correct")
    scr+=1
else:
    print("you are wrong!")  

q3=input("Q3.which animal is fastest in the world?\n")  
if q3.lower()=="cheetah":
    print("you are correct")
    scr+=1
else:
    print("you are wrong!") 
    
print("your score:",scr)    
         