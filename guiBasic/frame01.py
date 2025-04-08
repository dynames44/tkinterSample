from tkinter import *

mainFrame = Tk()
mainFrame.title("Python GUI")

# 화면 너비와 높이 가져오기
screen_width = mainFrame.winfo_screenwidth()
screen_height = mainFrame.winfo_screenheight()

# 창 크기
window_width = 640
window_height = 480

# 좌표 계산
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# 창 위치 + 크기 설정 : 가로사이즈 x 세로사이즈 + 가로위치 + 세로위치
mainFrame.geometry(f"{window_width}x{window_height}+{x}+{y}")

mainFrame.configure(bg="lightblue")
mainFrame.resizable(False, False)
mainFrame.mainloop();