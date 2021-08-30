from tkinter import *
root=Tk()
root.title("답이 정해진 너, 함수")
#더하기 기능
#버튼: 입력,출력,더하기
def button_add():
    num1=E1.get()
    num2=E2.get()
    E3.insert(0,int(num1)+int(num2))
L1=Label(root,text="더하기만 할 수 있으니까 안 쓸거면 들어오지 마!")
L1.pack()
E1=Entry(root,width=35)
E1.pack()
E2=Entry(root,width=35)
E2.pack()
B1=Button(root,width=35,bg="pink1",command=button_add)
B1.pack()
E3=Entry(root,width=35)
E3.pack()
#더하기 함수
root.mainloop()
