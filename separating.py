from bs4 import BeautifulSoup
import pandas as pd

def read_html(path):
    opened = open(path,'r', encoding="utf8")
    html = opened.read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def extract_between(text,end,start = 0):
    return text[start:end]
def extract_part(collector,text,title):
    mark = text.find(title)+len(title)+1 # extra + cause of \n
    collector.append(extract_between(text,mark))
    return text[mark:]
def get_line_before_this(text,index):
    if index >= len(text) or index < 0:
        raise ValueError("Index out of bounds")

        # Find the start of the line by searching for the nearest newline character before the index
    start_of_line = text.rfind('\n', 0, index)

    # If there is no newline character before the index, consider the start of the text as the beginning of the line
    if start_of_line == -1:
        start_of_line = 0
    else:
        # Move one position forward to exclude the newline character
        start_of_line += 1

    # Find the end of the line by searching for the nearest newline character after the index
    end_of_line = text.find('\n', index)

    # If there is no newline character after the index, consider the end of the text as the end of the line
    if end_of_line == -1:
        end_of_line = len(text)

    # Extract the last full line
    last_full_line = text[start_of_line:end_of_line].strip()

    return last_full_line,start_of_line

if __name__ == "__main__":
    text = read_html('adr_full-html.html')

    total_data = list()

    #Start first one manually

    start_mark = text.find("NOTIFIED - ")
    title,start_index = get_line_before_this(text,start_mark-3)
    current = list()
    current.append(title)
    text = text[text.find("1. CONTACT DETAILS")+len("1. CONTACT DETAILS")+1:]



    while True:
        text = extract_part(current,text,"2. TYPE AND SECTOR OF DISPUTES")
        text = extract_part(current, text, "3. PROCEDURE")
        text = extract_part(current, text, "4. HISTORY")
        next_mark = text.find("NOTIFIED - ")
        if next_mark == -1: # last case in file
            current.append(text)
            total_data.append(current)
            break
        else:
            next_title,history_end = get_line_before_this(text,next_mark-3)
            current.append(text[:history_end])
            total_data.append(current)
            current = list()
            current.append(next_title)
            text = text[text.find("1. CONTACT DETAILS")+len("1. CONTACT DETAILS")+1:]

    titles = ["title","contact_details","type_and_sector","procedure","history"]
    df = pd.DataFrame(data=total_data,columns=titles)
    df.to_csv('data.csv',index=False)
