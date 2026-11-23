
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_songs(self, song):
        if song is not self.songs:
            self.songs.append(song)
            print(f"{song} added to playlist")
        else:
            print("song already exist")    

    def remove_songs(self, song):
        if song in self.songs:
             self.songs.remove(song)
             print(f"{song} remove from playlist")
        else:
            print("song not exist")      

    def list_of_songs(self):
        for i in self.songs:
            print(f"{i}")


s1 = Playlist("favorites")     
s1.add_songs("tera")       
s1.add_songs("kera")       
s1.add_songs("mera")       
s1.add_songs("lera")       

s1.list_of_songs()
s1.remove_songs("lera")
s1.list_of_songs()
            

        