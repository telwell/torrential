import bencode

from hashlib import sha1


class Torrent:
    def __init__(self, torrent_path):
        self.meta = {}
        self._get_meta(torrent_path)

    def __str__(self):
        return f'Filename: {self.meta["info"]["name"]}\n \
        File length: {self.meta["info"]["length"]}\n \
        Announce URL: {self.meta["announce"]}\n \
        Hash: {self.info_hash}'

    def _get_meta(self, torrent_path):
        with open(torrent_path, 'rb') as f:
            meta = f.read()
            torrent = bencode.decode(meta)
            self.meta = torrent
            this_info = bencode.encode(self.meta['info'])
            self.info_hash = sha1(this_info).digest()

