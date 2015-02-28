from collections import Counter

numbers = []
max_number = 0

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
