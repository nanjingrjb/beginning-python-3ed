import fileinput, re
#查找类似于python jython的字符串
pstr=r'.ython'
pat = re.compile(pstr)
linex=0
for line in fileinput.input():
    linex+=1
    t=re.findall(pstr,line)
    if t:
        if len(t) >1:
            m=pat.match(line)
            print(m.group())
        #print(linex,t)
'''
    m = pat.match(line)
    if m:
        print(m.group(0))
'''
