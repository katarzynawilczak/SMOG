## SMOG: symulacja rozprzestrzeniania się zanieczyszczeń

Projekt SMOG realizowany w ramach ćwiczeń projektowych Modelowanie i Symulacja Systemów z użyciem języka Python. 

### Cel projektu

Na podstawie symulacji rzeczywistych danych pogodowych oraz pomiarów pm10 i pm2.5 określić uproszczony model propagacji zanieczyszczeń. 
Rzeczywiste dane pogodowe pochodziły ze strony - windy.com, a poziom zanieczyszczeń - airly.com. Symulacja została przeprowadzona dla dwóch przedziałów czasowych - codziennie, co 12h przez tydzień oraz co goidzinę dla jednego konkretnego dnia. Na tej podstawie skonstruowałyśmy prosty model propagacji zanieczyszczenia na terenie centrum Krakowa, biorąc pod uwagę takie czynniki atmosferyczne jak: temperatura powietrza, opady, czy siła i kierunek wiatru. Po podaniu aktualnych danych pogodowych, propagacja przewiduje zanieczyszczenia dla następnych 5h. 

### Instrukcja uruchomienia programu

Wymagania:
*minimalna wersja python2.7 
*zainstalowane biblioteki: tkinter, matplotlib, numpy, scipy

Instalacja bibliotek
```
pip install tkinker
pip install matplotlib
pip install numpy
pip install scipy
```

Pobranie i uruchomienie programu w terminalu (linux)
```
git clone https://github.com/katarzynawilczak/SMOG.git
cd SMOG
cd src
python picker.py
```
Następnie postępuj zgodnie z poleceniami w oknach i obserwuj wyniki symulacji. Generowanie kolejnych klatek może potrwać chwilę.

### Przykładowe wyniki symulacji 

**Przykładowe wyniki propagacji**

![propagacja](https://i.postimg.cc/526w16Zq/prop-nasze.jpg)


### Pełna dokumentacja projektu

Pełna dokumentacja projektu dostępna jest w folderze ```doc``` lub pod poniższym linkiem.

[Pełna dokumentacja](doc/smog-doc.pdf)

#### Linki
[Diagram klas ](https://www.draw.io/?state=%7B%22ids%22:%5B%221KJV--jaG2o_GnW2Z4IpWZ37yDqpHKIWj%22%5D,%22action%22:%22open%22,%22userId%22:%22104827397287133303073%22%7D#G1KJV--jaG2o_GnW2Z4IpWZ37yDqpHKIWj)
