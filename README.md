# flashcard_program
Python-based flashcard program that tests knowledge of top 900 most commmonly used simplified Mandarin characters against English.

This program was developed from Angela Yu - 100 Days of Code and adapted for Mandarin.
This includes 900+ words from: https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/1-1000 accessed 6/26/2021.
Translation of individual characters was done by Google Translate.

When running the program, the front of the card will display the Mandarin simplified character and pinyin for 3 seconds and then will flip to the backside.
The translation is displayed on the back of the card. 
The user decides if they got the answer right or wrong and click on the appropriate button.
Right answers are taken out of the list of flashcards.
To reset the list back to the original, delete words_to_learn.csv, and the program will regenerate that file from the master list.
