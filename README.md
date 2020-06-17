Code by Alex Webber

#Japanese Language learning program, compatible with Python 3.

- vocab_lists contains the vocabulary lists used.

- Run vocab from a command line to begin.

****

How to operate a test in the program:

The user chooses which vocabulary lists (from the Genki Japanese Language books) to use in the test, and whether the program should display the English or the Japanese version of the list. 

In each question, the user is prompted with a vocabulary item. The user writes the translation on paper, then presses Enter to see whether they wrote down the correct answer. The user then determines if they were correct and whether they would like to look up the vocabulary item in an online dictionary. If the answer was correct, the vocabulary item is removed from the list of questions, and if it was incorrect, it is put to the back of the queue. 

All questions are cycled through and the test ends when all questions have been answered correctly at least once. Statistics are then displayed where the user is told how long they took to complete the test, how many times they answered incorrectly, and which questions they got incorrect.
