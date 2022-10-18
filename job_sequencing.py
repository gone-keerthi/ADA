# program to implement Job sequencing with deadlines
# Function to schedule the jobs
def jobschedule(array, t):
    m = len(array)

    # Sort all jobs accordingly
    for j in range(m):
        for q in range(m - 1 - j):
            if array[q][2] < array[q + 1][2]:
                array[q], array[q + 1] = array[q + 1], array[q]
    res = [False] * t

    # To store result
    job = ['-1'] * t
    for q in range(len(array)):
        # Find a free slot
        for q in range(min(t-1,array[q][1]-1),-1,-1):
            if res[q] is False:
                res[q] = True
                job[q] = array[q][0],array[q][1] #to display job and it's corresponding profit
                break
    # print
    print(job)
array = [['j1', 200, 2],
         ['j2', 100, 1],
         ['j3', 150, 1],
         ['j4', 100, 2],
         ['j5', 250, 1]]
#to print the required data 
for i in  array:
    print(i)
print("Maximum profit sequence of jobs is: ")
jobschedule(array, 3)