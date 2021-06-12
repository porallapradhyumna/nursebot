# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:15:47 2021

@author: PRADHYUMNA
"""

import pafy
import urllib.request
import re
  
#search_keyword="chitti"
def music_searcher(search_keyword):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[0]  
    
    video = pafy.new(url)
      
    
    best = video.streams[0]
    
    return best.url
"""
import vlc


best = music_searcher('dilaziz')
media = vlc.MediaPlayer(best)
  

media.play()

media.audio_set_volume(50)

media.pause()

media.stop()
"""
