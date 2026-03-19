analyzer = int(input("How many numbers do you want to analyze?: "))

while analyzer <= 0:
    print("Invalid quantity")
    analyzer = int(input("Please enter a valid quantity: "))
total = 0
counter = 0

while  counter < analyzer: 
        number = int(input("Enter a number: "))
        if counter == 0:
            biggest = number
            smallest = number
        else:
            if number > biggest:
                biggest = number
            if number < smallest:
                smallest = number
        
        counter += 1 
        total += number
    
mean = total / analyzer
print(f"Biggest: {biggest}\nSmallest: {smallest}\nTotal: {total}\nMean: {mean}\n")
