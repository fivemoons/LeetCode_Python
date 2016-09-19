fin = open('./C-small-attempt0.in.txt', 'r')
fout = open('./C-small-attempt0.out.txt', 'w')
T = int(fin.readline())
for ii in range(T):
    m = {}
    N = int(fin.readline().strip())
    for n in range(N):
        key, value = fin.readline().strip().split('=')
        value = value.split('(')[1][0:-1].split(',')
        m[key] = set(value) if value[0] != '' else set()
    End = False
    while not End:
        End = True
        for key in m.keys():
            if len(m[key]) == 0:
                End = False
                for key2 in m.keys():
                    if key in m[key2] and key != key2:
                        m[key2].remove(key)
                del m[key]
    ans = 'GOOD' if len(m) == 0 else 'BAD'

    print >> fout, 'Case #%d: %s' % (ii + 1, ans)
fin.close()
fout.close()
