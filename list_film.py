class Prak5e1:
    
def main():
        films = []
        for i in range(5):
            film = input("Film favorit KE-{}: ".format(i+1))
            films.append(film)
        
        print("==========DAFTAR FILM FAVORIT==========")
        loops = 1
        for film in films:
            print(f"{loops}.) {film}")
            loops+=1
    
    def name(self, name, nim):
        return f'Praktikum 5 ({name} - {nim})'

