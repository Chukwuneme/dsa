
class Music():
	"""represents a single music in the list"""
	def __init__(self, name):
		self.name = name
		self.next = None
		self.prev = None

class Music_list():
	"""represents a music playlist"""
	def __init__(self):
		self.first_music = None
		self.current = None
		self.last_music = None
		self.songs = []

	def add_music(self, name):
		music = Music(name)

		if not self.first_music:
			self.first_music = music
			self.current = music
			self.last_music = music
			self.songs.append(music.name)


		else:
			self.last_music.next = music #add this new music as next
			music.prev = self.last_music #set the previous music
			self.last_music = music #set the last music to our new music
			self.songs.append(music.name)

	def play(self, name):
		if name in self.songs:
			print("currently playing -> {}".format(name))
			return
		else:
			print("Song not in playlist")


	def play_next(self,):
		"""code to play next song"""
		if self.current == None:
			print("No music currently selected")
			return

		elif self.current.next == None:
			print("No next music to play")
			return

		self.current = self.current.next
		print("currently playing -> {}".format(self.current.name))


	def play_current(self):
		"""code to play current song"""
		if self.current == None:
			print("No music currently selected")
			return

		print("currently playing -> {}".format(self.current.name))

	
	def play_previous(self):
		"""code to play previuos song"""
		if self.current == None:
			print("No music currently selected")
			return

		elif self.current.prev == None:
			print("No previous music to play")
			return

		self.current = self.current.prev
		print("currently playing -> {}".format(self.current.name))

	def play_all(self):
		"""code to paly all songs in play list"""
		self.current = self.first_music
		if not self.current:
			print("No music to play")
			return

		while self.current:
			song_name = self.current.name
			self.play(song_name)
			self.current = self.current.next

		print("All songs played")


"""music1 = Music("I have a dream")
music2 = Music("Last last")
music3 = Music("Buga")
music4 = Music("Azonto")
music5 = Music("random")"""

"""lets set the order of the music"""

songs = Music_list()

song_list = ["I have a dream", "Last last", "Buga", "Azonto", "random"]

for name in song_list:
	songs.add_music(name)

print("Playing previous music.....")
songs.play_previous()
print("")

print("Playing current music.....")
songs.play_current()
print("")

print("Playing next music.....")
songs.play_next()
print("")

print("Playing next music.....")
songs.play_next()
print("")

print("Playing all music...")
songs.play_all()






