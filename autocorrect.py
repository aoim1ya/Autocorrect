import math
file = open(r'C:\Users\Admin\Downloads\alphabet.txt', 'r')
keyword = input()
points = -1000
kcach = 1000
word = ''
loaitru = []
n = ''
diemtoida = len(keyword) - 2 + 3 + 2 + len(keyword) * 3
def tinhdiem(a,b):
    global diem
    if len(a) <= len(b):
        lenmin = len(a)
    else:
        lenmin = len(b)
    diem = 0
    diem += -(abs(len(a) - len(b))) 
    for i in range(lenmin):
        if a[i] in b:
            diem += 1
        if a[i] == b[i]:
            if i == 0:
                diem += 3
            if i == 1:
                diem += 2
            if i > 1:
                diem += 1
        if 1 <= i < lenmin - 1:
            if a[i-1] + a[i] + a[i+1] == b[i-1] + b[i] + b[i+1]:
                diem += 1
        if a.count(a[i]) == b.count(a[i]):
            diem += 1

            
        
while n != 'y':
    points = -1000
    kcach = 1000
    word = ''
    file.seek(0)  
    for line in file:
        n = ''
        if line.strip() not in loaitru:
            tinhdiem(line.strip(),keyword)
            if diemtoida - diem < kcach and diem > points:
                points = diem
                kcach = diemtoida - diem
                word = line.strip()
            if diem == diemtoida:
                word = line.strip()
                break
    print(word)    
    n = input('Tu nay co dung khong? (y/n): ')
    if n == 'y':
        break
    if n == 'n':
        loaitru.append(word)
    if word == '':
        print('Khong tim thay tu')
        