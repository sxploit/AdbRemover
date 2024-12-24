# github.com/sxploit
import os

def remove_pkg(package_name):
    try:
        cmd = f"adb uninstall --user 0 {package_name}"
        result = os.system(cmd)
        if result == 0:
            print(f"Package: '{package_name}' has been succesfully removed")
        else:
            print(f"Packaage: '{package_name}' cant be removed")
    except Exception as e:
        print(e)
        
def adbremover():
    print("Script for removing packages via adb")
    
    while True:
        package_name = input("> ")
        if package_name == "exit":
            exit()
        else:
            remove_pkg(package_name)

if __name__ == "__main__":
    adbremover()
