# SWEA PS 문제 테스트케이스 활용하기

> SWEA에서 PS를 진행할때 input.txt, ouput.txt 활용이 불편하였습니다.
> 이를 해결하고자 프로그램을 구상해보았고 도움이 되길 바랍니다.



## 1. 겪었던 문제점

### 1.1반복 디버깅 작업이 상당히 고됨

> 가장 중요한 이유였습니다.
> PS 특성상 여러번 디버깅을 진행 해야하는데 SWEA는 여러 불편함이 존재했습니다.
>
> SWEA에서 제공하는 에디터의 UI가 불편하여 사용이 불편하니, 
> `VScode`나 `Pycharm` 같은 IDE를 통해 디버깅 하는 경우가 대부분이었습니다.
>
> 그럴때마다 input 케이스를 드래그해서 복사하고 붙여넣는 과정이 너무 불편했습니다.
> (특히, 노트북으로 공부할 경우 작은 화면이라 더더욱...)
> (백준의 경우 복사하기 버튼이 존재하죠...)
>
> 아래엔 기타 문제점을 더 설명해 보겠습니다.

### 	1. 2 고용량  케이스로 인해 디버깅이 안되는 경우

> SWEA 에디터에서 Run으로 정답 케이스를 확인하고 제출하고자 하는데, 
> 아래와 같이 용량 문제로 실행이 안되는 경우가 존재하였습니다.

<img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122181633546-16428448259491.png" alt="image-20220122181633546" style="zoom:50%;" />

### 1.3  테스트케이스가 생략된 경우

> 디버깅을 진행할때 입력란이 길어 ... 으로 표시된 문제가 있습니다.
> 이럴경우 input.txt 파일을 다운받거나, 본인의 판단으로 임의로 케이스를 제작해서 붙여넣는 불상사가 발생하였습니다.

<img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122182207017.png" alt="image-20220122182207017" style="zoom:50%;" />

### 1.4 정답인지 아닌지 콘솔에서 확인이 힘든 경우

> 혹여나 1.2에서 언급한 input.txt를 다운받아 터미널창에 복붙하더라도,
> 너무 많은 입력 란으로 인해 정답확인이 쉽지 않습니다.
> 예) #6 10008을 확인하더라도 다른 케이스의 정답을 확인하려면 열심히 드래그해야합니다..ㅜㅠ

<img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122182949931.png" alt="image-20220122182949931" style="zoom:50%;" />



## 해결방안

> **크게 해결하고 싶은 부분은 다음 3가지이며 설명드리겠습니다.**
>
> 1. input.txt를 저장하여 복붙없이 바로 디버깅 되도록 할것
>
> 2. 라이브러리화 하여 import하여 편하게 함수로 사용할 수 있을 것
>
>    ``` python
>    from my_package.hjtc import swea_tc
>    '''
>    your code
>    '''
>    swea_tc(f'#{t} {answer}')
>    ```
>
> 3. 정답유무를 체크해 줄 것
>
>    ```python
>    #1 13 -> O
>    #2 32 -> O
>    #3 54 -> O
>    #4 25 -> O
>    #5 87 -> O
>    #6 14 -> O
>    #7 39 -> X, answer: #7 40
>    #8 26 -> O
>    #9 13 -> X, answer: #9 12
>    #10 29 -> X, answer: #10 55
>    ```

```python
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
def swea_tc(_answer_print):
    
    # _answer_list[0]의 첫번째 값을 불러와 앞뒤에 존재하는 띄어쓰기(\n) 삭제
    _answer = _answer_list[0].strip()
    
    # 정답을 판단하여 출력, 틀린경우 실제 정답값 출력
    if _answer == _answer_print:
        print(f'{_answer_print} -> O')
    else:
        print(f'{_answer_print} -> X, answer: {_answer}')
    
    # 비교가 완료된 answer_list의 값(첫번째줄) 은 삭제
    _answer_list.pop(0)
```

