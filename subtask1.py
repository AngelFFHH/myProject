def LargSquare(n): #we define the function LargSquare
    q = 0
    while q*q <= n: #we evaluate the condition and stop the loop when we find the value.
        q += 1
    #We adjusted q
    q -= 1
    q = q*q
    #We print the solution
    print(f"The larger square of {n} is {q}")

LargSquare(35) #we have to call the function

