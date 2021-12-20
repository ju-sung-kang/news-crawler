from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime


def crawler(date):
    url_date = str(date).replace("-", "")
    url = "https://news.daum.net/ranking/popular?regDate=" + str(url_date)
    related_words = ['코로나', '오미크론', '확진', '방역', '백신', '화이자', '모더나', '아스트라제네카', '얀센', '접종', '거리두기', '거리 두기', '집단감염', '집단 감염', '비대면']

    related_news = 0
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(response.text, 'html.parser')
    titles = html.select("div.news_type1 div.cont_ranking div.rank_news a.link_txt")

    for title in titles:
        title_text = title.get_text()
        for word in related_words:
            if word in title_text:
                related_news += 1
                break

    return related_news


def main():
    RESULT_PATH = '[your local path]' # 결과파일이 저장될 경로를 입력해주어야 한다. 예를들어 'C:/Users/desktop/yourname/' 이런식으로 적으면 된다.

    s_date = input("검색기간 시작일 입력 (ex) 2019.01.04 :")  # 2019.01.04
    e_date = input("검색기간 종료일 입력 (ex) 2019.01.05 :")  # 2019.01.05

    y, m, d = map(int, s_date.split('.'))
    s_date = datetime.date(y, m, d)

    y, m, d = map(int, e_date.split('.'))
    e_date = datetime.date(y, m, d)

    date_list = []
    count_list = []
    cur_date = s_date
    while cur_date <= e_date:
        count = crawler(cur_date)
        date_list.append(cur_date)
        count_list.append(2 * count)
        print(cur_date)
        cur_date += datetime.timedelta(days=1)

    result = {"date": date_list, "count": count_list}
    df = pd.DataFrame(result)
    outputFileName = 'crel_rate-' + str(s_date) + '-' + str(e_date) + '.csv'
    df.to_csv(RESULT_PATH + outputFileName, sep=',', encoding='utf-8-sig')


if __name__ == "__main__":
    main()
