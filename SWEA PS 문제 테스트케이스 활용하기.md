

# SWEA PS 문제 테스트케이스 활용하기

> SWEA에서 PS를 진행할때 input.txt, ouput.txt 활용이 불편하였습니다.
> 이를 해결하고자 프로그램을 구상해보았고 도움이 되길 바랍니다.



## 1. 겪었던 문제점

### 1.1반복 디버깅 작업이 상당히 고됨

> 가장 중요한 이유였습니다.
> PS 특성상 여러번 디버깅을 진행 해야하는데 SWEA는 여러 불편함이 존재했습니다.
>
> SWEA에서 제공하는 에디터의 UI가 불편하여 사용이 불편하니,   
>`VScode`나 `Pycharm` 같은 IDE를 통해 디버깅 하는 경우가 대부분이었습니다.
> 
>그럴때마다 input 케이스를 드래그해서 복사하고 붙여넣는 과정이 너무 불편했습니다.  
> (특히, 노트북으로 공부할 경우 작은 화면이라 더더욱...)  
>(백준의 경우 복사하기 버튼이 존재하죠...)
> 
>아래엔 기타 문제점을 더 설명해 보겠습니다.

  <br />

  <br />

  <br />

  <br />

### 	1. 2 고용량  케이스로 인해 디버깅이 안되는 경우

> SWEA 에디터에서 Run으로 정답 케이스를 확인하고 제출하고자 하는데,  
> 아래와 같이 용량 문제로 실행이 안되는 경우가 존재하였습니다.

<img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122181633546-16428448259491.png" alt="image-20220122181633546" width = "50%" height = "50%" />



### 1.3  테스트케이스가 생략된 경우

> 디버깅을 진행할때 입력란이 길어 ... 으로 표시된 문제가 있습니다.  
>이럴경우 input.txt 파일을 다운받거나, 본인의 판단으로 임의로 케이스를 제작해서 붙여넣는 불상사가 발생하였습니다.

<img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122182207017.png" alt="image-20220122182207017" width = "50%" height = "50%" />



### 1.4 정답인지 아닌지 콘솔에서 확인이 힘든 경우

> 혹여나 1.2에서 언급한 input.txt를 다운받아 터미널창에 복붙하더라도,  
>너무 많은 입력 란으로 인해 정답확인이 쉽지 않습니다.
> 
>예) #6 10008을 확인하더라도 다른 케이스의 정답을 확인하려면 열심히 드래그해야합니다..ㅜㅠ

<img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122182949931.png" alt="image-20220122182949931" width = "50%" height = "50%"/>







## 2. 해결방안

**크게 해결하고 싶은 부분은 다음 3가지이며 설명드리겠습니다.**

1. **input.txt를 저장하여 복붙없이 바로 디버깅 되도록 할것**
   - 경로 이슈가 있을 수 있으니, **아래에 추가 설명 참고**

> <img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122190044894.png" alt="image-20220122190044894" width = "30%" height = "30%" />
>
> 
>
> 

2. **라이브러리화 하여 import하여 편하게 함수로 사용할 수 있을 것**

> ``` python
> from my_package.hjtc import swea_tc
> '''
> your code
> '''
> # print('your_answer') 대신 swea_tc('your_answer') 사용
> swea_tc(f'#{t} {answer}')
> ```
>
> ​    

3. **정답 유무를 알려줄것**

> ```python
> --- Debug consol ---
> #1 13 -> O
> #2 32 -> O
> #3 54 -> O
> #4 25 -> O
> #5 87 -> O
> #6 14 -> O
> #7 39 -> X, answer: #7 40 -> 틀릴경우 실제 정답값 표시
> #8 26 -> O
> #9 13 -> X, answer: #9 12
> #10 29 -> X, answer: #10 55
> ```



### 2.1 input.txt를 저장하여 복붙없이 바로 디버깅 되도록 할것

> 우선 각자의 개발 환경이 다르다 보니 `절대경로`, `상대경로` 등으로 인한 `문제가 발생`할 수 있습니다.  
> 따라서 제일 간단한 방법부터, 제가 고안한 방법까지 설명드리겠습니다.    



