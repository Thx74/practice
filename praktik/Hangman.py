from tkinter import *
import random as r

# Constant
WINDOW_WIDTN = 1200
WINDOW_HEIGHT = 800
MARGIN = 100
BG_COLOR = 'green'
BTN_COLOR = 'white'
TXT_COLOR = 'black'
SPEC_COLOR = 'black'
LINES_COLOR = 'yellow'
LINES_WIDTH = 4
FG_COLOR = 'red'
MAN_COLOR = 'beige'
label_word = []
btn_alpha = []

#vicilica
def start_pos_man():
    line_0_1 = canvas.create_line(MARGIN // 4, WINDOW_HEIGHT - (MARGIN // 2), MARGIN, WINDOW_HEIGHT - (MARGIN * 1.7), MARGIN * 1.1, WINDOW_HEIGHT - (MARGIN * 1.7), MARGIN // 2.8, WINDOW_HEIGHT - (MARGIN // 2), MARGIN // 4, WINDOW_HEIGHT - (MARGIN // 2), width=LINES_WIDTH, fill=LINES_COLOR)
    line_0_2 = canvas.create_line(MARGIN * 1.1, WINDOW_HEIGHT - (MARGIN * 1.7), MARGIN * 1.2, WINDOW_HEIGHT - (MARGIN * 1.7), MARGIN * 1.95, WINDOW_HEIGHT - (MARGIN // 2), MARGIN * 1.85, WINDOW_HEIGHT - (MARGIN // 2), MARGIN * 1.1, WINDOW_HEIGHT - (MARGIN * 1.7), width=LINES_WIDTH, fill=LINES_COLOR)
    line_0_3 = canvas.create_line(MARGIN * 1.05, WINDOW_HEIGHT - (MARGIN * 1.6), MARGIN * 1.05, WINDOW_HEIGHT - (MARGIN // 2), MARGIN * 1.15, WINDOW_HEIGHT - (MARGIN // 2), MARGIN * 1.15, WINDOW_HEIGHT - (MARGIN * 1.6), width=LINES_WIDTH, fill=LINES_COLOR)
    
    line_1 = canvas.create_line(MARGIN, WINDOW_HEIGHT - (MARGIN * 1.7), MARGIN, MARGIN // 1.25, MARGIN * 1.2, MARGIN // 1.25, MARGIN * 1.2, WINDOW_HEIGHT - (MARGIN * 1.7), width=LINES_WIDTH, fill=LINES_COLOR)
    
    line_2_1 = canvas.create_line(MARGIN, MARGIN, MARGIN // 2, MARGIN, MARGIN // 2, MARGIN * 1.2, MARGIN, MARGIN * 1.2, width=LINES_WIDTH, fill=LINES_COLOR)
    line_2_2 = canvas.create_line(MARGIN * 1.2, MARGIN, MARGIN * 3.5, MARGIN, MARGIN * 3.5, MARGIN * 1.2, MARGIN * 1.2, MARGIN * 1.2, width=LINES_WIDTH, fill=LINES_COLOR)
    
    line_3_1 = canvas.create_line(MARGIN * 3.2, MARGIN, MARGIN * 3.2, MARGIN // 1.25, MARGIN * 3.3, MARGIN // 1.25, MARGIN * 3.3, MARGIN, width=LINES_WIDTH, fill=LINES_COLOR)
    line_3_2 = canvas.create_line(MARGIN * 3.3, MARGIN * 1.2, MARGIN * 3.3, MARGIN * 2, MARGIN * 3.2, MARGIN * 2, MARGIN * 3.2, MARGIN * 1.2, width=LINES_WIDTH, fill=LINES_COLOR)
    
#alphabet
def start_pos_alphabet():
    shift_x = shift_y = 0
    count = 0
    
    for c in range(ord('А'), ord('Я') + 1):
        btn = Button(text=chr(c), bg=BTN_COLOR, foreground=TXT_COLOR, font='Arial 19', relief=SOLID)
        btn.place(x=WINDOW_HEIGHT - MARGIN*2 + shift_x, y=MARGIN*4.5 - shift_y)
        btn.bind('<Button-1>', lambda event: check_alpha(event, word))
        btn_alpha.append(btn)
        shift_x += 65
        count += 1
        
        if (count == 8):
            shift_x = count = 0
            shift_y -= 65
            
#word
def start_word():
    count = 0
    f = open('words.txt', encoding='utf-8')
    
    for s in f:
        count += 1
        
    num_word = r.randint(1, count)
    word = ''
    count = 0
        
    f = open('words.txt', encoding='utf-8')
    
    for s in f:
        count += 1
        
        if(count == num_word):
            word = s[:len(s) - 1:]
        
    word = word.upper()
    return word

#word in __
def start_pos_word(word):
    shift = 0
    
    for i in range(len(word)):
        label_under = Label(window, text='__', font='Arial 24', bg=BG_COLOR, foreground=FG_COLOR)
        label_under.place(x = WINDOW_HEIGHT - MARGIN*2 + shift, y= MARGIN*3.5)
        shift += 50
        label_word.append(label_under)
        
# draw man
def draw(lifes):
    if (lifes == 4):
        head = canvas.create_oval(MARGIN * 2.95, MARGIN * 2, MARGIN * 3.55, MARGIN * 2.6, fill=MAN_COLOR)
    elif (lifes == 3):
        body = canvas.create_oval(MARGIN * 2.95, MARGIN * 2.6, MARGIN * 3.55, MARGIN * 4.1, fill=MAN_COLOR)
    elif (lifes == 2):
        left_hand = canvas.create_line(MARGIN * 3, MARGIN * 3, MARGIN * 2.3, MARGIN * 2.3, width=6, fill=MAN_COLOR)
        right_hand = canvas.create_line(MARGIN * 3.5, MARGIN * 3, MARGIN * 4.2, MARGIN * 2.3, width=6, fill=MAN_COLOR)
    elif (lifes == 1):
        left_foot = canvas.create_line(MARGIN * 3.1, MARGIN * 3.9, MARGIN * 2.5, MARGIN * 5.6, width=7, fill=MAN_COLOR)
        right_foot = canvas.create_line(MARGIN * 3.4, MARGIN * 3.9, MARGIN * 4, MARGIN * 5.6, width=6, fill=MAN_COLOR)
    elif (lifes == 0):
        game_over('lose')
        
# check alphabet
def check_alpha(event, word):
    alpha = event.widget['text']
    pos = []
    
    for i in range(len(word)):
        if (word[i] == alpha):
            pos.append(i)
            
    if (pos):
        for i in pos:
            label_word[i].config(text='{}'.format(word[i]))
            
        count_alpha = 0
        
        for i in label_word:
            if (i['text'].isalpha()):
                count_alpha += 1
                
        if (count_alpha == len(word)):
            game_over('win')
    
    else:
        lifes = int(label_life.cget('text')) - 1
        
        if (lifes != 0):
            label_life.config(text=' {}'.format(lifes))
        
        draw(lifes)
            
# if game over or win
def game_over(status):
    for btn in btn_alpha:
        btn.destroy()
        
    if (status == 'win'):
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 100, font=('Futura PT Heave', 50), text='   ПОБЕДА\nпоздравляем', fill=SPEC_COLOR)
    
    else:
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 100, font=('Futura PT Heave', 50), text='   ПРОВАЛ\nпопробуй еще', fill=SPEC_COLOR)
    
window = Tk()
window.title('Висилица')
window.resizable(False, False)

lifes = 5

label_text = Label(window, text='Жизни:', font=('Futura PT Heave', 40), foreground=TXT_COLOR)
label_text.place(x=930, y= 10)
label_life = Label(window, text=' {}'.format(lifes), font=('Futura PT Heave', 40), foreground=TXT_COLOR)
label_life.place(x=1110, y=10)

canvas = Canvas(window, bg=BG_COLOR, height=WINDOW_HEIGHT, width=WINDOW_WIDTN)
canvas.place(x=0, y=70)

window.geometry('1200x880')

start_pos_man()
start_pos_alphabet()
word = start_word()
start_pos_word(word)
#print(word) #output the response to the console

window.mainloop()