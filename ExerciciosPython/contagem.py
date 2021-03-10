
from time import sleep
for c in range(11,0,-1):
    c -= 1
    print(c,end='')
    sleep(0.3)
    if c > 0:
        print('...',end='')
    elif c == 0:
        print('Acabou')
    sleep(0.5)
