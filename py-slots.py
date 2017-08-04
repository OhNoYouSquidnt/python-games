import sys, time
import random

print('''Welcome to the Slot Machine Simulator

You'll start with $50. You'll be asked if you want to play.

Each losing spin costs $1!

Type exit to stop.

To win you must get one of the following combinations:

:)\t:)\t:)\t\tpays\t$250

:|\t:|\t:| OR :)\tpays\t$20

:/\t:/\t:/ OR :)\tpays\t$14

:(\t:(\t:( OR :)\tpays\t$10

:/\t:/\t:|\t\tpays\t$7

:/\t:/\t:(\t\tpays\t$5

''')

#Constants:

INIT_STAKE = 50

ITEMS = [":)", ":(", ":/", ":|"]

stake = INIT_STAKE


def play():
    global stake
    input('Press enter to spin or type exit to stop!')
    stopper = ""
    while stopper != "exit" and stake != 0:
        print('Your current balance is :: $%s' % stake)
        one, two, three = spin()
        winnings, text = score(one, two, three)
        stake += winnings
        print("\n" + text + ", so you have a total of $%s\n\n" % stake)
        stopper = input('Press enter to spin again or type exit to stop!')

    if stopper.lower() == "exit":
        print('You leave with $%s!' % stake)
        quit()



def spin():
    x = random.randint(30,41)
    count = 0
    cycle = random.randint(0,3)
    x2 = random.randint(30,41)
    cycle2 = random.randint(0,3)
    count2 = 0
    cycle3 = random.randint(0,3)
    count3 = 0

    x3 = random.randint(30,41)
    pr = ITEMS[cycle]
    pr2 = ITEMS[cycle2]
    pr3 = ITEMS[cycle3]
    while count != x:
        if cycle > 3:
            cycle = 0
            pr = ITEMS[cycle]
            sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
            sys.stdout.write('|||| %s |||| ' % pr + pr2 + ' |||| ' + pr3 + " ||||")
            sys.stdout.flush()
            time.sleep(0.1)
            cycle+=1
        else:
            pr = ITEMS[cycle]
            sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
            sys.stdout.write('|||| %s |||| ' % pr + pr2 + ' |||| ' + pr3 + " ||||")
            sys.stdout.flush()
            time.sleep(0.1)
            cycle+=1
        count+=1
    sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
    pri = pr
    sys.stdout.write('|||| ' +  pri + ' |||| ' + pr2 + ' |||| ' + pr3 + " ||||")
    sys.stdout.flush()

    while count2 != x2:
        if cycle2 > 3:
            cycle2 = 0
            pr2 = ITEMS[cycle2]
            sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
            sys.stdout.write('|||| ' +  pri + ' |||| %s |||| ' % ITEMS[cycle2] + pr3 + " ||||")
            sys.stdout.flush()
            time.sleep(0.1)
            cycle2+=1
        else:
            pr2 = ITEMS[cycle2]
            sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
            sys.stdout.write('|||| ' +  pri + ' |||| %s |||| ' % ITEMS[cycle2] + pr3 + " ||||")
            sys.stdout.flush()
            time.sleep(0.1)
            cycle2+=1
        count2+=1

    sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
    pri2 = pr2
    sys.stdout.write('|||| ' +  pri + ' |||| ' + pri2 + ' |||| ' + pr3 + " ||||")
    sys.stdout.flush()

    while count3 != x3:
        if cycle3 > 3:
            cycle3 = 0
            pr3 = ITEMS[cycle3]
            sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
            sys.stdout.write('|||| ' +  pri + ' |||| ' + pri2 + ' |||| %s ||||' % ITEMS[cycle3])
            sys.stdout.flush()
            time.sleep(0.1)
            cycle3+=1
        else:
            pr3 = ITEMS[cycle3]
            sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
            sys.stdout.write('|||| ' +  pri + ' |||| ' + pri2 + ' |||| %s ||||' % ITEMS[cycle3])
            sys.stdout.flush()
            time.sleep(0.1)
            cycle3+=1
        count3+=1

    sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
    pri3 = pr3
    sys.stdout.write('|||| ' +  pri + ' |||| ' + pri2 + ' |||| ' + pri3 + " ||||")

    return pri, pri2, pri3

def score(one, two, three):
    if one == ":)" and two == ":)" and three == ":)":
        return 250, "JACKPOT!!! You win $250"
    elif one == ":|" and two == ":|" and (three == ":|" or three == ":)"):
        return 20, "Congrats! You win $20"
    elif one == ":/" and two == ":/" and (three == ":/" or three == ":)"):
        return 14, "Nice! You win $14"
    elif one == ":(" and two == ":(" and (three == ":(" or three == ":)"):
        return 10, "Hooray! You win $10"
    elif one == ":/" and two == ":/" and three == ":|":
        return 7, "Cool! You win $7"
    elif one == ":/" and two == ":/" and three == ':(':
        return 5, "Sweet! You win $5"
    else:
        return -1, "Better luck next time! You lose $1"

if __name__ == '__main__':
    play()
