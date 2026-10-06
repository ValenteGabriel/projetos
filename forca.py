
secret_word = 'panda'

guessed_letters = []
errors = 0
max_errors = 6


print('=== FORCA NO TERMINAL ===')


for letter in secret_word:
    if letter in guessed_letters:
        print(letter, end=' ')
    else:
        print('_', end=' ')

guess = input('\n\nDigite uma letra: ').lower()
guessed_letters.append(guess)

if guess in secret_word:
    print(f'A letra {guess} está na palavra secreta. Parabéns!')
else:
    errors += 1
    tries = max_errors - errors
    print(f'A letra {guess} não está na palavra secreta. Tente novamente.')
    print(f'Tentativas restantes: {tries}/{max_errors}')