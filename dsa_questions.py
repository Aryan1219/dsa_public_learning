import math


def evenlyDivides(n: int):
    count = 0
    act_num = n
    # Extracting digits from a number
    # It is done in reverse order

    # Until the int part is 0 , we continue extracting digits
    while n != 0:
        d = n % 10
        # If the dividing num is 0,  update n and skip it
        if d == 0:
            n //= 10
            continue
        if act_num % d == 0:
            count += 1
        # Updating n
        n //= 10
    return count

    # There is one more approach
    # Using logarithmic functions
    # count_of_digits = int(math.log10(n) + 1) (if the division happens by 10  then log base 10 ,if 5 then log base 5, and so on ,)
    # return count_of_digits


def reverse_num(n: int):
    rev = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n != 0:
        d = n % 10
        # Multiplying the last added digit by 10 to shift it left and then adding the next digit
        rev = rev * 10 + d
        n //= 10
    return rev * sign if -(2**31) < rev < (2**31) - 1 else 0

    # if n ==0:
    #     return n
    # elif n < 0:
    #     negative = True
    #     n*= -1
    # else:
    #     negative = False
    # rev = 0
    # exp = int(math.log10(n))

    # while n != 0:
    #     d = n%10
    #     rev+= d *(10**exp)
    #     exp -= 1
    #     n//=10
    # if rev > (2**31)-1 or rev < -1*(2**31):
    #     return 0
    # return rev*-1 if negative else rev


def isPalindrome(x: int) -> bool:
    act_num = x
    if x < 0:
        return False
    sum = 0
    while x != 0:
        d = x % 10
        sum = (sum * 10) + d
        x //= 10
    return True if sum == act_num else False


def isArmStrong(n: int) -> bool:
    act_num = n
    length = int(math.log10(n) + 1)
    sum = 0
    while n != 0:
        d = n % 10
        sum += d * length
        n //= 10
    if sum == act_num:
        return True
    else:
        return False


def sumOfDivisors(n: int) -> int:
    total = 0
    testes = {}
    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i) + 1)):
            if i % j == 0:
                total += j
                if i // j != j:
                    total += i // j
    return total


def checkForPrime(n: int) -> bool:
    if n < 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def calculate(n: list[int]) -> int:
    area = 0
    start = 0
    end = len(n) - 1
    while start < end:
        x = min(n[start], n[end])
        dist = end - start
        area = max(area, dist * x)
        if n[start] < n[end]:
            start += 1
        else:
            end -= 1
    return area


def longestConsecutive(nums: list[int]) -> int:
    ans = 0
    seen = set(nums)

    for num in nums:
        if num - 1 in seen:
            continue
        length = 0
        while num in seen:
            num += 1
            length += 1
    ans = max(length, ans)
    return ans


def cal_gcd(n, m):
    # for i in range(min(n,m),0,-1):
    #     if n%i == 0 and m%i==0:
    #         gcd = i
    #         break
    # return gcd
    mini = min(n, m)
    maxi = max(n, m)
    if mini != 0:
        return cal_gcd(maxi % mini, mini)
    return maxi


def lcmAndGcd(a, b):
    # code here
    def gcd(a, b):

        mini = min(a, b)
        maxi = max(a, b)

        if mini != 0:
            return gcd(maxi % mini, mini)
        return max(mini, maxi)

    gcd = gcd(a, b)
    lcm = a * b // gcd
    return [lcm, gcd]


def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]


def selection_sort(arr: list):
    for current_index in range(len(arr) - 1):
        next_min = min(arr[current_index:])
        min_index = arr[current_index:].index(next_min) + current_index
        swap(arr, min_index, current_index)


def bubbleSort(arr: list[int]):
    for i in range(len(arr) - 1, 0, -1):
        did_swap = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                did_swap += 1
        if did_swap  == 0:
            break
        print('runs')

def insertion_sort(arr : list[int]):
    for i in range(len(arr)):
        j = i
        while(j > 0 and arr[j-1] > arr[j]):
            swap(arr,j-1,j)
            j -= 1


if __name__ == "__main__":
    # with open("/home/aryan/Desktop/DSA_prep/inputs.txt", "r") as file:
    #     inputs = file.readlines()

    # for value in inputs:
    #     n = int(value.strip())
    #     print(sumOfDivisors(n))
    inputs = [-1,6,-2,0,98745,2,3,3]

    insertion_sort(inputs)
    print(inputs)
