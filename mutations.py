def mutate_string(string, position, character):
    st=list(string)
    st[position]=c
    st=''.join(st)
    return st

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new