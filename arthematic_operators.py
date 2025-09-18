wallet=1500
spend_on_food=300
transport=250
shoping_cost=400
income_frelancer=500
t_money=income_frelancer + wallet
t_money_spend=spend_on_food + transport + shoping_cost
final_balance=(wallet + income_frelancer) - (spend_on_food + transport + shoping_cost)
total_percentage_spent=(t_money / t_money_spend) *100
print("total money : ",t_money)
print("total money spend : ", t_money_spend)
print("final balance : ", final_balance)
print("total percentage spend : ", total_percentage_spent )






score=0
level1=score+10
bonus=level1+5
level2=bonus-3
booster=level2*2
print("starting score = ", score)
print("level 1 score = ", level1)
print("bonous score and level one score = ", bonus)
print("level 2 score = ", level2)
print(" boster score = ", booster)


student_marks=int(input("enter marks"))
if student_marks > 60:
    print("you are qualifed set conformation will send to your mail")

elif student_marks == 60:
    print("you are selection process is on going if you selected we will inform")

else:
    print(" your not qualifed")


laptop_cost=50000
user=int(input("enter money you have"))
parents=input("Are your parents helping? (yes/no): ")
parents_helping= parents=="yes"
parents.lower()

if user < laptop_cost and parents == parents_helping:
    print("hoo you can by the laptop")
    
elif user > laptop_cost:
    print("you can by your laptop own")
elif user < laptop_cost or parents != parents_helping:
    print("you are earning money on your own")
    
else:
    print(None)


patationt=int(input("enter your age   :"))
previous_checkup=input("Did you have a check-up last year? (yes/no)")
previous_checkup.lower()
if patationt < 40:
    print("your not eligble")
    
elif patationt > 40 and previous_checkup=="no":
    print("you are eligble to free  health checkup")
elif patationt > 40 and previous_checkup=="yes":
    print("you are not eligble for free health checkup")
    
else:
    print(None)