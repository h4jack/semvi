remove_nth_level(_, [], []).
remove_nth_level(N, [H|T], [RH|RT]) :-
    is_list(H),
    remove_nth_level(N, H, RH),
    remove_nth_level(N, T, RT).
remove_nth_level(N, List, Result) :-
    \+ is_list(List),
    remove_every_nth(N, List, Result).

remove_every_nth(N, List, Result) :-
    remove_every_nth(N, List, 1, Result).

remove_every_nth(_, [], _, []).
remove_every_nth(N, [_|T], N, R) :-
    remove_every_nth(N, T, 1, R).
remove_every_nth(N, [H|T], C, [H|R]) :-
    C \= N,
    C1 is C + 1,
    remove_every_nth(N, T, C1, R).
