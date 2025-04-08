from tkinter import *
from tkinter import messagebox  # 메시지 박스 모듈 추가

# 메인 윈도우 생성
mainFrame = Tk()
mainFrame.title("Python GUI Text Input")  # 윈도우 제목
mainFrame.geometry("600x400")  # 윈도우 크기
mainFrame.configure(bg="lightblue")  # 배경색

# ------------------------------
# Label 생성 (설명용 텍스트)
textLabel = Label(mainFrame, text="Text")  # Text 위젯용 Label
entryLabel = Label(mainFrame, text="Entry")  # Entry 위젯용 Label

# ------------------------------
# Text 위젯: 여러 줄 입력 가능 (Textarea)
inputTxt1 = Text(mainFrame, width=20, height=1)
inputTxt1.insert(END, "Text!!")  # 초기값 설정

# Entry 위젯: 한 줄 입력 (Input Text)
inputEty1 = Entry(mainFrame, width=20)
inputEty1.insert(0, "Entry")  # 초기값 설정

# ------------------------------
# 이벤트 핸들러 함수 정의

# Text 입력값 가져오기
def getText():
    txtStr = inputTxt1.get("1.0", END)  # "1.0" : 1번째 줄, 0번째 문자부터 END까지
    messagebox.showinfo("알림", txtStr)  # 메시지 박스에 출력

# Entry 입력값 가져오기
def getEntry():
    entStr = inputEty1.get()  # Entry 에서 텍스트 가져오기
    messagebox.showinfo("알림", entStr)

# Text 입력값 삭제
def delText():
    messagebox.showinfo("알림", "텍스트 입력값 삭제!!!")
    inputTxt1.delete("1.0", END)  # Text 위젯 전체 삭제

# Entry 입력값 삭제
def delEntry():
    messagebox.showinfo("알림", "엔트리 입력값 삭제!!!")
    inputEty1.delete(0, END)  # Entry 위젯 전체 삭제

# ------------------------------
# 버튼 생성 (이벤트 연결)
getTextBtn = Button(mainFrame, text="Get Text!!", command=getText)
delTextBtn = Button(mainFrame, text="Del Text!!", command=delText)

getEntryBtn = Button(mainFrame, text="Get Entry!!", command=getEntry)
delEntryBtn = Button(mainFrame, text="Del Entry!!", command=delEntry)  # (수정) 버튼 텍스트 Get → Del

# ------------------------------
# 위젯 배치 (grid 레이아웃)

# Text 관련 위젯 배치
textLabel.grid(row=0, column=0, padx=3, pady=10)
inputTxt1.grid(row=0, column=1, padx=3, pady=10)
getTextBtn.grid(row=0, column=2, padx=3, pady=10)
delTextBtn.grid(row=0, column=3, padx=3, pady=10)

# Entry 관련 위젯 배치
entryLabel.grid(row=1, column=0, padx=3, pady=10)
inputEty1.grid(row=1, column=1, padx=3, pady=10)
getEntryBtn.grid(row=1, column=2, padx=3, pady=10)
delEntryBtn.grid(row=1, column=3, padx=3, pady=10)

# ------------------------------
# 메인 이벤트 루프 실행 (창이 닫힐 때까지 프로그램 유지)
mainFrame.mainloop()
