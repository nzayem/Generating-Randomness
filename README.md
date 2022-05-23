# Generating-Randomness

Simple introduction to machine learning track (in the JetBrains Academy) within a game context, where the next user input is predicted (0 or 1) based on historical data.

First, the user will enter a number of characters, and the program will filter the 0 and 1 only and build a string of desired length (100 in this case).

<img src="https://github.com/nzayem/Generating-Randomness/blob/master/Initial-data.png" height="200" width="650">

Next, the program will calculate the frequency of 0 and 1 after each pattern (triad in this case). Data is stored in a dictionary:

<img src="https://github.com/nzayem/Generating-Randomness/blob/master/Frequency-Dictionary.png" height="200" width="850">


Finally the program will ask for a user to enter random number and try to predict the next digit after each triad in this number:

<img src="https://github.com/nzayem/Generating-Randomness/blob/master/Prediction.png" height="450" width="1000">
