remove_nth(1, [_|T], T).
remove_nth(N, [H|T], [H|R]) :-
    N > 1,
    N1 is N - 1,
    remove_nth(N1, T, R).
