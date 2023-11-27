const INF = Number.MAX_SAFE_INTEGER;

function dijkstra(n, m, edges, a, b) {
    const bus = Array.from({ length: n }, () => []);
    
    for (let i = 0; i < m; i++) {
        const [x, y, z] = edges[i];
        bus[x - 1].push([y - 1, z]);
    }

    const que = [];
    que.push([0, a - 1]);
    
    const check = Array(n).fill(INF);
    check[a - 1] = 0;

    while (que.length > 0) {
        const [count, city] = que.shift();
        
        if (city === b - 1) {
            break;
        }

        for (const [c, cnt] of bus[city]) {
            if (count + cnt < check[c]) {
                check[c] = count + cnt;
                que.push([count + cnt, c]);
            }
        }
    }

    return check[b - 1];
}

// Example usage
const n = 3;
const m = 3;
const edges = [
    [1, 2, 1],
    [2, 3, 2],
    [1, 3, 5]
];
const a = 1;
const b = 3;

const result = dijkstra(n, m, edges, a, b);
console.log(result);
