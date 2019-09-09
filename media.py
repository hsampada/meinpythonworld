import webbrowser

class movie():
    def __init__(self,title,storyline,poster,youtubel):
        self.title=title
        self.storyline=storyline
        self.poster_image_url=poster
        self.trailer_youtube_url=youtubel
        
    def show_trailor(self):
        webbrowser.open(self.trailer_youtube_url)
    
    def show_poster(self):
        webbrowser.open(poster_image_url)
