import sys
import os
from collections import deque

root = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(root + '\\testcase\\input.txt', 'r')
_answer_que = deque(open(root + '\\testcase\\output.txt', 'r').readlines())

def swea_tc(_answer_yours):
    _answer = _answer_que[0].strip()
    
    if _answer == _answer_yours:
        print(f'{_answer_yours} -> O')
    else:
        print(f'{_answer_yours} -> X, answer: {_answer}')
        
    _answer_que.popleft()