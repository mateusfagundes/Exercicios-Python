#!python3

lockdawn = False
grana = 30

status = 'Em casa' if lockdawn or grana <= 100 else 'Uhuu'

print(f'O status é: {status}')