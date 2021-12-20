from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime


def crawler(query, date):
    url = "https://search.naver.com/search.naver?"

    string_date = str(date)

    dot_date = string_date.replace("-", ".")
    only_num_date = string_date.replace("-", "")

    params = {
        "where": 'news',

        "sm": "tab_pge",

        "query": query,  # 검색 키워드

        "sort": 0,  # 정렬방식 (0 : 관련도순, 1 : 최신순, 2 : 오래된순)

        "ds": dot_date,  # 검색기간 시작일

        "de": dot_date,  # 검색기간 종료일

        "nso": f"so:r,p:from{only_num_date}to{only_num_date},a:all",

        "start": 1  # 페이징

        # "nso": 'so:r,p:1d,a:all' => 최근 1일을 검색하는 옵션
    }

    daily_count = 0
    while params['start'] <= 3991:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params=params)

        html = BeautifulSoup(response.text, 'html.parser')
        titles = html.select("div.group_news > ul.list_news > li div.news_area > a.news_tit")

        for title in titles:
            title_text = title.get_text()
            if params['query'] in title_text:
                daily_count += 1

        if len(titles) < 10:
            return daily_count
        else:
            params['start'] = params['start'] + 10

    return 4000


def main():
    RESULT_PATH = 'your local path' # 결과파일이 저장될 경로를 입력해주어야 한다. 예를들어 'C:/Users/desktop/yourname/' 이런식으로 적으면 된다.

    query = input("검색어 입력: ")
    s_date = input("검색기간 시작일 입력 (ex) 2019.01.04 :")
    e_date = input("검색기간 종료일 입력 (ex) 2019.01.05 :")

    y, m, d = map(int, s_date.split('.'))
    s_date = datetime.date(y, m, d)

    y, m, d = map(int, e_date.split('.'))
    e_date = datetime.date(y, m, d)

    try:
        date_list = []
        count_list = []
        cur_date = s_date
        while cur_date <= e_date:
            count = crawler(query, cur_date)
            date_list.append(cur_date)
            count_list.append(count)
            print(cur_date) # 기사의 수 카운트 완료한 날짜는 출력
            cur_date += datetime.timedelta(days=1)

        result = {"date": date_list, "count": count_list}
        df = pd.DataFrame(result)
        outputFileName = str(s_date) + '-' + str(e_date) + '-' + query + '2.csv'
        df.to_csv(RESULT_PATH + outputFileName, sep=',', encoding='utf-8-sig')
    except:
        print("error")


if __name__ == "__main__":
    main()
