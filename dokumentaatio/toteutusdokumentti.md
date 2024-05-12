# Toteutusdokumentti

## Yleisrakenne

Ohjelma on luolaston generointi työkalu. Ohjelmaa käytetään graafisella käyttöliittymällä (pygame), josta käyttäjä voi valita huoneiden määrän ja generoida luolaston. Käyttäjä voi myös tutkia eri luolaston generointiin käytettyjen algoritmien vaiheita graafisina esityksinä. Generointi alkaa huoneiden sijaintien ja kokojen arpomisesta. Sitten ohjelma suorittaa Bowyer-Watsonin algoritmin huoneiden keskipisteiden kolmiointiin. Tämän jälkeen Primin algoritmi etsii kolmioinnista pienimmän virittävän puun. Sitten osa alkuperäisen kolmioinnin kaarista lisätään äsken saatuujen kaarien joukkoon, ja saadaan lista huoneita, joiden välillä on käytävä. Lopuksi vielä käytetään A* algoritmia käytävien lopullisten reittien määrittämiseen. A* on toteutettu niin, että olemassa olevien käytävien kautta kulkeminen on halvempaa, kuin uuden käytävän muodostaminen. 

### Rakenne kaaviona

```mermaid
classDiagram
ui --> services
services --> entities

class ui {
    Ui
}

class services {
    RoomService
    Logic
    Mst
    Astar
    Triangulation
}

class entities {
    Room
    Vertex
    Triangle
}

```

### Luokkakaavio

```mermaid
classDiagram

Ui --> Logic

Logic --> RoomService
Logic --> Triangulation
Logic --> Mst
Logic --> Astar
Logic ..> Triangle
Logic ..> Vertex
Logic ..> Room

Triangulation ..> Triangle
Triangulation ..> Vertex

class Ui {
    +logic: Logic
    +start()
}

class Logic{
    +room_service: RoomService
    +reset()
    +generate_rooms(amount: int) -> list
    +generate_room_vertices() -> list
    +get_triangulation() -> tuple
    +get_mst(triangulation: list) -> list
    +get_chosen_edges() -> list
    +get_a_star_paths() -> list
}

class RoomService {
    +check_overlap(checked_room: Room, rooms: list) -> bool
    +check_inside_triangle(room: Room, triangle: Triangle) -> bool
    +check_room_in_rect(room: Room) -> bool
    +check_point_inside_triangle(point: tuple, triangle: Triangle) -> bool
}

class Triangulation {
    +super_triangle: Triangle
    +room_vertices: list
    +get_triangulation() -> tuple
    +get_bad_triangles(point: tuple) -> list
    +get_polygon(bad_triangles: list) -> list
    +add_triangles(polygon: list, point: tuple)
    +remove_super_triangle() -> list
}

class Mst {
    +room_vertices: list
    +triangulation: list
    +get_mst() -> list
    +calculate_distance(vertex1: Vertex, vertex2: Vertex) -> float
    +create_graph() -> list
    +get_min_index(distance: list, visited: list) -> int
    +get_mst_edges(parent: list) -> list
}

class Astar {
    +add_rooms_to_maze(room_list: list)
    +make_edge_list()
    +get_astar_paths(paths: list, room_list: list) -> list
    +run_astar(start: tuple, end: tuple)-> list
    +update_maze(pos: tuple)
    +choose_door(start_room: Room, end_room: Room) -> tuple
    +get_door(room: Room) -> list
}

class Room {
    +x: int
    +y: int
    +width: int
    +height: int
    +str() -> str
}

class Vertex {
    +x: int
    +y: int
    +str() -> str
}

class Triangle {
    +vertex1: Vertex
    +vertex2: Vertex
    +vertex3: Vertex
    +str() -> str
    +get_circum_center() -> list
    +do_vertex_calculations(vertex1: Vertex, vertex2: Vertex) -> tuple
    +point_in_circumcircle(point: tuple) -> bool
}

```
## Aikavaativuudet
- Bowyer-Watson algoritmi on toteutettu O(N log N) ajassa
- Prim algoritmi toteutettu O(N^2) ajassa
- A* algoritmi toteutettu O(b^d) ajassa

## Puutteet ja parannusehdotukset
Ohjelman suurin kompastuskivi on luolastojen generoinnin hitaus. Tällä hetkellä generointiin menee noin 5-10 sekunttia. Hitaus johtuu Astar luokan make_edge_list metodista, jossa generoidaan 1200x900 solmulle kaarilista.
Ohjelmaa voisi myös parantaa antamalla käyttäjälle mahdollisuuden syöttää haluamansa huoneiden määrän valmiiksi annettujen vaihtoehtojen sijaan. Lisäksi mahdollisuus ladata generointu luolasto omalle laitteelle tekisi ohjelmasta hyödyllisemmän. 

## Laajat kielimallit
Ohjelmassa on hyödynnetty ChatGPT:tä seuraavissa tapauksissa:
- Apuna Triangle-luokan kolmion ulkoympyrän keskipisteen laskevissa metodeissa get_cirmum_center ja do_vertex_calculations
- Ui-luokan koodin refaktoroinnissa, sekä huoneiden määrää muuttavien nappien koordinaattien laskennassa
- RoomService-luokan check_point_inside_triangle metodin toteutuksen apuna
- Mst-luokan create_graph metodin debuggaamisessa

## Viitteet
- https://vazgriz.com/119/procedurally-generated-dungeons/ 
- https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/ sivu 124
- https://www.gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/
- https://www.freecodecamp.org/news/prims-algorithm-explained-with-pseudocode/
