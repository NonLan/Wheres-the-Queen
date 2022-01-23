# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.


import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     for i in range(0,50,2):
         other.append(deck[i])
         dealer.append(deck[i+1])
     other.append(deck[50])

     return(dealer, other)
    

def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    
    rankOfl = []
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    #put all ranks into a list
    for i in l:
        if len(i)==2:
            char = i[0]
            rankOfl.append(char)
        if len(i)==3:
            char = i[0:2]
            rankOfl.append(char)
            

    remove_index = []
    three = []
    for x in range(len(rankOfl)):
        if rankOfl.count(rankOfl[x])==2 or rankOfl.count(rankOfl[x])==4:
            remove_index.append(x)
        elif rankOfl.count(rankOfl[x])==3 and three.count(rankOfl[x])==0:
            three.append(rankOfl[x])

    for t in three:
        remove_index.append([i for i, c in enumerate(rankOfl) if c == t][0])
        remove_index.append([i for i, c in enumerate(rankOfl) if c == t][1])
    
    remove = []
          
    for ri in remove_index:
        remove.append(l[ri])

    for r in remove:
        l.remove(r)

    for char in l:
        no_pairs.append(char)
        
    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for i in range(len(deck)):
        if i<=len(deck)-2:
            print(deck[i], end=" ")
        elif i==len(deck)-1:
            print(deck[i])
        
   
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     s = "Give me an integer between 1 and " + str(n) + ": "
     sAgain = "Invalid number. " + s
     user = input(s)
     flag = False
     while flag==False:
         if 1<=int(user)<=n:
             return(user)
             flag = True
         else:
             user = input(sAgain)
             flag = False

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     turn = 1

     while turn==1 and len(dealer)!=0 and len(human)!=0:
         print("*********************************")
         print("Your turn.\n")
         print("Your current deck of cards is:\n")
         print_deck(human)
         print("\nI have", len(dealer), "cards. If 1 stands for my first card and")
         print(len(dealer), "for my last card, which of my cards would you like?")
         num = int(get_valid_input(len(dealer)))
         if num == 1:
             print("You asked for my ", num, "st card.", sep="")
         elif num == 2:
             print("You asked for my ", num, "nd card.", sep="")
         elif num == 3:
             print("You asked for my ", num, "rd card.", sep="")
         else:
             print("You asked for my ", num, "th card.", sep="")
         print("Here it is. It is", dealer[num-1])
         print()
         print("With", dealer[num-1], "added, your current deck of cards is:\n")
         human.append(dealer[num-1])
         print_deck(human)
         dealer.remove(dealer[num-1])
         print("\nAnd after discarding pairs and shuffling, your deck is:\n")
         human = remove_pairs(human)
         print_deck(human)
         wait_for_player()
         turn = 2


         if turn==2 and len(dealer)!=0 and len(human)!=0:
             print("*********************************")
             print("My turn.")
             take = random.randint(0, len(human)-1)
             dealer.append(human[take])
             human.remove(human[take])
             if take+1 == 1:
                 print("\nI took your ", take+1, "st card", sep="")
             elif take+1 == 2:
                 print("\nI took your ", take+1, "nd card", sep="")
             elif take+1 == 3:
                 print("\nI took your ", take+1, "rd card", sep="")
             else:
                 print("\nI took your ", take+1, "th card", sep="")
             dealer = remove_pairs(dealer)
             
             wait_for_player()
             turn = 1
             
         if len(human) == 0:
             print("*********************************")
             print("Ups. You do not have any more cards")
             print("Congratulations! You, Human, win")
             return True

         elif len(dealer) == 0:
             print("*********************************")
             print("Ups. I do not have any more cards")
             print("You lost! I, Robot, win")
             return False
            
         
# main
want_to_play = True
wins, games = 0, 0
print("Hello. My name is Robot and I am the dealer.")
print("Welcome to my card game!")

while want_to_play:
    games += 1
    game = play_game()

    if game:
        wins += 1

    cont = input("Rematch? Enter 'q' to quit and any other key to continue: ")
    if cont == 'q':
        want_to_play = False

    print()
    print()

print("Thanks for playing!")
print("Your stats:")
print("Games played: ", games)
print("Games won: ", wins)
print("Win ratio: ", int((wins / games) * 100), '%')


























