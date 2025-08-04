import datetime
import json
import sys
import tkinter
from tkinter import messagebox as msg

import ctypes
PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

root = tkinter.Tk()
root.title('考试倒计时')
# root.attributes('-topmost', True)
root.resizable(False, False)
root.attributes('-toolwindow', True)
root.config(bg='red')
closed = False
rop = None

if len(sys.argv) > 1:
    try:
        json.loads(open(sys.argv[1], encoding='utf-8').read())
    except:
        msg.showerror('设置失败', '目标文件格式错误，设置失败')
    else:
        with open(sys.argv[0].rsplit('.', 1)[0]+'.config', 'w', encoding='utf-8') as f:
            f.write(sys.argv[1])
        msg.showinfo('设置成功', f'目标文件已设置为：\n{sys.argv[1]}')
try:
    with open(sys.argv[0].rsplit('.', 1)[0]+'.config', 'r', encoding='utf-8') as f:
        path = f.read()
except:
    with open(sys.argv[0].rsplit('.', 1)[0]+'.config', 'w', encoding='utf-8') as f:
        f.write(sys.argv[0].rsplit('.', 1)[0]+'.json')
        path = sys.argv[0].rsplit('.', 1)[0]+'.json'
try:
    labels = json.loads(open(path, encoding='utf-8').read())
except:
    msg.showerror('日程文件错误', f'日程文件"{path}"不存在或格式错误，请检查或重新生成并设置日程文件！')
    sys.exit(-1)

numbers4x8 = [
    '0110'
    '1001'
    '1001'
    '1001'
    '1001'
    '1001'
    '1001'
    '0110',
    '0010'
    '0110'
    '1010'
    '0010'
    '0010'
    '0010'
    '0010'
    '1111',
    '0110'
    '1001'
    '0001'
    '0001'
    '0010'
    '0100'
    '1000'
    '1111',
    '0110'
    '1001'
    '0001'
    '0110'
    '0001'
    '0001'
    '1001'
    '0110',
    '0001'
    '0011'
    '0101'
    '1001'
    '1111'
    '0001'
    '0001'
    '0001',
    '1111'
    '1000'
    '1000'
    '1110'
    '0001'
    '0001'
    '0001'
    '1110',
    '0110'
    '1000'
    '1000'
    '1110'
    '1001'
    '1001'
    '1001'
    '0110',
    '1111'
    '0001'
    '0010'
    '0010'
    '0100'
    '0100'
    '0100'
    '0100',
    '0110'
    '1001'
    '1001'
    '0110'
    '1001'
    '1001'
    '1001'
    '0110',
    '0110'
    '1001'
    '1001'
    '1001'
    '0111'
    '0001'
    '1001'
    '0110'
]

number100 = {(i%10, i//10) for i, c in enumerate('0000000000'
                                                 '0010111111'
                                                 '0110001000'
                                                 '0010011110'
                                                 '0010010010'
                                                 '0010011110'
                                                 '0010010010'
                                                 '0010010010'
                                                 '0111011110'
                                                 '0000000000') if c == '1'}

