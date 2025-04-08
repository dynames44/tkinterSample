from tkinter import *

mainFrame = Tk()
mainFrame.title("Python GUI Lable")
mainFrame.geometry("600x400")
mainFrame.configure(bg="lightblue")

lable1 = Label(mainFrame, text="Label") #기본 lable (텍스트만 지정)
lable2 = Label(mainFrame, text="Red Label", fg="red") # 색상지정 
lable3 = Label(mainFrame, text="Label Bold", font=("Arial", 8, "bold")) # 폰트트변경 

# label2의 표시 여부 상태 저장 변수 (초기에는 표시되어 있으므로 True)
label2_visible = True

def lableChg():
    lable1.config(text="lable Change!!!")
    
def lableDsp():
    global label2_visible # 함수안의  scope 변수가 아닌 저 위의 label2_visible의 값을 바꾼다.
    if label2_visible:
        lable2.grid_remove()  # 숨기기
        label2_visible = False
    else:
        lable2.grid()  # 다시 보이기
        label2_visible = True

btn1 = Button(mainFrame, text="Label1 텍스트 변경" ,command=lableChg) 
btn2 = Button(mainFrame, text="Label2 토글", command=lableDsp)

lable1.grid(row=0, column=0, padx=3, pady=10)
lable2.grid(row=0, column=1, padx=3, pady=10)
lable3.grid(row=0, column=2, padx=3, pady=10)

btn1.grid(row=1, column=0, padx=3, pady=10)
btn2.grid(row=1, column=1, padx=3, pady=10)
mainFrame.mainloop(); # 메인 이벤트 루프 실행 (창이 닫힐 때까지)