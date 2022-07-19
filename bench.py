from subprocess import check_output 
import sys
 
def main():
    for l in sys.stdin.readlines():
        m, n, k = [v.strip() for v in l.split(',')]
        res = check_output([sys.argv[1], m, n, k])
        l2, l3 = res.decode().split('\n')[1:3]
 
        gflop = float(l2.split()[0])
        gib = float(l3.split()[0])
 
        print(m, n, k, gflop, gib, sep=',')
 
if __name__ == '__main__':
    main()
 
