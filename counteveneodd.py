def calculate_sum(num):
    odd=0
    even=0
    for i in range(len(num)):
        if i%2==0:
            even+=num[i]
        else:
            odd+=num[i]
    print("sum of even index positions numbers ",even)
    print("sum of odd index positions numbers ",odd)
num=[1,2,3,4,5,6,7,8,9]
calculate_sum(num)
