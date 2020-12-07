# https://gist.github.com/aeksei/015d69a636effde7fcf29dc782515bcd
import re

#todo download file from git? change the path to it
FILENAME = r"C:\Users\1\PycharmProjects\LearnPythonProject\Sample text.txt"
# PATTERN1 = r"^#{4} (?P<pos>\d{1,2})\.\s+\[(?P<book>...+)\]\((?P<amazon>...+)\) by (?P<author>...+) \((?P<recomended>\d{1,2}\.\d{1,2})\%"
PATTERN1 = r"^#{4} (?P<pos>\d{1,2})\.\s+\[(?P<book>...+)\]\((?P<amazon>...+)\) by (?P<author>...+) \((?P<recomended>\d{1,2}\.\d{1,2})\%"
# PATTERN1 = r"#{4} (?P<pos>\d{1,2})\.\s+\[(?P<book>...+)\]"
# PATTERN1 = r"#{4} (\d{1,2})\.\s+\[(...+)\]"


def main():
    with open(FILENAME, 'r', encoding='utf-8') as txtFile:
        textData = str(txtFile.read())
    # print(textData)
    pattern = re.compile(PATTERN1, re.MULTILINE)  # , flags=re.MULTILINE
    print("*" * 20)
    for dataSet in pattern.finditer(textData):
        print(dataSet[1])
        print(dataSet[2])
        print(dataSet[3])
        print(dataSet[4])
        print(dataSet[5])


if __name__ == '__main__':
    main()
