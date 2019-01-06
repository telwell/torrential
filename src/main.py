import os
from torrent import Torrent

# A torrent to test with for now
TORRENT = os.path.abspath(os.path.join('examples', 'ubuntu.torrent'))

if __name__ == '__main__':
    t = Torrent(TORRENT)
    print(t)