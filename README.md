# CodingDojo_Django_GreatNumberGame
Create a game that stores a random number in sessions and allows the user to attempt to guess the number generated. 

1. Have the main route check sessions to see if random number is already being stored.  If not, generate random number between 1 - 100 and store in session. 
2. Create a POST method to check the integer submitted in the form.  
3. If the integer from form is greater than random number stored in session, have the message display "Too High!"
4. If the integer from form is less than random number stored in session, have the message display "Too Low!"
5. If the integer from is equals the random number stored in session, have the message display "You win!" and display a button to play again. 
6. Create the route "/reset" clear session.  The button displayed after game is one linked to the route.  
7. Create a static file that changes the color of the message depending on if the guess is incorrect (red) or if the guess is correct (green).  

