encoded = [65, 66, 65, 128, 128, 129, 131, 134, 130, 129, 66, 138, 139, 138]
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = str(input())
#
#     encoded.append(ele)
decode = []
dectionaryindex = []
dectionaryval = []
decode.append(chr(encoded[0]))
i = 1
l = 0
while i < len(encoded):
    dectionaryindex.append(l + 128)
    l += 1
    if encoded[i] <= 127:
        decode.append(chr(encoded[i]))
        dectionaryval.append(decode[i-1] + decode[i])
    elif encoded[i] > 127:
        found = dectionaryindex.index(encoded[i])
        dectionaryval.append(decode[i - 1]+decode[i - 1][0])
        decode.append(dectionaryval[found])
    i += 1

for x in decode:
    print(x, end="")