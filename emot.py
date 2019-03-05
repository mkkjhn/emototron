
questions = ["Are you a man or woman?\n1 - Man\n2 - Woman\n0 - Quit",
             "What is your name?",
             "How old are you?\n1 - under 20\n2 - 21 - 30\n3 - 31 - 40\n4 - Mature\n0 - Quit",
             "Are you in a relationship?\n1 - Yes\n2 - No\n0 - Quit",
             "What is your occupation? (Policeman, engineer, etc.)"]

discourage_m = ["You remind me of a song: Dude looks like a lady.",
                "What a stupid name.",
                "Who did you have to suck off to get that job?"]
discourage_f = ["Really? Manly jawline and those eye brows, Yikes.",
                "Cheap name for a cheap girl.",
                "Who did you have to suck off to get that job?"]

relationship_m_d = ["Hard to believe.", "Momma is still #1."]
relationship_f_d = ["He is cheating on you.", "Still aiming too high."]

discourage_age_m = ["So.. still a virgin. Good.",
                    "By now you must know that girls do not like you?",
                    "Say goodbye to your early morning erection.",
                    "Why are you still here?"]
discourage_age_f = ["Inexperienced in life but not in bed.",
                    "I want to be your 111th boyfriend.",
                    "Woman's 30's is a man's 50's, getting old and useless.",
                    "I met the fathers of your children, all five of them."]

motivate_m = ["Wrong. You are The Man.",
              "A proper name for a Hero.",
              "You are a gift for Mankind."]
motivate_f = ["And a very beautiful one.",
              "Lovely.",
              "With a smile like that they should pay you extra!"]
motivate_age_m = ["A Stud in the making.",
                  "Full of testosterone, watch out ladies!",
                  "A Man in his prime.",
                  "You still got the charms, handsome."]
motivate_age_f = ["Young and Beautiful, will you marry me?",
                  "They still don't deserve you!",
                  "Nothing beats beauty with experience.",
                  "Still more than anyone deserves."]
motivate_rel_m = ["Of course you are, you handsome Stud-Muffin!",
                  "Too handsome for your own good."]
motivate_rel_f = ["I did not want to hear that. :(",
                  "Really? Well, I am single.. if you are interested in an automaton."]

isMale = True


def setMode():
    print("EMOT-O-TRON >> Select mode:")
    print("1 - Motivate me.")
    print("2 - Discourage me.")        
    print("0 - I do not want to play this game. (Quit)")
    index = input("Choice: ")
    return index

def discourage(a, q):    

    global isMale
    print("\n")
    if q == 0 and a == '1':
        isMale = True
        print(discourage_m[q])
    elif q == 0 and a == '2':
        isMale = False
        print(discourage_f[q])

    if isMale:
        if q == 1:
            print(discourage_m[q])
        elif q == 2:
            print(discourage_age_m[int(a) - 1])
        elif q == 3:
            print(relationship_m_d[int(a) - 1])
        elif q == 4:
            print(discourage_m[q - 2])
    else:
        if q == 1:
            print(discourage_f[q])
        elif q == 2:
            print(discourage_age_f[int(a) - 1])
        elif q == 3:
            print(relationship_f_d[int(a) - 1])
        elif q == 4:
            print(discourage_f[q - 2])

    print("\n")

def motivate(a, q):

    global isMale
    print("\n")
    
    if q == 0 and a == '1':
        isMale = True
        print(motivate_m[q])
    elif q == 0 and a == '2':
        isMale = False
        print(motivate_f[q])

    if isMale:
        if q == 1:
            print(motivate_m[q])
        elif q == 2:
            print(motivate_age_m[int(a) - 1])
        elif q == 3:
            print(motivate_rel_m[int(a) - 1])
        elif q == 4:
            print(motivate_m[q - 2])
    else:
        if q == 1:
            print(motivate_f[q])
        elif q == 2:
            print(motivate_age_f[int(a) - 1])
        elif q == 3:
            print(motivate_rel_f[int(a) - 1])
        elif q == 4:
            print(motivate_f[q - 2])

    print("\n")

def interact(message):
    print("EMOT-O-TRON >> \n{}".format(message))    
    answer = input("Answer: ")
    return answer


def getMessage(q):
    return questions[q]


def main():    
    run = True
    q = 0

    index = setMode()

    if index == '0':
            run = False
            print("Goodbye")
    
    while run:
        if q <= 4:
            answer = interact(getMessage(q))
            if index == '0' or answer == '0':
                run = False
                print("Goodbye")
            elif index == '1':
                motivate(answer, q)
            elif index == '2':
                discourage(answer, q)
        else:
            print("Goodbye and good luck.")
            run = False
            break;
        
        q += 1

        if answer == '0':
            run = False


if __name__ == "__main__":
    main()
