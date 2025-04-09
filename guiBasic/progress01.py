import time
from tkinter import Tk, messagebox, IntVar, DoubleVar
from tkinter.ttk import Label, Button, Frame, Style, Progressbar
import threading

# 메인 윈도우 생성
mainFrame = Tk()
mainFrame.title("Python GUI ProgressBar")  # 윈도우 타이틀 설정
mainFrame.geometry("600x400")                # 윈도우 크기 설정

# 스타일 정의
style = Style()
style.configure("TButton", padding=6)
style.configure("TLabel", padding=6)

# Progressbar 스타일 추가
style.configure("custom.Horizontal.TProgressbar", 
                troughcolor='white',    # 배경색 (트랙 색상)
                background='green',     # 진행 바 색상
                thickness=20)

# ------------------------------
# Frame으로 그룹화 (그룹별로 위젯을 묶어서 관리)
group1_frame = Frame(mainFrame)

# ------------------------------
# Label 생성 (설명용 텍스트)
label1 = Label(group1_frame, text="Progress1")  # 첫 번째 그룹 설명 레이블
label2 = Label(group1_frame, text="Progress2")  # 두 번째 그룹 설명 레이블

# ------------------------------
# 변수 설정 (Progressbar 연동 변수)
p_var2 = DoubleVar()  # Progressbar2 연동 변수 (현재 값 유지)
progress2_running = False  # Progressbar2 실행 여부 플래그

# ------------------------------
# 이벤트 핸들러 함수 정의

# progressbar1: indeterminate 모드로 동작 (정지 함수)
def progressStop1():
    progressbar1.stop()

# progressbar2: determinate 모드로 동작 (값 증가)
def progressStart2():
    global progress2_running
    progress2_running = True  # 실행 플래그 True

    def run_progress():
        current_value = p_var2.get()
        for i in range(int(current_value), 101):
            if not progress2_running:
                break  # 플래그가 False 면 루프 종료
            
            time.sleep(0.05)  # 속도 조절
            p_var2.set(i)  # 현재 진행도 설정
            progressbar2.update()

    threading.Thread(target=run_progress, daemon=True).start()  # 별도 쓰레드로 실행

# progressbar2: determinate 모드로 일시 정지 (플래그 변경)
def progressStop2():
    global progress2_running
    progress2_running = False  # 실행 플래그 False 로 변경

# ------------------------------
# Progressbar 생성
progressbar1 = Progressbar(
    group1_frame,
    maximum=100,  # 최대값 (100%)
    mode="indeterminate"  # 불확정 진행 모드 (무한 루프)
    # 추가 옵션:
    # length: 프로그레스 바의 길이 (픽셀)
    # orient: 방향 (HORIZONTAL, VERTICAL)
    # value: 현재 값
    # variable: 연동 변수 (DoubleVar, IntVar 등)
    # style: 스타일 이름
)
progressbar1.start(50)  # 50ms 간격으로 진행

progressbar2 = Progressbar(
    group1_frame,
    maximum=100,  # 최대값
    length=150,  # 프로그레스 바 길이
    variable=p_var2,  # 진행도 값을 저장하는 변수
    mode="determinate"  # determinate 모드 (값 기반 진행)
    # 추가 옵션:
    # orient: HORIZONTAL / VERTICAL
    # style: 커스텀 스타일 지정
    # value: 현재 진행값 직접 지정 가능
)

# ------------------------------
# 버튼 생성
btn1 = Button(group1_frame, text="중지 (Progress1)", command=progressStop1)
btn2 = Button(group1_frame, text="시작 (Progress2)", command=progressStart2)
btn3 = Button(group1_frame, text="중지 (Progress2)", command=progressStop2)

# ------------------------------
# 위젯 배치: grid 레이아웃 사용
# 첫 번째 그룹 Frame 내부 배치
label1.grid(row=0, column=0, padx=3, pady=10)  # Progress1 레이블
progressbar1.grid(row=0, column=1, padx=3, pady=10)
btn1.grid(row=0, column=2, padx=3, pady=10)

label2.grid(row=1, column=0, padx=3, pady=10)  # Progress2 레이블
progressbar2.grid(row=1, column=1, padx=3, pady=10)
btn2.grid(row=1, column=2, padx=3, pady=10)
btn3.grid(row=1, column=3, padx=3, pady=10)

# Frame 자체를 메인 윈도우에 배치
group1_frame.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# 메인 이벤트 루프 실행 (윈도우 실행)
mainFrame.mainloop()
