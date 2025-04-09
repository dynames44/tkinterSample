from tkinter import *
from tkinter import messagebox  # 메시지 박스 모듈 추가

# 메인 윈도우 생성
mainFrame = Tk()
mainFrame.title("Python GUI CheckBox")  # 윈도우 타이틀 설정
mainFrame.geometry("600x400")           # 윈도우 크기 설정
mainFrame.configure(bg="lightblue")     # 배경색 설정

# ------------------------------
# Label 생성 (설명용 텍스트)
checkboxLabel1 = Label(mainFrame, text="checkbox1")  # 첫 번째 체크박스 설명 레이블
checkboxLabel2 = Label(mainFrame, text="checkbox2")  # 두 번째 체크박스 설명 레이블

# ------------------------------
# 이벤트 핸들러 함수 정의
# 체크박스 1 상태 확인 버튼 클릭 시 실행 함수
def checkboxBtn1():
    
    if checkvar1.get() == 1:
        messagebox.showinfo("checkbox1 Status", "선택됨")
    else:
        messagebox.showinfo("checkbox1 Status", "선택 안 됨")    
        
# 체크박스1 상태 변경 시 실행 함수
def chgCheckbox1():
    
    if checkvar1.get() == 1:
        messagebox.showinfo("checkbox1 상태 변경", "선택 안 됨 -> 선택됨")
    else:
        messagebox.showinfo("checkbox1 상태 변경", "선택됨 -> 선택 안 됨")            

# 체크박스 2 상태 확인 버튼 클릭 시 실행 함수
def checkboxBtn2():
    if checkvar2.get() == 1:
        messagebox.showinfo("checkbox2 Status", "선택됨")
    else:
        messagebox.showinfo("checkbox2 Status", "선택 안 됨")    
        
# 체크박스2 상태 변경 시 실행 함수
def chgCheckbox2():
    
    if checkvar2.get() == 1:
        messagebox.showinfo("checkbox2 상태 변경", "선택 안 됨 -> 선택됨")
    else:
        messagebox.showinfo("checkbox2 상태 변경", "선택됨 -> 선택 안 됨")     

# ------------------------------
# 체크박스 생성

# 체크박스 1 설정
checkvar1 = IntVar()  # 체크 상태를 저장할 변수 (정수형) 0: 선택 안 됨, 1: 선택됨
checkbox1 = Checkbutton(
     mainFrame                   # 부모 윈도우
    ,text="체크 박스1"           # 체크박스 옆에 표시할 텍스트
    ,variable=checkvar1           # 체크 상태를 저장할 변수 연결
    # 추가 옵션 설명:
    # onvalue=1, offvalue=0: 기본값 (생략 가능). 선택 시 1, 해제 시 0 저장
    ,command=chgCheckbox1 #체크박스 상태 변경 시 호출할 함수
    # bg='color': 배경색 지정
    # fg='color': 텍스트 색상 지정
    # font=('폰트명', 크기): 폰트 지정
)
checkbox1.deselect()  # 기본 상태를 '선택 안 됨' 으로 설정

# 체크박스 2 설정
checkvar2 = IntVar()  # 체크 상태를 저장할 변수 (정수형)
checkbox2 = Checkbutton(
     mainFrame
    ,text="체크 박스2"
    ,variable=checkvar2
    ,command=chgCheckbox2
)
checkbox2.select()  # 기본 상태를 '선택됨' 으로 설정
               

# 버튼 생성 (체크박스 상태 확인용)
checkboxBtn1 = Button(mainFrame, text="checkboxBtn1", command=checkboxBtn1)
checkboxBtn2 = Button(mainFrame, text="checkboxBtn2", command=checkboxBtn2)

# 위젯 배치: grid 레이아웃 사용
checkboxLabel1.grid(row=0, column=0, padx=3, pady=10)  # 첫 번째 라벨 배치
checkbox1.grid(row=0, column=1, padx=3, pady=10)       # 첫 번째 체크박스 배치
checkboxBtn1.grid(row=0, column=2, padx=3, pady=10)    # 첫 번째 버튼 배치

checkboxLabel2.grid(row=1, column=0, padx=3, pady=10)  # 두 번째 라벨 배치
checkbox2.grid(row=1, column=1, padx=3, pady=10)       # 두 번째 체크박스 배치
checkboxBtn2.grid(row=1, column=2, padx=3, pady=10)    # 두 번째 버튼 배치

# 메인 이벤트 루프 실행 (윈도우 실행)
mainFrame.mainloop()
