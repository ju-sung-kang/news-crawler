# news-crawler
일자별 코로나 관련 기사 수를 카운트해보기 위한 크롤링 코드


## daum_news_crawler.py
https://news.daum.net/ranking/popular<br/>

해당 페이지를 크롤링한다.<br/>

해당 페이지는 1위부터 50위까지 사람들이 해당 날짜에 많이 본 50개의 기사를 보여주는데, 50개중 몇퍼센트의 기사가 코로나 관련기사인지 날짜별로 기록한다.<br/>

코드를 실행하면 기간을 입력하게 하고, 기간에 해당하는 각 날짜에 몇퍼센트의 기사가 코로나 관련기사인지 기록한다.<br/>

'코로나', '오미크론', '확진', '방역', '백신', '화이자', '모더나', '아스트라제네카', '얀센', '접종', '거리두기', '거리 두기', '집단감염', '집단 감염' 등의 키워드들 중 하나라도 제목에 포함하는 기사는 코로나 관련 기사라고 정의했다.<br/>

## naver_news_crawler.py
이 코드의 경우, 네이버 뉴스 홈을 크롤링하지는 않는다, 위와는 조금 방식이 다르다.<br/>

![image](https://user-images.githubusercontent.com/77263282/146775160-ae09652a-5853-4d64-beb8-45e67cbf8699.png)

위처럼 검색창에 키워드를 입력하고 뉴스 탭을 클릭하고 몇가지 옵션들을 설정해 검색된 뉴스의 수를 날짜별로 크롤링해온다.<br/>

<br></br>
<br></br>
<br></br>

참고한 문서들
1. [네이버 뉴스 기사 크롤링](https://kyounghwan01.github.io/blog/etc/python/naver-news-crawling/#%E1%84%8F%E1%85%A9%E1%84%83%E1%85%B3)
2. [파이썬을 이용한 네이버 뉴스 리스트 크롤링](https://github.com/sbomhoo/naver_news_crawling)
