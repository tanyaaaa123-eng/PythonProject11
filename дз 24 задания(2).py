#16388
from re import finditer
with open(r"task-24\24_16388.txt") as f:
    data = f.readline()
pattern = r"(LM|M)N?(KLMN)+(KLM|KL|K)?"
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key = len)))
# ответ 182
#17685
from re import finditer
with open(r"task-24\24_17685.txt") as f:
    data = f.readline()
number = r"([1-9][0-9]+)|0)"
zero = rf"({number}\*)*0(\*{number})*"
pattern = rf"({zero}\+)*{zero}"
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len)))
#17641
from re import finditer
with open(r"task-24\24_17641.txt") as f:
    data = f.readline()
number = r"([1-9][0-9]+)|0"
pattern = rf"({number}[+*])+{number}"
matches = [match.group() for match in finditer(pattern,data)]
#for i in matches:
#    a=0
#    i1=i.split("+")
#    for x in i1:
 #       if x!=0:
#            a+=1
print(len(max(matches,key=len)))

