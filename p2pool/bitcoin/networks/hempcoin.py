import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'a5a5fd01'.decode('hex')
P2P_PORT = 21054
ADDRESS_VERSION = 40
RPC_PORT = 12055
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'hempcoin' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 125*100000000 >> (height + 1)//500000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'THC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Hempcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Hempcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.Hempcoin'), 'Hempcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
