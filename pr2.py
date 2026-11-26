student = [(19, 172, 94, "Анатолий"), (18, 181, 69, "Бронислав"), (19, 164, 128, "Вавилен"), (18, 175, 67, "Геннадий")]
ans =[]
for x in student:
    m = x[2]/(x[1])**2
    a = [x[3], m]
    ans.append(a)
ans.sort(key= lambda x:x[1])
print(", ".join([i[0] for i in ans]))