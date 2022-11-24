from colorama import Fore
from threading import Lock
from datetime import datetime
from ctypes import windll
from pystyle import Center,Colors,Colorate
from os import system


lock = Lock()

class Console:
    
    @staticmethod
    def printsc(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}Hesap Oluşturuldu{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
    
    @staticmethod
    def printe(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}Hata Oluştu{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
        
    @staticmethod
    def printi(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}Bilgi{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
        
    @staticmethod
    def printm(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}Mail Onaylandı{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
        
    @staticmethod
    def printhc(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTMAGENTA_EX}İnsanlaştırma Tamamlandı{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()


class Tools:

    @staticmethod
    def clear():
        system('cls')

    @staticmethod
    def setTitle(threads: int, proxies: int, created: int):

        windll.kernel32.SetConsoleTitleW(
            f"özgr#0001  |  Threads: {threads}  |  Yüklenen Proxyler: {proxies}  |  Oluşturulan: {created}  |  özgr#0001")

    @staticmethod
    def printLogo():
        print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter("""
                          ▄████████  ▄▄▄▄███▄▄▄▄                  ▄████████
                         ███    ███  ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███
                         ███    █▀   ███    █▀  ███   ███   ███   ███    ███  
                        ▄███▄▄▄      ███        ███   ███   ███   ███    ███
                       ▀▀███▀▀▀    ▀███████████ ███   ███   ███ ▀███████████
                         ███     █▄         ███ ███   ███   ███   ███    ███
                         ███    ███   ▄█    ███ ███   ███   ███   ███    ███
                         ██████████ ▄████████▀   ▀█   ███   █▀    ███    █▀ 
                      ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
                      ┇                     özgr#0001                      ┇                    
                      ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
                      
                      """)))