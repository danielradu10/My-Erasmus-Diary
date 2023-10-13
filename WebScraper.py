import requests
import re
import random
from bs4 import BeautifulSoup

id_and_chapters = {
    "Geneza": "25",
    "a doua carte a lui Moise": "32",
    "Leviticul": "47",
    "Numerii":"59",
    "Deuteronom":"17",
    "Iosua":"41",
    "Judecatori":"46",
    "Rut":"71",
    "1 Regi":"66",
    "2 Regi":"67",
    "3 Regi":"68",
    "4 Regi":"69",
    "Paralipomena":"14",
    "2 Paralipomena":"15",
    "Ezdra":"23",
    "Neemia":"58",
    "Esterei":"21",
    "Iov":"42",
    "Psalmi":"65",
    "Proverbe":"63",
    "Ecclesiastul":"18",
    "Cantari":"9",
    "Isaia":"43",
    "Ieremia":"31",
    "Plângerile lui Ieremia":"64",
    "Iezechiel":"33",
    "Daniel":"16",
    "Osea":"60",
    "Amos":"3",
    "Miheia":"56",
    "Ioil":"39",
    "Avdie":"6",
    "Iona":"40",
    "Naum":"57",
    "Avacum":"5",
    "Sofonie":"73",
    "Agheu":"2",
    "Zaharia":"82",
    "Maleahi":"52",
    "Tobit":"81",
    "Iudita":"45",
    "Baruh":"8",
    "Ieremia Eistola":"20",
    "3 tineri":"1",
    "3 Ezdra":"24",
    "Intelepciunile lui Solomon":"74",

    "Matei":"55",
    "Marcu":"53",
    "Luca":"48",
    "Ioan":"35",
    "Faptele Apostolilor":"26",
    "Romani":"70",
    "1 Corinteni":"12",
    "2 Corinteni":"13",
    "Galateni":"29",
    "Efeseni":"19",
    "Filipeni":"28",
    "Coloseni":"10",
    "1 Tesaloniceni":"76",
    "2 Tesaloniceni":"77",
    "1 Timotei":"78",
    "2 Timotei":"79",
    "Tit":"80",
    "Filimon":"27",
    "Evrei":"22",
    "Iacov":"30",
    "1 Petru":"61",
    "2 Petru":"62",
    "1 Ioan":"36",
    "2 Ioan":"37",
    "3 Ioan":"38",
    "Iuda":"44",
    "Apocalipsa":"4"

}

categories_and_links = {
    "credinta":["https://www.wordproject.org/bibles/verses/romanian/04_faith.htm"],
    "dragoste":["https://www.wordproject.org/bibles/verses/romanian/05_love.htm"],
    "putere":["https://www.wordproject.org/bibles/verses/romanian/31_boldness.htm", "https://www.wordproject.org/bibles/verses/romanian/18_strength.htm"],
    "fericire":["https://www.wordproject.org/bibles/verses/romanian/17_happiness.htm"],
    "perioada grea":["https://www.wordproject.org/bibles/verses/romanian/28_dependency.htm", "https://www.wordproject.org/bibles/verses/romanian/22_discipline.htm", "https://www.wordproject.org/bibles/verses/romanian/26_peace.htm"],
    "mandire":["https://www.wordproject.org/bibles/verses/romanian/33_pride.htm"]

}

class WebScraper:

    def generate_verse(self, categorie) -> (str, str):
        verset = ""
        if(len(categories_and_links[categorie]) == 1):
            req = requests.get(categories_and_links[categorie][0])
            soup = BeautifulSoup(req.content, "html.parser")
        else:
            req = requests.get(categories_and_links[categorie][random.randint(0, len(categories_and_links[categorie]))-1])
            soup = BeautifulSoup(req.content, "html.parser")

        versete_lista = []

        for link in soup.find_all('a'):
            str_link = str(link)
            if (str_link.__contains__("opens new window")):

                first_list = ' '.join(re.findall(r'(>.*? \d+:\d+<)', str_link)).removeprefix(">").removesuffix("<")
                if (len(first_list) != 0):
                    versete_lista.append(first_list)
                second_list = re.findall(r'(>.*? \d+:(\d+, )+\d+<)', str_link)
                if (len(second_list) != 0):
                    versete_lista.append(second_list[0][0].removeprefix(">").removesuffix("<"))





        verset_ales = random.randint(0, len(versete_lista)-1)


        print("Verset ales: ")
        print(versete_lista[verset_ales])

        capitol = re.findall(".*? \d+", versete_lista[verset_ales])[0].removesuffix("")
        nume_capitol = re.sub(" \d+", '', capitol)
        numar_capitol = re.findall(" \d+:", versete_lista[verset_ales])[0].removesuffix(":").removeprefix(" ")
        numere_versete = re.findall(":\d+", versete_lista[verset_ales])[0].removeprefix(":").split(", ")




        id = id_and_chapters[nume_capitol]
        url = "https://www.bibliaortodoxa.ro/carte.php?id="
        cap = "&cap="

        try:
            continut = requests.get(url + id + cap + numar_capitol)

            soup = BeautifulSoup(continut.content, "html.parser")
            my_versets = []
            for my_verset in soup.find_all("td"):
                if (my_verset.next != "\n"):
                    my_versets.append(my_verset.next)

            print(numere_versete)
            for numar in numere_versete:
                try:

                     verset = verset + my_versets[int(numar) - 1]
                     print(my_versets[int(numar) - 1])
                except:
                    print("Mai incearca o data")


        except Exception:
            print("Mai incearca o data, te rog")

        return (verset, versete_lista[verset_ales])

