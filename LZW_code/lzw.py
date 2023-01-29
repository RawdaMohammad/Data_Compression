#data = "ABAABABBAABAABAAAABABBBBBBBB"
data = input("Enter data to compress: ")
tags = []
dectionaryindex = []
dectionaryval = []
index = 0
i = 0
found = -1
while index < len(data):
    if index == 0:
        dectionaryval.append(data[0:2])
        dectionaryindex.append(i + 128)
        tags.append(ord(data[index]))
    else:
        NumOfStep = 2
        c = 0
        while index < len(data):
            f = found
            if (data[index:index + NumOfStep]) in dectionaryval:
                found = dectionaryval.index((data[index:index + NumOfStep]))
                c += 1
                f = found
            else:
                found = -1
            if found == -1 or (index + NumOfStep) >= len(data):
                if (index + NumOfStep) < len(data):
                    dectionaryval.append(data[index:(index + NumOfStep)])
                    dectionaryindex.append(i + 128)

                if NumOfStep == 2 and found == -1:
                    tags.append(ord(data[index]))
                else:
                    tags.append(dectionaryindex[f])
                index += c
                break
            NumOfStep += 1

    index += 1
    i += 1

print(tags)
