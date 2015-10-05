from tkinter import *
import tkinter 
from tkinter import Canvas
from builtins import range
import time
import tkinter.messagebox

#from FinalSUDOKU_GUI import count_down

#import tkMessageBox
#from timer import count_down
#from FinalSUDOKU_GUI import mbutton6
x=10
y=10
r=0
a=[[0,0,0,0,9,5,0,0,8],[3,0,0,7,0,0,0,0,0],[0,2,0,0,0,1,0,6,0],[0,0,0,2,7,3,0,9,0],[0,6,2,0,5,0,7,0,0],[0,0,0,0,0,0,0,0,0],[9,3,1,0,0,0,0,0,0],[0,0,0,0,2,0,4,0,0],[0,0,0,0,6,0,0,1,9]]
n=[[0,0,0,0,9,5,0,0,8],[3,0,0,7,0,0,0,0,0],[0,2,0,0,0,1,0,6,0],[0,0,0,2,7,3,0,9,0],[0,6,2,0,5,0,7,0,0],[0,0,0,0,0,0,0,0,0],[9,3,1,0,0,0,0,0,0],[0,0,0,0,2,0,4,0,0],[0,0,0,0,6,0,0,1,9]]

l=[[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1]]
m=[[4,1,7,6,9,5,3,2,8],[3,5,6,7,8,2,9,4,1],[8,2,9,4,3,1,5,6,7],[5,8,4,2,7,3,1,9,6],[1,6,2,9,5,4,7,8,3],[7,9,3,8,1,6,2,5,4],[9,3,1,5,4,8,6,7,2],[6,7,8,1,2,9,4,3,5],[2,4,5,3,6,7,8,1,9]]

                    
class SudokuBoard:
   
    def get_row(self, row):
        return self.grid[row]

    def get_cols(self, col):
        return [y[col] for y in self.grid]
    
    def get_nearest_region(self,row,col):
        def make_index(v):
            if v <= 2:
                return 0
            elif v <= 5:
                return 3
            else:
                return 6
        return [y[make_index(col):make_index(col)+3] for y in 
                self.grid[make_index(row):make_index(row)+3]]

    def set(self, row,col, v, lock= False):
        print("Inside set")
        print(row)
        print(col)
        print(v)
        if v == self.grid[row][col] or (row,col) in self.locked:
            return
        for v2 in self.get_row(row):
            if v == v2:
                raise ValueError()
        for v2 in self.get_cols(col):
            if v == v2:
                raise ValueError()
        for y in self.get_nearest_region(row,col):
            for x in y:
                if v == x:
                    raise ValueError()
        self.grid[row][col] = v
        if lock:
            self.locked.append((row.col))

    def get(self, row,col):
        return self.grid[row][col]
    
    def __init__(self):
        self.clear()

    def clear(self):
        self.grid = [[0 for x in range(9)] for y in range(9)]
        self.locked = []


 
   
