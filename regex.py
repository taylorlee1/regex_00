#! /usr/bin/env python3

tabInc=2

def isMatch(p, s):
    return _isMatch(p,0,s,0,0)

def _isMatch(p,pidx,s,sidx,ts):
    print("%sisMatch %s" % (' ' * ts, (p[pidx:],s[sidx:]),))
    if pidx >= len(p) and sidx >= len(s):
        return True
    elif pidx >= len(p):
        return False
    elif sidx >= len(s)  and pidx == len(p) - 1 and p[pidx] == '*':
        return True
    elif sidx >= len(s):
        return False

    if p[pidx] == s[sidx] or p[pidx] == '.':
        return _isMatch(p,pidx+1,s,sidx+1, ts+tabInc)

    elif p[pidx] == '*':
        res0 = _isMatch(p,pidx,s,sidx+1, ts+tabInc)
        res1 = _isMatch(p,pidx+1,s,sidx-1, ts+tabInc) if not res0 else False

        return res0 | res1
    else:
        return False

    return False

if __name__ == "__main__":
    print(isMatch('aa.*aa', 'aabcaa'))
    print(isMatch('aa.*aa', 'aaa'))
    print(isMatch('aa.*', 'aaa'))
    print(isMatch('a.*aa', 'aaa'))
    print(isMatch('.*', 'aa'))
    print(isMatch('ba*ba*', 'baaba'))
