# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 02

#--------------ques04------------------
import random
import requests
words = ['abuse','drama','adult','dream','agent','dress','anger','drink','apple','drive','award','earth','basis','enemy','beach','entry','birth','error',
         'block','event','blood','faith','board','fault','brain','field','bread','fight','break','final','brown','floor','buyer','cause','chain','chair',
         'chest','chief','child','class','clock','coach','coast','court','cover','cream','crime','cross','crowd','crown','cycle','dance','death','depth',
         'doubt','draft','focus','force','frame','front','fruit','glass','grass','green','group','guide','heart','horse','hotel','house','image','index',
         'input','issue','judge','knife','layer','level','light','limit','lunch','major','march','match','metal','model','money','month','motor','mouth',
         'music','night','noise','north','novel','nurse','offer','order','other','owner','panel','paper','party','peace','phase','phone','piece','pilot',
         'pitch','place','plane','plant','plate','point','pound','power','press','price','pride','prize','proof','queen','radio','range','ratio','reply',
         'right','river','round','route','scale','scene','scope','score','sense','shape','share','sheep','sheet','shift','shirt','shock','sight','skill',
         'sleep','smile','smoke','sound','south','space','speed','spite','sport','squad','staff','stage','start','state','steam','steel','stock','stone',
         'store','study','stuff','style','sugar','table','taste','theme','thing','title','total','touch','tower','track','trade','train','trend','trial',
         'trust','truth','uncle','union','unity','value','video','visit','voice','waste','watch','water','while','white','whole','woman','world','youth']

word = random.choice(words)

def new_game():
    global word, input_word
    print("-------------WORDLE-------------")
    input_word = input("Enter a five letter word: ")
    response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+input_word)
    if len(input_word)!=5:
        input_word = input("incorrect length, try again: ")
    elif response.status_code==404:
        input_word = input("word doesnt exist, try again: ")
    
    chances = 1
    while chances < 6 and input_word!=word:
        correct_places = ['-','-','-','-','-']
        incorrect_places = []
        if input_word==word:
            print("---------!!!!YOU WON!!!!---------")
            break
        for i in range(len(input_word)):
            if input_word[i]==word[i]:
                correct_places[i] = (input_word[i])
            elif input_word[i]!=word[i] and input_word[i] in word:
                incorrect_places.append(input_word[i])
        print('Letters in correct places: ',end='')
        for i in correct_places:
            print(i,end=' ')
        print()
        print('Letters in incorrect places but in the word: ',end='')
        for i in incorrect_places:
            print(i,end=' ')
        print()
        print("No of tries left:",6-chances)
        print()

        chances+=1
        input_word = input("try again: ")
        response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+input_word)
        if len(input_word)!=5:
            input_word = input("incorrect length, try again: ")
        elif response.status_code==404:
            input_word = input("word doesnt exist, try again: ")

new_game()

if input_word==word:
    print("---------!!!!YOU WON!!!!---------")
elif input_word!=word:
    print("....You lose....")
    print("correct word was",word)

f = input('play again? (y/N): ')
if f == 'y':
    new_game()
else:
    pass
