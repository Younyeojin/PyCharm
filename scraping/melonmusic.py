from bs4 import BeautifulSoup
from urllib.request import urlopen


class MelonMusic(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artists = 0
        n_title = 0
        ls = soup.find_all(name='div', attrs={'class':'artist'})
        ls2 = soup.find_all(name='div', attrs={'class':'artist'})
        print(f'Top {len(ls)}')
        for i in ls:
            n_artists += 1
            print(str(n_artists)+"Rank")
            print("Artist: " + i.find('a').text + ' - '+ls2[n_title].find('a').text)
            n_title += 1


def main():
    MelonMusic(f'https://www.melon.com/chart/index.htm?'
               'dayTime=2021072109').scrap()


if __name__ == '__main__':
    main()