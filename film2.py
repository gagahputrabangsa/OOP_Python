class Film:
    
def __init__(self, film, year, director):
        self.film = film
        self.year = year
        self.director = director

    def person(self, name, id):
        return f'Prak 5 ({name} - {id})\n-------------------ELKOM 2-------------------'


# obj
film1 = Film("Alice in the hood", 1999, 'james wan')
film2 = Film("Makan dimakan", 2001, 'wg brother')
film3 = Film("Naruto The legend of spiderman", 2015, 'uzumaki kirito')
film4 = Film("Kuntilanak 2", 2020, 'saipul jamilah')
film5 = Film("Jane Doe", 2022, 'james wan')


# List of object film
people_list = [film1, film2, film3, film4, film5]

#  object film
person = Film('', 0, '')
# call person func

persons = person.person('nama', 'nim')
print(persons.center(93))

# access with loop
loops = 1
for film in people_list:
    print(f'Film favorit ke-{loops}:\nJudul: {film.film}\nRilis: {film.year}\nDirector: {film.director}\n=================')
    loops += 1
