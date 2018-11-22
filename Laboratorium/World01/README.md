# Opis świata

W katalogu ```begin``` znajduje się definicja świata w którym rządzą następujące zasady:
* świat jest płaski i posiada wysokość i szerokość
* każdy organizm na świecie posiada: 
    * ```power```: zwiększa się co jedną turę o 1; decyduje o sile organizmu
    * ```initiative```: priorytet w kolejności wykonania ruchu w ramach jednej tury
    * ```position```: położenie w świecie
    * ```liveLength```: liczba tur do końca życia
    * ```powerToReproduce```: granica dolna siły, powyżej której może się rozmnażać; po rozmnożeniu traci połowę siły
    * ```sign```: znak reprezentujący organizm w świecie
    * ```world```: świat, w którym żyje organizm
* jedynym organizmem żyjącym na świecie jest trawa

# Zadanie

## Zwierze

* bazując na definicji organizmu napisać definicję
zwierzęcia, które prócz własności organizmu potrafi się przemieszczać i pamięta swoją ostanią pozycję
* w wyniku przemieszczania organizm może spotkać inny organizm; w wyniku takiego spotkania zachodzą konsekwencje opisane w organiźmie

## Owca
* bazując na definicji zwierzęcia zdefiniować owcę
* owca przemieszcza się i je trawę
* owca posiada następujące atrubuty:
    * ```power = 3```
    * ```power = 3```
	* ```initiative = 3```
	* ```liveLength = 10```
	* ```powerToReproduce = 6```
	* ```sign = 'S'```

Do świata dodać owcę o obserwować jak się rozwija w poszczególnych turach.