class SudokuGUI():
    def closewindow(self):
        #answer=tkinter.messagebox.askyesno("Sudoku", "Do you want to exit??")
        #if answer==True:
        exit()
            
                
    def new_game(self):
        self.board.clear()
        #self.generate_input()
        #h=2
        self.sync_board(x,y,r)
        
    def construct_grid(self):
        print("Inside construct grid")
        c = Canvas(master,width=530,height=530,bg='yellow')
        c.pack()
    
        self.rectangle1 = [[None for x in range(9)]for y in range (9)]
        self.handles = [[None for x in range(9)] for y in range(9)]
        cellsize = 530/9 
        gridsize = 530/3 
    
        for x in range(9):
            for y in range(9):
                (xr, yr) = (x*gridsize, y*gridsize)
                self.rectangle1[x][y] = c.create_rectangle(xr+2, yr+2, xr+gridsize, yr+gridsize, width=3)
                (xr, yr) = (x*cellsize, y*cellsize)
                r = c.create_rectangle(xr+1, yr+1, xr+cellsize, yr+cellsize,width=1)  
                t = c.create_text(xr+cellsize/2, yr+cellsize/2, text="",font="System 15 bold")
                self.handles[x][y] = (r, t)
        self.canvas=c

        
    def sync_board(self,x,y,r):
        g = self.board.grid
        if x==10 and y==10:
            g=[[0,0,0,0,9,5,0,0,8],[3,0,0,7,0,0,0,0,0],[0,2,0,0,0,1,0,6,0],[0,0,0,2,7,3,0,9,0],[0,6,2,0,5,0,7,0,0],[0,0,0,0,0,0,0,0,0],[9,3,1,0,0,0,0,0,0],[0,0,0,0,2,0,4,0,0],[0,0,0,0,6,0,0,1,9]]
            print("just to print")   
            for x in range(9):
                for y in range(9):
                    if l[x][y]==1 and g[x][y]!=0:
                        r= g[x][y]
                        l[x][y]=0
                        if r!= 0:
                            self.canvas.itemconfig(self.handles[x][y][1], 
                                                   text=int(r))
                            self.board.set(x, y,r)
                        else:
                            self.canvas.itemconfig(self.handles[x][y][1], 
                                                   text= '') 
                    
        else:
            #g=[[0,0,0,0,9,5,0,0,8],[3,0,0,7,0,0,0,0,0],[0,2,0,0,0,1,0,6,0],[0,0,0,2,7,3,0,9,0],[0,6,2,0,5,0,7,0,0],[0,0,0,0,0,0,0,0,0],[9,3,1,0,0,0,0,0,0],[0,0,0,0,2,0,4,0,0],[0,0,0,0,6,0,0,1,9]]
            a[x][y]=r               
            for x in range(9):
                for y in range(9):
                    r= a[x][y]
                    if l[x][y]==1 and r!=0:
                        if r!= 0:
                            self.canvas.itemconfig(self.handles[x][y][1], 
                                                   text=int(r))
                        else:
                            self.canvas.itemconfig(self.handles[x][y][1], 
                                                   text= '') 
        #self.generate_input(g)
        #print("hello")
    def help(self,x,y):
        print("entered in help")
        #self.canvas.bind("<Button-1>", self.canvas_click)
        print (x)
        print(y)
       
        z=m[x][y]
        #a[x][y]=z
        self.canvas.itemconfig(self.handles[x][y][1], 
                                   text=int(z))
        self.board.set(x, y,z)
    
            
    def count_down(self):
        for t in range(600, -1, -1):
                sf = "{:02d}:{:02d}".format(*divmod(t, 60))
                time_str.set(sf)
                master.update()
                time.sleep(1) 
                   

    def show_solution(self):
        answer=tkinter.messagebox.askyesno("Sudoku", "Do you want to see the solution??")
        if answer == True:
            for x in range(9):
                        for y in range(9):
                           
                            z=m[x][y]
                            #a[x][y]=z
                            self.canvas.itemconfig(self.handles[x][y][1], 
                                                       text=int(z))
                            self.board.set(x, y,z)
            answer=tkinter.messagebox.askyesno("Sudoku", "Do you want to play again??")
            if answer==True:
                self.startagain()
                    #self.count_down()
                        
    
                    
    def startagain(self):
        answer=tkinter.messagebox.askyesno("Sudoku", "Do you want to load puzzle??")
        if answer==True:
            for x in range(9):
                        for y in range(9):
                            z=n[x][y]
                            if z!=0:
                                self.canvas.itemconfig(self.handles[x][y][1], 
                                                           text=int(z))
                                self.board.set(x, y,z)
                            else:
                                self.canvas.itemconfig(self.handles[x][y][1], 
                                                           text='')
            self.count_down()
            answer=tkinter.messagebox.askyesno("Sudoku", "Time over: Do you want to see the solution???")
            print(answer)
            if answer == True:
                self.show_solution()  
            else:
                self.startagain()
            
    def checksol(self):
        for x in range(9):
                    for y in range(9):
                        if a[x][y]==m[x][y]:
                            flag=1
                        else:
                            flag=0
                            break
        if flag==1:
            tkinter.messagebox.showinfo("Sudoku", "You win")
            print("you win")
            
        else:
            tkinter.messagebox.showinfo("Sudoku", "You lose try again")
            print("you lose")
            self.startagain()
            
        #self.count_down()
        
           
    def canvas_key(self,event):
        #self.board=self.sync_board()
        #q=1
        
        print("Inside canvas key")
        print("Click! (%s)" % (event.char))
        if event.char.isdigit() and int(event.char) >= 0 and self.current:
            (x,y) = self.current
        r=int(event.char)
        print(r)
        if r!=0:
          
            try:
                self.board.set(x, y,int(event.char))
                self.sync_board(x,y,r)
                
                
            except ValueError:
                tkinter.messagebox.showinfo("Sudoku", "you cannot insert that value here")
                pass
                
        else:
            answer=tkinter.messagebox.askyesno("Sudoku", "Do you want help??")
            if answer==True:
                self.help(x,y)
            
            
        return
    
    def canvas_click(self,event):
        
        print("Inside  canvas click")
        print("Click! (%d,%d)" % (event.x, event.y))
        self.canvas.focus_set()
        rsize = 512/9
        (x,y) = (0, 0)
        if event.x > rsize:
            x = int(event.x/rsize)
        if event.y > rsize:
            y = int(event.y/rsize)
        print(x,y)
        #mlabel1 = tkinter.Label(text="Press 0 for help").place(x=event.x,y=event.y)
        
        
        #mlabel1.pack(side="bottom")
        if self.current:
            (tx, ty) = self.current
        self.current = (x,y)
        return
    
    def __init__(self,master,board):
        #tkinter.messagebox.showinfo("Sudoku", "Play and win")
        print("init called")
        self.board=board
        
        self.construct_grid()
        #tkinter.messagebox.showinfo("Sudoku", "Play and win")
        #mbutton1= tkinter.Button(master,text="NEW GAME",height=3,width=15,font="bold",command=self.new_game()).pack(side="left")
        mlabel3 = tkinter.Label(text="S\n\nU\n\nD\n\nO\n\nK\n\nU\n\n\n\nS\n\nO\n\nL\n\nV\n\nE\n\nR",fg='blue')
        mlabel3.place(x=380,y=0)
        mlabel1 = tkinter.Label(text="Press 0 \n to get help",fg='blue')
        mlabel1.place(x=950,y=0)
        
        mbutton2= tkinter.Button(master,text="LOAD PUZZLE",command=self.startagain,height=3,width=25,font="bold",bg="blue",fg="white")
        mbutton2.place(x=430,y=550)
        mbutton3= tkinter.Button(master,text="SUBMIT SOLUTION",command=self.checksol,height=3,width=25,font="bold",bg="blue",fg="white")
        mbutton3.place(x=430,y=625)
    
        mbutton4= tkinter.Button(master,text="SHOW SOLUTION",command=self.show_solution,height=3,width=25,font="bold",bg="blue",fg="white")
        mbutton4.place(x=700,y=550)
        
        mbutton6 = tkinter.Button(master,text="EXIT GAME",command=self.closewindow,height=3,width=25,font="bold",bg="blue",fg="white")
        mbutton6.place(x=700,y=625)
        
        #mbutton5 = tkinter.Button(master, text='MEDIUM', command=self.medium,height=3,width=15,font="bold")
        #mbutton5.pack(side="left")
       
        
        mlabel = tkinter.Label(master,textvariable=time_str)
        mlabel.pack(side="top")
        #mlabel1.pack(side="bottom")
        self.canvas.bind("<Button-1>", self.canvas_click)
        self.canvas.bind("<Key>", self.canvas_key)
        self.current = None
        
                            
if __name__ == '__main__':
    print("main called")
    board = SudokuBoard()
    master = tkinter.Tk()
    master.title("SUDOKU PUZZLE")
    
    time_str = tkinter.StringVar()
    gui = SudokuGUI(master,board)
    master.geometry('1500x1000')
    master.mainloop()

