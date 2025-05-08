% Base case: empty list has even length
evenlength([]).
evenlength([_|T]) :- oddlength(T).

% One-element list has odd length
oddlength([_]).
oddlength([_|T]) :- evenlength(T).
