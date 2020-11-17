# Dim rnrs As Short = 0 'number of runners in race
#     Dim winp() As Single  'implied win probability based on price and overround
#     Dim posp(0, 0) As Single 'derived probability of horse finishing in a specific position
#     Dim plcp() As Single  'derived place probability based on place terms and probability of finishing in a placed position
#     Dim podd() As Single  'derived place odds based on place probability
#     Dim ornd As Single 'overround

# Function Harville(ByVal WinOdds() As Single)

#         'Purpose:       Creates perms of up to 4 horses and calculates probability of each of these perms occurring and, 
#         '               iteratively, the probability of a given horse appearing in that perm.  Probability of a horse being 
#         '               placed is then derived by selecting the perm for the specified number of places

#         rnrs = UBound(WinOdds)
#         ornd = 0

#         ReDim winp(rnrs)

#         For i = 0 To rnrs
#             winp(i) = 1 / WinOdds(i)                                'Derive implied win prob for this horse
#             ornd += winp(i)                                         'Add to overround
#         Next

#         For i = 0 To rnrs
#             winp(i) = winp(i) / ornd                                'Recalculate win prob, taking into account overround
#         Next

#         'Enter place terms
#         Dim plce As Short = 0
#         plce = placeTerms

#         Do While plce > rnrs Or plce > 4 Or plce <= 0
#             If plce > rnrs Then
#                 MsgBox("Number of places > Number of runners", MsgBoxStyle.Exclamation, "Error")
#             ElseIf plce <= 0 Then
#                 MsgBox("Not enough places", MsgBoxStyle.Exclamation, "Error")
#             ElseIf plce <= rnrs And plce > 4 Then
#                 MsgBox("Can only calculate up to 4 places", MsgBoxStyle.Exclamation, "Error")
#             End If
#         Loop

#         ReDim posp(rnrs, rnrs), plcp(rnrs)

#         Dim r1, r2, r3, r4 As Short

#         For j = 0 To rnrs

#             If plce = 1 Then
#                 plcp(j) = winp(j)
#             End If

#             'Up to 2 places
#             If plce = 2 Then
#                 For r1 = 0 To rnrs
#                     For r2 = 0 To rnrs
#                         If r1 <> r2 Then '(r1,r2) is a perm of 2 from n horses
#                             If r1 = j Or r2 = j Then
#                                 plcp(j) = plcp(j) + (winp(r1) * winp(r2)) / (1 - winp(r1))
#                             End If
#                         End If
#                     Next
#                 Next
#             End If

#             'Up to 3 places
#             If plce = 3 Then
#                 For r1 = 0 To rnrs
#                     For r2 = 0 To rnrs
#                         For r3 = 0 To rnrs
#                             If r1 <> r2 And r1 <> r3 And r2 <> r3 Then '(r1,r2,r3) is a perm of 3 from n horses
#                                 If r1 = j Or r2 = j Or r3 = j Then
#                                     plcp(j) = plcp(j) + (winp(r1) * winp(r2) * winp(r3)) / ((1 - winp(r1)) * (1 - winp(r1) - winp(r2)))
#                                 End If
#                             End If
#                         Next
#                     Next
#                 Next
#             End If

#             'Up to 4 places
#             If plce = 4 Then
#                 For r1 = 0 To rnrs
#                     For r2 = 0 To rnrs
#                         For r3 = 0 To rnrs
#                             For r4 = 0 To rnrs
#                                 If r1 <> r2 And r1 <> r3 And r1 <> r4 And r2 <> r3 And r2 <> r4 And r3 <> r4 Then '(r1,r2,r3,r4) is a perm of 4 from n horses
#                                     If r1 = j Or r2 = j Or r3 = j Or r4 = j Then
#                                         plcp(j) = plcp(j) + (winp(r1) * winp(r2) * winp(r3) * winp(r4)) / ((1 - winp(r1)) * (1 - winp(r1) - winp(r2)) * (1 - winp(r1) - winp(r2) - winp(r3)))
#                                     End If
#                                 End If
#                             Next
#                         Next
#                     Next
#                 Next
#             End If

#         Next

#         ReDim podd(rnrs)

#         For i = 0 To rnrs
#             podd(i) = 1 / plcp(i)
#         Next

#         Return podd

#     End Function

#     Function HarvilleDiscounted(ByVal WinOdds() As Single)

#         'Purpose:       Creates perms of up to 4 horses and calculates probability of each of these perms occurring and, 
#         '               iteratively, the probability of a given horse appearing in that perm.  Probability of a horse being 
#         '               placed is then derived by selecting the perm for the specified number of places.  As opposed to the version
#         '               above, this version also discounts the place probability according to the Lo/Bacon-Shone approximation of
#         '               the Henery adaptation of the original Harville formula

#         rnrs = UBound(WinOdds)
#         ornd = 0

#         ReDim winp(rnrs)

#         For i = 0 To rnrs
#             winp(i) = 1 / WinOdds(i)                                'Derive implied win prob for this horse
#             ornd += winp(i)                                         'Add to overround
#         Next

#         For i = 0 To rnrs
#             winp(i) = winp(i) / ornd                                'Recalculate win prob, taking into account overround
#         Next

#         'Enter place terms
#         Dim plce As Short = 0
#         plce = placeTerms

#         Do While plce > rnrs Or plce > 4 Or plce <= 0
#             If plce > rnrs Then
#                 MsgBox("Number of places > Number of runners", MsgBoxStyle.Exclamation, "Error")
#             ElseIf plce <= 0 Then
#                 MsgBox("Not enough places", MsgBoxStyle.Exclamation, "Error")
#             ElseIf plce <= rnrs And plce > 4 Then
#                 MsgBox("Can only calculate up to 4 places", MsgBoxStyle.Exclamation, "Error")
#             End If
#         Loop

