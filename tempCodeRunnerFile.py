f = open("01.txt", "r")
file_content = f.read().splitlines()

max = []
sum = 0
for i in file_content:
    if i == '':
        max.append(sum)
       
        sum = 0
    else:
        sum = sum + int(i)
max.sort()    
print("input 1:", max[len(max)-1])
print("input 2:", max[len(max)-1] + max[len(max)-2] + max[len(max)-3])
