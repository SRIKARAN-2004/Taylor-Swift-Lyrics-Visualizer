# app.py

import streamlit as st
import lyricsgenius
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Replace with your Genius API token
GENIUS_API_TOKEN = 'rb1KmYsMfFS24W_XFKYo-m5Lubo3ACkFI-orVbPF_YhNZFKlrcAt3e9jRNe6VGgR'

# Initialize Genius client
genius = lyricsgenius.Genius(GENIUS_API_TOKEN)

# Streamlit UI
st.title("🎶 Taylor Swift Lyrics & Word Cloud Generator")
st.write("Enter a Taylor Swift song title to get the lyrics and generate a word cloud.")

# Input field
song_title = st.text_input("Enter Song Title:")

if song_title:
    with st.spinner('Fetching lyrics...'):
        try:
            # Search for the song (Taylor Swift specific)
            song = genius.search_song(song_title, artist="Taylor Swift")
            
            if song:
                lyrics = song.lyrics
                
                # Display lyrics in textbox
                st.subheader("Lyrics")
                st.text_area("Lyrics:", lyrics, height=300)
                
                # Generate word cloud
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(lyrics)
                
                # Display word cloud
                st.subheader("Word Cloud")
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                st.pyplot(fig)
            else:
                st.error("Song not found. Please check the title.")
                
        except Exception as e:
            st.error(f"Error: {e}")
