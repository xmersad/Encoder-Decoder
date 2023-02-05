from tkinter import *
import tkinter.filedialog 
from PIL import Image,ImageTk
import tkinter.filedialog
from tkinter import messagebox as mb
from tkinter import messagebox
import stepic
import webbrowser
import colorama
from colorama import Fore, Back, Style
#----------------------------------------------------------------
global picfile,exit_pic,encoded_pic,count_save
picfile="Not"
exit_pic=False
encoded_pic=False
count_save=0
def closefile():
    window.destroy()

def help_github():
    url='https://github.com/xmersad'
    webbrowser.open(url)
def info_autor():
    messagebox.showinfo("Autor :", "Mersad Karimi \n\n Tel Id:@mersadkarimi")
    pass
def endocing():
    global encoded_pic
    global encoder
    the_file=picfile
    flag_text=True
    flag_pic=True
    if user_text.get("1.0",END)=="\n":
        print(Fore.RED+"TextBox is Empty"+Fore.WHITE)
        flag_text=False
    if picfile=="Not":
        print(Fore.RED+"PictureBox is Empty"+Fore.WHITE)
        flag_pic=False
    if flag_pic==True and flag_text==True:
        img = Image.open(the_file)
        yourtext=user_text.get("1.0",END)
        encoder = stepic.encode(img,yourtext.encode())
        a=str(encoder)
        encoded_pic=True
        #print(a)
        if "<" in a:
            print(Fore.GREEN+"Successfully"+Fore.WHITE)
    pass

def decoing():
    #print(exit_pic)
    if exit_pic==True:
        file_to_decode=picfile
        img_to_decode = Image.open(file_to_decode)
        decoder = stepic.decode(img_to_decode)
        if len(decoder)>=2:
            print("Text is :",decoder)
    pass

def save_file():
    global encoded_pic,count_save
    #encoded_pic =tkinter.filedialog.asksaveasfilename(defaultextension=".espace", filetypes=(("espace file", "*.espace"),("All Files", "*.*") ))
    if encoded_pic==True:
        encoder.save(f"Encode_Pic{str(count_save)}.png")
        print(Fore.GREEN+f"Successfully saved\nFile Name :Encode_Pic{str(count_save)}.png"+Fore.WHITE)
        count_save+=1
    elif encoded_pic==False:
        print("There is no encoded pic to save")

def view_dark():
    Choise.set("Dark")
    Them_Dark()
def view_light():
    Choise.set("Light")
    Them_Dark()

def clear_text():
    user_text.delete("1.0","end")
def clear_picture():
    global exit_pic
    global picfile
    label_picture.config(image="")
    status(False)
    if exit_pic==True:
        picfile="Not"
        exit_pic=False
    elif exit_pic==False:
        #print("there is no picture")
        pass
def new_file():
    if picfile!="Not":
        res=mb.askquestion('New Application', 'Do you really want to new appliction with out save ?')
        if res == 'yes' :
            clear_picture()
            clear_text()
    else:
        clear_text()

def status(flag):
    if flag==TRUE:
        status_label.config(text="Picture Loaded",fg="Green")
    else:
        status_label.config(text="Picture Unloaded",fg="Red")


def Them_Dark():
    if str(Choise.get())=="Dark":
        user_text.config(bg="Black", insertbackground='white',fg="Green")
        top_text.config(bg="#B0B0B0",fg="#CF7F3A",)
        top_pic.config(bg="#B0B0B0",fg="#CF7F3A")
        config_paned.config(bg="#616161",fg="#CF7F3A")
        Radio_light.config(bg="#616161")
        Radio_dark.config(bg="#616161")
        Radio_Label.config(bg="#616161")
        decode_button.config(bg="#F2AE1D")
        Encode_button.config(bg="#F2AE1D")
        status_label.config(bg="#616161")
        label_picture.config(bg="#B0B0B0")
        pass
    elif str(Choise.get())=="Light":
        user_text.config(bg="White",fg="Black",insertbackground='black')
        top_text.config(bg="#F0F0F0",fg="Black",)
        top_pic.config(bg="#F0F0F0",fg="Black")
        config_paned.config(bg="#CFD8DC",fg="Black")
        Radio_Label.config(bg="#CFD8DC")
        Radio_dark.config(bg="#CFD8DC")
        Radio_light.config(bg="#CFD8DC")
        decode_button.config(bg="#F0F0F0")
        Encode_button.config(bg="#F0F0F0")
        status_label.config(bg="#CFD8DC")
        label_picture.config(bg="#F0F0F0")
    pass
