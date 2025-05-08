% Base case: reversing an empty list gives an empty list
reverse([], []).

% Recursive case
reverse([H|T], R) :-
    reverse(T, RT),
    append(RT, [H], R).
