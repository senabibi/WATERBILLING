def gallon():
    code=str(input("Enter customer code:")).lower()
    begin_read=int(input("Beginning meter reading:"))
    while not begin_read>=0:
        print("Beginner meter must be a positive number.")
        begin_read=int(input("Beginning meter reading:"))
    end_read=int(input("Enter ending meter reading:"))
    if end_read<=begin_read:
        end_reading=end_read
        begin_reading=999999999-begin_read
        subs=end_reading+begin_reading
    else:
        subs=(end_reading-begin_reading)   
    
    subs=abs(subs)/10
    if code=='r':
        payment=5+(subs*0.0005)
    if code=='c':
        if subs<=4000000:
            payment=1000
        else:
            payment=1000+(.00025*(subs-4000000))
    if code=='i':
        if subs<=4000000:
            payment=1000
        elif 4000000<subs<=10000000:   
            payment=2000
        elif 10000000<subs:
            payment=2000+(.00025*(subs-10000000))    


    print(f"Customer code:{code}")
    print(f"Beginning meter reading:{begin_read}")
    print(f"Ending meter reading:{end_read}")
    print(f"Gallons of water used:{(subs)}")
    print(f"Amount billed:${(payment)}.00")        
gallon()



