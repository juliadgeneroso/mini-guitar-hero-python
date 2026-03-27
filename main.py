import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

teclas = ["a", "s", "d"]
pontos = 0

print(Fore.MAGENTA + "🎸 Mini Guitar Hero 🎸")
print(Fore.CYAN + "Aperte a tecla certa o mais rápido possível!\n"

for rodada in range(5):
  tecla_certa = random.choice(teclas)

  print(Fore.YELLOW + f"Rodada {rodada + 1")
  print(Fore.GREEN) + f"Aperte: {tecla_certa.upper()}")

  inicio = time.time()
  resposta = input(Fore.WHITE + "Sua resposta: ").lower()
  fim = time.time()

  tempo = fim - inicio

  if resposta == tecla_certa and tempo < 2:
    print(Fore.GREEN + "BOAAA")
    pontos += 1
  else:
    print(Fore.RED + "Errou ou foi lento")
    
  print(Fore.BLUE + f"Tempo: [tempo:.2f} segundos\n")

print(Fore.MAGENTA + f"Pontuação final: {pontos}/5")

if pontos == 5:
  print(Fore.GREEN + "VOCÊ É UM ROCKSTAR")
elif pontos >= 3:
  print(Fore.CYAN




