import main as xp
import setup as s
import commands as cmds
import curses
import sys
import os

def readin():
    content = input(f"{s.bcolors.OKGREEN}What text do you want to output?\n>>>{s.bcolors.ENDC}")
    print(content)
    #When importing remove content

def clear():
  curses.setupterm()
  e3 = curses.tigetstr('E3') or b''
  clear_screen_seq = curses.tigetstr('clear') or b''
  os.write(sys.stdout.fileno(), e3 + clear_screen_seq)

def logout():
    clear()
    exit()