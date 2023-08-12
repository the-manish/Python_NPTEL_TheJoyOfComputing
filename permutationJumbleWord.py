def play():
     plname=input('Player1,Please enter your name')
     p2name=input('Player2,Please enter your name')
     pp1=0
     pp2=0
     turn=0
     while(1):
        #computer's task
        picked-word=choose()
        #create question
        qn=jumble(picked_word)
        print qn
        if turn%2=0:
            print(p1name,'Your turn.')
            ans=input('What is on my mind?')
            if ans =picked_words:
                ppl=ppl+1
                print('Your score is:'ppl)
            else:
                print('Better luck next time,I thought:',picked_word)
            c=input('Press 1 to continue and 0 to quit :')
            if c=0:
                thank(p1name,p2name,pp1,pp2)
                break
            #player2
        else:
            print(p1name,'Your turn.')
            ans=input('What is on my mind?')
            if ans =picked_words:
                ppl=ppl+1
                print('Your score is:'ppl)
            else:
                print('Better luck next time,I thought:',picked_word)
            c=0:
            thank(p1name,p2name,pp1,pp2)
            break