# https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()

res = spotify_worldwide_daily_song_ranking.groupby(['artist']).size().reset_index(name='n_occurences')
res
