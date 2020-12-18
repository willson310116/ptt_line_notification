import requests
from bs4 import BeautifulSoup
import sys

def send_line_msg(msg1):
  url = f"https://maker.ifttt.com/trigger/notification/with/key/igLyG943EL0lS4nmYnCXTcfW-elbqzr_TVISjHrEMBa"
  value = f"?value1={msg1}"
  res = requests.get(url+value)
  # return res

def get_last_page_url(url):
  """
  The function will get the url of the last page of ptt.
  url: The current url you're in.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  element = soup.select("div.btn-group a")[3]
  # print(element)
  href = element.get("href")
  last_page_url = f"https://www.ptt.cc/{href}"
  return last_page_url

def get_bbs_article_item(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  text = ""
  elements = soup.select('div.title a')
  for element in elements:
    href = element.get("href")
    url = f"https://www.ptt.cc{href}"
    title = element.text
    text = f"{text}\n{title}\n{url}"
  return text

def get_page_urls(catg):
  urls = []
  url = f"https://www.ptt.cc/bbs/{catg}/index.html"
  # url = "https://www.ptt.cc/bbs/studyabroad/index.html"
  for i in range(10):
    urls.append(url)
    url = get_last_page_url(url)
  return urls

def main(page_number, catg):
  target_url = get_page_urls(catg)[page_number]
  text = f"{catg}\n{get_bbs_article_item(target_url)}"
  send_line_msg(text)

if __name__ == "__main__":
  # page = int(input())
  # for i in range(1,page+1):
    # main(i)
  main(int(sys.argv[1]), sys.argv[2])

