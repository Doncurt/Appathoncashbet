import requests
from bs4 import BeautifulSoup

questions = []
answers = []


# script https://coin.cashbet.com/faq/
def loadWord():
    quote_page = "https://coin.cashbet.com/faq/"
    page = requests.get(quote_page)
    soup = BeautifulSoup(page.content, "html.parser")
    # questions are in <a>
    for s in soup.findAll('a'):
        questions.append(s.findAll(text=True))

    # answers are in <div, class="panel-body">
    for s in soup.findAll('div', {"class": "panel-body"}):
        answer = ""
        # each paragraph is in <p>
        for p in s.findAll('p'):
            paragraph = p.findAll(text=True)
            if paragraph != []:
                if answer == "":
                    answer += paragraph[0]
                else:
                    answer = answer + " " + paragraph[0]
            # scraping youtube video url
            for url in p.find_all('iframe'):
                if answer == "":
                    answer += url['src']
                else:
                    answer = answer + " " + url['src']
        # scraping bullet points
        for li in s.findAll('li'):
            list_ = li.findAll(text=True)
            answer = answer + " " + list_[0]
        answers.append(answer)
    # for url in soup.find_all('iframe'):
    #     print(url['src'])
    # for s in soup.findAll('p'):
        # answers.append(s.findAll(text=True))
    # answers.append(s.findAll(text=True)) for s in soup.findAll('p'))
    # print(answers)
    return (questions, answers)


# write data in text files
def write_data_txt(scripted_data):
    questions, answers = scripted_data
    # create text file for questions
    questions_txt_file = open("questions.text", "w")
    # create text file for answers
    answers_txt_file = open("answers.text", "w")
    for question in questions:
        if question != []:
            # to get only question sentense, filters by ?
            if question[0][len(question[0])-1] == "?":
                questions_txt_file.write(question[0] + "\n")
    questions_txt_file.close()
    for answer in answers:
        # if answer != []:
        answers_txt_file.write(answer + "\n")
    answers_txt_file.close()


def main():
    scripted_data = loadWord()
    write_data_txt(scripted_data)


if __name__ == "__main__":
    main()
