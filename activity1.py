#Take input for the student that he can attend the exam or not
medical_cause=input("did you have a medical cause Y or N: ")
#Take input of the attendance
atten = int(input("enter the attendance of the student"))

#checking the user input predicting output accordindingly

if medical_cause == 'Y':#chicking the condition 1
    print ("You are allowed")
else:
    if atten>=75: #checking the condition 2
      print ("allowed")
    else:
       print("Not allowed")
