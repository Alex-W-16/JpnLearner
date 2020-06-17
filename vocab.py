import random
import time
from vocab_lists import *
import webbrowser

test_types = []
for var in dir():
    if var.startswith("var_"):
        test_types.append(var)
enter = "	enter"
###Choosing Category###

def category_selection():
    print("Which Category?")
    for i in range(len(test_types)):
        print('   For', test_types[i].strip('var_').replace("_"," ")+',', enter, i)
    
    while True:
        try:
            chosen_test_index = int((input("> ")))
            if chosen_test_index in range(len(test_types)):
                 break
            print("Invalid choice, try again")
        except:
            print("Invalid choice, try again")

    return chosen_test_index
    


while True:

    chosen_test_index = category_selection()

    chosen_test = dict(eval(test_types[chosen_test_index]))
    list_of_chosen_tests = [(test_types[chosen_test_index].strip('var_')\
                             .replace("_"," "))]
    
    
    
    ####Choosing Mode###
    while True:
        print("Chosen Categories:")
        for cat in list_of_chosen_tests:
            print("  ", cat)
        print("Choose Mode:")
        print("   For English to Japanese,",enter, 0)
        print("   For Japanese to English,",enter, 1)
        print("   For vocab list,	",enter, 2)
        print("   To add another category,", enter, 3)
        print("   To clear category choices,", enter, 4)
        while True:
            try:
                mode = int((input("> ")))
                if mode in range(6):
                    break
                print("Invalid choice, try again")
            except:
                print("Invalid choice, try again")
                
        run_test = True

        if mode == 0:
            break
        
        elif mode == 1:
            #chosen_test = {val:key for (key, val) in chosen_test.items()}
            break

        elif mode == 2:

            for k,v in sorted(chosen_test.items()):

                print(k,v,"/n")

            run_test = False
            break
            
        elif mode == 3:
            chosen_test_index = category_selection()
            new_test = dict(eval(test_types[chosen_test_index]))
            chosen_test.update(new_test)           
            list_of_chosen_tests.append((test_types[chosen_test_index]\
                                        .strip('var_').replace("_"," ")))

        elif mode == 4:
            break
            
    if mode == 5:
        continue
    
    
    
    ###Running Test###
    if run_test:

        print('Include Kanji? y/n')
        while True:
            try:
                nmode = input("> ")
                if nmode.lower() == 'y':
                    kanji_mode =  True
                    break
                elif nmode.lower() == 'n':
                    kanji_mode = False
                    break
                else:
                    print("Invalid choice, try again")
            except:
                print("Invalid choice, try again")        

        print("After a question input, \n"
              "\tEnter if correct,\n"
              "\tc; for correct and search the term in Jisho (online English/Japanese dictionary,\n"
              "\tc# for correct and search the kanji in Jisho,\n"
              "\t; for incorrect and search the term in Jisho,\n"
              "\t# for incorrect and search the kanji in Jisho,"
              "\tAny other key for incorrect\n> ")


        incorrect_list = []
        start_time = time.time()
        test_keys = list(chosen_test.keys())
        random.shuffle(test_keys)

        while len(chosen_test) > 0:
            test_item = test_keys[0]
            answer = chosen_test[test_item]
            #print(mode)
            if mode == 0:
                if answer[1] == "":
                    kanji_mode = False
                
                print(str(len(chosen_test)), "questions remaining.")
                input("Question: "+test_item)

                if kanji_mode:
                    print("Answer:\t ", answer[0], '|', answer[1],)# "\t\tC:", answer[2], "\tP:", answer[3])
                    search_item = answer[1]
                else:
                    print("Answer:\t ", answer[0], )#"\t\tC:", answer[2], "\tP:", answer[3])
                    search_item = answer[0]

                print("C:", answer[2], "\tP:", answer[3])

            if mode == 1:
                if answer[1] == "":
                    kanji_mode = False
                    
                print(str(len(chosen_test)), "questions remaining.")
                #input("Question: "+test_item)

                if kanji_mode:
                    input("Question: "+answer[0]+' | '+answer[1],)# "\t\tC:", answer[2], "\tP:", answer[3])
                    search_item = answer[1]
                else:
                    input("Question: "+answer[0], )#"\t\tC:", answer[2], "\tP:", answer[3])
                    search_item = answer[0]

                print("Answer:\t ", test_item)
                print("C:", answer[2], "\tP:", answer[3])
                    
            while True:
                correct = (input("Correct?"))

                #Ask user if their answer is correct. If correct, remove from list of vocab questions.
                #If incorrect, move it to the back of the back of the question queue

                        #Correct Answer
                if correct.lower() in ['','c#','c;']:
                    chosen_test.pop(test_item)
                    if correct.lower() == 'c#':
                        url = "https://jisho.org/search/"+search_item+"%20%23kanji"
                        webbrowser.open(url)
                    if correct.lower() == 'c;':
                        url = "https://jisho.org/search/"+search_item
                        webbrowser.open(url)
                    break
                        #Incorrect Answer
                else:
                    if correct.lower() == '#':
                        url = "https://jisho.org/search/"+search_item+"%20%23kanji"
                        webbrowser.open(url)
                    if correct.lower() == ';':
                        url = "https://jisho.org/search/"+search_item
                        webbrowser.open(url)
                        
                    incorrect_list.append("Q: "+test_item+"\tA: "+ \
                                    answer[0]+", "+answer[1]+", "+answer[2]+", "+answer[3])
                    test_keys.append(test_item)
                    break

            del test_keys[0]    
        
        
        completion_time = time.time() - start_time
        mins = int(completion_time/60)
        secs = int(completion_time - mins*60)
        num_incorrect = len(incorrect_list)

        print("Completed in", mins, "minute(s) and", secs, "second(s)!")
        print("With",num_incorrect,"incorrect answer(s)!")
        if num_incorrect > 0:
            print("These were:")
            for i in range(num_incorrect):
                print(incorrect_list[i])

    ###Continue?###    
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
