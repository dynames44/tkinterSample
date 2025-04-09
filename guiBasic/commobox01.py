from tkinter import Tk, messagebox
from tkinter.ttk import Label, Button, Frame, Style, Combobox

# 메인 윈도우 생성
mainFrame = Tk()
mainFrame.title("Python GUI ComboBox")  # 윈도우 타이틀 설정
mainFrame.geometry("600x400")                # 윈도우 크기 설정

# 스타일 정의
style = Style()
style.configure("TButton", padding=6)
style.configure("TLabel", padding=6)

# ------------------------------
# Frame으로 그룹화 (그룹별로 위젯을 묶어서 관리)
group1_frame = Frame(mainFrame)
group2_frame = Frame(mainFrame)

# ------------------------------
# Label 생성 (설명용 텍스트)
label1 = Label(group1_frame, text="ComboBox1")  # 첫 번째 그룹 설명 레이블
label2 = Label(group2_frame, text="ComboBox2")  # 두 번째 그룹 설명 레이블

# 첫 번째 콤보박스 (리스트 아이템 기반) - '선택' 항목 포함
listItems = ["선택", "사과", "바나나", "딸기", "수박", "배", "포도"]
comboBox1 = Combobox(
                         group1_frame
                        ,height=10  # 표시할 최대 항목 수 (화면에 보이는 높이)
                        ,values=listItems # 선택 가능한 값들의 리스트
                        ,state="readonly" # 입력 불가, 드롭다운에서만 선택 가능
                        # postcommand: 드롭다운 열기 전 실행할 콜백 함수
                        # width: 콤보박스의 너비 (글자 수 기준)
                        # justify: 텍스트 정렬 방식 ('left', 'center', 'right')
                        # textvariable: 선택된 값을 저장할 변수 (StringVar 등)
                    )

comboBox1.set("선택")

# 두 번째 콤보박스 (dictData1 기반) - '선택' 항목 포함
dictData1 = [
    {'seqId': '001', 'name': 'name001'},
    {'seqId': '002', 'name': 'name002'},
    {'seqId': '003', 'name': 'name003'}
]

comboBox2_values = ["선택"] + [item['name'] for item in dictData1]
comboBox2 = Combobox(
    group2_frame,
    height=10,  # 표시할 최대 항목 수 (화면에 보이는 높이)
    values=comboBox2_values,  # 선택 가능한 값들의 리스트
    state="readonly"  # 입력 불가, 드롭다운에서만 선택 가능
)
comboBox2.set("선택")

# ------------------------------
# 이벤트 핸들러 함수 정의
# 콤보박스 1 상태 확인 버튼 클릭 시 실행 함수
def checkBtn1():
    selected = comboBox1.get()
    if selected == "선택" or not selected:
        messagebox.showinfo("ComboBox1 선택 값", "선택된 값이 없습니다.")
    else:
        messagebox.showinfo("ComboBox1 선택 값", selected)
    comboBox1.set("선택")  # 선택 후 자동으로 초기화

# 콤보박스 2 상태 확인 버튼 클릭 시 실행 함수
def checkBtn2():
    selected = comboBox2.get()
    if selected == "선택" or not selected:
        messagebox.showinfo("ComboBox2 선택 값", "선택된 값이 없습니다.")
    else:
        # 선택된 name 값에 해당하는 seqId 찾기
        seqId = next((item['seqId'] for item in dictData1 if item['name'] == selected), 'Unknown')
        messagebox.showinfo("ComboBox2 선택 값", f"선택한 값: {selected}\nseqId: {seqId}")
    comboBox2.set("선택")  # 선택 후 자동으로 초기화

# ComboBox1 선택 변경 시 실행 함수 (실시간 이벤트)
def on_comboBox1_change(event):
    selected = comboBox1.get()
    if selected != "선택" and selected:
        messagebox.showinfo("이벤트", "ComboBox1 변경")

# ComboBox2 선택 변경 시 실행 함수 (실시간 이벤트)
def on_comboBox2_change(event):
    selected = comboBox2.get()
    if selected != "선택" and selected:
        messagebox.showinfo("이벤트", "ComboBox2 변경")

# ComboBox 선택 변경 이벤트 바인딩
comboBox1.bind("<<ComboboxSelected>>", on_comboBox1_change)
comboBox2.bind("<<ComboboxSelected>>", on_comboBox2_change)

# ------------------------------
# 버튼 생성 (콤보박스 상태 확인용)
btn1 = Button(group1_frame, text="ComboBox1 확인", command=checkBtn1)
btn2 = Button(group2_frame, text="ComboBox2 확인", command=checkBtn2)

# ------------------------------
# 위젯 배치: grid 레이아웃 사용 (Frame 내부에서 배치)
# 첫 번째 그룹 Frame 내부 배치
label1.grid(row=0, column=0, padx=3, pady=10)  # 첫 번째 그룹 레이블 배치
comboBox1.grid(row=0, column=1, padx=3, pady=10)  # 첫 번째 콤보박스 배치
btn1.grid(row=0, column=2, padx=3, pady=10)  # 첫 번째 그룹 확인 버튼

# 두 번째 그룹 Frame 내부 배치
label2.grid(row=0, column=0, padx=3, pady=10)  # 두 번째 그룹 레이블 배치
comboBox2.grid(row=0, column=1, padx=3, pady=10)  # 두 번째 콤보박스 배치
btn2.grid(row=0, column=2, padx=3, pady=10)  # 두 번째 그룹 확인 버튼

# Frame 자체를 메인 윈도우에 배치 (group1_frame, group2_frame)
group1_frame.grid(row=0, column=0, sticky="w", padx=10, pady=10)  # 첫 번째 그룹 프레임 배치
group2_frame.grid(row=1, column=0, sticky="w", padx=10, pady=10)  # 두 번째 그룹 프레임 배치

# 메인 이벤트 루프 실행 (윈도우 실행)
mainFrame.mainloop()
