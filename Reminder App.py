

import pandas
import time

from plyer import *

Map_Data = pandas.read_excel('Reminder.xlsx').to_dict('records')
for reader in  Map_Data:
    time.sleep(reader['Seconds'])
    notification.notify(
            title = reader['Reminder Title'],
            message = reader['Reminder Title'] + " at " + str(reader['Time'])
        )

    


    

