# HeatCheck
CS302 Final Project

<h2>General description:</h2>
Fashion = life && money;<br>

“Heat Check” is an image classification and ranking system that uses a webcam to rank a subject’s outfit. Our app uses computer vision to identify each article of clothing a subject is wearing and, using a classification algorithm based on a number of different style niches, determine how each piece of clothing matches an aesthetic. Our algorithm then determines how similar and unique the subject’s outfit is (based on what style the outfit most closely matches) and quantifies this as “Heat.” The user’s “Heat” is then placed on the leaderboard hosted by a small-scale Azure server (this has basic user authentication).


<h2>Duties:</h2>
Adam: Developing algorithm to separate each article of clothing from jpg passed from Andrew's code and pass to Christian as jpg image. Also develop web interface using Azure (if time allows) to host back and frontend. Frontend is a simple GUI that requests webcam permissions and creates leaderboard for all users.<br><br>
Alex: Scraping outfit data off Pinterest so we have data to judge our heat. Digging into the Pinterest API, figuring out how to make it all work.<br><br>
Andrew: Interfacing with webcam to take images and stream a preview, learning Python hehe<br><br>
Christian: Work on image classifier to identify article of clothing and color of clothing and (if time allows) the style of the article of clothing

<br><h2>Run Instructions:</h2>
To run locally (as we are currently for testing), create a virtual environment for python3 (https://python.land/virtual-environments/virtualenv) and install python dependencies. Ensure the npm is installed and up to date.
<br>
<h3>Frontend Setup</h3>
Install Node and npm. Then, use command line to run "npm install -g @angular/cli@latest" followed by "npm install". 
<br>
<h3>Backend Setup</h3>
To activate virtual environment (assuming you created it already), run "source my_project_env/bin/activate" (or "my_project_env\Scripts\activate" on Windows). pip install all dependencies.

<br><br>
To run the backend, navigate to HeatCheck/backend and run python main.py. In another terminal, navigate to HeatCheck/angular-frontend and run ng serve. Open the localhost address that appears.

