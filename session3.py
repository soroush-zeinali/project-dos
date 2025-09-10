x = input('choose rock , paper or scissors player 1 ?')
y = input('choose rock , paper or scissors player 2 ?')
if(x == 'rock' and y == 'scissors') or \
     (x == 'scissors' and y =='paper') or \
          (x == 'paper' and y == 'rock') :
    print('player 1 win')
else:
    print('player 2 win')