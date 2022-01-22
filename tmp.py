# my_package의 폴더의 위치는 현재 작업하고있는 파일 위치와 동일해야함
# SWEA폴더 안에서 .py를 만들어 공부할 경우 SWEA 폴더안에 my_package 폴더가 존재해야함
import sys
import os

# my_package 폴더의 절대경로(root_path) 복사
# > 의문점: 해당 절대경로는 C:\dir1\dir2\ 방식으로 되어있음
# > window환경에선 \ 를 통한 경로는 이스케이프코드(\t)로 인식되지 않을까 걱정
_root = os.path.dirname(os.path.realpath(__file__))

# `input 케이스 자동 불러오기 기능`
# root_path를 통해 testcase에 속한 input.txt 오픈
# 해당 과정을 통해 input.txt의 testcase를 한줄씩 읽어드림
# 따라서 터미널창에 testcase를 수동으로 복붙할 필요가 없음
sys.stdin = open(_root + '\\testcase\\input.txt', 'r')

# `나의 출력과 정답 출력 비교`
# root_path를 통해 testcase에 속한 output.txt 오픈
# .readlines()를 통해 ouput.txt의 모든 라인을 리스트로 불러옴
# ex) ['#1 13\n', '#2 32\n', '#3 54\n', '#4 25\n']
_answer_list = open(_root + '\\testcase\\output.txt', 'r').readlines()

# 기존 print() 출력을 swea_tc() 함수로 변경하면 됨
# print(f'#{t} {answer})' -> swea_tc(f'#{t} {answer}')
def swea_tc(_answer_yours):
    
    # _answer_list[0]의 첫번째 값을 불러와 앞뒤에 존재하는 띄어쓰기(\n) 삭제
    _answer = _answer_list[0].strip()
    
    # 정답을 판단하여 출력, 틀린경우 실제 정답값 출력
    if _answer == _answer_yours:
        print(f'{_answer_yours} -> O')
    else:
        print(f'{_answer_yours} -> X, answer: {_answer}')
    
    # 비교가 완료된 answer_list의 값(첫번째줄) 은 삭제
    _answer_list.pop(0)