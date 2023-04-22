from random import choice
import aiohttp
import asyncio
from json import loads
from arsein.Error import ErrorServer
from threading  import Thread


list_servers = []

while 1:
    try:
        for server_rubika in range(1):
            async def GETservers(server):
                async with aiohttp.ClientSession() as session:
                    async with session.get(server) as response:
                        Post =  await response.text()
                        return Post
            servers = loads(asyncio.get_event_loop().run_until_complete(GETservers("https://getdcmess.iranlms.ir/"))).get('data').get("default_apis")
            for added in servers:
                servere = "https://messengerg2caddad.iranlms.ir"
                replace = servere.replace("addad",f"{added}")
                list_servers.append(replace)
        break
    except aiohttp.client_exceptions.ClientConnectorError:
        raise ErrorServer("Please check your is not internet")
    except:
        continue


class default_api:
    def defaultapi(self):
        return choice(list_servers)
