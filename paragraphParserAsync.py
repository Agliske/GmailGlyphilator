# Import the necessary libraries
from bs4 import BeautifulSoup
from bs4 import Comment
import requests
import lxml
import time
import os
import selenium
import selenium.webdriver
import selenium.webdriver.firefox
import selenium.webdriver.firefox.options
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, TimeoutError, ProcessPoolExecutor
user_agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

# Fetch the HTML content from a webpage
url = 'https://www.nationalacademies.org/news/2024/10/workshop-explores-the-opportunity-and-perils-of-using-ai-in-medical-diagnosis'

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def articleParse(url, method = 0):
    # print("hello articleparse")
    if "pdf&ct" in url and method != 3:
        print("pdf detected at link")
        # articleData = {
        # "url": url,
        # "title": None,
        # "date": None,
        # "content": ""
        # }
        # return articleData
        return articleParse(url,method=3)
        
    
    if method == 0:
        response = requests.get(url)
        html_content = response.text
        print("Text retrieved with requests lib")
        soup = BeautifulSoup(html_content, 'lxml')
        paragraphs = soup.find_all(['p','strong'])
        
        if paragraphs == []:
            paragraphs = soup.find_all(string=True)
            # print(paragraphs)

    if method == 1:
        
        def selenium_retrieval(url,result):
            
            # try:
            print("Text retrieved with selenium lib")
            options = selenium.webdriver.FirefoxOptions()
            # options.add_argument("--headless")
            driver = selenium.webdriver.Firefox(options=options)
            driver.get(url)

            time.sleep(2)
        
            result['html_content'] = driver.page_source
            print("we got html of len", len(result['html_content']))
            
            driver.close()
            driver.quit()
            print("thread should close now")
            # except:
            #     articleParse(url,method=3)
        result = {}
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(selenium_retrieval, url, result)
            try:
                success = future.result(timeout=50)
                if success == True:
                    print("html content len = ", len(result["html_content"]))
                else:
                    print("thread failed")
            except TimeoutError:
                print("thread timed out")
                result["html_content"] = None
        html_content = result.get('html_content',"")
        print("len html_content after results.get:",len(html_content))
        soup = BeautifulSoup(html_content, 'lxml')
        paragraphs = soup.find_all(string=True)

    if method == 3:
        articleData = {
        "url": url,
        "title": None,
        "date": None,
        "content": ""
        }
        print("Can't Parse article at the following URL:" , url , "\n Moving to next result")
        return articleData
        

    print("we got past pagegen")

    articleData = {
        "url": url,
        "title": None,
        "date": None,
        "content": ""
    }

  
    mainTag = soup.find(["main"])
    
    try:
        titleTag = soup.find(["h1"])
        title = titleTag.get_text()
        articleData["title"] = title
    except:
        print("couldnt find article title at ", url)
        articleData["title"] = "Title Not Found"
    

    
    paragraphs = filter(tag_visible, paragraphs)
    
    
    content = ""
    # Extract and the text from each <p> tag, and add it to content
    for p in paragraphs:
        text = p.get_text()
        
        if len(text) >= 100:
            content = content + text
            # if method == 0: print('we assigned content var with')
        
        # print(text)

    articleData["content"] = content

    if articleData["content"] == "" and method == 1:
            print("Failure to parse article at URL:  ", articleData["url"])
            articleData["title"] = "Couldn't Find Title"

            return articleData
    if articleData['content'] == "":
        articleData = articleParse(url, method = 1 )
         


    return articleData

def txtFileParse(filepath):
    filepath = str(filepath)

    articleData = {
        "url": url,
        "title": None,
        "date": None,
        "content": ""
    }

    if filepath.endswith(".txt"):
        with open(filepath) as file:
            articleData["content"] = file.read()
        
        articleData["url"] = None#filepath
        articleData["title"] = str(os.path.splitext(os.path.basename(filepath))[0])
        articleData["date"] = str(datetime.fromtimestamp(os.path.getmtime(filepath)))

    return articleData

# url = "https://www.google.com/url?rct=j&sa=t&url=https://www.frontiersin.org/journals/radiology/articles/10.3389/fradi.2024.1433457/pdf&ct=ga&cd=CAEYECoUMTc2NTAxMDM2OTc4MDc5MjgwNzAyGmU2ZGY0ZjAyYTg1NzhlZmQ6Y29tOmVuOlVT&usg=AOvVaw19VxnEzZecVfdU7fAOnf8y"
# article = articleParse(url,method=1)
# print(article["content"])



