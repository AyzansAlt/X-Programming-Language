import main as xp
import setup as s
import console
import time

cmd = input(xp.pointer)


while True:
#If the command contains help then
    if cmd.find("console.help()") != -1:
        print(f"{s.bcolors.OKBLUE}console.readin(): Prints the given data\nconsole.clear(): Clears the console\nconsole.logout(): Go back to Python3")
        cmd = input(xp.pointer)

    elif cmd.find("console.readin()") != -1:
        console.readin()
        cmd = input(xp.pointer)

    elif cmd.find("console.clear()") != -1:
        console.clear()
        print(f"[ {xp.xp} Programming Language ] [ Build 1.10 ] [ Default ] [ (C) 2020 ]")
        time.sleep(1)
        cmd = input(xp.pointer)

    elif cmd.find("console.logout()") != -1:
        console.logout()

    else:
        print(f"{s.bcolors.FAIL}{cmd} is not a command!")
        cmd = input(xp.pointer)