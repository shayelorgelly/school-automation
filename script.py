import subprocess
def dark_mode():
    subprocess.run(["powershell.exe", 'iex (iwr "https://raw.githubusercontent.com/shayelorgelly/school-automation/refs/heads/main/dark-mode.ps1")'])
def light_mode():
    subprocess.run(["powershell.exe", 'iex (iwr "https://raw.githubusercontent.com/shayelorgelly/school-automation/refs/heads/main/light-mode.ps1")'])
loop = True
while loop == True:
    x = input("dark[0] or light[1]")
    if x == "0" or x == "dark":
        dark_mode()
        loop = False
    elif x == "1" or x == "light":
        light_mode()
        loop = False
    else:
        print("0 or 1")