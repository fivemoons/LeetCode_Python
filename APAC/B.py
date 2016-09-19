fin = open('./B-large.in.txt', 'r')
fout = open('./B-large.out.txt', 'w')
T = int(fin.readline())
for i in range(T):
    R, C, K = map(int, fin.readline().strip().split(' '))
    m = []
    ans = []
    out = 0
    for r in range(R):
        m.append([])
        ans.append([])
        for c in range(C):
            m[r].append(0)
            ans[r].append(0)
    for k in range(K):
        Ri, Ci = map(int, fin.readline().strip().split(' '))
        m[Ri][Ci] = 1
    for r in range(R):
        for c in range(C):
            if m[r][c] == 1:
                continue
            shang = ans[r-1][c] if r > 0 else 0
            zuo = ans[r][c-1] if c > 0 else 0
            zuoshang = ans[r-1][c-1] if r > 0 and c > 0 else 0
            ans[r][c] = min(zuoshang, min(shang, zuo)) + 1
            out += ans[r][c]
    print >> fout, 'Case #%d: %s' % (i + 1, out)
fin.close()
fout.close()
