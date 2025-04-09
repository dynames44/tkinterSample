from tkinter import *
from tkinter import messagebox  # 메시지 박스 모듈 추가

# 메인 윈도우 생성
mainFrame = Tk()
mainFrame.title("Python GUI ListBox with Scrollbars")
mainFrame.geometry("600x400")
mainFrame.configure(bg="lightblue")

# ------------------------------
# Label 생성 (설명용 텍스트)
listboxLabel = Label(mainFrame, text="Listbox1")
listboxLabel2 = Label(mainFrame, text="Listbox2")

# ------------------------------
# Listbox1 및 스크롤바 생성
scrollbar1 = Scrollbar(mainFrame, orient=VERTICAL)

listbox = Listbox(
    mainFrame,
    selectmode="single",
    height=1,
    yscrollcommand=scrollbar1.set
)

scrollbar1.config(command=listbox.yview)

listItems = ["사과", "바나나", "딸기", "수박", "배", "포도"]

for idx, item in enumerate(listItems):
    listbox.insert(idx, item)

# ------------------------------
# Listbox2 및 스크롤바 생성
scrollbar2 = Scrollbar(mainFrame, orient=VERTICAL)

listbox2 = Listbox(
    mainFrame,
    selectmode="single",
    height=1,
    yscrollcommand=scrollbar2.set
)

scrollbar2.config(command=listbox2.yview)

dictData1 = [
    {'seqId': '001', 'name': 'name001'},
    {'seqId': '002', 'name': 'name002'},
    {'seqId': '003', 'name': 'name003'}
]

for idx, data in enumerate(dictData1):
    listbox2.insert(idx, data['name'])

# ------------------------------
# 이벤트 핸들러 함수

def getItem():
    try:
        selectIdx = listbox.curselection()[0]
        selectedItem = listbox.get(selectIdx)
        messagebox.showinfo("selected Idx", f"selected Idx: {selectIdx}, selected Text: {selectedItem}")
    except IndexError:
        messagebox.showinfo("selected Idx", "아이템 선택 해라!!!")

def getSize():
    itemCount = listbox.size()
    messagebox.showinfo("ListBox Item Count", itemCount)

def getDicItem():
    try:
        selectIdx = listbox2.curselection()[0]
        selectedData = dictData1[selectIdx]
        seqId = selectedData['seqId']
        name = selectedData['name']
        messagebox.showinfo("선택 결과", f"seqId: {seqId}, name: {name}")
    except IndexError:
        messagebox.showinfo("선택 결과", "아이템 선택 해라!!!")

# ------------------------------
# 버튼 생성
getItemBtn = Button(mainFrame, text="getItem", command=getItem)
getSizeBtn = Button(mainFrame, text="getSize", command=getSize)
getDictBtn = Button(mainFrame, text="getDicItem", command=getDicItem)

# ------------------------------
# 위젯 배치 (grid 레이아웃)

# Listbox1 + Scrollbar1
listboxLabel.grid(row=0, column=0, padx=3, pady=10)
listbox.grid(row=0, column=1, padx=3, pady=10)
scrollbar1.grid(row=0, column=2, sticky='ns', padx=3, pady=10)

getItemBtn.grid(row=1, column=0, padx=3, pady=10)
getSizeBtn.grid(row=1, column=1, padx=3, pady=10)

# Listbox2 + Scrollbar2
listboxLabel2.grid(row=2, column=0, padx=3, pady=10)
listbox2.grid(row=2, column=1, padx=3, pady=10)
scrollbar2.grid(row=2, column=2, sticky='ns', padx=3, pady=10)

getDictBtn.grid(row=3, column=0, padx=3, pady=10)

# ------------------------------
# 메인 이벤트 루프
mainFrame.mainloop()
