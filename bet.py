class Bet:

    @staticmethod
    def kelly(prob, odds, bank):
        
        """ Calculate the recommended Kelly criterion bet 
        for any given win probability, decimal win odds and size of bank"""

        p = prob  # Win probability
        q = 1 - p  # Loss probability
        o = odds - 1 # Converts 'odds' from decimal into odds to 1
        
        fraction_to_bet = ((o * p) - q) / o # Kelly formula, aka "edge over odds"  
        kelly = bank * fraction_to_bet     

        return kelly if kelly > 0 else 0
                
#     Shared Function Odds(ByVal Probability As Single) As Single

#         'Purpose:       Converts the probability of an occurrence into decimal
#         '               win odds for that occurrence

#         Dim o, p As Single

#         'o is decimal odds
#         'p is probability in the range 0 < p < 1

#         p = Probability

#         o = 1 / p

#         Odds = o

#     End Function

#     Shared Function Prob(ByVal Odds As Single) As Single

#         'Purpose:       Converts decimal win odds for an occurrence into the
#         '               equivalent probability of that occurrence happening

#         Dim o, p As Single

#         'o is decimal odds
#         'p is probability in the range 0 < p < 1

#         o = Odds

#         p = 1 / o

#         Prob = p

#     End Function

#     Shared Function DecOdds(ByVal Numerator As Short, ByVal Denominator As Short) As Single

#         'Purpose:       Converts traditional odds of the form 9/4 or 100/30 into
#         '               decimal odds of the form 3.25 or 4.33 (to 2 dec. places)

#         Dim o As Single
#         Dim n, d As Short

#         'o is decimal odds
#         'n is the numerator of the traditional odds, e.g. 9 in 9/4
#         'd is the denominator of the traditional odds, e.g. 4 in 9/4

#         n = Numerator
#         d = Denominator

#         o = n / d + 1           'Calculates odds in decimal form

#         DecOdds = o

#     End Function

#     Shared Function TradOdds(ByVal DecOdds As Single) As String

#         'Purpose:       Converts decimal odds of the form 3.25 or 4.33 into their
#         '               traditional equivalent of the form 9/4 or 100/30
#         'Note:          The traditional odds are output as a string, not an integer

#         Dim i, j, k As Short            'Count variables
#         Dim o As Decimal                'Odds to 1 as a decimal
#         Dim n As Short                  'Numerator of traditional odds, e.g. 9 in 9/4
#         Dim d As Short                  'Denominator of the traditional odds, e.g. 4 in 9/4
#         Dim t As String                 'Traditional odds as a string, e.g. 9/4

#         Dim testn, testd As Decimal     'Numerator and denominator used during testing
#         Dim diff As Decimal = 1000      'Difference between decimal odds and traditional odds expressed as a ratio

#         Dim a, b As Short               'Working variables
#         Dim x, y, z As Decimal          'Working variables

#         Dim valid As Boolean = False    'Used for validity test to see if odds generated are acceptable as traditional odds

#         o = DecOdds - 1                 'Converts regular decimal odds into decimal odds to 1

        
#         'This procedure tests the numbers 1 to 100 as prospective denominators for our traditional odds.  
#         'Firstly it generates the corresponding numerator.  Both figures are then validated to see if they create an actual SP.
#         'If they do then the ratio of numerator to denominator is calculated and compared with the decimal odds. 
#         'This is done iteratively until we find the closest approximation to the decimal odds.
#         '2/8/11 - Long odds on (shorter than 1/100) added.  Old-fashioned odds (x/8, 85/x, 100/6,7,8) removed.

#         For i = 1 To 1000

#             If i < 100 Or i Mod 10 = 0 Then                 'Cuts out some stages to speed process up

#                 For j = 1 To 1000

#                     If i < 100 Or i Mod 10 = 0 Then         'Cuts out some stages to speed process up

#                         x = i                               'Try i as numerator
#                         y = j                               'Try j as denominator
#                         z = Abs(x / y - o)

#                         'Check to see whether these traditional odds are valid as SPs.  
#                         'If they are acceptable then set "valid" to true
#                         'If they are not acceptable then "valid" will remain false and a new denominator will be tested

#                         valid = False               'Make assumption that odds are unacceptable

#                         If o < 1 Then               'This case tests for odds on
#                             a = x
#                             b = y
#                         Else                        'This case tests for odds against
#                             a = y
#                             b = x
#                         End If
#                         If a = 1 And (b <= 12 Or b = 14 Or b = 16 Or b = 18 Or b = 20 Or b = 22 Or b = 25 Or b = 28 Or b = 33 Or b = 40 Or b = 50 Or b = 66 Or b = 80 Or b = 100 Or b = 150 Or b = 200 Or b = 250 Or b = 300 Or b = 400 Or b = 500 Or b = 750 Or b = 1000) Then
#                             'The traditional selection of odds to 1 are acceptable....
#                             valid = True
#                         End If
#                         If a = 2 And b <= 15 Then   'Any odds to 2, less than 15/2 are acceptable....
#                             valid = True
#                         End If
#                         If a = 3 And b = 10 Then    'etc.....
#                             valid = True
#                         End If
#                         If a = 4 And b <= 11 Then
#                             valid = True
#                         End If
#                         If a = 5 And b <= 12 Then
#                             valid = True
#                         End If
#                         'If a = 6 And b = 100 Then
#                         'valid = True
#                         'End If
#                         'If a = 7 And b = 100 Then
#                         'valid = True
#                         'End If
#                         If a = 8 And (b = 11 Or b = 13 Or b = 15) Then  'Or b = 100 Then
#                             valid = True
#                         End If
#                         If a = 10 And (b = 11 Or b = 21) Then
#                             valid = True
#                         End If
#                         'If a = 15 And b = 100 Then
#                         'valid = True
#                         'End If
#                         If a = 20 And b = 21 Then 'Or b = 85
#                             valid = True
#                         End If
#                         'If (a = 30 Or a = 85) And b = 100 Then
#                         'valid = True
#                         'End If
#                         'If a = 40 And b = 85 Then
#                         'valid = True
#                         'End If

#                         If valid = True Then            'If the odds are a valid SP then,

#                             If z < diff Then            'If the difference is less than the one currently stored (it always is on the first iteration) then
#                                 diff = z                'make this the new benchmark and set the selected numerator and denominator to those just tested.  
#                                 testn = x               'They will only be changed if a subsequent iteration can produce traditional odds which get closer
#                                 testd = y               'to the decimal odds
#                             End If

#                         End If

#                     End If

#                 Next

#             End If

#         Next

#         n = testn                           'Set final numerator to that selected during testing
#         d = testd                           'Set final denominator to that selected during testing

#         t = n & "/" & d                     'Compiles odds into a string

#         'Common conversions
#         If t = "10/3" Then t = "100/30"
#         If t = "3/10" Then t = "30/100"
#         If t = "3/2" Then t = "6/4"
#         If t = "2/3" Then t = "4/6"

#         TradOdds = t

#     End Function

# End Class