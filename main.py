# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
import openai
from flask import Flask, render_template, request
from flaskwebgui import FlaskUI
import random

FAQ = Flask(__name__)
faqg=FlaskUI(FAQ)



@FAQ.route("/")
def start():
    generate_web_list()
    return render_template("start.html",list=website_list)

@FAQ.route("/",methods=["POST"])
def website_page():
    webpage=request.form.get("article")
    print(webpage)
    heading=heading_gen(webpage)
    qna=gen(webpage)
    return render_template("view.html",link=webpage,title=heading,list_qna=qna)


openai.api_key="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"

website_list=[]

def generate_web_list():
    #response in in jason format 
    response=requests.get("https://www.bajajfinservhealth.in/articles-sitemap-0.xml")
    main_doc=response.text
    web_details= BeautifulSoup(main_doc,'html.parser')
    #to get all the websites to website_list
    for link in web_details.find_all('loc'):
        website_list.append(link.text)
    print(len(website_list))

def heading_gen(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    heading = soup.find('h1').get_text()
    return heading

def gen(url):
    article_content = ""

    # url = "https://www.bajajfinservhealth.in/articles/safety-measures-for-employees"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    for i in range(5):
        chosen_p = random.choice(soup.select('p span'))
        article_content += chosen_p.get_text()
    return ques_ans(article_content)

def ques_ans(content):  #to generate questions for text
    
    prompt="list 3 short questions for the given text '"+ content +"'"
    response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=100,temperature=0.1)

    #gets only the text from the output
    questions=response["choices"][0]["text"]
    ques_list=questions.split("\n")
    #to seperate the numbers
    print(ques_list)

    #remove numbering
    for i in range(2,5):
         ques_list[i]=ques_list[i].split(".")[1]

    list_of_qna = []
    # #answering the questions
    for i in range(2,5):
    
        prompt= "Answer in following question one line,"+ques_list[i]
        response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=100)
        answer=response["choices"][0]["text"]

        list_of_qna.append(ques_list[i])
        list_of_qna.append(answer.strip())

    return list_of_qna

    
#to run app
# use incase of debugging
# if __name__ == '_main_':
#     FAQ.run(debug = True)
FAQ.run()