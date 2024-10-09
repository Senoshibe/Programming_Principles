def fibonacci_sequence(n):
    fibonacci_num = []
    num1, num2 = 0, 1

    for _ in range(n):
        if len(fibonacci_sequence) == 0 or len(fibonacci_sequence[-1]) == 4: 
            fibonacci_sequence.append([])
            
        fibonacci_sequence[-1].append(num1)    
        num1, num2 = num2, num1 + num2

    return fibonacci_sequence


    