#### 2.1.1 제일 단순한 방법인 input.txt 파일만 읽기

> 우선 input.txt를 본인이 원하는 위치에 다운 받아줍니다.  
>그다음 PS 문제를 풀때 위에 아래 코드 2줄만 넣어주면 됩니다.
> 
>**root는 절대 경로를 불러오길 추천합니다.**  
> *(폴더나, IDE에서 손쉽게 절대경로 복사가 가능할 것입니다.)**
>
> ```python
>import sys
> # root = 저장된 경로
># ex) C:\\Users\\SWEA\testcae\\.py
> sys.stdin = open(root + 'input.txt', 'r')
> 
> '''
> your code
> '''
> ```

> sys.stdin을 선언하면 input.txt를 읽어와 줍니다.  
>그리고 문제 풀기위해 작성한 `input()` 함수가 input.txt를 한줄씩 읽어서 확인을 진행합니다.
> 
>따라서 위에 언급한 `1.4`의  문제는 해결할 수 있습니다!  
> **하지만 정답유무는 눈으로 직접 대조하여 체크해야합니다.**

  

#### 2.1.2 라이브러리를 통한 input.txt, output.txt 비교하기

> 해당 과정을 진행하기전에 폴더를 만들어줘야합니다.  
>**폴더 및 코드는 나중에 업로드할 예정**
> 
>우선 공부하실때 작업하는 폴더가 있으실 거에요.  
> 저같은 경우는 SWEA란 폴더에서 난이도 별로 D1, D2, D3 폴더를 만들어서 내부에 .py 파일을 제작하여 코딩하고있습니다.
>
> <img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122190044894.png" alt="image-20220122190044894" width = "30%" height = "30%" />

  

이를 정리해서 보면 `SWEA 폴더` → `D1, D2, D3`, `D3` → `my_package` → `testcase` 이렇게 경로가 설정됩니다.

> ``` python
>C:.
> ├─SWEA #
>├─D1
> ├─D2
>└─D3
> └─my_package
>     └─testcase
> ```
>
> **즉 `my_package` 폴더를 작업할 폴더인 `D3` 폴더에 생성해야(넣어줘야)합니다.**  
>만약 `D1` 폴더에서 작업하고 있으면, `my_package` 를 D1에 복사해서 넣어주길 바랍니다.
> 
>혹자는 `SWEA`  폴더에 `my_package`를 설치하면 안되냐고 하실 수 있는데, 경로 설정에 어려움이 있으실까봐 그렇습니다.  
> 경로 설정 핸들링이 가능하시면, 코드를 수정해서 변경하셔도 됩니다.

  

**그다음 `my_package` 내부 `testcase` 폴더에는 `SWEA 문제 페이지`에 존재하는 `input.txt` `output.txt` 를 넣어줍니다.**

> 여기서 여러문제를 풀다가 `input(1).txt` 로 다운받아질 수 있는데, 꼭 **파일명 확인**하시길 바랍니다.
>
> <img src="SWEA PS 문제 테스트케이스 활용하기.assets/image-20220122193905010.png" alt="image-20220122193905010" width = "30%" height = "30%" />
>
> 
>

**그다음 `hjtc.py` `my_package` 폴더 안에 저장합니다**. (파일명 바꿔도 상관없습니다.)

