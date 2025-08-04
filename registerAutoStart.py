import sys
import winreg
import rich
import os
import time
import tkinter as tk
from tkinter import filedialog
 
def open_file():
    filetypes = (
        ('可执行文件', '*.exe'),
        ('所有文件', '*.*')
    )
 
    filename = filedialog.askopenfilename(
        title='请选择考试倒计时的可执行文件',
        initialdir='.',
        filetypes=filetypes)
 
    return filename
 
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

def does_autorun_exist(name):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_READ)
        winreg.QueryValueEx(key, name)
        return True
    except FileNotFoundError:
        return False
    except PermissionError:
        return False

def set_autostart(on_off, name, path):
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Run',
        0,
        winreg.KEY_WRITE
    )
 
    if on_off:
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, path)
    else:
        winreg.DeleteValue(key, name)
    winreg.CloseKey(key)

KEY_NAME = "KaoShiDaoJiShi.PiYuanZhouLv"
exe_path = os.path.abspath("考试倒计时.exe")
rich.print(f'默认脚本位置：{os.path.abspath("考试倒计时.exe")}')
exe_exists = os.path.exists("考试倒计时.exe")
rich.print(f'是否检测到脚本：{"[green]是[/green]" if exe_exists else "[red]否[/red]"}')
rich.print(f'开机自启动是否开启：{"[green]是[/green]" if does_autorun_exist(KEY_NAME) else "[red]否[/red]"}')
choice = input("是否开启？[Y=开启;N=关闭]").upper()
if choice == "Y":
    try:
        if not exe_exists:
            path = open_file()
            if not path:
                rich.print('[red]未选择可执行文件路径，设置失败！[/red]')
                rich.print("程序运行结束，可以安全关闭窗口！如需操作请重新运行此程序")
                while True:
                    time.sleep(1)
                sys.exit(-1)
            exe_path = os.path.abspath(path)

        set_autostart(True, KEY_NAME, f'"{exe_path}"')
    except Exception:
        rich.get_console().print_exception()
        rich.print('[red]发生异常,设置失败[/red]')
        rich.print('[red]请检查错误或寻求专业人士帮助[/red]')
    else:
        rich.print('[green]设置成功！[/green]')
elif choice == "N":
    try:
        set_autostart(False, KEY_NAME, "")
    except Exception:
        rich.get_console().print_exception()
        rich.print('[red]发生异常,设置失败[/red]')
        rich.print('[red]请检查错误或寻求专业人士帮助[/red]')
    else:
        rich.print('[green]设置成功！[/green]')
else:
    rich.print('[yellow]未知指令，请输入Y或N！[/yellow]')

rich.print("程序运行结束，可以安全关闭窗口！如需操作请重新运行此程序")
while True:
    time.sleep(1)