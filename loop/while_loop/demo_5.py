#skip those number which are divisible by 3 & 5...

i=1
while i<=100:
    if(i%3==0 or i%5==0):
        i+=1
    else:
        print(i)
        i=i+1


'''
output :
1
2
4
7
8
11
13
14
16
17
19
22
23
26
28
29
31
32
34
37
38
41
43
44
46
47
49
52
53
56
58
59
61
62
64
67
68
71
73
74
76
77
79
82
83
86
88
89
91
92
94
97
98
'''

