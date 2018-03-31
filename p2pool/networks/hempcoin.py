from p2pool.bitcoin import networks

PARENT = networks.nets['hempcoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 12*60*60//15 # shares
REAL_CHAIN_LENGTH = 12*60*60//15 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'ab330cb6aa17efff'.decode('hex')
PREFIX = '10a5fce4ff99be22'.decode('hex')
P2P_PORT = 9433
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 9434
BOOTSTRAP_ADDRS = 'rav3n.dtdns.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-rav'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: None
