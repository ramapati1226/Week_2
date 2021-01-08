def lexSmallest(a, n): 
    a.sort(reverse=True)
    answer = ""
    for i in range(n):
        answer += a[i]
    return answer
if __name__ == "__main__":
    a=input("enter first number :")
    b=input("enter second number :")
    c=input("enter third number :")
    d = [a, b, c]
    n = len(d)
    print(lexSmallest(d, n))

