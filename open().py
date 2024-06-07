
numbers= open("avg.txt", "w")
numbers.write("10,11,12,13,14,15,16,17,18,19,20")
numbers.close()


read = open("avg.txt", "r")
line= read.read()
sum=0
for num in line.split(","):
    sum+=int(num)

Number_of_numbers= 11
print(sum/Number_of_numbers)