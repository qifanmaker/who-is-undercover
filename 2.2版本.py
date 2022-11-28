"""
作者：启帆创客
版权归 启帆创客 所有
侵权必究
"""
import random
import tkinter as tk
import tkinter.messagebox
from database import *    #数据库
def main():
    window = tk.Tk()
    window.title("who's undercover")
    window.geometry('500x300')

    PP = tk.StringVar()
    tf = 0
    tk.Label(window, text='number of people:', font=('Arial', 12), width=60, height=2).place(x=-200, y=50)
    tk.Entry(window, textvariable=PP, show=None, font=('Arial', 14)).place(x=150, y=60)
    def play():
        people = int(PP.get())
        if people <= 2:
            tk.messagebox.showerror(title='warning', message='Please enter a number greater than 2!')
        else:
            window_play = tk.Tk()
            window_play.title("play")
            window_play.geometry("500x300")

            words_number = random.randint(0,len(words)-1)   #在字典words的下标范围内，获取一个随机数
            words_class = words[str(words_number)]    #将字典words中找到words_number中储存的随机数对应的词语类
            ordinary = 0    #定义变量ordinary，意为普通
            undercover = 0   #定义变量undercover，意为卧底
            while ordinary == undercover:   #只要变量ordinary与undercover相同，就重新获取
                ordinary = eval(words_class)[random.randint(0,len(eval(words_class))-1)]    #在words_class中存储的词语类中随机获取一个词语，并存储在变量ordinaty中
                undercover = eval(words_class)[random.randint(0,len(eval(words_class))-1)]    #在words_class中存储的词语类中随机获取一个词语，并存储在变量undercover中
            lt = tk.Label(window_play, text='Please let players take turns to get words', font=('Arial', 12), width=60, height=2)
            lt.pack()
            def obtain():
                UCnumber =random.randint(0,people-1)   #在变量people的数值范围内获取一个随机数，并存储到变量UCnumber中，但因为要作为下标，需要-1
                player_number = 0
                for i in range(0,people):
                    if UCnumber == player_number:
                        tk.messagebox.showinfo(title='occlusion',message="")
                        tk.messagebox.showinfo(title='words',message=undercover)
                    else:
                        tk.messagebox.showinfo(title='occlusion',message="")
                        tk.messagebox.showinfo(title='words',message=ordinary)
                    player_number += 1
                tk.messagebox.showinfo(title='occlusion',message="undercover is ...")
                tk.messagebox.showinfo(title='words',message="卧底是"+str(UCnumber+1)+"号 ，是“"+str(undercover)+"” ，\n    平民是“"+str(ordinary)+"”。")
            OB = tk.Button(window_play, text="obtain", command=obtain)
            OB.pack()
    tk.Button(window, text="play", command=play).place(x=250, y=90)
    window.mainloop()
if __name__ == "__main__":
    main()

