from tkinter import Tk, Menu

# 메인 윈도우 생성
mainFrame = Tk()
mainFrame.title("Python GUI Menu")  # 윈도우 타이틀 설정
mainFrame.geometry("600x400")       # 윈도우 크기 설정

# 메뉴 바 생성
menu_bar = Menu(mainFrame)

basic_menu = Menu(menu_bar, tearoff=0) # '기본 위젯' 메뉴 생성
option_menu1 = Menu(menu_bar, tearoff=0) # '메뉴옵션1' 메뉴 생성 (서브 메뉴가 추가될 예정)

# 메뉴 바에 대메뉴 추가 (add_cascade)
# - label: 메뉴 이름
# - menu: 연결할 하위 메뉴(Menu 객체)
# - underline: 밑줄 위치 (Alt 키 접근용), 예: underline=0
# - state: 메뉴 상태 ('normal', 'disabled')
# - accelerator: 단축키 표시 (표시만, 동작은 bind 필요)
menu_bar.add_cascade(label="기본 위젯", menu=basic_menu)
menu_bar.add_cascade(label="메뉴옵션1", menu=option_menu1)

# '기본 위젯' 메뉴에 소메뉴 추가 (add_command)
# - label: 메뉴 항목 이름
# - command: 클릭 시 실행할 함수
# - underline: 밑줄 위치 (Alt 키 접근용), 예: underline=0
# - state: 메뉴 상태 ('normal', 'disabled')
# - accelerator: 단축키 표시 (표시만, 동작은 bind 필요)
basic_menu.add_command(label="레이블")
basic_menu.add_command(label="텍스트")

# 구분선 추가 (add_separator)
basic_menu.add_separator()

basic_menu.add_command(label="버튼")
basic_menu.add_command(label="리스트 박스")
basic_menu.add_separator()

# 비활성화된 메뉴 항목 추가 (state="disabled")
basic_menu.add_command(label="폐기 위젯1", state="disabled")
basic_menu.add_command(label="폐기 위젯2", state="disabled")
basic_menu.add_separator()

# 종료 메뉴 항목 추가
basic_menu.add_command(label="종료", command=mainFrame.quit)

# '메뉴옵션1' 하위에 '선택1' 서브 메뉴 추가
select1_submenu = Menu(option_menu1, tearoff=0)
option_menu1.add_cascade(label="선택1", menu=select1_submenu)

# '선택1' 서브 메뉴에 라디오 버튼 메뉴 추가 (add_radiobutton)
# - 그룹 내에서 하나만 선택 가능
# - label: 메뉴 항목 이름
# - command: 클릭 시 실행할 함수
# - value: 선택 값
# - variable: 선택 상태를 저장할 변수 (tkinter.StringVar 또는 IntVar)
# - underline: 밑줄 위치 (Alt 키 접근용), 예: underline=0
# - state: 메뉴 상태 ('normal', 'disabled')
# - accelerator: 단축키 표시 (표시만, 동작은 bind 필요)
select1_submenu.add_radiobutton(label="한국어")
select1_submenu.add_radiobutton(label="영어")
select1_submenu.add_radiobutton(label="스페인어")

# '메뉴옵션1' 하위에 '선택2' 서브 메뉴 추가
select2_submenu = Menu(option_menu1, tearoff=0)
option_menu1.add_cascade(label="선택2", menu=select2_submenu)

# '선택2' 서브 메뉴에 체크 버튼 메뉴 추가 (add_checkbutton)
select2_submenu.add_checkbutton(label="선택1")
select2_submenu.add_checkbutton(label="선택2")

# 메인 윈도우에 메뉴 바 설정
mainFrame.config(menu=menu_bar)

# 메인 이벤트 루프 실행 (윈도우 실행)
mainFrame.mainloop()
