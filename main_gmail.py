import gmailFetcher
import paragraphParser
import numpy as np

scopes = ['https://www.googleapis.com/auth/gmail.readonly']

service = gmailFetcher.authenticate(scopes)
messages = gmailFetcher.fetchNewsAlerts(service,query="grok ai",maxResults=200)
print("messages type,len", type(messages),",",len(messages))
final_links = []
for message in messages:
    html = gmailFetcher.extract_html(message,service)
    links = gmailFetcher.extractUrl(html)
    for link in links:
        final_links.append(link)

# final_links = np.concatenate(final_links).tolist()
print('len final_links',len(final_links))
print(final_links)
# links = ['https://med.stanford.edu/news/all-news/2025/01/walton-ai-conference.html']
# print(np.array(links))
# print(links)

# subjects = gmailFetcher.subject_fetcher(service)
# print(subjects)
articleData = []
iterator = 0
# # dict = paragraphParser.articleParse(links[0],method=1)
# for link in links:
#     artDataDict = paragraphParser.articleParse(link,method=1)
#     print(artDataDict["title"])
#     articleData.append(artDataDict)
#     iterator+=1
#     print("articles Processed = ", iterator)
#     print("appended article length = ", len(artDataDict["content"]))


