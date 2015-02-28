from collections import Counter

numbers = []
max_number = 0

def main():
    length_of_list = getNumber("Enter the amount of numbers you want to use: ")
    
    index = 1 # Acts as counter so user knows how many numbers have been entered so far
    while (len(numbers) != length_of_list):
        item = getNumber("Enter number %d: " %(index))
        numbers.append(item)
        index++
        
    print("")
    print("Here are your numbers: " + str(numbers))
    numbers.sort()
    print("Here are your numbers, sorted: " + str(numbers))
    print("")
    
    print("Mean: " + mean())
    print("Median: " + median())
    print("Mode: " + mode())
    
def getNumber(prompt):
    # Prompts user for starting number. Exception/While loop 
    # catches inputs that aren't proper integers.
    success = False
    while (!success):
        try:
            print(prompt)
            number = raw_input()
            success = True
        except:
            pass
    
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

if (__name__ == "__main__"):
    main()

'''
#Fix so it can loop if user inputs string for "max_number"
while (max_number <= 0):
    max_number = int(raw_input("Enter the amount of numbers you want to use: "))
    
index = 1    
while (len(numbers) != max_number):
    try:
        item = float(raw_input("Enter a number (%d): " %index))
        numbers.append(item)
        index += 1
    except ValueError:
        item = float(raw_input("Please enter a numeral: "))
        numbers.append(item)
        index += 1

print ""
print "Here are your numbers: " + str(numbers)
numbers.sort()
print "Here are your numbers, sorted: " + str(numbers)
print ""

### Mean ###
print "Mean: " + str((sum(numbers)/len(numbers)))

### Median ###
if ((len(numbers)%2) != 0):
    median = numbers[len(numbers)/2]
else:
    digit_first = numbers[len(numbers)/2 - 1]
    digit_last = numbers[len(numbers)/2]
    median = (digit_first + digit_last)/2.0    
print "Median: " + str(median)

### Mode ###
data = Counter(numbers)
data.most_common()
mode = str(data.most_common(1))
print "Mode (mode, # of times mode appeared): " + mode
print ""
raw_input("Press Enter when finished")
'''
