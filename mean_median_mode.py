from collections import Counter

numbers = []
max_number = 0

def main():
    length_of_list = getNumber("Enter the amount of numbers you want to use: ")
    
    index = 1 # Acts as counter so user knows how many numbers have been entered so far
    for num in range(0, length_of_list):
        item = getNumber("Enter number %d: " %(index))
        numbers.append(item)
        index += 1
        
    print("")
    print("Here are your numbers: " + str(numbers))
    numbers.sort()
    print("Here are your numbers, sorted: " + str(numbers))
    print("")
    
    print("Mean: " + mean())
    print("Median: " + str(median()))
    print("Mode: (mode, # of times mode appeared)" + mode())
    
def getNumber(prompt):
    # Prompts user for starting number. Exception/While loop 
    # catches inputs that aren't proper integers.
    success = False
    number = 0
    while (not success):
        try:
            print(prompt)
            number = int(raw_input())
            success = True
        except:
            pass
        
    return number
    
def mean():
    return str((sum(numbers)/len(numbers)))
    
def median():
    median = 0
    if ((len(numbers)%2) != 0): # If the length of numbers is odd, get middle
        median = numbers[len(numbers)/2]
    else: #if length of numbers is even, get average of two middle numbers
        digit_first = numbers[len(numbers)/2 - 1]
        digit_last = numbers[len(numbers)/2]
        median = (digit_first + digit_last)/2.0
        
    return median
    
def mode():
    data = Counter(numbers)
    #data.most_common()
    mode = str(data.most_common(1))
    
    return mode

if (__name__ == "__main__"):
    main()
