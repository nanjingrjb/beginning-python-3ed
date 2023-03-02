# find_sender.py
        
import fileinput, re
pat = re.compile('From (.*) <.*?>$')
for line in fileinput.input():
    print(line)
    m = pat.match(line)
    if m: 
        print(m.group(1))
    else:
        print('no found')

