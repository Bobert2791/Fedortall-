startup = """
███████╗███████╗██████╗  ██████╗ ██████╗ ████████╗ █████╗ ██╗     ██╗     
██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║     
█████╗  █████╗  ██║  ██║██║   ██║██████╔╝   ██║   ███████║██║     ██║     
██╔══╝  ██╔══╝  ██║  ██║██║   ██║██╔══██╗   ██║   ██╔══██║██║     ██║     
██║     ███████╗██████╔╝╚██████╔╝██║  ██║   ██║   ██║  ██║███████╗███████╗
╚═╝     ╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝                                                                          
"""                                                              

print("welcome to fedortall")
print(startup)
   

input("procced with installation? (press Enter)")
import subprocess
import getpass

# get sudo password
sudo_password = getpass.getpass

#repositories

coolercontrolrep = "sudo dnf -y copr enable codifryed/CoolerControl && sudo dnf -y install coolercontrol" 
steamrep ="sudo dnf -y install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y"
steamrep2 ="sudo dnf -y config-manager --enable fedora-cisco-openh264 -y"
flatpakrepo ="flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo"
repos =f"{coolercontrolrep} && {steamrep2} && {steamrep} && {flatpakrepo}"

#packages

packages = "sudo dnf -y install steam coolercontrol mangohud corectrl"
heroicgames= "flatpak install flathub com.heroicgameslauncher.hgl"

mainpackagesstr=f"{packages} && {heroicgames}"

#occasional settings 
finalconfig = "sudo systemctl enable --now coolercontrold"

#main
mainthing =f"{mainpackagesstr} && {finalconfig}"

#copr repository

copr = subprocess.run(
repos,
stderr=subprocess.DEVNULL,
shell=True,
text=True,
check=True

)

#main process

process = subprocess.run(

    mainthing,
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.DEVNULL,
    text=True,
    stderr=subprocess.PIPE
)

#liquorix kernel setup

liquorixins = "sudo dnf -y copr enable rmnscnce/kernel-lqx"
dnfliquor = "sudo dnf -y in kernel-lqx"
mainliquor = f"{liquorixins} && {dnfliquor}"
licor = input("do you want to install the liquorix kernel? (y/n):")

if licor == "y":
  print("installing...")
  subprocess.run(
  mainliquor, 
  shell=True, 
  check=True
  )
elif licor == "n":
  print("lqx kernel will not be installed")
else: print("invalid key")

#Dualshock 4 bluetooth support
DSEXIT = "exit"
DS4MAIN = '''sudo su | touch /etc/udev/rules.d/bluetooth.rules; echo ACTION=="add", SUBSYSTEM=="hid", ATTR{power/control}="on" >> /etc/udev/rules.d/bluetooth.rules'''
DS4 = input("install Dualshock 4 Bluetooth support? (y/n)")
if DS4 == "y":
  print("installing... (again)")
  DS4PROCESS= subprocess.run( 
  DS4MAIN,
  DSEXIT,
  shell=True,
  check=True,
  stdout=True,
  stderr=True,
  
  )
elif DS4 == "n":
  print("DS4 support will not be installed")
else: print("invalid key")

print("Installation successful thanks for believing in me ●‿●")


stdout = process.stdout
stderr = process.stderr
print(stderr)

#code and idea by Bobert.C
