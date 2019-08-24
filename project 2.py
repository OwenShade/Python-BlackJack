import random
def welcome():
    #Asks user to enter their name so game can personalised throughout#
    print("Hello. Please enter your name.")
    name = str(input())
    #Validates that the name entered is less than 20 characters to stop use of madeup names#
    while len(name) > 20:
        print("Please enter another name, it should be no longer than 20 characters.")
        name =str(input())
    print("Hi", name, ". Welcome to blackjack.")
    return name


def card_deck():
    #sets the card values#
    deck = [1, 1, 1, 1 , 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    return deck
    

def instructions():
    #Iniatilises the variable bank to 100, meaning the user starts off with £99#
    bank = 49
    print("Would you like an explanation of the rules?")
    answer = str(input())
    #validates that the question asked recieves a yes or no answer#
    while answer != "yes" and answer!= "no":
        print("Invalid answer, please either enter yes or no.")
        answer = str(input())
    while answer == "yes":
        #uses a while loop to explain rules of the game to the user, this means that the user can receive
        #multiple explanations incase they don't understand the first time#
        print("The objective of this blackjack is to get closer to 21 than the dealer, without going over.")
        print("Cards are worth the number in the corner of the card, apart from aces and royals.")
        print("Royals are worth 10 and aces are worth 1.")
        print("After being dealt an intial 2 cards, you will be asked if you want to stick or twist.")
        print("If you choose to twist, you will be dealt another card.")
        print("But if you stick, the dealer will reveal his total. if you are closer to 21 than the dealer,")
        print("You Win!")
        print("Would you like to go over the rules again?")
        answer = str(input())
        while answer != "yes" and answer!= "no":
            print("Please enter either yes or no.")
            answer = str(input())
    if answer == "no":
        print("Great, let's get started.")
    
    #tells the user how much they have to bet (all users start with £100) and then asks they user
    #how much they would like to bet based on that information#
    print("you currently have £", bank, " to bet, how much would you like to bet on this game?")
    wager = int(input())
    #validates that the user enters a bet which is not more than what they have#
    while wager > bank:
        print("You only have £",bank," in your bank, please enter a bet under or equal to this amount.")
        wager = int(input())
    #validates that the user doesn't try to enter a negative bet#
    while wager < 0:
        print("Please bet an amount greater than 0.")
        wager = int(input())
    bank = bank - wager
    return bank, wager

def shuffle_cards(deck):
    #uses the pre-coded random function to shuffle the values of the cards into a random order#
    random.shuffle(deck)
    return deck

def draw_cards(deck):
    #defines the sub-program "draw_cards" and reads in deck.
    #deck was shuffled and then returned in the last procedure, therefore the version being used
    #in this sub-program is the shuffled version#
    counter=0
    #sets up two arrays. One for the dealers cards and one for the users cards.#
    user_cards=[]
    dealer_cards=[]
    print("2 Cards will now be drawn for both you and the dealer")
    print("The cards you have so far are: ")

    #defines a loop which picks 2 starter cards for the user using the variable 'loop'
    #as a pointer for the array. The pointer is then incremented are the cards displayed
    #to the user#
    for loop in range(2):
       print(deck[loop])
       user_cards.append(deck[loop])
    counter = counter + len(user_cards)

    #another loop is set up for picking the dealers cards, using the same principle as the user loop#
    for loop in range(counter,4):
        dealer_cards.append(deck[loop])
    counter = counter + len(user_cards) + len(dealer_cards)

    #shows one of the dealers cards, and keeps the other one unknown; as per the rules of 21#
    print(" ")
    print("The dealer has now also been dealt two cards.")
    print("One of which is turned face up")
    print("One of the dealers cards is ", dealer_cards[0])


    return user_cards, dealer_cards
    

def total_number(dealer_cards, user_cards, wager, bank, deck):
    #the purpose of this method is to determine whether or not the user has won the game
    #multiple if statements are set up to determine who was the closest value to 21, whilst still being under.
    #if the user is still under 21, they are asked if the would like to stick with the current value, or be given another card.
    #the result is then returned to the main program to be processed and used later.#
    stick = False
    counter = 4

        
    while sum(user_cards)<21 and stick == False:
        print("you currently have", sum(user_cards), ".")
        print("Would you like to stick or hit?")
        answer = str(input())
        if answer == "hit":
            user_cards.append(deck[counter])
            counter=counter+1
        elif answer == "stick":
                print("The dealer has the cards:")
                print(dealer_cards)
                print("Making a total of: ", sum(dealer_cards))
                stick = True

    if stick == True and sum(dealer_cards)>sum(user_cards) and sum(dealer_cards)< 21:
        print("THE DEALER HAS", sum(dealer_cards), ". WHERE AS YOU ONLY HAVE", sum(user_cards))
        print("MEANING THE DEALER WINS")
        print("You lost £", wager)
        print("You now have £", bank, "in your bank")
        

    if stick == True and sum(user_cards)>sum(dealer_cards) and sum(user_cards)< 21:
        print("YOU HAVE", sum(user_cards), ". WHERE AS THE DEALER ONLY HAS", sum(dealer_cards))
        print("MEANING YOU WIN!")
        bank = bank + wager * 2
        print("You won £", wager * 2)
        print("You now have £", bank, "in your bank.")
        

    if sum(user_cards)>21:
        print("You have went over 21! You are BUST and the dealer wins!")
        print("You lost £", wager)
        print("You now have £", bank, "in your bank.")

    if sum(user_cards)==21:
        print("You have 21! Meaning you win!")
        print("You won £", wager)
        print("You now have £", bank, "in your bank.")

    strbank=str(bank)
    return strbank        
        

def read_file_int(file):
    text_file=open(file,"r")
    myList=text_file.read().splitlines()
    array1=[]
    for row in myList:
        value1=row.split('\t')
        array1.append(value1)
    text_file.close()
    return array1

def read_file_str(file):
    text_file=open(file,"r")
    myList=text_file.read().splitlines()
    text_file.close
    array1=[]
    for row in myList:
        value1=row.split('\t')
        array1.append(value1)
    text_file.close()
    
    return array1


def write_to_file(col1,file):
    output_file=open(file,"a")
    output_file.write('\n')
    output_file.write(col1)
    output_file.close()



def bubbleSort(alist,blist):
    for x in range(len(alist)-1,0,-1):
        for i in range(x):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                tempb=blist[i]
                alist[i] = alist[i+1]
                blist[i]=blist[i+1]
                alist[i+1] = temp
                blist[i+1]=tempb

#https://docs.python.org/3/howto/sorting.html

def display(array1,array2):
    print("Leaderboard")
    print("name     money")
    for counter in range(0,len(array1)):
        print(array1[counter],"",array2[counter])
        


    
def again():

    print("Would you like to play again?")
    answer = str(input())
    while answer != "yes" and answer!= "no":
       print("Invalid answer, please either enter yes or no.")
       answer = str(input())
    if answer== "yes":
            main()
    
    elif answer == "no":
        print("Thank you for playing.")
       
    

def main():        
    name=welcome()
    deck=card_deck()
    bank, wager = instructions()
    deck=shuffle_cards(deck)
    user_cards, dealer_cards = draw_cards(deck)
    strbank = total_number(dealer_cards, user_cards, wager, bank, deck)
    write_to_file(name,"name.txt")
    write_to_file(strbank,"money.txt")
    moneylist=read_file_int("money.txt")
    namelist=read_file_str("name.txt")
    bubbleSort(moneylist,namelist)
    display(namelist,moneylist)
    again()

main()