#         ReDim posp(rnrs, rnrs), plcp(rnrs)

#         Dim r1, r2, r3, r4, rz As Short
#         Dim lambda As Decimal = 0.76
#         Dim lambdadenom As Decimal
#         Dim rho As Decimal = 0.62
#         Dim rhodenom As Decimal
#         Dim tau As Decimal = 1  'Need to find a suitable approximation for tau.  None given in the literature
#         Dim taudenom As Decimal

#         For j = 0 To rnrs

#             If plce = 1 Then
#                 plcp(j) = winp(j)
#             End If

#             'Formulas for discounted Harville are:

#             '2 places
#             '(winp(r1) * (winp(r2) ^ lambda))/ Sum(winp(r2) ^ lambda ...... winp(rn) ^ lambda)

#             '3 places
#             '(winp(r1) * ((winp(r2) ^ lambda))/ Sum(winp(r2) ^ lambda ...... winp(rn) ^ lambda) *
#             '((winp(r3) ^ rho)/ sum(winp(r3) ^ rho ...... winp(rn) ^ rho)

#             '4 places
#             '(winp(r1) * ((winp(r2) ^ lambda))/ Sum(winp(r2) ^ lambda ...... winp(rn) ^ lambda) *
#             '((winp(r3) ^ rho)/ sum(winp(r3) ^ rho ...... winp(rn) ^ rho) *
#             '((winp(r4) ^ tau)/sum(winp(r4) ^ rho ...... winp(rn) ^ tau)

#             'Up to 2 places
#             If plce = 2 Then
#                 For r1 = 0 To rnrs
#                     For r2 = 0 To rnrs
#                         If r1 <> r2 Then '(r1,r2) is a perm of 2 from n horses
#                             If r1 = j Or r2 = j Then
#                                 lambdadenom = 0 'Reset denominator
#                                 For rz = 0 To rnrs
#                                     If rz <> r1 Then 'For all other runners apart from the first one
#                                         lambdadenom += Math.Pow(winp(rz), lambda)
#                                     End If
#                                 Next
#                                 plcp(j) = plcp(j) + (winp(r1) * Math.Pow(winp(r2), lambda)) / lambdadenom
#                             End If
#                         End If
#                     Next
#                 Next
#             End If

#             'Up to 3 places
#             If plce = 3 Then
#                 For r1 = 0 To rnrs
#                     For r2 = 0 To rnrs
#                         For r3 = 0 To rnrs
#                             If r1 <> r2 And r1 <> r3 And r2 <> r3 Then '(r1,r2,r3) is a perm of 3 from n horses
#                                 If r1 = j Or r2 = j Or r3 = j Then
#                                     'Reset denominators
#                                     lambdadenom = 0
#                                     rhodenom = 0
#                                     For rz = 0 To rnrs
#                                         If rz <> r1 Then 'For all other runners apart from the winner
#                                             lambdadenom += Math.Pow(winp(rz), lambda) 'Add to lambda denominator
#                                         End If
#                                         If rz <> r1 And rz <> r2 Then 'For all other runners apart from the first two
#                                             rhodenom += Math.Pow(winp(rz), rho) 'Add to rho denominator
#                                         End If
#                                     Next
#                                     plcp(j) = plcp(j) + winp(r1) * Math.Pow(winp(r2), lambda) / lambdadenom * Math.Pow(winp(r3), rho) / rhodenom
#                                 End If
#                             End If
#                         Next
#                     Next
#                 Next
#             End If

#             'Up to 4 places
#             If plce = 4 Then
#                 For r1 = 0 To rnrs
#                     For r2 = 0 To rnrs
#                         For r3 = 0 To rnrs
#                             For r4 = 0 To rnrs
#                                 If r1 <> r2 And r1 <> r3 And r1 <> r4 And r2 <> r3 And r2 <> r4 And r3 <> r4 Then '(r1,r2,r3,r4) is a perm of 4 from n horses
#                                     If r1 = j Or r2 = j Or r3 = j Or r4 = j Then
#                                         'Reset denominators
#                                         lambdadenom = 0
#                                         rhodenom = 0
#                                         taudenom = 0
#                                         For rz = 0 To rnrs
#                                             If rz <> r1 Then 'For all other runners apart from the winner
#                                                 lambdadenom += Math.Pow(winp(rz), lambda) 'Add to lambda denominator
#                                             End If
#                                             If rz <> r1 And rz <> r2 Then 'For all other runners apart from the first two
#                                                 rhodenom += Math.Pow(winp(rz), rho) 'Add to rho denominator
#                                             End If
#                                             If rz <> r1 And rz <> r2 And rz <> r3 Then 'For all other runners apart from the first three
#                                                 taudenom += Math.Pow(winp(rz), tau)
#                                             End If
#                                         Next
#                                         plcp(j) = plcp(j) + winp(r1) * Math.Pow(winp(r2), lambda) / lambdadenom * Math.Pow(winp(r3), rho) / rhodenom * Math.Pow(winp(r4), tau)
#                                     End If
#                                 End If
#                             Next
#                         Next
#                     Next
#                 Next
#             End If

#         Next

#         ReDim podd(rnrs)

#         For i = 0 To rnrs
#             podd(i) = 1 / plcp(i)
#         Next

#         Return podd

#     End Function

    

# End Module