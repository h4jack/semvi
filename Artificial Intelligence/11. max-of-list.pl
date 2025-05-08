% Base case: max of single-element list is that element
maxlist([X], X).

% Recursive case: compare head with max of tail
maxlist([H|T], Max) :-
    maxlist(T, MaxTail),
    (H >= MaxTail -> Max = H ; Max = MaxTail).
