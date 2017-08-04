from random import randint
def card_deck():
    #sets the card types and values
    card_value = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_type = ['Hearts','Spades','Clubs','Diamonds']
    deck = []
    #This iterates all 52 cards into a deck
    for i in card_type:
        for j in card_value:
            deck.append(j + ' of ' + i)
    return deck

def card_value(card):
    #only reading first slice to determine value of the card
    if card[:1] in ('J','Q','K','1'):
        return int(10)
    elif card[:1] in ('2','3','4','5','6','7','8','9'):
        #card[:1] example '2' out of the full '2 of Hearts' string
        return int(card[:1])
    elif card[:1] == 'A':
        print ("\n"+ str(card))
        num = input("Do you want this to be 1 or 11?\n>")
        while num !='1' or num !='11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Do you want this to be 1 or 11?\n>")


def new_card(deck):
    return deck[randint(0,len(deck)-1)]

def remove_card(deck,card):
    return deck.remove(card)


play_again = ''
while play_again != 'exit':
    #deck creation, card creation, card removal from deck, values and totals
    new_deck = card_deck()
    card1 = new_card(new_deck)
    remove_card(new_deck,card1)
    card2 = new_card(new_deck)
    remove_card(new_deck,card2)


    #dealer's hand
    dealer_card1 = new_card(new_deck)
    remove_card(new_deck,dealer_card1)
    dealer_card2 = new_card(new_deck)
    remove_card(new_deck,dealer_card2)
    dealer_value1 = card_value(dealer_card1)
    dealer_value2 = card_value(dealer_card1)
    dealer_total = dealer_value1 + dealer_value2

    print ("\n\n\nDealer Hand :: First a " + dealer_card1 + " and face down card.")

    print ("\n\n\nYour hand :: " + card1 + " and " + card2) #doing this statement first allows for selection between 1 and 11
    valu1 = card_value(card1)
    valu2 = card_value(card2)
    total = valu1 + valu2
    print("with a total of " + str(total) )

    if total == 21:
        print("Blackjack!")
    else:
        while total < 21: #not win or loss yet
            answer = input("\n\nWould you like to hit or stand?\n> ")
            if answer.lower() == 'hit':
                #more card creation, removal, and value added to total
                more_card = new_card(new_deck)
                remove_card(new_deck,more_card)
                more_value = card_value(more_card)
                total += int(more_value)
                print ("\n"+ more_card + " for a new total of " + str(total))
                if total > 21: #lose condition
                    print("\n\nYou LOSE!")
                    play_again = input("\n\nWould you like to continue? EXIT to leave\n")
                elif total == 21: #winning condition
                    print("\n\nYou WIN BIG WIN WOO WOO")
                    play_again = input("\n\nWould you like to continue? EXIT to leave\n")
                else:
                    continue
            elif answer.lower() == 'stand':
                print("\n\nThe dealer nods and reveals his other card to be ")
                print("a " + dealer_card2 + " for a total of " + str(dealer_total))
                if dealer_total < 17:
                    print("\n\nThe Dealer hits again.")
                    dealer_more = new_card(new_deck)
                    more_dealer_value = card_value(dealer_more)
                    print("\n\nThe card is a " + str(dealer_more))
                    dealer_total += int(more_dealer_value)
                    if dealer_total > 21 and total <=21:
                        print("\n\nDealer Bust! You win!")
                    elif dealer_total < 21 and dealer_total > total:
                        print("\n\nDealer has " + str(dealer_total) + " You lose!")
                    else:
                        continue
                elif dealer_total == total:
                    print("\n\nEqual Deals, no winner")
                elif dealer_total < total:
                    print("\n\nYou win!")
                else:
                    print("\n\nYou Lose!")
                play_again = input("\n\n\nWould you like to continue? exit to leave\n")
                break
print("Thanks for playing!")
