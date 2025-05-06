# remove punctuation
import string
def Rem_punc(sentence):
	table=str.maketrans('','',string.punctuation)
	return sentence.translate(table)

n=input("")
print(Rem_punc(n))
