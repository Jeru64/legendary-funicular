medical_cause=input("did you have a medical cause Y or N:")
atten=int(input("enter attendance of the student:"))
if medical_cause=='Y' or medical_cause=='y':
    print("You are allowed")
else:
    if atten>75:
        print("You are allowed")
    else:
        print("You are not allowed")