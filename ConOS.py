import os,winsound,colorama,psutil,wikipedia,keyboard,time

#=======init=============
colorama.init()

#=======functions========
def ring():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    print("\n")

def add(n1,n2):
    print(n1+n2)
    print("\n")

def subtract(n1,n2):
    print(n1-n2)
    print("\n")

def multiply(n1,n2):
    print(n1*n2)
    print("\n")

def divide(n1,n2):
    print(n1/n2)
    print("\n")

def battery():
    btry = psutil.sensors_battery()
    print(btry.percent+"\n")

def wiki(term):
    wik = wikipedia.summary(term)
    print("\n"+wik+"\n")

def py():
    while 1:
        cmdrun=input("\nEnter Python Code\n>>>")
        exec(cmdrun)
  

#======fullscreen========

keyboard.press("F11")



#======flash-screen======

print("""┌─────────────────────┐
│                     │
│  ┌──┐ ─┐  ┌──┐ ─┐   │
│  │  │  │  │  │  │   │
│  │  │  │  │  │  │   │
│  │  │  │  │  │  │   │
│  └──┘ ─┴─ └──┘ ─┴─  │
│                     │
└─────────────────────┘
Loading ConOS v1.0 ...
""")
winsound.Beep(1000,500)
time.sleep(2)
os.system("cls")


#======header============
print("ConOS v1.0")
print("="*os.get_terminal_size().columns)
print(colorama.Fore.CYAN+"""
┌────────────────────────────┐
│ AVAILABLE COMMANDS -       │
│                            │
│ - add(n1,n2)               │
│ - battery()                │
│ - divide(n1,n2)            │
│ - multiply(n1,n2)          │
│ - subtract(n1,n2)          │
│ - py()                     │
│ - ring()                   │
│ - wiki()                   │
└────────────────────────────┘
"""+colorama.Style.RESET_ALL)


#======evaluate commands======
while True:
    command = input(colorama.Fore.WHITE+"Enter command - "+colorama.Fore.GREEN)
    print(colorama.Style.RESET_ALL)
    try:
        exec(command)

        input("Press [Enter to continue]")
        os.system("cls")
        
        print("ConOS v1.0")
        print("="*os.get_terminal_size().columns)
        print(colorama.Fore.CYAN+"""  
┌────────────────────────────┐
│ AVAILABLE COMMANDS -       │
│                            │
│ - add(n1,n2)               │
│ - battery()                │
│ - divide(n1,n2)            │
│ - multiply(n1,n2)          │
│ - subtract(n1,n2)          │
│ - py()                     │
│ - ring()                   │
│ - wiki()                   │
└────────────────────────────┘"""+colorama.Style.RESET_ALL)
    
    except:
        print(colorama.Fore.RED+"Error, try again!\n"+colorama.Style.RESET_ALL)
        input("Press [Enter] to continue ")
        os.system("cls")
        
        print("ConOS v1.0")
        print("="*os.get_terminal_size().columns)
        print(colorama.Fore.CYAN+"""  
┌────────────────────────────┐
│ AVAILABLE COMMANDS -       │
│                            │
│ - add(n1,n2)               │
│ - battery()                │
│ - divide(n1,n2)            │
│ - multiply(n1,n2)          │
│ - subtract(n1,n2)          │
│ - py()                     │
│ - ring()                   │
│ - wiki()                   │
└────────────────────────────┘"""+colorama.Style.RESET_ALL)
        