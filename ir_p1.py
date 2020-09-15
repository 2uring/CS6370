import nltk

myPara = "Frank Lampard's men got off to an ideal start after 23 minutes. New signing Timo Werner drew a penalty after he was taken down by Brighton goalkeeper Mat Ryan, and Jorginho stepped up to give the Blues the lead."
tokens = nltk.word_tokenize(myPara)
print(tokens)
