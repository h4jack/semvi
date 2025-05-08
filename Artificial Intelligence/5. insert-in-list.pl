insert_nth(_, _, [], []).
insert_nth(Item, N, [H|T], [ResH|ResT]) :-
    is_list(H), 
    insert_nth(Item, N, H, ResH),
    insert_nth(Item, N, T, ResT).
insert_nth(Item, N, List, Result) :-
    \+ is_list(List),
    insert_at(Item, N, List, Result).

insert_at(Item, 1, List, [Item|List]).
insert_at(Item, N, [H|T], [H|R]) :-
    N > 1,
    N1 is N - 1,
    insert_at(Item, N1, T, R).
