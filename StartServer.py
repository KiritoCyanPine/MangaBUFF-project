import os
filepath1=os.getcwd()+"/bin/MangaBUFF_FileServer.bat"
filepath2=os.getcwd()+"/bin/MangaBUFF_server.bat"
try:
    os.startfile(filepath1)
    os.startfile(filepath2)
except:
    print("There was an error in the application start")
    input()


