# Käyttöohje

## Asennus

Aja repon kloonauksen jälkeen seuraavat komennot:
```
cd tira-harjoitustyo
```
```
poetry install
```
## Käynnistys

Käynnistä sovellus komennolla: 
```
poetry run invoke start
```

## Ohjelman käyttö
![image](https://github.com/Savones/tira-harjoitustyo/assets/63465444/a8b92193-2d0f-49ce-993c-09975a60184d)
- Generoi uusi luolasto painamalla "Generoi luolasto" nappia
- Muuta seuraavalla generoinnilla generoitavien huoneiden määrää painamalla oikeassa alakulmassa olevia lukuja
- Näytä luolaston generointiin käytettyjen algoritmien eri vaiheita painamalla "Näytä vaiheet" painiketta. Jokainen painallus näyttää uuden vaiheen, kunnes lopullinen luolasto näkyy jälleen.

## Huom
Käyttöliittymä on toteutettu pygame kirjastolla. Pygame:n asetusten aikarajoitteiden takia saatat välillä kohdata seuraavan ilmoituksen:
![image](https://github.com/Savones/tira-harjoitustyo/assets/63465444/a8e9a441-ac17-40a2-b0c2-c55670ad140b)
Tässä tapauksessa "odota" napin painamisen jälkeen ohjelman pitäisi toimia normaalisti.

## Muita komentoja

Aja testit komennolla: 
```
poetry run invoke test
```
Generoi testikattavuusraportti komennolla: 
```
poetry run invoke coverage-report
```
Aja pylint komennolla: 
```
poetry run invoke lint
```
