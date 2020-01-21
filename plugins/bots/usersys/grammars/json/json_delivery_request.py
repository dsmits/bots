from bots.botsconfig import *

structure = [
    {ID: 'deliveryRequest', MIN: 1, MAX: 1,
     LEVEL: [
         {ID: 'parties', MIN: 1, MAX: 1, LEVEL: [
             {ID: 'party', MIN: 1, MAX: 10}
         ]}
     ]}
]

recorddefs = {
    'party': [
        ['BOTSID', 'M', 5, 'AN'],
        ['name', 'M', 35, 'AN']
    ],
    'deliveryRequest': [
        ['BOTSID', 'M', 15, 'AN']
    ],
    'parties': [
        ['BOTSID', 'M', 7, 'AN']
    ]
}