> 코드 내용은 아래와 같습니다.   
>부족한 부분이 많으니 코드내용 읽어보시고 수정하시면 저에게도 알려주세요 :)  
> 
>```python
> # my_package의 폴더의 위치는 현재 작업하고있는 파일 위치와 동일해야함
># SWEA폴더 안에서 .py를 만들어 공부할 경우 SWEA 폴더안에 my_package 폴더가 존재해야함
> import sys
>import os
> 
># my_package 폴더의 절대경로(root_path) 복사
> # > 의문점: 해당 절대경로는 C:\dir1\dir2\ 방식으로 되어있음
># > window환경에선 \ 를 통한 경로는 이스케이프코드(\t)로 인식되지 않을까 걱정
> _root = os.path.dirname(os.path.realpath(__file__))
>
> # `input 케이스 자동 불러오기 기능`
> # root_path를 통해 testcase에 속한 input.txt 오픈
> # 해당 과정을 통해 input.txt의 testcase를 한줄씩 읽어드림
> # 따라서 터미널창에 testcase를 수동으로 복붙할 필요가 없음
> sys.stdin = open(_root + '\\testcase\\input.txt', 'r')
> 
>    # `나의 출력과 정답 출력 비교`
>    # root_path를 통해 testcase에 속한 output.txt 오픈
> # .readlines()를 통해 ouput.txt의 모든 라인을 리스트로 불러옴
># ex) ['#1 13\n', '#2 32\n', '#3 54\n', '#4 25\n']
> _answer_list = open(_root + '\\testcase\\output.txt', 'r').readlines()
>
> # 기존 print() 출력을 swea_tc() 함수로 변경하면 됨
># print(f'#{t} {answer})' -> swea_tc(f'#{t} {answer}')
> def swea_tc(_answer_yours):
>
> # _answer_list[0]의 첫번째 값을 불러와 앞뒤에 존재하는 띄어쓰기(\n) 삭제
>_answer = _answer_list[0].strip()
> 
># 정답을 판단하여 출력, 틀린경우 실제 정답값 출력
> if _answer == _answer_yours:
>print(f'{_answer_yours} -> O')
>   else:
>print(f'{_answer_yours} -> X, answer: {_answer}')
>   
># 비교가 완료된 answer_list의 값(첫번째줄) 은 삭제
> _answer_list.pop(0)
>```
> 



> 마지막으로 해당 코드를 사용해 봅시다. (예를 들어 표현해 보겠습니다.)
>
> **hjtc라이브러리에서 swea_tc 함수 호출를 진행한 후에**  
> *print() 출력 대신 swea_tc()로 출력하면 됩니다.**  
>
> ```python
> # hjtc라이브러리에서 swea_tc 함수 호출
> from my_package.hjtc import swea_tc
> 
> T = int(input())
> for t in range(1, T+ 1):
> answer = 0
> 
> '''
> your code
> '''
> 
> 	'''정답 출력'''
> 	# 기존에 사용했던 출력 방법
> answer_print = f'#{t} {answer}'
> print(answer_print)
> '''혹은'''
> print(f'#{t} {answer}')
> 
> 	# 새롭게 제안하는 방법
> swea_tc(answer_print)
> '''혹은'''
> swea_tc(f'#{t} {answer}')
> ```
>
> 그럼 아래와 같이 콘솔에 출력이 되어 정답유무 및 오답 체크를 진행해 줍니다.  
> (틀렸을 경우 정답을 표시해줍니다.)  
>
> ```
> #1 13 -> O
> #2 32 -> O
> #3 54 -> O
> #4 25 -> O
> #5 87 -> O
> #6 14 -> O
> #7 39 -> X, answer: #7 40
> #8 26 -> O
> #9 13 -> X, answer: #9 12
> #10 29 -> X, answer: #10 55
> ```
>
> 모든 내용이 확인되면
>
> SWEA에 제출할땐 `print()` 함수를 기입하여 제출하면 됩니다.
>
> ```python
> from my_package.hjtc import swea_tc # 삭제
> swea_tc(answer) #삭제
> print(answer) # 기입 후 제출
> ```

  



##   끝으로..

> 현재 몇 문제 테스트를 해보았고 문제되는건 없어보입니다.  
>하지만 문제의 양이 방대하고 특이한 input.txt들이 존재하기 때문에 어떻게 에러가 발생할지 모릅니다.  
> 따라서 에러가 발생하면, 푸시는 문제를 알려주시길 바랍니다.  
>테스트하여 수정해보겠습니다.
> 
>유용하게 사용될지는 의문이지만, 도움이 되길 바랍니다.  
> 긴글 읽어주셔서 감사합니다 🙇‍♂️







