from tkinter import *
from tkinter import ttk
def mainwindow() :
    root = Tk()
    root.title("GUI4: My Sweety cake shop by[Rujira Navaen]")
    root.geometry("900x700")
    root.configure(bg='lightgreen')
    root.option_add('*font', 'Calibri 14')
    img_icon = PhotoImage(file="images/heart.png")
    root.iconphoto(False,img_icon)
   
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=4)
    return(root)

#สร้างเฟรมเพื่อแบ่งหน้า
def createframe(root) :
    top = Frame(root,bg='#FF8BC9')
    top.rowconfigure(0,weight=1)
    top.columnconfigure((0,1,2),weight=1)#แบ่ง สามคอลัมน์
    top.grid(row=0,columnspan=2,sticky='news')
   
    left = LabelFrame(root,bg='#FCBBD5',text='Menu')
    left.rowconfigure((0,1,2,3,4,5,6),weight=1)#แบ่ง 7 แถว
    left.columnconfigure((0,1),weight=1)
    left.grid(row=1,column=0,sticky='news')
   
    right = LabelFrame(root, text='Checkout',bg='#B688D3')
    right.rowconfigure((0,1,2,3),weight=1)#แบ่ง 4 แถว
    right.columnconfigure((0,1),weight=1)
    right.grid(row=1,column=1,sticky='news')
    
    bottom = Frame(root,bg='#F297D2')
    bottom.rowconfigure((0),weight=1)
    bottom.columnconfigure((0),weight=1)
    bottom.grid(row=2,columnspan=2,sticky='news')
    
    return(root,top,left,right,bottom)
#หัว
def widgettop(top) :
    lll = Label(top,text='My Cake Shop',width=20,height=4,bg='#FF8BC9',font=('Arial',20,'bold'),fg='#FFFFFF')
    lll.grid(row=0,columnspan=3)
#การแสดงผลทางฝั่งซ้าย
def widgetleft(left) :
    #
    tag1 = Label(left,image=cake1, bg='#FFA2C7')
    tag1.grid(row=0,rowspan=2)
    tag2 = Label(left,image=cake2, bg='#FFA2C7')
    tag2.grid(row=2,rowspan=2)
    tag3 = Label(left,image=cake3, bg='#FFA2C7')
    tag3.grid(row=4,rowspan=2)
    #รับจำนวน
    tagcake1 = Label(left,text='Product1: Wow1\nPrice 180 baht',bg='#B28CCD',fg='#FFFFFF')
    tagcake1.grid(row=0,column=1,pady=10)
    spinquan1=Spinbox(left, bg='#FFA2C7',width=10,justify=CENTER, from_=0,to=10,textvariable=qty1)
    spinquan1.grid(row=1,column=1,padx=50,pady=3)
    
    tagcake2 = Label(left,text='Product2: Wow2\nPrice 250 baht',bg='#B28CCD',fg='#FFFFFF')
    tagcake2.grid(row=2,column=1)
    spinquan2=Spinbox(left, bg='#FFA2C7',width=10,justify=CENTER, from_=0,to=10,textvariable=qty2)
    spinquan2.grid(row=3,column=1,padx=50,pady=3)
    
    tagcake3 = Label(left,text='Product3: Wow3\nPrice 380 baht',bg='#B28CCD',fg='#FFFFFF')
    tagcake3.grid(row=4,column=1)
    spinquan3 =Spinbox(left, bg='#FFA2C7',width=10,justify=CENTER, from_=0,to=10,textvariable=qty3)
    spinquan3.grid(row=5,column=1,padx=50,pady=3)
    
    btnc = Button(left,text="Checkout",image=cart,compound='left', command=checkout)
    btnc.grid(row=6,columnspan=2,ipadx=15,sticky='nwes')
    return spinquan1,spinquan2,spinquan3
#แสดงผลรวมของสินค้า
def widgetright(right) :
 
    p1 = Label(right, text='Product1: Wow 1 \nPrice 180 baht',bg='#F5E98F')
    p1.grid(row=0, column=0, sticky='e')
    cake_label1 = Label(right,justify=CENTER, bg="#FFA7D6",width=20,height=1)
    cake_label1.grid(row=0,column=1,sticky="w",padx=20,ipady=15)
 
    p2 = Label(right, text='Product2: Wow 2 \nPrice 250 baht',bg='#F5E98F')
    p2.grid(row=1, column=0, sticky='e')
    cake_label2 = Label(right,justify=CENTER, bg="#FFA7D6",width=20,height=1)
    cake_label2.grid(row=1,column=1,sticky="w",padx=20,ipady=15)
    
    p3 = Label(right, text='Product3: Wow 3 \nPrice 380 baht',bg='#F5E98F')
    p3.grid(row=2, column=0, sticky='e')
    cake_label3 = Label(right,justify=CENTER, bg="#FFA7D6",width=20,height=1)
    cake_label3.grid(row=2,column=1,sticky="w",padx=20,ipady=15)
    

 
    lb3 = Label(right, text='Total: ',bg='#F5E98F')
    lb3.grid(row=3, column=0, sticky='e')
    ent_total = Label(right,justify=CENTER, bg="#8BFFAA",width=20,height=1)
    ent_total.grid(row=3,column=1,sticky="w",padx=20)
    return cake_label1,cake_label2,cake_label3,ent_total
#คำนวนผลรวมของสินค้่า
def checkout():
    total = 0
  
    quantity_cake1 = int(spinquan1.get())
    quantity_cake2 = int(spinquan2.get())
    quantity_cake3 = int(spinquan3.get())
    
    #แสดงผลรวมเค้ก1
    total_cake1 = quantity_cake1 * 180
    caketotal1 = StringVar()
    caketotal1.set("%0.2f"%total_cake1)
    cake_label1["text"] = caketotal1.get()
    cake_label1["fg"] = 'white'
    #แสดงผลรวมเค้ก2
    total_cake2 = quantity_cake2 * 250
    caketotal2 = StringVar()
    caketotal2.set("%0.2f"%total_cake2)
    cake_label2["text"] = caketotal2.get()
    cake_label2["fg"] = 'white'
    #แสดงผลรวมเค้ก3
    total_cake3 = quantity_cake3 * 380
    caketotal3 = StringVar()
    caketotal3.set("%0.2f"%total_cake3)
    cake_label3["text"] = caketotal3.get()
    cake_label3["fg"] = 'white'
    #แสดงผลรวมทั้งหมด
    total = (total_cake1 + total_cake2 + total_cake3 )
    strtotal = StringVar()
    strtotal.set("%0.2f"%total)
    ent_total["text"] = strtotal.get()
    ent_total["fg"] = '#7E8DFF'
def widgetbottom(bottom):
    #ปุ่มกดออก
     btn1 = Button(bottom,text=" Exit",image=img_exit, compound='left', command=quit)
     btn1.grid(row=4,column=0,padx=20,ipadx=10, sticky='e')
root = mainwindow()
 
qty1=StringVar()
qty2=StringVar()
qty3=StringVar()

img_exit = PhotoImage(file='images/exit.png')
cake1 = PhotoImage(file='images/cake1.png')
cake2= PhotoImage(file='images/cake2.png')
cake3 = PhotoImage(file="images/cake3.png")
cart = PhotoImage(file='images/cart.png')
 
root,top,left,right,bottom = createframe(root)
widgettop(top)
spinquan1,spinquan2,spinquan3 = widgetleft(left)
widgetbottom(bottom)
cake_label1,cake_label2,cake_label3,ent_total=widgetright(right)
root.mainloop()

