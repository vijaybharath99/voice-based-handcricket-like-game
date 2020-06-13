import os.path
import nltk
from nltk.corpus import wordnet
import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import random


def synonyms(word): #to get synonyms of a word
    synms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synms.append(l.name())
    ans = list(set(synms))
    lans=len(ans)
    for i in range(lans):ans[i]=ans[i].replace("_"," ")
    return ans

def play_cricket(turn,num):
    if turn == "bat":
        plysco = []
        afisco = []
        speak("you are batting now.")
        for i in range(6):
            speak("your turn..")
            plywrd = get_audio()
            while plywrd not in num:
                speak("please choose number between 1 and 6")
                plywrd = get_audio()
                #plywrd = input("user : ").lower()
            afino = random.randint(1,6) #cricket_game random choice.
            plyno = num.get(plywrd)
            speak("my choice is " + str(afino))
            if afino == plyno:
                speak("you are out..")
                break
            else:
                plysco.append(plyno)
        speak("you are bowling now.")
        for i in range(6):
            speak("your turn..")
            plywrd = get_audio()
            #plywrd = input("user : ").lower()
            while plywrd not in num:
                speak("please choose number between 1 and 6")
                plywrd = get_audio()
                #plywrd = input("user : ").lower()
            afino = random.randint(1,6)
            plyno = num.get(plywrd)
            speak("my choice is " + str(afino))
            if afino == plyno:
                speak("i lost my wicket.")
                break
            else:
                afisco.append(afino)
        finply = sum(plysco)
        finafi = sum(afisco)
        speak("your score is " + str(finply) + " and my score is " + str(finafi))
        if finply > finafi:
            speak("Hurry! You won.")
        elif finply < finafi:
            speak("You have lost. Better luck next time.")
        else:
            speak("this is a tie.")
    else:
        plysco = []
        afisco = []
        speak("you are bowling now.")
        for i in range(6):
            speak("your turn..")
            plywrd = get_audio()
            #plywrd = input("user : ").lower()
            while plywrd not in num:
                speak("please choose number between 1 and 6")
                plywrd = get_audio()
                #plywrd = input("user : ").lower()
            afino = random.randint(1,6)
            plyno = num.get(plywrd)
            speak("my choice is " + str(afino))
            if afino == plyno:
                speak("i lost my wicket.")
                break
            else:
                afisco.append(afino)
        speak("you are batting now.")
        for i in range(6):
            speak("your turn..")
            plywrd = get_audio()
            #plywrd = input("user : ").lower()
            while plywrd not in num:
                speak("please choose number between 1 and 6")
                plywrd = get_audio()
                #plywrd = input("user : ").lower()
            afino = random.randint(1,6)
            plyno = num.get(plywrd)
            speak("my choice is " + str(afino))
            if afino == plyno:
                speak("you are out..")
                break
            else:
                plysco.append(plyno)
        finply = sum(plysco)
        finafi = sum(afisco)
        speak("your score is " + str(finply) + " and my score is " + str(finafi))
        if finply > finafi:
            speak("Hurry! You won.")
        elif finply < finafi:
            speak("You have lost. Better luck next time.")
        else:
            speak("this is a tie.")
                

def hand_cricket():
    speak("would you like to know rules and basic tutorials of game?")
    ans = get_audio()
    #ans = input("user : ").lower()
    ans = ans.split(" ")
    temp = 0
    for ech in ans:
        if ech in ["yes", "would", "will","like"]+synonyms("ok"):
            temp = 1
            break
    if temp == 1:
        text = "the game is very simple. we have one over(6 balls). you choose one number and i choose one in between 1 and 6(including both). the batsman will get the score of the number they commit and gets out if bowler number equals batsman. be carefull batsman have only one wicket(life). my number is genune and made from predefined random function. lets have fun."
    else:
        text = "lets get into the game."
    speak(text)
    rep = "yes"
    while "yes" in rep:
        num = {"one":1, "won":1, "two":2, "tu":2, "to":2, "too":2, "three":3, "free":3, "four":4, "five":5, "six":6, "sex":6, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6}
        tsword = {1:"heads", 2:"tails"}
        choose = {1:"bat", 2:"bowl"}
        speak("heads or tails?")
        toss = get_audio()
        #toss = input("user : ").lower()
        if "head" in toss or "hack" in toss:
            plytoss = 1
            afitoss = 2
        else:
            plytoss = 2
            afitoss = 1

        tosswin = random.randint(1,2)
        if tosswin == plytoss:
            speak("its " + tsword.get(plytoss) + " what you choose bat or bowl?")
            resp = get_audio()
            #resp = input("user : ").lower()
            if "bat" in resp:
                plytrn = "bat"
                afitrn = "bowl"
            else:
                plytrn = "bowl"
                afitrn = "bat"
        else:
            afitrn = choose.get(random.randint(1,2))
            plytrn = "bat" if afitrn == "bowl" else "bowl"
            speak("its " + tsword.get(afitoss) + " i choose to " + afitrn)
        play_cricket(plytrn,num)
        speak("say yes to play one more game and no for exit.")
        rep = get_audio()
        #rep = input("user : ").lower()
        
def speak(txtop):
    tts=gTTS(text=txtop, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    txtop = txtop.lower()
    print("Cricket_Game : " + txtop)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    num = {"one":1, "won":1, "two":2, "tu":2, "to":2, "too":2, "three":3, "free":3, "four":4, "five":5, "six":6, "sex":6, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6}
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("listening...")
        audio = r.listen(Source)
        said=""
        try:
            said = r.recognize_google(audio)
            said = said.lower()
            if said in num: 
                print("User : " + str(num.get(said)))
            else:
                print("User : " + said)
        except Exception as e:
            print("No audio recognized ...")
    return said

speak("Welcome to voice based hand cricket game.")
hand_cricket()
