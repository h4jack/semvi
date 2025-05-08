append_list([], L, L).
append_list([H|T], L, [H|R]) :-
    append_list(T, L, R).
