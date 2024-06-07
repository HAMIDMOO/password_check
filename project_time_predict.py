import random



First_phase_1= int(input("in best situation "))
First_phase_2= int(input("in worst situation "))

second_phase_1= int(input("in best situation "))
second_phase_2= int(input("in worst situation "))


third_phase_1= int(input("in best situation "))
third_phase_2= int(input("in worst situation "))

in_total_1=  int(input("in best situation "))
in_total_2=  int(input("in worst situation "))

F_sum=0
S_sum=0
T_sum=0
total_sum=0
for i in range (0, 100):
    F_sum+=random.uniform(First_phase_1, First_phase_2)

    S_sum+=random.uniform(second_phase_1, second_phase_2)

    T_sum+= random.uniform(third_phase_1, third_phase_2)

    total_sum+= random.uniform(in_total_1, in_total_2)
    

avg_1= F_sum/100
avg_2= S_sum/100
avg_3= T_sum/100
avg_tot= total_sum/100

total= avg_1+ avg_2+ avg_3+ avg_tot

print(round(random.gauss(avg_1, 1)))
print(round(random.gauss(avg_2, 1)))
print(round(random.gauss(avg_3, 1)))
print(round(random.gauss(avg_tot, 1)))

