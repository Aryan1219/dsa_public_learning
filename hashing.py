
# hasharr = [0]*16
# for i in arr:
#     hasharr[i] += 1
# print(hasharr)



# arr = [*'ARYAN']
# hasharr = [0]*26
# for i in arr:
#     hasharr[ord(i) - 65] += 1
# print(hasharr[ord('A')])
# print(chr(97))
# print(hasharr)
# print(sorted(arr))
# print(len(arr))
# print(sum(hasharr))
from collections import defaultdict
from sortedcontainers import SortedDict
# from collections import OrderedDict
arr = [1,6,2,3,1,5,4,5,5,5,5,5,2]

spp = SortedDict()
mpp = defaultdict(int)
for i in arr:
    if i in spp:
        spp[i] += 1
    else:
        spp[i] == 1
print(sorted(arr))

print(spp)