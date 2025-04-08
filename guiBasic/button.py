from tkinter import *
from tkinter import messagebox  # 메시지 박스 모듈 추가

mainFrame = Tk()
mainFrame.title("Python GUI")
mainFrame.geometry("600x400")
mainFrame.configure(bg="lightblue")

def buttonCmd ():
     messagebox.showinfo("알림", "버튼이 클릭되었습니다!")  # 정보 메시지

btn1 = Button(mainFrame, text="Button1") # Button 1: 기본 버튼 (텍스트만 지정)
btn2 = Button(mainFrame, text="Button2", padx=5,pady=10) # Button 2: 좌우 여백 (padx), 상하 여백 (pady) 추가
btn3 = Button(mainFrame, text="Button3", width=15,height=1) # Button 3: 버튼의 크기 지정 (width, height: 텍스트 기준 단위)
btn4 = Button(mainFrame, text="Button4", fg="red", width=15,height=1) # Button 4: 텍스트 색상 변경 (fg: foreground)

# 이미지 버튼 예시 (이미지 경로에 맞게 사용 시)
#photo = PhotoImage(".. 버튼 이미지 경로") 
#btn5 = Button(mainFrame, image=photo) # 이미지 파일을 버튼으로  
btn5 = Button(mainFrame, text="Button5", command=buttonCmd) # Button 5: 클릭 이벤트 연결

# pack: 가장 간단한 배치 방법, 위젯을 위에서 아래로 또는 방향 지정하여 배치
#btn1.pack(side=LEFT);
#btn2.pack(side=LEFT);
#btn3.pack(side=LEFT);
#btn4.pack(side=LEFT);
#btn5.pack(side=LEFT);

#grid : 무형의 그리드(테이블 생성하여....)
btn1.grid(row=0, column=0, padx=10, pady=10)
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3.grid(row=1, column=0, padx=10, pady=10)
btn4.grid(row=1, column=1, padx=10, pady=10)
btn5.grid(row=2, column=0, columnspan=2, padx=10, pady=20)  # 두 열을 병합해서 중앙 정렬

#place : 입력된 좌표 기준으로 노출 
#btn1.place(x=50, y=50)
#btn2.place(x=150, y=100)

mainFrame.mainloop(); # 메인 이벤트 루프 실행 (창이 닫힐 때까지)


