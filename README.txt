------FIFA 20 Player Finder------
---------------------------------
Requirements for running this program:
	-Python 3.8
	-pandas package
	-scikit-learn package
	-PySimpleGUI package

This project was made a couple of years back due to FIFA tournaments me and some friends used to hold, where we would
have lineup restrictions regarding what nationality the players could be, what their contracts values could be etc.
By wanting to streamline and ease the process I made this project.

This program is based on a dataset found on: "https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset".
The program utilizes the k-means method of clustering, for clustering players based on the similiraty of their FIFA 20
stats in 7 categories: Overall, Shooting, Passing, Dribbling, Defending, Goalkeeping.

The user inputs the name of the player they are looking to substitute, and the category regarding which they are substituting him,
after which they are presented with a list of names of players, alongside their main information, such as their overall rating,
nationality, contracts etc.