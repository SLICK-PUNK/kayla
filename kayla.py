import subprocess
import colorama 
import sys
import time
def banner():
    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + '''
███████████████████████████████
█▄─█─▄██▀▄─██▄─█─▄█▄─▄████▀▄─██
██─▄▀███─▀─███▄─▄███─██▀██─▀─██
▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀ '''  + colorama.Style.RESET_ALL) 
colorama.init()
name = subprocess.run(["echo", "%username%"], stdout=subprocess.PIPE, shell=True)
name = (name.stdout.decode("utf-8"))
name = str.rstrip(name)

n = 1
def printopt(texxt):  
    global n
    print(colorama.Fore.BLUE + "[" +  colorama.Style.RESET_ALL + str(n) + colorama.Fore.BLUE + "] " + colorama.Fore.LIGHTBLUE_EX + texxt + colorama.Style.RESET_ALL)
    n += 1  
def printopty(opt, texxt):
    print(colorama.Fore.BLUE + "[" +  colorama.Style.RESET_ALL + str(opt) + colorama.Fore.BLUE + "] " + colorama.Fore.LIGHTBLUE_EX + texxt + colorama.Style.RESET_ALL)
def  clean():
    subprocess.run("cls", shell=True)
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run("cleanmgr")
    print(colorama.Style.RESET_ALL)
    subprocess.run("cls", shell=True)
    menu()
    


def ping(): 
    subprocess.run("cls", shell=True)
    site = input(f"{colorama.Fore.LIGHTBLUE_EX}Type Website URL/IP to ping: {colorama.Fore.LIGHTGREEN_EX}")
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run(['ping', site])  
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()
    


def netstat():
    subprocess.run("cls", shell=True)
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run("netstat") 
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()
    


def tracert():
    subprocess.run("cls", shell=True)
    site = input(f"{colorama.Fore.LIGHTBLUE_EX} Type Website URL/IP to trace packets to: {colorama.Fore.LIGHTGREEN_EX}")
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run(["tracert", site])  
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()
    


def powercfg():
    subprocess.run("cls", shell=True)
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run(["powercfg", "-energy"])
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()
    


def sysinfo():
    subprocess.run("cls", shell=True)
    print(f"{colorama.Fore.LIGHTCYAN_EX}")
    subprocess.run("systeminfo")
    print(colorama.Style.RESET_ALL) 
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu() 
    


def sfcscan():
    subprocess.run("cls", shell=True)
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run(['sfc', '/scannow'])
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()
    


def chkdsk():
    subprocess.run("cls", shell=True)
    #cfpbs = check for physically bad sectors
    cfpds = ''
    a = input(f"{colorama.Fore.LIGHTBLUE_EX} Do you also want to check for physically bad sectors? y/n?: {colorama.Fore.LIGHTGREEN_EX}")
    if a == "y":
        cfpds = "/r"
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")  
    subprocess.run("cls", shell=True)
    menu()  


    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run(['chkdsk', '/f', cfpds])
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()
    


def utilman():
    subprocess.run("cls", shell=True)
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run("utilman")
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()
    


def control():
    subprocess.run("cls", shell=True)
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run("control", shell=True)
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()


def dism():
    subprocess.run("cls", shell=True)
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run(["DISM", "/Online", "/Cleanup-Image", "/RestoreHealth" ])
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()


def tree():
    subprocess.run("cls", shell=True)
    subprocess.run("tree", shell=True)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu() 
    
    
def mrt():
    subprocess.run("cls", shell=True)
    print(colorama.Fore.LIGHTCYAN_EX)
    subprocess.run(["mrt"])
    print(colorama.Style.RESET_ALL)
    input(f"{colorama.Fore.LIGHTBLUE_EX}Press enter to return to menu{colorama.Style.RESET_ALL}")
    subprocess.run("cls", shell=True)
    menu()

def menu():
    printopt("Clean up unneeded system files to free up space (Can be run regularly)")
    printopt("Ping a website of your choice to see if your wifi works/website is up and measure latency of the connection")
    printopt("Get a list of all active TCP connections from your computer.")
    printopt("Show path your internet traffic takes to get from your browser to a remote system like Google servers")
    printopt("Check power configuration to diagnose battery drain/generates warnings and/or to help you improve battery life")
    printopt("Get info about you system ")
    printopt("Check for corruption of core system files (caused by viruses or other means). Fixes system irregularites")
    printopt("Check disk/storage for errors and bad sectors")
    printopt("Open Ease of Access settings")
    printopt("Scan and repair for problems in the windows image using DISM")
    printopt("List all folders and files in your system in a specific drive")
    printopt("Run the Windows Malicious Software Removal Tool (Remove small viruses and stuff)")
    printopty("E", "Exit")
    print(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "SOME OPTIONS MIGHT REQUIRE YOU TO RUN THIS AS AN ADMINISTRATOR!!" + colorama.Style.RESET_ALL)
    

    choice = input(f'{colorama.Fore.LIGHTMAGENTA_EX}{colorama.Fore.LIGHTRED_EX}{name}@sys>{colorama.Style.RESET_ALL} ').strip().lower()
    if choice == "1":
        clean()
    elif choice == "2":
        ping()
    elif choice == "3":
        netstat()
    elif choice == "4":
        tracert()
    elif choice == "5":
        powercfg()
    elif choice == "6":
        sysinfo()
    elif choice == "7":
        sfcscan()
    elif choice == "8":
        chkdsk()        
    elif choice == "9":
        utilman()  
    elif choice == "10":
        dism()
    elif  choice == "11":
        tree()  
    elif choice == "e" or choice  == "exit":
        subprocess.run("cls", shell=True)
        print(colorama.Fore.LIGHTRED_EX+ colorama.Style.BRIGHT)
        for letter in "Have a Great Day!":
            print(letter,end="", flush=True)
            time.sleep(0.05)
        time.sleep(1.5)    
        sys.exit(0)  

subprocess.run("cls", shell=True)
banner()
menu()

