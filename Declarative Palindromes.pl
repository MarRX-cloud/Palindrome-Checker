reverse([], []). % reverse(A, B) relates the list A with its reversal B
reverse([Element|Tail], Reversed) :-
  reverse(Tail, ReversedTail),
  append(ReversedTail, [Element], Reversed). % Adds the head to the reversed tail

palindrome(List) :- reverse(List, List). % A list is considered a palindrome if it equals its reversal

/** <examples>
?- palindrome([n,o,o,n]). output = true
?- palindrome([r,a,c,e,c,a,r]). output = true
?- palindrome([f,a,c,e]). output = false
*/
