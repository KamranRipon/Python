from urllib.request import urlopen
from bs4 import BeautifulSoup 
from tkinter import *
import requests
 
 
class ShowData():
    """ Present the scraped data as in a GUI """
 
    def __init__(self):
        self.root = Tk()
 
        self.titleVar = StringVar()
        self.textVar = StringVar()
        self.linksVar = StringVar()
 
        self.urlVar = StringVar()
 
        self.make_widgets()
 
        self.root.mainloop()
 
    def make_widgets(self):
        self.root.title("Web page scraper")
 
        self.startButton = Button(command = self.fill_widgets, text = "URL 1:").grid(padx = 5, row = 0, column = 0)
        self.urlField = Entry(textvariable = self.urlVar, width = 50).grid(padx = 5, pady = 5, row = 0, column = 1)
##################################        
        self.startButton = Button(command = self.fill_widgets, text = "URL 2:").grid(padx = 5, row = 1, column = 0)
        self.urlField = Entry(textvariable = self.urlVar, width = 50).grid(padx = 5, pady = 5, row = 1, column = 1)
########################################## 
#        self.titlePrmpt = Label(self.root, text = "Title:").grid(row = 1, column = 0)
#        self.titleBox = Entry(self.root, textvariable = self.titleVar, width = 50).grid(row = 1, column = 1)
 
        self.textPrmpt = Label(self.root, text = "All text:").grid(row = 2, column = 0)
        self.textBox = Entry(self.root, textvariable = self.textVar, width = 100).grid(row = 2, column = 1)
 
        self.linksPrmpt = Label(self.root, text = "Hrefs:").grid(row = 3, column = 0)
        self.linksBox = Entry(self.root, textvariable = self.linksVar, width = 100).grid(row = 3, column = 1)
 
        self.allHtmlPrmpt = Label(self.root, text = "All HTML:").grid(row = 4, column = 0)
        self.allHtml = Text(self.root, width = 100)
        self.allHtml.grid(row = 4, column = 1)
 
    def fill_widgets(self):
        self.data = GetData(self.urlVar.get())
 
        self.titleVar.set(self.data.soupData["title"])
        self.textVar.set(self.data.soupData["text"])
        self.linksVar.set(self.data.soupData["hrefs"])
        self.allHtml.insert(END, self.data.soup.prettify())
 
 
class GetData():
    """ Get web-scraped data """
 
    def __init__(self, url):
        self.html = self.get_html(url)
        self.soup = BeautifulSoup(self.html)
        self.soupData = self.get_soup_data(self.soup)
 
    def get_html(self, url):
        raw = urlopen(url)
        return raw.read()
 
    def get_soup_data(self, soup):
        info = {"title": soup.title.string,
                "text": soup.get_text(),
                "links": soup.find_all("a"),
                "hrefs": []}
 
        for link in soup.find_all("a"):
            info["hrefs"].append(link.get("href"))
 
        return info
 
ShowData()