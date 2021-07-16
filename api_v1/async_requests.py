import asyncio
import aiohttp
from address_api.settings.secret import Secret


async def address_ko(keyword):
    """ request two types of addresses in Korean (Jibun, load)
    :param keyword:
    :return: dictionary type of Korean address
    """
    secret_key = Secret.JUSO_KO_KEY
    url = "https://www.juso.go.kr/addrlink/addrLinkApi.do"
    payload = {'confmKey': secret_key, 'currentPage': "1", 'countPerPage': "5",
               'hstryYn': 'Y', 'keyword': keyword, 'resultType': 'json'}
    async with aiohttp.ClientSession().get(url, params=payload) as new_resp:
        soup = await new_resp.text()
    return soup


async def address_en(keyword):
    """ request one types of addresses in English
    :param keyword:
    :return: dictionary type of English address
    """
    secret_key = Secret.JUSO_EN_KEY
    url = "https://www.juso.go.kr/addrlink/addrEngApi.do"
    payload = {'confmKey': secret_key, 'currentPage': "1", 'countPerPage': "5",
               'hstryYn': 'Y', 'keyword': keyword, 'resultType': 'json'}
    async with aiohttp.ClientSession().get(url, params=payload) as new_resp:
        soup = await new_resp.text()
    return soup


async def address_main(keyword):
    """ call async address functions
    :param keyword:
    :return:
    """
    return await asyncio.gather(address_ko(keyword), address_en(keyword))
