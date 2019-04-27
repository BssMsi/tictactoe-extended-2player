<<<<<<< HEAD
from tkinter import Tk, Frame, Label, Button, RAISED, NORMAL, DISABLED, N, S, W, E, Toplevel
from functools import partial
=======
from Tkinter import Tk, Frame, Label, Button, RAISED, NORMAL, DISABLED, N, S, W, E, Toplevel
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc


class TicTacToe:
    win = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8'], ['0', '3', '6'], ['1', '4', '7'], ['2', '5', '8'],
           ['0', '4', '8'], ['2', '4', '6']]

    def __init__(self):
        self.root = Tk()
<<<<<<< HEAD
        self.root.wm_title("2-player Extended TicTacToe")
=======
        self.root.wm_title("Extended TicTacToe")
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
        #self.root.state('zoomed')

        self.draw()
        self.root.mainloop()

    def draw(self):
<<<<<<< HEAD
        screen_width, screen_height = self.root.winfo_screenwidth()*0.7, self.root.winfo_screenheight()*0.7
=======
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc

        self.main_frame = Frame(self.root, width=screen_width, height=screen_height)
        self.main_frame.grid(row=0, column=0)

        header = Frame(self.main_frame, width=screen_width, relief=RAISED)
        header.grid(row=0, columnspan=3)
        Label(header, text='EXTENDED TIC-TAC-TOE', font=("times", 25, "bold")).grid(row=0)

<<<<<<< HEAD
        self.conq = []      # Check for conquered blocks
=======
        self.conq = []
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
        self.player = "X"
        self.board_status = dict()

        # Draw Board
        self.sub_frame = []
<<<<<<< HEAD
        for row in range(1, 4):
            for col in range(3):
=======
        for row in xrange(1, 4):
            for col in xrange(3):
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
                self.sub_frame.append(Frame(self.main_frame, width=screen_width / 3, height=screen_height / 3,
                                            highlightbackground='black', highlightthickness=2))
                self.sub_frame[-1].grid(row=row, column=col)
        # # Draw Buttons
        self.buttons = dict()
<<<<<<< HEAD
        for i in range(9):
            for j in range(9):
                self.buttons[str(i) + str(j)] = Button(self.sub_frame[i],  width=int(screen_width / 100),
                                                       height=int(screen_height / 255), cursor='tcross', font=40,
                                                       command=partial(self.move, i, j), text=" ")
                self.buttons[str(i) + str(j)].grid(row=int(j / 3), column=int(j % 3))
=======
        for i in xrange(9):
            for j in xrange(9):
                self.buttons[str(i) + str(j)] = Button(self.sub_frame[i],  width=screen_width / 100,
                                                       height=screen_height / 255, cursor='tcross', font=40,
                                                       command=lambda no=i, x=j: self.move(no, x), text=".")
                self.buttons[str(i) + str(j)].grid(row=j / 3, column=j % 3)
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
                self.board_status[str(i) + str(j)] = 0

        # Status Bar
        footer = Frame(self.main_frame, width=screen_width)
        footer.grid(row=4, columnspan=3)
<<<<<<< HEAD
        self.turn = Label(footer, text='Player ' + self.player+' plays first', font=('times', 20, 'italic'))
=======
        self.turn = Label(footer, text='Player' + self.player+' plays first', font=('times', 20, 'italic'))
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
        self.turn.grid(row=0)

    def shift_focus(self, frame_no):
        if frame_no in self.conq:
<<<<<<< HEAD
            for i in range(9):
                if i in self.conq:
                    for j in range(9):
=======
            for i in xrange(9):
                if i in self.conq:
                    for j in xrange(9):
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
                        self.buttons[str(i) + str(j)].configure(state=DISABLED, cursor='pirate')
                    self.sub_frame[i].configure(highlightbackground='black')

                else:
<<<<<<< HEAD
                    for j in range(9):
=======
                    for j in xrange(9):
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
                        self.buttons[str(i) + str(j)].configure(state=NORMAL,
                                                                cursor=('circle', 'tcross')[self.player == 'X'])
                    self.sub_frame[i].configure(highlightbackground='red')
        else:
<<<<<<< HEAD
            for i in range(9):
                if i == frame_no and i not in self.conq:
                    for j in range(9):
=======
            for i in xrange(9):
                if i == frame_no and i not in self.conq:
                    for j in xrange(9):
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
                        self.buttons[str(i) + str(j)].configure(state=NORMAL,
                                                                cursor=('circle', 'tcross')[self.player == 'X'])
                    self.sub_frame[i].configure(highlightbackground='red')

                else:
<<<<<<< HEAD
                    for j in range(9):
=======
                    for j in xrange(9):
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
                        self.buttons[str(i)+str(j)].configure(state=DISABLED, cursor='pirate')
                    self.sub_frame[i].configure(highlightbackground='black')

    def check_small(self, i):
        i = str(i)
        for wins in self.win:
            if self.board_status[i + wins[0]] + self.board_status[i + wins[1]] + self.board_status[i + wins[2]] == 3:
<<<<<<< HEAD
                for j in range(9):
=======
                for j in xrange(9):
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
                    self.buttons[i + str(j)].configure(text=self.player, state=DISABLED)
                self.conq.append(int(i))
                break
            elif self.board_status[i + wins[0]] + self.board_status[i + wins[1]] + self.board_status[i + wins[2]] == -3:
<<<<<<< HEAD
                for j in range(9):
=======
                for j in xrange(9):
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
                    self.buttons[i + str(j)].configure(text=self.player, state=DISABLED)
                self.conq.append(int(i))
                break
        if len(self.conq) > 2:
            self.check_win()

    def check_win(self):
        for wins in self.win:
            flag = True
            for t in wins:
                if int(t) not in self.conq:
                    flag = False
                    break
            if flag is True:
                break
        if flag is True:
<<<<<<< HEAD
            # Disable Current Frame
            for child in self.main_frame.winfo_children():
                child.configure(state='disable')
            # Notify Winner
            t = Toplevel(self.root)
            self.over_frame = Frame(t, width=100, height=100)
=======
            t = Toplevel(self.root)
            self.over_frame = Frame(t)
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc
            self.over_frame.grid(row=0)
            Label(self.over_frame, text=self.player+' Wins').grid(row=0)
            Button(self.over_frame, text='New game', command=self.draw).grid(row=1)

    def move(self, i, j):
<<<<<<< HEAD
        if self.buttons[str(i)+str(j)]['text'].strip() == "":
            self.buttons[str(i)+str(j)].configure(text=self.player)

            if self.player == "X":
                self.board_status[str(i) + str(j)] = 1
                self.check_small(i)
                self.player = "O"
            else:
                self.board_status[str(i) + str(j)] = -1
                self.check_small(i)
                self.player = "X"

            # Shift focus to corresponding cell
            self.shift_focus(j)
            self.turn.configure(text='Player ' + self.player + ' turn')
=======
        self.buttons[str(i)+str(j)].configure(text=self.player)

        if self.player == "X":
            self.board_status[str(i) + str(j)] = 1
            self.check_small(i)
            self.player = "O"
        else:
            self.board_status[str(i) + str(j)] = -1
            self.check_small(i)
            self.player = "X"

        # Shift focus to corresponding cell
        self.shift_focus(j)
        self.turn.configure(text='Player  ' + self.player + ' turn')
>>>>>>> 2530b55a297a9872102814a84b04904e3ace5dcc


run = TicTacToe()
