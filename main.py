import string

inp = open('input.txt', 'r')
s = [x for x in string.ascii_lowercase]
delta= 365**5 + 52**10 + 7**20 + 457981573849226022
ap = []

for x in inp.readlines():
    ap.append([int(a) for a in x.strip('\n').split(' ')])

pos = [-1]*len(ap)
pos[0] = 0
heads = ap[0]
ap[0] = [heads[0]]
mpos = [len(x)-1 for x in ap]

def add_pos(p, arr):
    for x in range(len(p)-1, -1, -1):
        if p[x-1] == -1:
            continue
        elif p[x] + 1 > mpos[x]:
            p[x] = -1
            continue
        else:
            p[x]+=1
            break
    return p   

def get_num(p, arr):
    num = 1
    for i in range(len(p)):
        if p[i] == -1:
            continue
        else:
            num*=arr[i][p[i]]
    return num
def get_seq(p, arr):
    seq = []
    seq.append(get_num(p, arr))         
    while p != mpos:
        p = add_pos(p, arr)
        seq.append(get_num(p, arr))
    return seq

def swap_pairs(arr:list):
    for i in range(0, len(arr), 2):
        if i == len(arr) - 1:
            break
        a = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = a
    return [x for x in reversed(arr)]


def seq_to_str(arr:list):
    return ''.join([s[x%26] for x in arr])

def bitwise(s:str):
    bs = ''.join(format(ord(x), 'b') for x in s)
    a = int(bs[0:16], base=2)
    b = int(bs[-16:], base=2)
    return a&b
def part2group(n:int):
    n = [x for x in str(n)]
    a = []
    for x in range(0, len(n), 2):
        if x == len(n) - 1:
            a.append(int(n[x]))
            break
        a.append(int(n[x]+n[x+1]))
    return a

def get_numer(n:int):
    a = part2group(n)
    return str(sum(a))

if __name__=='__main__':
    seq2=[]
    for x in heads:
        ap[0] = [x]
        pos = [-1]*len(ap)
        pos[0] = 0
        mpos = [len(x)-1 for x in ap]
        seq = get_seq(pos, ap)
        seq = swap_pairs(seq)
        num = bitwise(seq_to_str(seq))
        seq2.append(get_numer(num))
    key = int(''.join(seq2))
    key = (key - delta)
    key = part2group(key)
    key = seq_to_str(key)
    print(key)
    