from bots.botsconfig import *

structure = [
    {ID: 'deliveryRequest', MIN: 1, MAX: 1,
     LEVEL: [
         {ID: 'party', MIN: 1, MAX: 10}
     ]},
]

recorddefs = {
    'party': [
        ['name', 'M', 35, 'AN']
    ],
}
