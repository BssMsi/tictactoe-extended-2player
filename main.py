from Tkinter import *


class TicTacToe:
    win = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8'], ['0', '3', '6'], ['1', '4', '7'], ['2', '5', '8'],
           ['0', '4', '8'], ['2', '4', '6']]

    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Extended TicTacToe")
        #self.root.state('zoomed')

        self.draw()
        self.root.mainloop()

    def draw(self):
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.main_frame = Frame(self.root, width=screen_width, height=screen_height, relief=SUNKEN)
        self.main_frame.grid(row=0, column=0)

        header = Frame(self.main_frame, width=screen_width, relief=RAISED)
        header.grid(row=0, columnspan=3)
        Label(header, text='EXTENDED TIC-TAC-TOE', font=("arial", 20, "bold")).grid(row=0)

        self.conq = []
        self.player = "X"
        self.board_status = dict()

        # Draw Board
        self.sub_frame = []
        for row in range(1, 4):
            for col in range(3):
                self.sub_frame.append(Frame(self.main_frame, width=screen_width / 3, height=screen_height / 3,
                                            highlightbackground='black', highlightthickness=2))
                self.sub_frame[-1].grid(row=row, column=col)
        # # Draw Buttons
        self.buttons = dict()
        for i in range(9):
            for j in range(9):
                self.buttons[str(i) + str(j)] = Button(self.sub_frame[i], width=screen_width / 81,
                                                       height=screen_height / 155, cursor='tcross',
                                                       command=lambda no=i, x=j: self.move(no, x), text=".")
                self.buttons[str(i) + str(j)].grid(row=j / 3, column=j % 3)
                self.board_status[str(i) + str(j)] = 0

        # Status Bar
        footer = Frame(self.main_frame, width=screen_width)
        footer.grid(row=4, columnspan=3)
        self.turn = Label(footer, text='Player' + self.player+' plays first', font=('times', 20, 'italic'))
        self.turn.grid(row=0)

    def act(self, frame_no):
        if frame_no in self.conq:
            for i in xrange(9):
                if i in self.conq:
                    for j in range(9):
                        self.buttons[str(i) + str(j)].configure(state=DISABLED, cursor='pirate')
                    self.sub_frame[i].configure(highlightbackground='black')

                else:
                    for j in range(9):
                        self.buttons[str(i) + str(j)].configure(state=NORMAL,
                                                                cursor=('tcross', 'circle')[self.player == 'X'])
                    self.sub_frame[i].configure(highlightbackground='red')
        else:
            for i in range(9):
                if i == frame_no and i not in self.conq:
                    for j in range(9):
                        self.buttons[str(i) + str(j)].configure(state=NORMAL,
                                                                cursor=('tcross', 'circle')[self.player == 'X'])
                    self.sub_frame[i].configure(highlightbackground='red')

                else:
                    for j in range(9):
                        self.buttons[str(i)+str(j)].configure(state=DISABLED, cursor='pirate')
                    self.sub_frame[i].configure(highlightbackground='black')

    def check_small(self, i):
        i = str(i)
        for wins in self.win:
            if self.board_status[i + wins[0]] + self.board_status[i + wins[1]] + self.board_status[i + wins[2]] == 3:
                for j in range(9):
                    self.buttons[i + str(j)].configure(text=self.player, state=DISABLED)
                self.conq.append(int(i))
                break
            elif self.board_status[i + wins[0]] + self.board_status[i + wins[1]] + self.board_status[i + wins[2]] == -3:
                for j in range(9):
                    self.buttons[i + str(j)].configure(text=self.player, state=DISABLED)
                self.conq.append(int(i))
                break
        if len(self.conq) > 2:
            self.check_win()

    def check_win(self):
        for wins in self.win:
            flag = True
            for t in wins:
                print wins, self.conq
                if int(t) not in self.conq:
                    flag = False
                    break
            if flag is True:
                break
        if flag is True:
            self.main_frame.destroy()
            self.over_frame = Frame(self.root)
            self.over_frame.grid(row=0)
            Label(self.over_frame, text=self.player+' Wins').grid(row=0)
            Button(self.over_frame, text='New game', command=self.draw).grid(row=1)

    def move(self, i, j):
        self.buttons[str(i)+str(j)].configure(text=self.player)
        # Shift focus to corresponding cell
        self.act(j)
        if self.player == "X":
            self.board_status[str(i) + str(j)] = 1
            self.check_small(i)
            self.player = "O"
        else:
            self.board_status[str(i) + str(j)] = -1
            self.check_small(i)
            self.player = "X"
        self.turn.configure(text='Player ' + self.player + ' turn')


run = TicTacToe()
