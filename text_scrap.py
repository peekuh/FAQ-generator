# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re

#response in in jason format 
response=requests.get("https://www.bajajfinservhealth.in/articles-sitemap-0.xml")
main_doc=response.text
web_details= BeautifulSoup(main_doc,'html.parser')

count=0
website_list=[]
#to get all the websites to website_list
for link in web_details.find_all('loc'):
    website_list.append(link.text)

# print(website_list)

print(len(website_list)," no. of articles found \n #########################")

# for i in website_list:
check=requests.get(website_list[3])
doc=check.text
web= BeautifulSoup(doc,'html.parser')

c=(web.find("div",class_="e-css-7h4c0a"))

avoid=["strong","img","a"]

tags=["h2","h3","p","ul","li"]
for k in c:
    if (k.name not in avoid):
        if (k.name=="h2"):
            print("------------------------")
        if (k.name=="h3"):
            print("\n")
        if (k.string!=None):    
            print(k.string)
        else:
            for j in k:
                print(j.text)


def ques_ans(content):  #to generate questions for text
    prompt="Generate 5 questions from the given text '"+ content +"'"
    response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=1000,temperature=0.1)

    #gets only the text from the output
    questions=response["choices"][0]["text"]
    ques_list=questions.split("\n")
    #to seperate the numbers

    #remove numbering
    for i in range(2,7):
        ques_list[i]=ques_list[i].split(".")[1]

    #answering the questions
    for i in range(2,7):
    
        prompt= "Answer this question,"+ques_list[i]
        response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=100)
        answer=response["choices"][0]["text"]
    
        print("Q: ",ques_list[i])
        print("ans: ",answer.strip(),"\n")

def gen(url):
    article_content = ""

    # url = "https://www.bajajfinservhealth.in/articles/safety-measures-for-employees"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    for i in range(10):
        chosen_p = random.choice(soup.select('p span'))
        article_content += chosen_p.get_text()
    ques_ans(article_content)

    ###################################

from bs4 import BeautifulSoup
import requests
import random
import openai
openai.api_key="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"

def ques_ans(content):  #to generate questions for text
    prompt="Generate 5 questions from the given text '"+ content +"'"
    response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=1000,temperature=0.1)

    #gets only the text from the output
    questions=response["choices"][0]["text"]
    ques_list=questions.split("\n")
    #to seperate the numbers

    #remove numbering
    for i in range(2,7):
        ques_list[i]=ques_list[i].split(".")[1]

    list_of_qna = []
    #answering the questions
    for i in range(2,7):
    
        prompt= "Answer this question,"+ques_list[i]
        response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=100)
        answer=response["choices"][0]["text"]

        list_of_qna.append(ques_list[i])
        list_of_qna.append(answer.strip())

        print("Q: ",ques_list[i])
        print("ans: ",answer.strip(),"\n")

def gen(url):
    article_content = ""

    # url = "https://www.bajajfinservhealth.in/articles/safety-measures-for-employees"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    for i in range(10):
        chosen_p = random.choice(soup.select('p span'))
        article_content += chosen_p.get_text()
    ques_ans(article_content)

def heading_gen(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    heading = soup.find('h1').get_text()
    print(heading)


heading_gen("https://www.bajajfinservhealth.in/articles/homeopathy-medicine-for-hair-fall")

gen("https://www.bajajfinservhealth.in/articles/homeopathy-medicine-for-hair-fall")