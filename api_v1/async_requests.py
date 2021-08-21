import asyncio
import aiohttp
from address_api.settings.secret import Secret


async def get_address_ko(keyword, address_number):
    """ request two types of addresses in Korean (Jibun, load)
    :param address_number:
    :param keyword:
    :return: dictionary type of Korean address
    """
    secret_key = Secret.JUSO_KO_KEY
    url = "https://www.juso.go.kr/addrlink/addrLinkApi.do"
    payload = {'confmKey': secret_key, 'currentPage': "1", 'countPerPage': address_number,
               'hstryYn': 'Y', 'keyword': keyword, 'resultType': 'json'}
    async with aiohttp.ClientSession().get(url, params=payload) as new_resp:
        soup = await new_resp.text()
    return soup


async def get_address_en(keyword, address_number):
    """ request one types of addresses in English
    :param address_number:
    :param keyword:
    :return: dictionary type of English address
    """
    secret_key = Secret.JUSO_EN_KEY
    url = "https://www.juso.go.kr/addrlink/addrEngApi.do"
    payload = {'confmKey': secret_key, 'currentPage': "1", 'countPerPage': address_number,
               'hstryYn': 'Y', 'keyword': keyword, 'resultType': 'json'}
    async with aiohttp.ClientSession().get(url, params=payload) as new_resp:
        soup = await new_resp.text()
    return soup


async def get_address_all(keyword, address_number):
    """ call async address functions
    :param address_number:
    :param keyword:
    :return:
    """
    return await asyncio.gather(get_address_ko(keyword, address_number), get_address_en(keyword, address_number))
