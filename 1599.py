import sys
input = sys.stdin.readline


minKey = {'a':'a', 'b':'b', 'k':'c', 'd':'d', 'e':'e', 'g':'f', 'h':'g', 'i':'h', 'l':'i', 'm':'j', 'n':'k', 'ng':'l', 'o':'m', 'p':'n', 'r':'o', 's':'p', 't':'q', 'u':'r', 'w':'s', 'y':'t'}

testCase = int(input())
minDict = dict()

for _ in range(testCase):
    minDict[input().rstrip()] = ''
    
for eng in minDict.keys():
    tmpKey = eng

    while len(eng):
        if len(eng) > 1:
            if eng[:2] == 'ng':
                minDict[tmpKey] += minKey[eng[:2]]
                eng = eng[2:]
            else:
                minDict[tmpKey] += minKey[eng[:1]]
                eng = eng[1:]
        
        else:
            minDict[tmpKey] += minKey[eng[0]]
            break

for ms in sorted(minDict, key=lambda x:minDict[x]):
    print(ms)
    
    