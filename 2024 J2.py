
dusa_size = int(input().strip())

import sys

for line in sys.stdin:
    yobi = int(line.strip())
    
    if yobi < dusa_size:
        dusa_size += yobi  
    else:
        break  
print(dusa_size)
