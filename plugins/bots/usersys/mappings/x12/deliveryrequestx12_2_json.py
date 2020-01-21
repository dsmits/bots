def main(inn, out):
    out.put({'BOTSID': 'deliveryRequest'})
    loop = inn.getloop({'BOTSID': 'ISA'}, {'BOTSID': 'GS'}, {'BOTSID': 'ST'}, {'BOTSID': 'N1'})
    loop = list(loop)

    print(loop)

    for partyIn in loop:
        print('New loop...')
        try:
            partyOut = out.putloop({'BOTSID': 'deliveryRequest'}, {'BOTSID': 'parties'}, {'BOTSID': 'party'})
            partyOut.put({'BOTSID': 'party', 'name': partyIn.get({'BOTSID': 'N1', 'N102': None})})
        except Exception as e:
            print(e)

    out.root.display()
