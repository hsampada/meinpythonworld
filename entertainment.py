import media
import fresh_tomatoes

ddlj=media.movie("Dilwale Dulhaniya","Raj takes away simran","https://en.wikipedia.org/wiki/Dilwale_Dulhania_Le_Jayenge#/media/File:Dilwale_Dulhania_Le_Jayenge_poster.jpg","https://www.youtube.com/watch?v=c25GKl5VNeY")

#print(ddlj.inline)
#ddlj.show_trailor()
#ddlj.show_poster()

hahk=media.movie("Hum aapke","Family story","https://en.wikipedia.org/wiki/Hum_Aapke_Hain_Koun..!#/media/File:Hahk.jpg","https://www.youtube.com/watch?v=45JY12a6zJA")

movie=[ddlj,hahk]
fresh_tomatoes.open_movies_page(movie)