def open_file():
    global file
    global picfile
    global exit_pic
    file =tkinter.filedialog.askopenfilename(initialdir="/",title="Select an Image",filetypes=[("all file",pic_exit)])
    print(file)
    if file!="":
        last_img=Image.open(file)
        new_image=last_img.resize((290,205))
        real_image=ImageTk.PhotoImage(new_image)
        label_picture.image=real_image
        label_picture.config(image=real_image)
        status(True) 
        picfile=file
        exit_pic=True

#----------------------------------------------------------------
window=Tk()
window.title("Encoder & Decoder")
window.resizable(False,False)
window.geometry("500x500")
#----------------------------------------------------------------------
#Menu
menubar=Menu(window)
file_menu=Menu(menubar,tearoff=0)
file_menu.add_command(label="New File",command=new_file)
file_menu.add_command(label="Open File",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Close File",command=closefile)

edit_menu=Menu(menubar,tearoff=0)
#edit_menu.add_command(label="Clear Encode Picture")
edit_menu.add_command(label="Clear TextBox",command=clear_text)
edit_menu.add_command(label="Clear Picture Box",command=clear_picture)

view_menu=Menu(menubar,tearoff=0)
theme_menu=Menu(view_menu,tearoff=0)
theme_menu.add_command(label="Light",command=view_light)
theme_menu.add_command(label="Dark",command=view_dark)

about_menu=Menu(menubar,tearoff=0)
support_menu=Menu(about_menu,tearoff=0)
about_menu.add_cascade(label="Support",menu=support_menu)
support_menu.add_command(label="GitHub",command=help_github)
about_menu.add_command(label="Autor",command=info_autor)

menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="Edit",menu=edit_menu)
menubar.add_cascade(label="View",menu=view_menu)
menubar.add_cascade(label="Help",menu=about_menu)
view_menu.add_cascade(label="Theme",menu=theme_menu)

window.config(menu=menubar)
#----------------------------------------------------------------------
#top_paned
top_Paned_window=PanedWindow(window,bg="gray",orient=HORIZONTAL)
top_Paned_window.pack(fill="both",expand=1)

#pic_frame
top_pic=LabelFrame(top_Paned_window,text="Top Pic")
top_Paned_window.add(top_pic,stretch="never",width=250,height=5)

label_picture=Label(top_pic,image=None)
label_picture.pack()

#text_frame
top_text=LabelFrame(top_Paned_window,text="Top text")
top_Paned_window.add(top_text,stretch="never",width=250,height=5)
user_text=Text(top_text)
user_text.pack()

#----------------------------------------------------------------
#Bottom_Paned
bottom_paned_window=PanedWindow(window,bg="white",orient=VERTICAL,sashpad=1)
bottom_paned_window.pack(fill=BOTH,expand=1)

#Bottom_Fram
config_paned=LabelFrame(bottom_paned_window,text="Config",bg="#CFD8DC")
bottom_paned_window.add(config_paned)

#Status_Label
status_label=Label(config_paned,bg="#CFD8DC")
status_label.pack()

#Button_of_Bottom
decode_button=Button(config_paned,text="Decode",bd=6 ,font="Tahoma 15",highlightcolor="gray",width=10,command=decoing)
Encode_button=Button(config_paned,text="Encode",bd=6 ,font="Tahoma 15",highlightcolor="gray",width=10,command=endocing)
Encode_button.place(x=70,y=55)
decode_button.place(x=300,y=55)

#radio_of_bottom
Choise=StringVar()
Choise.set("Light")

Radio_dark=Radiobutton(config_paned,text="Dark",variable=Choise,value="Dark",font="Tahoma 13",bg="#CFD8DC",command=Them_Dark)
Radio_dark.place(x=235,y=190,anchor=W)
Radio_light=Radiobutton(config_paned,text="Light",variable=Choise,value="Light",font="Tahoma 13",bg="#CFD8DC",command=Them_Dark)
Radio_light.place(x=235,y=165,anchor=W)

Radio_Label=Label(config_paned,text="Theme : ",font="Tahoma 12 ",bg="#CFD8DC")
Radio_Label.place(x=166,y=164)

#author
autor_label=Label(config_paned,text=None)
pic_exit=r"*.png *.jpg *.jpeg"

#--------------------------------------------------------------------------
window.mainloop()

