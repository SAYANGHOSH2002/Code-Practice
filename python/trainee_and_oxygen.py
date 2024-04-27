# Selection of MPCS exams include a fitness test which is conducted on ground. There will be a batch of 3 trainees, appearing for running test in track for 3 rounds. You need to record their oxygen level after every round. After trainee are finished with all rounds, calculate for each trainee his average oxygen level over the 3 rounds and select one with highest oxygen level as the most fit trainee. If more than one trainee attains the same highest average level, they all need to be selected.

# Display the most fit trainee (or trainees) and the highest average oxygen level.

# Note:

# The oxygen value entered should not be accepted if it is not in the range between 1 and 100.
# If the calculated maximum average oxygen value of trainees is below 70 then declare the trainees as unfit with meaningful message as “All trainees are unfit.
# Average Oxygen Values should be rounded.
# Example 1:
# INPUT VALUES
# 95
# 92
# 95
# 92
# 90
# 92
# 90
# 92
# 90

# OUTPUT VALUES
# Trainee Number : 1
# Trainee Number : 3

# Note:
# Input should be 9 integer values representing oxygen levels entered in order as

# Round 1

# Oxygen value of trainee 1
# Oxygen value of trainee 2
# Oxygen value of trainee 3
# Round 2

# Oxygen value of trainee 1
# Oxygen value of trainee 2
# Oxygen value of trainee 3
# Round 3

# Oxygen value of trainee 1
# Oxygen value of trainee 2
# Oxygen value of trainee 3
# Output must be in given format as in above example. For any wrong input final output should display “INVALID INPUT”

t1 = []
t2 = []
t3 = []
t_avg = []

for i in range(3):
    t1.append(int(input()))
    t2.append(int(input()))
    t3.append(int(input()))

avg = [0, 0, 0]
for i in range(3):
    avg[0] += t1[i]
    avg[1] += t2[i]
    avg[2] += t3[i]

t_avg.append(avg[0] // 3)
t_avg.append(avg[1] // 3)
t_avg.append(avg[2] // 3)

max_num = max(t_avg)

if max_num <= 70:
    print('All trainees are unfit')

print(t_avg)

for i in range(3):
    if t_avg[i] == max_num:
        print('Trainee number:', i + 1)