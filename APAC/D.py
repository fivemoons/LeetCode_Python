fin = open('./D-small-attempt0.in.txt', 'r')
fout = open('./D-small-attempt0.out.txt', 'w')
T = int(fin.readline())
for i in range(T):
    N = int(fin.readline())
    flag = False
    ans = False
    maxa, maxd= 0, 0
    alist, dlist = [], []
    for n in range(N):
        Ak, Dk = map(int, fin.readline().strip().split(' '))
        alist.append(Ak)
        dlist.append(Dk)
        maxa = max(maxa, Ak)
        maxd = max(maxd, Dk)
    for ii in range(len(alist)):
        if not flag:
            if alist[ii] == maxa and dlist[ii] == maxd:
                print >> fout, 'Case #%d: %s' % (i + 1, 'YES')
                flag = True
    for ii in range(len(alist)):
        if not flag:
            if alist[ii] < maxa and dlist[ii] < maxd:
                print >> fout, 'Case #%d: %s' % (i + 1, 'YES')
                flag = True
    if not flag:
        print >> fout, 'Case #%d: %s' % (i + 1, 'NO')


fin.close()
fout.close()
