#  _____  _           __     ______   ______     __
# |  __ \| |        /\\ \   / /  _ \ / __ \ \   / /
# | |__) | |       /  \\ \_/ /| |_) | |  | \ \_/ / 
# |  ___/| |      / /\ \\   / |  _ <| |  | |\   /  
# | |    | |____ / ____ \| |  | |_) | |__| | | |   
# |_|    |______/_/    \_\_|  |____/ \____/  |_|   
                                                  
                                         
                                            
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.RED + '  _____ ______ _____        _____            _____   ____  _____  ')
print(Fore.YELLOW + ' / ____|  ____|  __ \ /\   |  __ \     /\   |  __ \ / __ \|  __ \ ')
print(Fore.CYAN + '| (___ | |__  | |__) /  \  | |__) |   /  \  | |  | | |  | | |__) |')
print(Fore.BLUE + ' \___ \|  __| |  ___/ /\ \ |  _  /   / /\ \ | |  | | |  | |  _  / ')
print(Fore.GREEN + ' ____) | |____| |  / ____ \| | \ \  / ____ \| |__| | |__| | | \ \ ')
print(Fore.MAGENTA + '|_____/|______|_| /_/    \_\_|  \_\/_/    \_\_____/ \____/|_|  \_\.\n\n')


try:
    with open('db.txt', 'r', encoding="utf8") as file: # Alterar "db.txt" pela lista de e-mails/domínios/palavras que irá utilizar.
        for line in file.readlines():
            try:
                if '@globo.com.br' in str(line.lower()): # Inserir no "@globo.com.br" o domínio/palavra que você quer separar para outro '.txt'.
                    with open('globo.txt', 'a', encoding="utf8") as file2: # Nome do arquivo para onde irá as palavras/e-mails/domínios que separar, alterar "globo.txt"
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass
                else:
                    pass
            except Exception:
                pass
        input('\n               Processo Finalizado! Pressione ENTER Para Fechar!') # Processo finalizado, verificar o novo arquivo ".txt" criado.
        exit()
except Exception as ee:
    print(f'\n\n      Erro Critico -> {ee}') # Erro, pode ser causado por nome incorreto do arquivo .txt inicial.
    input()
    exit()