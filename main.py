#get peers from docker wireguard and change data to fit my port tunneling need
import os

if os.popen("whoami").read().strip('\n')!="root":
     print("pls use sudo")
     exit()
#default values
HOMEDIR="/home/"+os.popen("who am i | awk '{print $1}'").read().strip('\n')
OUTDIR=input("pls input the directory of this new folder (default: current user's home dir, if you want root dir, pls type /root ): ").replace("~",HOMEDIR)
FROM=input("pls input the value that you like to change from (default: wireguard.domain.com:51820): ")
TO=input("pls input the value that you want change to: ")

if OUTDIR=="":
     OUTDIR=HOMEDIR
if FROM=="":
     FROM="wireguard.domain.com:51820"

folderdir=OUTDIR+"/wireguardpeers"
os.system('mkdir '+folderdir)
os.system('docker cp wireguard:config '+folderdir)

#print(homepath+"/desktop")
#print(os.path.exists(homepath+"/desktop"))

#fromdir=homepath+"/desktop/config"
configdir=folderdir+"/config"

limit=True
size=0
#peerdir be line config/peer{n}
peerdir=configdir+"/peer"
while limit:
     size+=1
     limit=os.path.exists(peerdir+str(size))
#size = real size + 1
#print(size)

#1~real size
for i in range(1,size):
     #print(i)
     peerconfdir=peerdir+str(i)+"/peer"+str(i)+".conf"
     peerconf=os.popen('cat '+peerconfdir).read().strip('\n')
     #print (peerconf)
     peerconf=peerconf.replace(FROM,TO)
     os.system('echo "'+peerconf+'" > '+folderdir+'/peer'+str(i)+'.conf')
os.system("rm -r "+configdir)
     
