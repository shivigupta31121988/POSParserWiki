import nltk
import wikiquote
quote=wikiquote.quote_of_the_day()
#print (text[0])
'''print( text)
text = 'Sam is playing in the big fat world.'
text='The best preparation for tomorrow is doing your best today.'
'''
text = nltk.word_tokenize(quote[0])
result = nltk.pos_tag(text)
result=list(set(result))
#result = [i for i in result if i[0].lower() == 'big']
print ('Adjectives:-')
for key,val in result:
    if 'JJ' in val:
        print( key)
print('---\n')
print ('Verbs:-')
for key,val in result:
    if 'VB' in val:
        print( key)
print('---\n')
print ('Nouns:-')
for key,val in result:
    if 'NN' in val:
        print (key)
print('---\n')        

print(quote[0]+'--'+quote[1]) 
