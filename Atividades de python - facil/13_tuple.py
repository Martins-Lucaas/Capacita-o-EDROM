'''def main():
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

main()
'''

def main():
    n = int(input())
    line = input()
    tupla = tuple(map(int, line.split()))
    print(hash(tupla))

main()