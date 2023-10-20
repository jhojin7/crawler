from bs4 import BeautifulSoup

out_html = "<table border='1' flex>"


def get_question(idx):
    global out_html
    with open(f'examtopics-aws-dva-c02-{idx}.html', 'r') as f:
        html = f.read()
    bs = BeautifulSoup(html, 'lxml')
    question = bs.select_one("div.question-body")
    t1 = bs.select_one("p.card-text")
    t2 = bs.select_one("div.question-choices-container")
    # print(t1)
    # print(t2)

    out_html += "<tr flex>"
    out_html += f'<td flex ><br><a href="examtopics-aws-dva-c02-{idx}.html">{idx}</a></td>'
    out_html += f'<td id="p{idx}" flex style="overflow:auto;" >{t1.prettify()}<br>{t2.prettify()}</td>'
    # out_html += f"<td>{t2.prettify()}</td>"
    out_html += "</tr>"


# p.card-text
# div.question-choices-container

for i in range(101, 214):
    get_question(i)


outF = open("probs.html", 'w')
outF.write(out_html)
