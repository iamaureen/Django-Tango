import requests
from bs4 import BeautifulSoup
import json

class parser:
    def html_parse(self, html_data):
        soup = BeautifulSoup(html_data, 'html.parser')
        #print(soup.prettify()) #prints the byte content in html format

        question_dict = {} #store info about each question
        question_list = [] #store each question object

        div_brn_stream = soup.find_all('div', class_ ="brn-stream")
        #print(len(div_brn_stream)) #length=1; because only one div is present with this class

        #finds all the article in the above div and store it into article_list
        for article in div_brn_stream:
            article_list = article.find_all('article', class_ ="task brn-stream-question")
            #print(article_list)

        #prints number of questions present in the page
        print(len(article_list))

        for article in article_list:
            print(article.attrs) #print all the attributes
            #article['data-z'] gives a json with question id and other values

            if article.has_attr('data-z'):
                print('yes')
                data = json.loads(article['data-z']) #converting to Python data struction

                ##obtain question_id
                question_id = data['id']
                print('question id :: ', question_id)
                ##obtain number of responses for this particular question
                number_of_responses = data['responses']
                print('number of responses :: ', number_of_responses)

                ##obtain question_subject
                #article contains <li><a>..</a></li> which contains the subject info. so we use a select('li a') to obtain only one elemet.
                #then we obtain the text to get the subject name and use strip() to remove any white spaces
                question_subject = article.select('li a')[0].get_text().strip()
                print('question subject :: ', question_subject)

                ##obtain user name
                div_username_list = article.find_all('div', class_='sg-avatar ') #gives a list; with each iteration, there is only on div with this classname, so list size is
                                                                           #always 1. that is why we access the list with 0 index in the following line

                a_username_list = div_username_list[0].find_all('a') #this also gives a list of 1 element, since there is only one <a> tag here.
                username = a_username_list[0].get('title') #only one element, so we access it using index 0 and then extract the title
                print('username :: ', username)

                #print(article)
                print("-----------------------------------------------------------")
                question_dict['question_id'] = question_id
                question_dict['number_of_responses'] = number_of_responses
                question_dict['username'] = username
                question_dict['question_subject'] = question_subject

                question_list.append(question_dict.copy()) #https://stackoverflow.com/questions/23724136/appending-a-dictionary-to-a-list-in-a-a-loop-python


            else: #latest questions, does not have data-z tag
                print('no')
                tag_div = article.find_all('div', class_ = 'sg-content-box__title')
                #returns a list of one element, so need to access it using index 0
                tag_a = tag_div[0].find_all('a')
                #print(tag_a)
                for a in tag_a:
                    #get username
                    if 'profile' in a['href']:
                        #print(a['title'])
                        username = a['title']
                    #get question subject
                    elif 'subject' in a['href']:
                        #print(a.text.strip())
                        question_subject = a.text.strip()

                tag_div = article.find_all('div', class_ = 'sg-content-box__content')
                tag_a = tag_div[0].find_all('a')
                for a in tag_a:
                    if 'question' in a['href']:
                        #get question id
                        #print(a['href'].split('/')[2])
                        question_id = a['href'].split('/')[2]
                        #get question text
                        #print(a.text.strip())
                        question_text = a.text.strip()


                print("-----------------------------------------------------------")


        # #print(json.dumps(question_list))
        # return json.dumps(question_list)
