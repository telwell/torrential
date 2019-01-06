import aiohttp
import asyncio
import bencode
import os
from torrent import Torrent

# A torrent to test with for now
TORRENT = os.path.abspath(os.path.join('examples', 'ubuntu.torrent'))


async def main(some_torrent):
    announce_url = some_torrent.get_announce_with_params()
    async with aiohttp.ClientSession() as session:
        async with session.get(announce_url) as response:
            data = await response.read()
            print(bencode.decode(data))

if __name__ == '__main__':
    t = Torrent(TORRENT)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(t))
    print(t)
