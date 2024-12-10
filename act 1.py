def checksorted(a):
    length = len(a)

    if length == 0 or length == 1:
        return True
    return a[0] <= a[1] and checksorted(a[1:])

a = [1,2,3,4,5,7,9]

if checksorted(a):
    while True:
     print("Yes")
else:
    print("No")