father_age=int(input("enter your father age"))
mother_age=int(input("enyter your mother age"))
your_age=int(input("enter your age"))
total_age=father_age+mother_age+your_age
print(total_age)
diff_father_your_age=father_age-your_age
double_your_age=(your_age)*2
print(double_your_age)
sub_mother_age=mother_age-double_your_age
print(sub_mother_age)
if(your_age%2==0):
    print("your age is divisible by 2")
else:
    print("not divisible by 2")
print("end")
if(mother_age%3==0):
    print("mother is divisible by 3")
else:
    print("mother age is not divisible by 3")
print("end")
father_age_rem=father_age//4.5
print(father_age_rem)