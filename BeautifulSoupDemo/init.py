#ref 1: https://www.dataquest.io/blog/web-scraping-tutorial-python/
#ref 2: http://docs.python-requests.org/en/master/api/
import requests
from bs4 import BeautifulSoup
import re


page = requests.get("https://brainly.com/")
print(page) #prints response object
print(page.status_code) #prints status_code property
#print(page.content) #prints the HTML content of the website (in bytes)
#print(page.text) #prints the HTML content of the website (in unicode)
page_content = page.text

# file = open("content.txt", "w+")
# file.write(page.text)
# file.close()

#parse this document using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify()) #prints the byte content in html format
#select all the elements at the top level of the page using the children property of soup
#print(list(soup.children)) #output: ['\n', 'html', '\n', <html lang="en-US"> ....]
# select html tag and its children by taking the fourth element in the list
#html = list(soup.children)[3]
#print(list(html.children))
# but these are cumbersome. we can use specific methods to extract tags and elements
#print(soup.find_all('p')) #returns 2 <p> items #this returns a list
# find_all returns a list, so we’ll have to loop through, or use list indexing, it to extract text:
#print(soup.find_all('p')[1].get_text())
# search for any div tag that has the class "sg-content-box__content":
#print(soup.find_all('div', class_='sg-content-box__content'))
# look for any tag that has the class "sg-content-box__content":
#print(soup.find_all(class_='sg-content-box__content'))
# finds a tag inside div tag
#print(soup.select("div a"))
# -----------------------------------------------------------------------------------
#
#print(soup.find('div', class_ ="brn-stream"))
div_brn_stream = soup.find_all('div', class_ ="brn-stream")
#print(len(div_brn_stream)) #length=1

#finds all the article and store it into article_list
for article in div_brn_stream:
    article_list = article.find_all('article', class_ ="task brn-stream-question")
    #print(article_list)

#prints number of questions present in the page
print(len(article_list))
#ref: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes

for article in article_list:
    #print(article.attrs) #print all the attributes
    print(article['data-z']) #access attribute using 'attribute_name'



#capture all the question number in the format /question/*question_no* :: /question/519259
# for link in soup.find_all('a'):
#     bool = re.match("/question/[0-9]", link.get('href'))
#     if bool:
#         print(link.get('href'))



