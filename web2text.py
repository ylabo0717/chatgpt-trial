import os
import requests
from bs4 import BeautifulSoup

def crawl_site(url, depth=1):
    # 深さが0になったら終了
    if depth <= 0:
        return

    # URLからページのHTMLデータを取得
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # HTMLからテキストを抽出
    text = soup.get_text()

    # ファイルに保存
    filename = url.split("/")[-1]
    with open(f"./data/{filename}.txt", "w") as f:
        f.write(text)

    # リンクを抽出して再帰的に処理
    for link in soup.find_all("a"):
        if "href" in link.attrs:
            next_url = link.attrs["href"]
            if next_url.startswith("/"):
                next_url = f"{url}{next_url}"
            elif not next_url.startswith("http"):
                continue
            crawl_site(next_url, depth-1)

if __name__ == "__main__":
    url = "https://www.sony-semicon.com/ja/technology/is/index.html"
    crawl_site(url, depth=2)
