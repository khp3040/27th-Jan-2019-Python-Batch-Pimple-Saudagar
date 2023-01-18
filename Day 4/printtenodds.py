
number = input('Enter a number: ')
count = 1

while True:  # Condition is always to True Infinite
    if number % 2 == 1:
        print '%d. - %d is an odd number: ' %(count, number)
        count += 1
    number += 1

print 'All above are odd numbers'

number = input()
count = 1
while count <=10:
    if number % 2 ==1:
        print "%d, -- %d i an odd number" %(count,number)
        count+=1
    number+=1
else:
    print "All above are odd numbers"