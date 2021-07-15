# (구주소, 도로명주소, 영문주소) 동시 조회 API

<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>

[ aiohttp, drf, django ]

하나의 주소로 한글 (구, 도로명)주소, 영문 주소 모두 조회하는 비동기 API. 

#

### 만들게 된 이유

> 사이트별 주소 저장 방식이 달라 주소를 표준화하는 과정을 수행하기 위함.   

  

### 주소 API 호출 대상

[행정안전부 도로명주소 api](https://www.juso.go.kr/)

> 정부에서 제공하는 무료 API이며, 신청 후 사용할 수 있음

#### 필수 항목

[한글 API KEY 발급처](https://www.juso.go.kr/addrlink/devAddrLinkRequestWrite.do?returnFn=write&cntcMenu=URL)
selecet option [도로명주소API , 검색API, ...]

[영문 API KEY 발급처](https://www.juso.go.kr/addrlink/devAddrLinkRequestWrite.do?returnFn=write&cntcMenu=URL)
selecet option [영문주소API , 검색API, ...]

> 발급 후 변수 설정  
> _# secret.py
>>  secret.JUSO_KO_KEY :   
>> secret.JUSO_EN_KEY :   


##### 주의사항
<pre>
1. 해당 API는 1시스템당 1key가 원칙입니다.
2. 개발 key의 경우 사용 기한이 있습니다.
</pre>
