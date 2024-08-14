from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

input("Enter your link: ")

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams. get_highest_resolution()

yd.download(r'c:\Users\JXA1470\Downloads')