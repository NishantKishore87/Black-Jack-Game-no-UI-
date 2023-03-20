import random
suits = ('Heart', 'Diamond', 'Spade', 'Club')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
            'Queen':10, 'King':10, 'Ace':11}
class Cards:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.suit+' '+'of'+' '+self.rank


class Deck:
    dk=[]
    def __init__(self):
        for i in suits:
            for j in ranks:
                card=Cards(i,j)
                self.dk.append(card)
        #print(len(self.dk))
        random.shuffle(self.dk)
    def remove_one(self):
        return self.dk.pop()


class Player:
    name=''
    amount=0
    pc=[]
    sum=0
    def __init__(self):
        self.pc=[]
        self.sum=0
    
    def add_player_card(self,card):
        self.pc.append(card)

    def player_sum(self):
        psum=0
        for i in self.pc:
            psum=psum+values[i.rank]
        for j in self.pc:
            if(j.rank=='Ace'and psum>21):
                psum=psum-10
        self.sum=psum
        return psum

class Dealer:
    dc=[]
    sum=0
    def __init__(self):
        self.dc=[]
        self.sum=0
    def add_dealer_card(self,card):
        self.dc.append(card)
    
    def dealer_card_sum(self):
        dsum=0
        for i in self.dc:
            dsum=dsum+values[i.rank]
        for j in self.dc:
            if(j.rank=='Ace'and self.sum>21):
                dsum=dsum-10
        self.sum=dsum
        return dsum
def gamecontinue():
    will=input('Do you want to play again ')
    if(will.lower()=='yes'):
        return True
    else:
        return False

    
def Game():
    game_on=True
    name=input('Enter name ')
    p=Player()
    dealer=Dealer()
    p.name=name
    while(game_on):
        p.pc=[]
        dealer.dc=[]
        deck=Deck()
        bet_amount=int(input('Enter the betting amount '))
        print(f'The balance in players account is {p.amount}')
        p.add_player_card(deck.remove_one())
        dealer.add_dealer_card(deck.remove_one())
        p.add_player_card(deck.remove_one())
        print(f'The card in the Dealer hand is \n{dealer.dc[0]}')
        print("The cards in player hands are ")
        for i in p.pc:
            print(i)
        print(f'The sum of cards in players hands is {p.player_sum()}')
        if(p.player_sum()==21):
            print(f'BlackJack! {p.name} has won')
            p.amount=p.amount+bet_amount*2
            print(f'Your total amount is {p.amount}')
            if(gamecontinue()==True):
                continue
            else:
                break
        hitting=False
        ip=input("Do you want to hit or stop ")
        if(ip.lower()=='hit'):
            hitting=True
            psum=0
            while(hitting==True and psum<22):
                c=deck.remove_one()
                p.add_player_card(c)
                for i in p.pc:
                    print(i)
                psum=p.player_sum()
                print(f'The sum of your cards is {psum}')
                if(psum>=21):
                    break
                ag=input('Do you want to hit again? ')
                if(ag.lower()=='yes'):
                    continue
                else:
                    hitting=False
                    break
        if(p.player_sum()==21):
            print(f'BlackJack! {p.name} has won')
            p.amount=p.amount+bet_amount*2
            print(f'Your total amount is {p.amount}')
            if(gamecontinue()==True):
                continue
            else:
                print('Thanks for playing')
                break
        if(p.player_sum()>21):
            print(f' Busted {p.name} has lost the round')
            p.amount=p.amount-bet_amount
            print(f'Your total Amount is {p.amount}')
            if(gamecontinue()==True):
                continue
            else:
                print('Thanks for playing')
                break
        
        
        dealer.add_dealer_card(deck.remove_one())
        while(dealer.dealer_card_sum()<17):
            dealer.add_dealer_card(deck.remove_one())
        
        if(dealer.dealer_card_sum()>21):
            print(f'Dealer Busted {p.name} has won ')
            p.amount=p.amount+bet_amount*2
            print(f'Your total amount is {p.amount}')
            if(gamecontinue()==True):
                continue
            else:
                print('Thanks for playing')
                break
        elif(dealer.dealer_card_sum()<p.player_sum()):
            print('{p.name} has won the round')
            p.amount=p.amount+bet_amount*2
            print(f'Your total amount is {p.amount}')
            if(gamecontinue()==True):
                continue
            else:
                print('Thanks for playing')
                break
        else:
            print('The dealers card are ')
            for i in dealer.dc:
                print(i)
            print(f'{p.name} has lost the round')
            p.amount=p.amount-bet_amount
            print(f'Your total Amount is {p.amount}')
            if(gamecontinue()==True):
                continue
            else:
                print('Thanks for playing')
                break


Game()

            

            
            
                


        

 



    




        

