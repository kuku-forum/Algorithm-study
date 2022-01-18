import sys

N = int(sys.stdin.readline())
members = []
for i in range(N):
    member = sys.stdin.readline().split(' ')
    members.append((i, int(member[0]), member[1].rstrip()))

members.sort(key=lambda member: (member[1], member[0]))


for member in members:
    print('{} {}'.format(member[1], member[2]))

    