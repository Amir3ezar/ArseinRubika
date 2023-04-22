import aiohttp
import asyncio
from arsein.Encoder import encoderjson
from arsein.PostData import method_Rubika,httpfiles,_download_with_server
from json import loads
from pathlib import Path
from arsein.Clien import clien

class Upload:
    def __init__(self, Sh_account:str):
        self.Auth = Sh_account
        self.enc = encoderjson(Sh_account)
        self.methodUpload = method_Rubika(Sh_account)

    def requestSendFile(self,file):
        while 1:
            try:
                return self.methodUpload.methodsRubika("json",methode ="requestSendFile",indata = {"file_name": str(file.split("/")[-1]),"mime": file.split(".")[-1],"size": Path(file).stat().st_size},wn = clien.web).get("data")
                break
            except:
                continue

    def uploadFile(self, file):
        while 1:
            try:
                for tr in range(1):
                    if not ("http" or "https") in file:
                        REQUES = self.requestSendFile(file)
                        bytef = open(file,"rb").read()

                        hash_send = REQUES["access_hash_send"]
                        file_id = REQUES["id"]
                        url = REQUES["upload_url"]

                        header = {
                            'auth':self.Auth,
                            'Host':url.replace("https://","").replace("/UploadFile.ashx",""),
                            'chunk-size':str(Path(file).stat().st_size),
                            'file-id':str(file_id),
                            'access-hash-send':hash_send,
                            "content-type": "application/octet-stream",
                            "content-length": str(Path(file).stat().st_size),
                            "accept-encoding": "gzip",
                            "user-agent": "okhttp/3.12.1"
                        }

                        if len(bytef) <= 131072:
                            header["part-number"], header["total-part"] = "1","1"

                            while True:
                                try:
                                    #loop = asyncio.get_event_loop()
                                    j = self.methodUpload.methodsRubika(types = "file",server = url,podata = bytef,header = header)
                                    j = loads(j)['data']['access_hash_rec']
                                    break
                                except:
                                    continue

                            return [REQUES, j]
                        else:
                            t = round(len(bytef) / 131072 + 1)
                            for i in range(1,t+1):
                                if i != t:
                                    k = i - 1
                                    k = k * 131072
                                    while True:
                                        try:
                                            header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
                                            #loop = asyncio.get_event_loop()
                                            o = self.methodUpload.methodsRubika(types = "file",server = url,podata = bytef[k:k + 131072],header = header)
                                            o = loads(o)['data']
                                            break
                                        except:
                                            continue
                                else:
                                    k = i - 1
                                    k = k * 131072
                                    while True:
                                        try:
                                            header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
                                            #loop = asyncio.get_event_loop()
                                            p = self.methodUpload.methodsRubika(types = "file",server = url,podata = bytef[k:],header = header)
                                            p = loads(p)['data']['access_hash_rec']
                                            break
                                        except:
                                            continue
                                    return [REQUES, p]
                    else:
                        loop = asyncio.get_event_loop()
                        while 1:
                            try:
                                REQUES = self.methodUpload.methodsRubika("json",methode ="requestSendFile",indata = {"file_name": str(file.split("/")[-1]),"mime": file.split(".")[-1],"size": len(loop.run_until_complete(_download_with_server(server = file)))},wn = clien.web).get("data")
                                break
                            except:
                                continue

                        hash_send = REQUES["access_hash_send"]
                        file_id = REQUES["id"]
                        url = REQUES["upload_url"]
                        loop = asyncio.get_event_loop()
                        bytef = loop.run_until_complete(_download_with_server(server = file))

                        header = {
                            'auth':self.Auth,
                            'Host':url.replace("https://","").replace("/UploadFile.ashx",""),
                            'chunk-size':str(len(loop.run_until_complete(_download_with_server(server = file)))),
                            'file-id':str(file_id),
                            'access-hash-send':hash_send,
                            "content-type": "application/octet-stream",
                            "content-length": str(len(loop.run_until_complete(_download_with_server(server = file)))),
                            "accept-encoding": "gzip",
                            "user-agent": "okhttp/3.12.1"
                        }

                        if len(bytef) <= 131072:
                            header["part-number"], header["total-part"] = "1","1"

                            while True:
                                try:
                                    #loop = asyncio.get_event_loop()
                                    j = self.methodUpload.methodsRubika(types = "file",server = url,podata = bytef,header = header)
                                    j = loads(j)['data']['access_hash_rec']
                                    break
                                except:
                                    continue

                            return [REQUES, j]
                        else:
                            t = round(len(bytef) / 131072 + 1)
                            for i in range(1,t+1):
                                if i != t:
                                    k = i - 1
                                    k = k * 131072
                                    while True:
                                        try:
                                            header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
                                            #loop = asyncio.get_event_loop()
                                            o = self.methodUpload.methodsRubika(types = "file",server = url,podata = bytef[k:k + 131072],header = header)
                                            o = loads(o)['data']
                                            break
                                        except:
                                            continue
                                else:
                                    k = i - 1
                                    k = k * 131072
                                    while True:
                                        try:
                                            header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
                                            #loop = asyncio.get_event_loop()
                                            p = self.methodUpload.methodsRubika(types = "file",server = url,podata = bytef[k:],header = header)
                                            p = loads(p)['data']['access_hash_rec']
                                            break
                                        except:
                                            continue
                                    return [REQUES, p]
                break
            except:
                continue
