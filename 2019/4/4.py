

def test_number(n):
    digits=[int(x) for x in list(str(n))]
    has_same=False
    old=0
    for a in digits:
        if a<old:
            return False
        if digits.count(a)==2:
            has_same=True
        old=a
    if has_same:
        return True
    else:
        return False



n=0;

for i in range(264793,803935):
    if test_number(i):
        print i
        n+=1

print n
