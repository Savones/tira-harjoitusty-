# Määrittelydokumentti
## Yleistä
Opinto-ohjelmana tietojenkäsittelytieteen kandidaatti. Projektin dokumentaatiossa käytetty kieli on suomi, mutta mm. koodin muuttujien nimeämisessä sekä commit-viesteissä käyttökielenä englanti.
## Aihe ja ydin
Harjoitustyön aiheena on luolaston generointi ohjelma. Käyttäjä syöttää huoneiden määrän, minkä jälkeen ohjelma generoi luolaston, eli huoneet ja niiden väliset käytävät niin, että jokaiseen huoneeseen johtaa ainakin yksi käytävä.
Ohjelman ytimenä on huoneiden ja käytävien generointiin sovelletut algoritmit. Ohjelmalle toteutetaan graafinen käyttöliittymä.
## Syötteet
Ohjelma saa syötteenä generoitavien huoneiden määärän. Huoneiden määrä on kuitenkin rajoitettu.
## Algoritmit
- Bowyer-Watson algoritmi
  - Delaunay-kolmiointiin
  - Aikavaatimus O(N log N)
- Prim algoritmi
  - Saadaan käytävistä pienin virittävä puu
  - Aikavaativuus O(N^2)
- A* algoritmi
  - Saadaan yhdistettyä lopulliset käytävät
  - Aikavaatimus O(b^d)
## Ohjelmointkielet
Ohjelma toteutetaan Python ohjelmointikielellä. Vertaisarvioinnin voin tehdä Python projektille, tarvittaessa myös Javascript projektille.
