import asyncio
import aiohttp
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs
import re
from address_api.settings.secret import Secret


async def address_ko(keyword):
    secret_key = Secret.JUSO_KO_KEY
    url = "https://www.juso.go.kr/addrlink/addrLinkApi.do"
    payload = {'confmKey': secret_key, 'currentPage': "1", 'countPerPage': "5",
               'hstryYn': 'Y', 'keyword': keyword, 'resultType': 'json'}
    async with aiohttp.ClientSession().get(url, params=payload) as new_resp:
        soup = await new_resp.text()
    return soup


async def address_en(keyword):
    secret_key = Secret.JUSO_EN_KEY
    url = "https://www.juso.go.kr/addrlink/addrEngApi.do"
    payload = {'confmKey': secret_key, 'currentPage': "1", 'countPerPage': "5",
               'hstryYn': 'Y', 'keyword': keyword, 'resultType': 'json'}
    async with aiohttp.ClientSession().get(url, params=payload) as new_resp:
        soup = await new_resp.text()
    return soup


async def address_main(keyword):
    return await asyncio.gather(address_ko(keyword), address_en(keyword))
