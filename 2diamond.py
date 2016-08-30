num = int(input())
n = int((num - 1) / 2)
for l in range(n+1):
    space = ' ' * (n - l)
    nums = [str(i) for i in range(n-l+1, n-l+1+3)]
    left = space + ''.join(nums) + ' ' * l
    right = left[::-1].rstrip()
    middle = (str(num) if l == 0 else ' ')
    print(left+middle+right)
for l in range(n, -1, -1):
    space = ' ' * (n - l)
    nums = [str(i) for i in range(n-l+1, n-l+1+3)]
    left = space + ''.join(nums) + ' ' * l
    right = left[::-1].rstrip()
    middle = (str(num) if l == 0 else ' ')
    print(left+middle+right)
