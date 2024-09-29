# HeatCheck
CS302 Final Project

<br><h2>General description:</h2>
Fashion = life && money;<br>

“Heat Check” is an image classification and ranking system that uses a webcam to rank a subject’s outfit. Our app uses computer vision to identify each article of clothing a subject is wearing and, using a classification algorithm based on a number of different style niches, determine how each piece of clothing matches an aesthetic. Our algorithm then determines how similar and unique the subject’s outfit is (based on what style the outfit most closely matches) and quantifies this as “Heat.” The user’s “Heat” is then placed on the leaderboard hosted by a small-scale Azure server (this has basic user authentication).


<h2>Duties:</h2>
Adam: Developing algorithm to separate each article of clothing from jpg passed from Andrew's code and pass to Christian as jpg image. Also develop web interface using Azure (if time allows) to host back and frontend. Frontend is a simple GUI that requestes webcam permissions and creates leaderboard for all users.<br>
Alex: Scraping outfit data off Pinterest so we have data to judge our heat. Digging into the Pinterest API, figuring out how to make it all work.<br>
Andrew: Interfacing with webcam to take images and stream a preview, learning Python hehe<br>
Christian: work on image classifier to identify article of clothing and color of clothing and (if time allows) the style of the article of clothing


