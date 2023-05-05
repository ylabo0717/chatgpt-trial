import requests
from bs4 import BeautifulSoup

def crawl_site(url, depth=1):
    if depth <= 0:
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text()

    filename = url.split("/")[-1]
    with open(f"./data/{filename}.txt", "w") as f:
        f.write(text)

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
