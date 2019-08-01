#Basic - Print all integers from 0 to 150.
for x in range (150):
    print(x)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range (5,1000,5):
    print(x)


#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for val in range (100):
    if val / 5:
        continue
    print(val)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
i=1
sum=0
while i<=500000:
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)


#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
y=2018
while y>0:
    y=y-4
print(y)


#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flex_counter(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)