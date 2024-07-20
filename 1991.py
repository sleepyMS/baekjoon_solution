def preorder(graph, preord, current='A'):
    if current == '.':
        return 
    preord.append(current)
    preorder(graph, preord, graph[current]['L'])
    preorder(graph, preord, graph[current]['R'])

def inorder(graph, inord, current='A'):
    if current == '.':
        return 
    inorder(graph, inord, graph[current]['L'])
    inord.append(current)
    inorder(graph, inord, graph[current]['R'])

def postorder(graph, postord, current='A'):
    if current == '.':
        return 
    postorder(graph, postord, graph[current]['L'])
    postorder(graph, postord, graph[current]['R'])
    postord.append(current)


if __name__ == "__main__":
    n = int(input())
    node = [list(input().rstrip().split()) for _ in range(n)]
    graph = {}
    for i, j, k in node:
        graph[i] = {'L': j, 'R': k}
    
    preord = []
    inord = []
    postord = []
    
    preorder(graph, preord)
    inorder(graph, inord)
    postorder(graph, postord)
    
    print(''.join(preord))
    print(''.join(inord))
    print(''.join(postord))