import openai

openai.api_key="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"

text="Hormonal changes are also a major cause of why your hair may start thinning at a young age. Note that there are two phases of hair growth"

def ques_ans(content):  #to generate questions for text
    prompt="Generate 10 frequently asked questions from the given text '"+ content +"'"
    response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=1000,temperature=0.1)

    #gets only the text from the output
    questions=response["choices"][0]["text"]
    ques_list=questions.split("\n")
    #to seperate the numbers

    #remove numbering
    for i in range(2,12):
        ques_list[i]=ques_list[i].split(".")[1]

    #answering the questions
    for i in range(2,12):
    
        prompt= "Answer this question,"+ques_list[i]
        response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=100)
        answer=response["choices"][0]["text"]
    
        print("Q: ",ques_list[i])
        print("ans: ",answer.strip(),"\n")

ques_ans(text)

    



