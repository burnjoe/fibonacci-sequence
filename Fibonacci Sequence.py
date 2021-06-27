#ask user how many terms
term = int(input("Enter How Many Fibonacci Terms: "))

#declare variable
n1 = 0          #or n1, n2 = 0, 1
n2 = 1
ctr = 0

#conditioning (if user's input is a negative number then restart. elseif usinput is 1 then print 0)
#(else compute terms and print)
if term <= 0:
    print("Please Enter Positive Integer Only, Please Restart.")
elif term == 1:
    print(n1)
else:
    while ctr < term:
        print(n1)
        nth = n1 + n2 

        #update variable
        n1 = n2
        n2 = nth
        ctr += 1
