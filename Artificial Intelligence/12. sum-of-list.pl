% Base case: sum of empty list is 0
sumlist([], 0).

% Recursive case
sumlist([H|T], Sum) :-
    sumlist(T, Rest),
    Sum is H + Rest.
