#nums = list(map(int, input().split(", ")))
#t = 0

#for i in nums:
  #  t += i
#print(t)
# Program: Input a list of integers and print their sum

nums = list(map(int, input("Nhập danh sách số nguyên (cách nhau bởi dấu cách): ").split()))

total = sum(nums)

print("Tổng các số trong danh sách là:", total)
