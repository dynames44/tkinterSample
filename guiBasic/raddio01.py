from tkinter import *
from tkinter import messagebox  # 메시지 박스 모듈 추가

# 메인 윈도우 생성
mainFrame = Tk()
mainFrame.title("Python GUI Radio Button")  # 윈도우 타이틀 설정
mainFrame.geometry("600x400")                # 윈도우 크기 설정
mainFrame.configure(bg="lightblue")          # 배경색 설정

# ------------------------------
# Label 생성 (설명용 텍스트)
label1 = Label(mainFrame, text="Radio Group 1")  # 첫 번째 그룹 설명 레이블
label2 = Label(mainFrame, text="Radio Group 2")  # 두 번째 그룹 설명 레이블

# ------------------------------
# 이벤트 핸들러 함수 정의
# 라디오 그룹 1 상태 확인 버튼 클릭 시 실행 함수
def checkBtn1():
    if radioVar1.get() == 0:
        messagebox.showinfo("Radio1 선택 값", "선택 없음")
    else:
        messagebox.showinfo("Radio1 선택 값", radioVar1.get())

# 라디오 그룹 2 상태 확인 버튼 클릭 시 실행 함수
def checkBtn2():
    if radioVar2.get() == 0:
        messagebox.showinfo("Radio2 선택 값", "선택 없음")
    else:
        messagebox.showinfo("Radio2 선택 값", radioVar2.get())
        
def chgBtn1():
    messagebox.showinfo("Niotice","Radio1 상태 변경")
        
def chgBtn2():
    messagebox.showinfo("Niotice","Radio2 상태 변경")


# ------------------------------
# 라디오 버튼 그룹 1 설정
radioVar1 = IntVar()  # 그룹 1의 선택된 값을 저장할 변수

# Radiobutton 주요 옵션 설명:
# - master: 부모 컨테이너
# - text: 버튼 옆에 표시할 텍스트
# - variable: 연결된 변수 (같은 변수 공유 시 그룹이 됨)
# - value: 선택 시 변수에 저장될 값
# - command: 선택 시 호출할 함수
# - state: NORMAL, DISABLED (비활성화)
# - indicatoron: True (기본, 원형) / False (버튼 스타일)
# - selectcolor: 선택 시 원형 표시 색상
# - bg / fg: 배경색 / 글자색
# - font: 글꼴 스타일

grp1_radio1 = Radiobutton(
    mainFrame,
    text="그룹1-1",     # 라벨 텍스트
    value=1,           # 선택 시 radioVar1 에 저장될 값
    variable=radioVar1,  # 그룹 변수를 동일하게 지정하여 그룹화
    command = chgBtn1
)
grp1_radio1.select()  # 기본 선택 설정

grp1_radio2 = Radiobutton(mainFrame, text="그룹1-2", value=2, variable=radioVar1 ,command = chgBtn1)
grp1_radio3 = Radiobutton(mainFrame, text="그룹1-3", value=3, variable=radioVar1 ,command = chgBtn1)

# 라디오 버튼 그룹 2 설정
radioVar2 = IntVar()  # 그룹 2의 선택된 값을 저장할 변수

grp2_radio1 = Radiobutton(mainFrame, text="그룹2-1", value=10, variable=radioVar2 ,command = chgBtn2)
grp2_radio2 = Radiobutton(mainFrame, text="그룹2-2", value=20, variable=radioVar2 ,command = chgBtn2)
grp2_radio3 = Radiobutton(mainFrame, text="그룹2-3", value=30, variable=radioVar2 ) # 상태값 변경 적용 XXXXXX

# 버튼 생성 (라디오 상태 확인용)
btn1 = Button(mainFrame, text="Radio Group 1 확인", command=checkBtn1)
btn2 = Button(mainFrame, text="Radio Group 2 확인", command=checkBtn2)

# ------------------------------
# 위젯 배치: grid 레이아웃 사용
label1.grid(row=0, column=0, padx=3, pady=10)  # 첫 번째 그룹 레이블 배치
grp1_radio1.grid(row=0, column=1, padx=3, pady=10)  # 첫 번째 그룹 버튼 1
grp1_radio2.grid(row=0, column=2, padx=3, pady=10)  # 첫 번째 그룹 버튼 2
grp1_radio3.grid(row=0, column=3, padx=3, pady=10)  # 첫 번째 그룹 버튼 3
btn1.grid(row=0, column=4, padx=3, pady=10)          # 첫 번째 그룹 확인 버튼

label2.grid(row=1, column=0, padx=3, pady=10)  # 두 번째 그룹 레이블 배치
grp2_radio1.grid(row=1, column=1, padx=3, pady=10)  # 두 번째 그룹 버튼 1
grp2_radio2.grid(row=1, column=2, padx=3, pady=10)  # 두 번째 그룹 버튼 2
grp2_radio3.grid(row=1, column=3, padx=3, pady=10)  # 두 번째 그룹 버튼 3
btn2.grid(row=1, column=4, padx=3, pady=10)          # 두 번째 그룹 확인 버튼

# 메인 이벤트 루프 실행 (윈도우 실행)
mainFrame.mainloop()
