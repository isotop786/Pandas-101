# Creating, Reading and Writing 

import pandas as pd 

"""Creating Data. """

poll = pd.DataFrame({'Yes':[34,45],'No':[123,45]})

#print(poll)

smart_phone_poll = pd.DataFrame({'Bob':['I like it.', 'It was awfull'],'Sue':['Pretty good','Bland']}
             ,columns=['Male','Female']
             ,index =['IPhone','Android'])

print(smart_phone_poll)
