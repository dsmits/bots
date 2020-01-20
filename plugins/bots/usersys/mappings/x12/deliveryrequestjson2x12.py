def main(inn, out):
    for partyIn in inn.getloop({'BOTSID': 'ST'}, {'BOTSID': 'N1'}):
        partyOut = out.putloop({'BOTSID': 'deliveryRequest'}, {'BOTSID': 'partyName'})
        partyOut.put({'BOTSID': 'party', 'name': partyIn.get({'BOTSID': 'N1', 'N102': None})})
