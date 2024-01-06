Command line interface to play Lichess using only standard chess notation.

Make sure to create an API key at lichess.org and input it into the code where it says API_KEY_HERE

TODO:<br />
Add functionality to resume games<br />
Not able to start play using black. Program wait's for user to input first move.


Sample game output:

Enter Stockfish difficulty level (1-8): 1<br />
Do you want to play as white or black? white<br />
You are playing as white<br />
Type your move in standard notation (e.g., e4, Nf3), 'show' to display the board, or 'resign' to resign the game.<br />
Your move: e4<br />
Stockfish's move: e5<br />
Your move: c1<br />
Invalid move. Legal moves are:<br />
Legal moves are: Nh3, Nf3, Ne2, Ba6, Bb5, Bc4, Bd3, Be2, Ke2, Qh5, Qg4, Qf3, Qe2, Nc3, Na3, h3, g3, f3, d3, c3, b3, a3, h4, g4, f4, d4, c4, b4, a4<br />
Your move: show<br />
r n b q k b n r<br />
p p p p . p p p<br />
. . . . . . . .<br />
. . . . p . . .<br />
. . . . P . . .<br />
. . . . . . . .<br />
P P P P . P P P<br />
R N B Q K B N R<br />
Your move: resign<br />
You have resigned the game.<br />
Game over<br />
