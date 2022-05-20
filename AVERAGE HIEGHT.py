student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
th=sum(student_heights)
tn=len(student_heights)
ah=th/tn
print(round(ah))


#th=0
#tn=0
#for n in student_heights:
#  th+=n
#  tn+=1
#ah=round(th/tn)
#print(ah)