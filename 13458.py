import sys
input = sys.stdin.readline


testCase = int(input())
tester = list(map(int, input().split()))
mainObserver, subObserver = map(int, input().split())

result = testCase
for i in tester:
    if i - mainObserver > 0:
        if (i - mainObserver) % subObserver > 0:
            result += (i - mainObserver) // subObserver + 1
        else:
            result += (i - mainObserver) // subObserver
    
print(result)