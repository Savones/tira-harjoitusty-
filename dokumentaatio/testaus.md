# Testausdokumentti

## Testikattavuus
![image](https://github.com/Savones/tira-harjoitustyo/assets/63465444/ff01f150-d429-457d-927a-307a03d4554b)


## Mitä on testattu ja miten
Ohjelman käyttöliittymän kautta on testattu seuraavia asioita:
- Testattu, että “näytä vaiheet” painikkeen painaminen ennen yhdenkään luolaston generoimista ei aiheuta ongelmia.
- Testattu, että huoneiden määrää määrittelevien painikkeiden tapauksessa aina viimeiseksi painetun painikkeen määrä on se, montako huonetta generoituu seuraavalla “generoi luolasto” painikkeen painalluksella.
- Testattu, että huoneiden generointi toimii huoneiden määrän syötteillä 3 - 60. Graafiselle käyttöliittymälle määrät ovat kuitenkin rajoitettu valintoihin: 5. 10, 20, 30 ja 40. Alle 3 huoneen syötä aiheuttaa virheilmoituksen Prim algoritmissa, sillä kolmiointi lista on tyhjä. Yli 60 syöte puolestaan jumittuu huoneiden generointiin, sillä rajoitettuun tilaan ei mahdu niin montaa huonetta.
- Testattu  10 kertaa, että kaikki huoneiden keskipisteet ovat mukana Bowyer Watson kolmioinnissa, kun huoneita on 40.

Ohjelman nopeutta on testattu seuraavasti:
- Kun 5 huonetta generointiin 10 kertaan, keskimäärin painikkeen painalluksesta kului 6.829 sekuntia siihen, että graafinen esitys luolastosta näkyi. Min oli 5.942 sekuntia ja max 7.662 sekuntia.

- Kun 40 huonetta generointiin 10 kertaan, keskimäärin painikkeen painalluksesta kului 8.664 sekuntia siihen, että graafinen esitys luolastosta näkyi. Min oli 6.718, sekuntia ja max 11.204 sekuntia.

Ohjelman metodien toimivuutta on testattu automaattisilla yksikkötesteillä. Yksikkötestien seasta löytyy joitakin algoritmeja yleisemmällä tasolla testaavia testejä, esim:
- Bowyer-Watsonin algoritmin oikeellisuutta testattu automaattisella testillä, joka tarkastaa, että mikään huoneen keskipiste ei ole minkään lopullisen kolmioinnin kolmion ulkoympyrän sisällä. Lisäksi testattu, että yksikertaisemmalla esimerkillä kaikki huoneiden keskipisteet on otettu mukaan kolmiointiin. (Suuremmilla huone määrillä tehty sama manuaalisesti testaamalla)
- Testattu automaattisesti, että A* algoritmi valitsee halvimman reitin huoneesta toiseen. Testattu myös, että seinää esittävän 100 painoisen solmun A* osaa ohittaa halvimmalla mahdollisella tavalla. Automaattisesti testattu, että yksikertaisella esimerkillä A* etsii saman reitin huoneesta A huoneeseen B, kuin B:stä A:han. Kuitenkin manuaalisesti testaamalla havaittu, että joissain rajatapauksissa reitti on näillä eri.
- Prim:n algoritmia ei juurikaan testattu automaattisesti. Manuaalisesti kuitenkin testattu 10 kertaa, että 5:llä ja 40:llä huone määrällä jokaiseen huoneeseen löydetään vähintäänkin yksi reitti.

## Miten testit voi toistaa
Automaattiset testit voi ajaa komennolla:
```
poetry run invoke test
```
Testikattavuusraportin saa komennolla:
```
poetry run invoke coverage-report
```
Manuaalisesti testatut testit voi toistaa ajamalla ohjelman, ja toistamalla tämän dokumentin edellisessä osassa mainitut käyttöliittymän kautta tehdyt testit.

