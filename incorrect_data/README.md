# INCORRECT DATA

These are the processed data that have the function contain_dict_words broken and incorrect. 

## processed_data2.csv
This is the initial processed data where I used the nltk dictionary and only wordninja to detect dictionary words. It didn't detect all the words because the nltk wordlist is limited. Also wordninja didn't do a very good job of splicing words
since because it had trouble with numbers. 

## processed_data3.csv
This one has regrex combined with wordninja, but because the nltk wordlist was still being used it still didn't detect everything

## processed_data4.csv
This one uses a new word bank called SCOWL, I think its still wrong because I didn't consider repeated words caused from using regex + wordninja at the same time. idk i dont rmbr anymore

## Confusion Matrix
If you want you can do a confusion matrix for all of them and see what each accuracy is like. Just remember to do a confusion matrix for the actual correct processed data. You can screenshot the results and put it on the report so we have something to write about.
We gonna compare all these matrixes and that report will be so gg ez
