import bencode
import random

from hashlib import sha1
from urllib.parse import urlencode


class Torrent:
    def __init__(self, torrent_path, port=6889, compact=True):
        self.meta = None
        self.peer_id = None
        self.info_hash = None
        self.uploaded = 0
        self.downloaded = 0
        self.left = None
        self.port = port
        self.compact = compact
        self._get_meta(torrent_path)
        self._set_meta()

    def __str__(self):
        return f'Filename: {self.meta["info"]["name"]}\n \
        File length: {self.meta["info"]["length"]}\n \
        Announce URL: {self.meta["announce"]}\n \
        Hash: {self.info_hash}'

    def _get_meta(self, torrent_path):
        self.meta = bencode.bread(torrent_path)

    def _set_meta(self):
        self.info_hash = sha1(bencode.encode(self.meta['info'])).digest()
        self._get_peer_id()
        self.left = self.meta['info']['length']

    def _get_peer_id(self):
        if self.peer_id is None:
            self.peer_id = f'-PC0001-{"".join([str(random.randint(0, 9)) for _ in range(12)])}'
        return self.peer_id

    def get_announce_with_params(self):
        params = {
            'info_hash': self.info_hash,
            'peer_id': self.peer_id,
            'uploaded': self.uploaded,
            'downloaded': self.downloaded,
            'left': self.left,
            'port': self.port,
            'compact': '1' if self.compact else '0'
        }
        return f'{self.meta["announce"]}?{urlencode(params)}'
