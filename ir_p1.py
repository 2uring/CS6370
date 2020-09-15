import nltk

myPara = "New Delhi: Actor Kangana Ranaut's compared Mumbai to PoK and Pakistan today as a civic team demolished alleged illegal structures at her office in the middle of her massive row with Maharashtra's ruling Shiv Sena. Visuals showed a bulldozer at work at her office around the same time she took a flight to Mumbai, surrounded by heavy security."
tokens = nltk.word_tokenize(myPara)
print(tokens)