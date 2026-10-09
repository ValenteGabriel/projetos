
secret_word = 'python'

guessed_letters = []
errors = 0
max_errors = 3

print('=== FORCA NO TERMINAL ===')

while errors < max_errors:

    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')

    guess = input('\n\n\nDigite uma letra: ').lower()
    guessed_letters.append(guess)

    if guess in secret_word:
        print(f'A letra {guess.upper()} está na palavra secreta. Parabéns!')
    else:
        errors += 1
        tries = max_errors - errors
        print(f'A letra {guess} não está na palavra secreta. Tente novamente.')
        print(f'Tentativas restantes: {tries}/{max_errors}')

    if all(letter in guessed_letters for letter in secret_word):        
        print(f'\nA palavra secreta era "{secret_word.upper()}". Você acertou, parabéns!')
        break
else:
    print(f'\nTentativas esgotadas. Você perdeu!\nA palavra secreta era "{secret_word.upper()}".')
            
print('\nFIM DE JOGO')


