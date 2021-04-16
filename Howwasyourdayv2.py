current_feelings = {'good':'Your having a good day, thats great hopefully it stays that way',  
                 'alright':' Your day was alright well thats not bad i wish it was better. Well lets hope it gets better <3',
                 'bad':' sucks you are feeling bad today that sucks :(. We all have bad days, we all have good days, All that matters is that it always gets better :)', 
                 'depressed':' Hey brother we all have experienced depression at some point in our life. But honestly i just want you to know you matter more than you think. And if you or someone you know need to just have a conversation please call 833-456-4566 CANADA or 1-800-273-8255 US.... Because we all get and go through it at some point. Just know you are enough, you can do anything you set your mind too.  '}
                 
print ("How are you feeling today good, alright, or bad?:")
for key in current_feelings:
        print (key) 

feelings = input('Sooooo how was your day :) ? \n')

Day = current_feelings.get(feelings)
if Day == None: 
        print ('Sorry please choose between good, alright, bad')
else:
        print(' you chose ...\n', feelings,'...', Day )
