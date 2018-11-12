from html.parser import HTMLParser
N = int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->",i[0],">",i[1])


parser = MyHTMLParser()
for i in range(N):
    parser.feed(input())

# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
