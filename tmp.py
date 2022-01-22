import os

#현재 폴더 경로; 작업 폴더 기준
print(os.getcwd())

#현재 파일의 폴더 경로; 작업 파일 기준
print(os.path.dirname(os.path.realpath(__file__)))