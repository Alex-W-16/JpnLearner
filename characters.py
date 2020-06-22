# -*- coding: utf-8 -*-

'''Program to practise learning Japanese Hiragana and Katakana.'''


import random
import time

while True:
    hiragana = {
        '': ['あ','い','う','え','お'],
        'k': ['か','き','く','け','こ'],
        's': ['さ','し','す','せ','そ'],
        't': ['た','ち','つ','て','と'],
        'n': ['な','に','ぬ','ね','の'],
        'm': ['ま','み','む','め','も'],
        'y': ['や','ゆ','よ'],
        'r': ['ら','り','る','れ','ろ'],
        'w': ['わ','を','ん'],
        'g': ['が','ぎ','ぐ','げ','ご'],
        'z': ['ざ','じ','ず','ぜ','ぞ'],
        'd': ['だ','づ','で','ど'],
        'b': ['ば','び','ぶ','べ','ぼ'],
        'p': ['ぱ','ぴ','ぷ','ぺ','ぽ']
            }

    katakana = {
        '':  ['ア','イ','ウ','エ','オ'],
        'k': ['カ','キ','ク','ケ','コ'],
        's': ['サ','シ','ス','セ','ソ'],
        't': ['タ','チ','ツ','テ','ト'],
        'n': ['ナ','ニ','ヌ','ネ','ノ'],
        'm': ['マ','ミ','ム','メ','モ'],
        'y': ['ヤ','ユ','ヨ'],
        'r': ['ラ','リ','ル','レ','ロ'],
        'w': ['ワ','ヲ','ン'],
        'g': ['ガ','ギ','グ','ゲ','ゴ'],
        'z': ['ザ','ジ','ズ','ゼ','ゾ'],
        'd': ['ダ','ヅ','デ','ド'],
        'b': ['バ','ビ','ブ','ベ','ボ'],
        'p': ['パ','ピ','プ','ペ','ポ']
            }


    vowel_dict = {
        '':  ['a','i','u','e','o'],
        'k': ['a','i','u','e','o'],
        's': ['a','i','u','e','o'],
        't': ['a','i','u','e','o'],
        'n': ['a','i','u','e','o'],
        'm': ['a','i','u','e','o'],
        'y': ['a','u','o'],
        'r': ['a','i','u','e','o'],
        'w': ['a','o','n'],
        'g': ['a','i','u','e','o'],
        'z': ['a','i','u','e','o'],
        'd': ['a','u','e','o'],
        'b': ['a','i','u','e','o'],
        'p': ['a','i','u','e','o']
            }

    exceptions = {
        'wn' : 'n',
        'si' : 'shi',
        'ti' : 'chi',
        'zi' : 'ji',
        'tu' : 'tsu'
        }

    while True:
        mode = (input("Katakana or Hiragana? (k/h)\n> "))
        if mode in ('k','h'):
            if mode == 'k':
                letters = dict(katakana)
                break
            else:
                letters = dict(hiragana)
                break
        print("Invalid choice, try again")

    consonants = list(letters.keys())
    exceptions_keys = list(exceptions.keys())

    start_time = time.time()
    num_incorrect = 0
    incorrect_list = []

    while len(letters) > 0:
        chosen_consonant = random.choice(consonants)
        
        vowels = vowel_dict[chosen_consonant]
        chosen_vowel = random.choice(vowels)
        test = chosen_consonant + chosen_vowel

        v_pos = vowels.index(chosen_vowel)
            
        if test in exceptions_keys:
            test = exceptions[test]
        
        contin = input(test)
        print("Answer:", letters[chosen_consonant][v_pos]+'\n')
        if contin == '':
            
            del letters[chosen_consonant][v_pos]
            del vowel_dict[chosen_consonant][v_pos]

            if len(letters[chosen_consonant]) == 0:
                del letters[chosen_consonant]
                del vowel_dict[chosen_consonant]
                consonants = list(letters.keys())
        else:
            num_incorrect += 1
            incorrect_list.append(letters[chosen_consonant][v_pos])

    completion_time = time.time() - start_time
    mins = int(completion_time/60)
    secs = int(completion_time - mins*60)

    print("Completed in", mins, "minute(s) and", secs, "second(s)!")
    if num_incorrect == 1:
        print("With 1 incorrect answer!")
        print("This was", ', '.join(incorrect_list))
    else:
        print("With", num_incorrect, "incorrect answer(s)!")
        if num_incorrect > 1:
            incorrect_list[-2] = incorrect_list[-2] + " and " + incorrect_list[-1]
            del incorrect_list[-1]
            print("These were", ', '.join(incorrect_list))

    while True:
        answer = input('Run again? (y/n): ')
        if answer in ['y', 'n']:
            break
        print("Invalid choice, try again")
        
    if answer == 'y':
        print('\n--NEW RUN--\n')
        continue
    else:
        print('Goodbye')
        break