n2 = {i:{(1+j%4, 1+j//4) for j, c in enumerate(numbers4x8[i]) if c == '1'} for i in range(10)}
n3 = {i:{(6+j%4, 1+j//4) for j, c in enumerate(numbers4x8[i]) if c == '1'} for i in range(10)}
nc = {i:{(3+j%4, 1+j//4) for j, c in enumerate(numbers4x8[i]) if c == '1'}|{(i%10, i//10) for i, c in enumerate('0000000000'
                                                                                                                '1000000001'
                                                                                                                '1000000001'
                                                                                                                '1000000001'
                                                                                                                '1000000001'
                                                                                                                '1000000001'
                                                                                                                '1000000001'
                                                                                                                '0000000000'
                                                                                                                '1000000001'
                                                                                                                '0000000000') if c == '1'} for i in range(10)}

# n2a = set(map(lambda x: (1, x), range(2, 5)))
# n2b = set(map(lambda x: (x, 4), range(1, 5)))
# n2c = set(map(lambda x: (x, 4), range(4, 9)))
# n2d = set(map(lambda x: (8, x), range(2, 5)))
# n2e = set(map(lambda x: (x, 2), range(4, 9)))
# n2f = set(map(lambda x: (x, 2), range(1, 5)))
# n2g = set(map(lambda x: (4, x), range(2, 5)))
# n2 = {
#     1: n2b|n2c,
#     2: n2a|n2b|n2g|n2e|n2d,
#     3: n2a|n2b|n2c|n2d|n2g,
#     4: n2f|n2g|n2b|n2c,
#     5: n2a|n2f|n2g|n2c|n2d,
#     6: n2a|n2f|n2e|n2d|n2c|n2g,
#     7: n2a|n2b|n2c,
#     8: n2a|n2b|n2c|n2d|n2e|n2f|n2g,
#     9: n2a|n2f|n2g|n2b|n2c|n2d,
#     0: n2a|n2b|n2c|n2d|n2e|n2f
# }
# n3a = set(map(lambda x: (1, x+4), range(2, 5)))
# n3b = set(map(lambda x: (x, 4+4), range(1, 5)))
# n3c = set(map(lambda x: (x, 4+4), range(4, 9)))
# n3d = set(map(lambda x: (8, x+4), range(2, 5)))
# n3e = set(map(lambda x: (x, 2+4), range(4, 9)))
# n3f = set(map(lambda x: (x, 2+4), range(1, 5)))
# n3g = set(map(lambda x: (4, x+4), range(2, 5)))
# n3 = {
#     1: n3b|n3c,
#     2: n3a|n3b|n3g|n3e|n3d,
#     3: n3a|n3b|n3c|n3d|n3g,
#     4: n3f|n3g|n3b|n3c,
#     5: n3a|n3f|n3g|n3c|n3d,
#     6: n3a|n3f|n3e|n3d|n3c|n3g,
#     7: n3a|n3b|n3c,
#     8: n3a|n3b|n3c|n3d|n3e|n3f|n3g,
#     9: n3a|n3f|n3g|n3b|n3c|n3d,
#     0: n3a|n3b|n3c|n3d|n3e|n3f
# }
def get_block(days):
    phn, dspn = divmod(days, 100)
    if dspn == 0:
        phn -= 1
        dspn = 100
    if phn == 0:
        pht = f'仅剩{dspn}天'
    else:
        pht = f'+{phn}00'
    dspn1, dspnr = divmod(dspn, 100)
    dspn2, dspn3 = divmod(dspnr, 10)
    if dspn == 100:
        bn = number100
    elif dspn2 == 0:
        bn = nc[dspn3]
    else:
        bn = n2[dspn2]|n3[dspn3]
    lines = []
    for ln in range(10):
        line = []
        for col in range(10):
            if ln*10+col+1 <= dspn:
                if (col, ln) in bn:
                    line.append('★')
                else:
                    line.append('▧')
            else:
                if (col, ln) in bn:
                    line.append('☆')
                # elif phn:
                #     line.append(' ')
                else:
                    line.append(' ')
        lines.append(line)
    return lines, pht

def change_block(text, fg1, fg2, bg, change_color):
    for l1, l2 in zip(text, blocks):
        for s, b in zip(l1, l2):
            b['text'] = s
            if change_color:
                b['fg'] = fg1 if s in '★☆' else fg2
                b['bg'] = bg
            else:
                b['fg'] = 'red' if s in '★☆' else 'black'

max_text = ''
for label in labels[:]:
    if len(label[0]) > len(max_text):
        max_text = label[0]
    if datetime.date(label[1], label[2], label[3]) <= datetime.date.today():
        labels.remove(label)
labels.sort(key=lambda x: datetime.date(x[1], x[2], x[3]))

# [名称, 年, 月, 日, 背景颜色, 文本颜色, 强调文本颜色, 精确?]
texts = [
    (
        f'距离{name}{"还" if precious else "约"}有',
        f'{(datetime.date(year, month, day) - datetime.date.today()).days}天',
        bg, lg, tg, get_block((datetime.date(year, month, day) - datetime.date.today()).days)
    )
    for name, year, month, day, bg, lg, tg, precious in labels
]


tid = 0
last_turn_after = None


def turn_next(*args):
    global tid, last_turn_after
    tid += 1
    tid %= len(texts)
    current_ = texts[tid]
    if not closed:
        root['bg'] = current_[2]
        tit['bg'] = current_[2]
        timetit['bg'] = current_[2]
        tit['fg'] = current_[3]
        timetit['fg'] = current_[4]
        phnl['bg'] = current_[2]
        phnl['fg'] = current_[3]
        btf['bg'] = current_[2]
        
    change_block(current_[5][0], current_[4], current_[3], current_[2], not closed)
    phnl['text'] = current_[5][1]
    tit['text'] = current_[0]
    timetit['text'] = current_[1]
    last_turn_after = root.after(60 * 1000, turn_next)
    # root.after(3 * 1000, turn_next)


close_time = -1
last_close_after = None
on_close_event = False


def on_close(*args):
    global close_time, on_close_event, last_close_after
    on_close_event = True
    close_time += 1
    close_time %= len(close_events)
    if last_close_after:
        root.after_cancel(last_close_after)
    tit['width'] = 12
    tit['text'] = close_events[close_time][0]
    last_close_after = root.after(2000, close_event)


def on_see_through(*args):
    if not closed:
        close()
    else:
        reopen()


def close_event():
    global close_time, on_close_event
    current_ = texts[tid]
    tit['text'] = current_[0]
    tit['width'] = -1
    close_events[close_time][1]()
    close_time = -1
    on_close_event = False


def on_really_close():
    from tkinter import messagebox
    if messagebox.askokcancel("关闭确认", "确定要关闭吗?", default="cancel"):
        root.destroy()


def turn_to_next():
    global tid, last_turn_after
    if last_turn_after:
        root.after_cancel(last_turn_after)
    tid += 1
    tid %= len(texts)
    current_ = texts[tid]
    if not closed:
        root['bg'] = current_[2]
        tit['bg'] = current_[2]
        timetit['bg'] = current_[2]
        tit['fg'] = current_[3]
        timetit['fg'] = current_[4]
        phnl['bg'] = current_[2]
        phnl['fg'] = current_[3]
        btf['bg'] = current_[2]
        
    change_block(current_[5][0], current_[4], current_[3], current_[2], not closed)
    phnl['text'] = current_[5][1]
    tit['text'] = current_[0]
    timetit['text'] = current_[1]
    last_turn_after = root.after(60 * 1000, turn_next)
    # root.after(3 * 1000, turn_next)



close_events = [
    ("隐藏/显示", on_see_through),
    ("下一个日程", turn_to_next),
    ("再按3次关闭", lambda: None),
    ("再按2次关闭", lambda: None),
    ("再按1次关闭", lambda: None),
    ("关闭", on_really_close),
    ("取消", lambda: None)
]


def close(*args):
    global closed, rop
    root.attributes('-alpha', 0.4)
    closed = True
    tit['fg'] = 'black'
    timetit['fg'] = 'red'
    root['bg'] = '#F0F0F0'
    tit['bg'] = '#F0F0F0'
    timetit['bg'] = '#F0F0F0'
    
    btf['bg'] = '#F0F0F0'
    phnl['fg'] = 'black'
    phnl['bg'] = '#F0F0F0'
    for l in blocks:
        for b in l:
            b['fg'] = 'red' if b['text'] in '★☆' else 'black'
            b['bg'] = '#F0F0F0'
    root.attributes('-transparentcolor', '#F0F0F0')
    rop = root.after(5 * 60 * 1000, reopen)


def reopen(*args):
    global closed
    root.after_cancel(rop)
    root.attributes('-alpha', 1)
    closed = False
    root.attributes('-transparentcolor', '')
    current = texts[tid]
    root['bg'] = current[2]
    tit['bg'] = current[2]
    timetit['bg'] = current[2]
    tit['fg'] = current[3]
    timetit['fg'] = current[4]
    
    btf['bg'] = current[2]
    phnl['fg'] = current[3]
    phnl['bg'] = current[2]
    for l in blocks:
        for b in l:
            b['fg'] = current[4] if b['text'] in '★☆' else current[3]
            b['bg'] = current[2]

def check_iconic():
    root.geometry(f'+{max(0, min(root.winfo_screenwidth() - root.winfo_width() - 10, int(root.geometry().split("+")[-2])))}'
                  f'+{max(0, min(root.winfo_screenheight() - root.winfo_height() - 30, int(root.geometry().split("+")[-1])))}')
    root.after(10, check_iconic)


root.after(0, check_iconic)

tit = tkinter.Label(root, font=('default', 20))
tit.pack()
timetit = tkinter.Label(root, font=('default', 30, 'bold'))
timetit.pack()
btf = tkinter.Frame(root)
btf.pack()
blocks = []
for i in range(10):
    b_line = []
    for j in range(10):
        b = tkinter.Label(btf, font=('default', 10))
        b.grid(column=j, row=i)
        b_line.append(b)
    blocks.append(b_line)
phnl = tkinter.Label(btf)
phnl.grid(column=0, columnspan=10, row=10)
root.bind('<Enter>', lambda *args: root.attributes('-alpha', 0.4 if not closed else 0.4))
root.bind('<Leave>', lambda *args: root.attributes('-alpha', 1.0 if not closed else 0.4))
current = texts[tid]
root['bg'] = current[2]
tit['bg'] = current[2]
timetit['bg'] = current[2]
tit['fg'] = current[3]
timetit['fg'] = current[4]
tit['text'] = current[0]
timetit['text'] = current[1]
btf['bg'] = current[2]

phnl['bg'] = current[2]
phnl['fg'] = current[3]
change_block(current[5][0], current[4], current[3], current[2], not closed)
phnl['text'] = current[5][1]
last_turn_after = root.after(60 * 1000, turn_next)
# root.after(3 * 1000, turn_next)
root.protocol("WM_DELETE_WINDOW", on_close)
root.update()
root.geometry(f'+{root.winfo_screenwidth()-root.winfo_width()-10}+0')
root.mainloop()
