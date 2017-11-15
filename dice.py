#coding:utf-8  
from Tkinter import *
import ttk
import tkMessageBox
import random

root = Tk()
root.title('Dice game')
# root.overrideredirect(True)
# class Game:
# 	def __init__(self, PlayerNumber):
# 		self.PlayerNumber = PlayerNumber
# 		self.PlayerValue = 0
# 		self.Message = ''
# 	def Game_rule(self, PlayerNumber):
# 		self.PlayerValue = random.randint(1, 6)
# 		self.Message = 'Player'+str(PlayerNumber)+':'+str(self.PlayerValue)
# 		return self.PlayerValue, self.Message
# 	def show(self, Data):
# 		self.Data = Data
# 		print self.Data

def Event():
	PlayerValue1 = random.randint(1, 6)
	print 'Player1 get:'+' '+str(PlayerValue1)
	PlayValueShow1 = ttk.Entry()
	PlayValueShow1.insert (0, 'Player1 get:'+' '+str(PlayerValue1))                                         
	PlayValueShow1.grid(column=0, row=1, pady=15, sticky = W)
def Event2():
	PlayerValue1 = random.randint(1, 6)
	print 'Player2 get:'+' '+str(PlayerValue1)
	PlayValueShow1 = ttk.Entry()
	PlayValueShow1.insert (0, 'Player2 get:'+' '+str(PlayerValue1))                                         
	PlayValueShow1.grid(column=1, row=1, pady=15, sticky = W)
def ClearEntry():
	PlayValueShow1 = ttk.Entry()
	PlayValueShow1.delete (0, 'end')                                         
	PlayValueShow1.grid(column=0, row=1, pady=15, sticky = W)
	PlayValueShow1 = ttk.Entry()
	PlayValueShow1.delete (0, 'end')                                         
	PlayValueShow1.grid(column=1, row=1, pady=15, sticky = W)
	

	# def Result(self, PlayerNumber, PlayerValue):
	# 	self.Message = 'Player'+str(PlayerNumber)+':'+str(self.PlayerValue)
	# 	return self.Message

# Game(1).show(Game(1).Game_rule(1))
# # Play = Game(1)
# # PlayResult = Play.Game_rule(1)
# # print PlayResult
# # print PlayResult[0]

# Play1 = Game(2)
# print Play1.Game_rule(2)


# # print play

Play1 = Button(root, text='player1 start', command = Event)
Play1.grid(column=0, row=0)
Play1 = Button(root, text='player2 start', command = Event2)
Play1.grid(column=1, row=0)
# Play2 = Button(root, text='player2 play game', command = Game(2).Game_rule(2))
# Play2.grid(column=0, row=1)

PlayValueShow1 = ttk.Entry()                                     
PlayValueShow1.grid(column=0, row=1, pady=15, sticky = W)
PlayValueShow1 = ttk.Entry()                                     
PlayValueShow1.grid(column=1, row=1, pady=15, sticky = W)


Clear = ttk.Button(root, text='Restart game', command = ClearEntry)
Clear.grid(column=0, row=2)

root.update()
root.mainloop()


# from Tkinter import *  
  
# class App(object):  
#     """ 
#     建立左右两个列表，两个列表中的内容可以通过左右按钮交换 
#     """  
#     def __init__(self,root):  
#         self.language = 'Python','Perl','C','Ruby','PHP','Java'   
#         self.leftbox = StringVar()  
#         self.leftbox.set(self.language)  
#         self.rightbox = StringVar()  
#         self.rightbox.set('')  
             
#         self.list_left = Listbox(root, listvariable = self.leftbox, width = 16)  
#         self.list_left.pack(side = LEFT)  
  
#         self.frame = Frame(root)  
#         self.frame.pack(side = LEFT)  
#         Button(self.frame, text = '->', command = self.move_to_right, width = 7).pack(side = TOP)  
#         Button(self.frame, text = '<-', command = self.move_to_left, width = 7).pack(side = TOP)  
  
#         self.list_right = Listbox(root, listvariable = self.rightbox)  
#         self.list_right.pack(side = RIGHT)  
  
#     def move_to_right(self):  
#         """ 
#         将左列表中的内容移动到右列表中，用Listbox中的curselection()方法来捕捉鼠标选中的条目 
#         用delete()方法删除选中条目，用insert(END，)方法来向列表尾插入条目 
#         """  
#         self.list_right.insert(END,self.list_left.get(self.list_left.curselection()))  
#         self.list_left.delete(self.list_left.curselection())  
  
#     def move_to_left(self):  
#         self.list_left.insert(END,self.list_right.get(self.list_right.curselection()))  
#         self.list_right.delete(self.list_right.curselection())  
  
# if __name__ == '__main__':  
#     root = Tk()  
#     app = App(root)  
#     root.mainloop()  

# from Tkinter import *

# master = Tk()

# e = Entry(master)
# e.pack()

# e.focus_set()

# def callback():
#     print e.get()

# b = Button(master, text="get", width=10, command=callback)
# b.pack()

# mainloop()
# e = Entry(master, width=50)
# e.pack()

# text = e.get()
# def makeentry(parent, caption, width=None, **options):
#     Label(parent, text=caption).pack(side=LEFT)
#     entry = Entry(parent, **options)
#     if width:
#         entry.config(width=width)
#     entry.pack(side=LEFT)
#     return entry

# user = makeentry(parent, "User name:", 10)
# password = makeentry(parent, "Password:", 10, show="*")
# content = StringVar()
# entry = Entry(parent, text=caption, textvariable=content)

# text = content.get()
# content.set(text)

