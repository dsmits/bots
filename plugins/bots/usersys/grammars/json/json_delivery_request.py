from bots.botsconfig import *

structure = [
    {ID: 'deliveryRequest', MIN: 1, MAX: 1,
     LEVEL: [
         {ID: 'partyName', MIN: 1, MAX: 10}
     ]},
]

recorddefs = {
    'deliveryRequest': [
        ['partyName', 'M', 35, 'AN']
    ],
}
