"""
In soccer leagues, the winner of a match is awarded with 3 points and the
 loser 0 points. In case of a tie, both teams are awarded with 1 point each.

Create a class Soccer containing the method maxPoints which takes a int[] 
wins, the number of wins for each team in the league, and a int[] ties, 
the number of ties for each team in the league and returns an int, 
the maximum points a team in the league has. The i'th elements of wins 
and ties correspond to the number of wins and ties respectively for team i.
"""

class Soccer:
	def maxPoints(self, wins, ties):
		return max([3 * x[0] + x[1] for x in zip(wins, ties)])