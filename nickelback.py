# Define a set that contains tuples. 
# Each tuple should contain two strings:

# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback. 
# You can see a list of their greatest hits on Amazon.
# Using a set comprehension, create a new set that contains all songs that were 
# not performed by Nickelback.

all_songs = {
    ('Nickelback', 'Photograph'),
    ('Billy Joel' ,'Uptown Girl'),
    ('First Aid Kit', 'My Silver Lining'),
    ('Led Zeppelin', 'Immigrant Song'),
    ('Nickelback', 'How You Remind Me')
}

my_songs = { artist for artist in all_songs if artist[0] != 'Nickelback'}

print(my_songs)