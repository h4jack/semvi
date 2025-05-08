% Base case
maxlist_cut([X], X) :- !.

% Recursive with cut
maxlist_cut([H|T], Max) :-
    maxlist_cut(T, TempMax),
    (H >= TempMax -> Max = H ; Max = TempMax), !.
