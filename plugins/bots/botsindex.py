# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

version = '1.0'
plugins = [
    {'plugintype': 'channel', 'apop': False, 'archivepath': '', 'askmdn': '', 'certfile': '', 'charset': 'us-ascii',
     'desc': '', 'filename': 'delivery_request_*.x12', 'ftpaccount': '', 'ftpactive': False, 'ftpbinary': False,
     'host': '', 'idchannel': 'x12_2_json_in', 'inorout': 'in', 'keyfile': '', 'lockname': '', 'mdnchannel': '',
     'parameters': '', 'path': 'botssys/infile/x12_2_json/', 'port': 0, 'remove': False, 'rsrv1': '', 'rsrv2': None,
     'rsrv3': None, 'secret': '', 'sendmdn': '', 'starttls': False, 'syslock': False, 'testpath': '', 'type': 'file',
     'username': ''},
    {'plugintype': 'channel', 'apop': False, 'archivepath': '', 'askmdn': '', 'certfile': '', 'charset': 'us-ascii',
     'desc': '', 'filename': 'deliver_request_*_.json', 'ftpaccount': '', 'ftpactive': False, 'ftpbinary': False,
     'host': '', 'idchannel': 'x12_2_json_out', 'inorout': 'out', 'keyfile': '', 'lockname': '', 'mdnchannel': '',
     'parameters': '', 'path': 'botssys/outfile/x12_2_json', 'port': 0, 'remove': False, 'rsrv1': '', 'rsrv2': None,
     'rsrv3': None, 'secret': '', 'sendmdn': '', 'starttls': False, 'syslock': False, 'testpath': '', 'type': 'file',
     'username': ''},
    {'plugintype': 'channel', 'apop': False, 'archivepath': '', 'askmdn': '', 'certfile': '', 'charset': 'us-ascii',
     'desc': '', 'filename': '*', 'ftpaccount': '', 'ftpactive': False, 'ftpbinary': False, 'host': '',
     'idchannel': 'x12_2_xml_in', 'inorout': 'in', 'keyfile': '', 'lockname': '', 'mdnchannel': '', 'parameters': '',
     'path': 'botssys/infile/x12_2_xml', 'port': 0, 'remove': False, 'rsrv1': '', 'rsrv2': None, 'rsrv3': None,
     'secret': '', 'sendmdn': '', 'starttls': False, 'syslock': False, 'testpath': '', 'type': 'file', 'username': ''},
    {'plugintype': 'channel', 'apop': False, 'archivepath': '', 'askmdn': '', 'certfile': '', 'charset': 'us-ascii',
     'desc': '', 'filename': '{messagetype}_*.{editype}', 'ftpaccount': '', 'ftpactive': False, 'ftpbinary': False,
     'host': '', 'idchannel': 'x12_2_xml_out', 'inorout': 'out', 'keyfile': '', 'lockname': '', 'mdnchannel': '',
     'parameters': '', 'path': 'botssys/outfile/x12_2_xml', 'port': 0, 'remove': False, 'rsrv1': '', 'rsrv2': None,
     'rsrv3': None, 'secret': '', 'sendmdn': '', 'starttls': False, 'syslock': False, 'testpath': '', 'type': 'file',
     'username': ''},
    {'plugintype': 'translate', 'active': True, 'alt': '', 'desc': '', 'fromeditype': 'x12',
     'frommessagetype': 'x12_one2one', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': 'xmlnocheck',
     'tomessagetype': 'x12_one2one', 'topartner': None, 'tscript': 'x12_2_xml'},
    {'plugintype': 'routes', 'active': False, 'alt': '', 'defer': False, 'desc': '', 'fromchannel': 'x12_2_json_in',
     'fromeditype': 'x12', 'frommessagetype': 'x12', 'frompartner': None, 'frompartner_tochannel': None,
     'idroute': 'x12_2_json', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 1, 'testindicator': '',
     'tochannel': 'x12_2_json_out', 'toeditype': '', 'tomessagetype': '', 'topartner': None,
     'topartner_tochannel': None, 'translateind': 1, 'zip_incoming': None, 'zip_outgoing': None},
]
