first = input('What is your first name?')
last = input('What is your last name?')
name = first + ' ' + last
question = input('Ok, so your name is ' + name + '. Right?')
while(True):
          
    if question == 'no':
        print('Sorry about that lets try again.')
        first = input('What is your first name?')
        last = input('What is your last name?')
        name = first + ' ' + last
        question = input('Ok, so your name is ' + name + '. Right?')

    else : 
           finalname = name
           print('Thanks ' + finalname + '!')
           print('')
           break


           

print('Now that I know your name ' + first + ', lets get started!')       
print('')
print('First i will ask you a series of questions to determine the profit in this purchase.')
print('')
spent = input('To begin, how much money was spent on the merchandise ' + first + '?')
print('')
amount = input('Great,thank you. Now how much green did you get for the $' + spent + 'dollars? (enter amount in grams)')
print(eval(spent + amount))
pergram = spent/amount
print('Ok, so if you spent $' + spent + ' on ' + amount + ' grams, then you paid ' + pergram + ' per gram.')
