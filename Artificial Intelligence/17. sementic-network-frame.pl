% Semantic network: relations
is_a(robin, bird).
is_a(bird, animal).
has_wings(bird).
can_fly(bird).
color(robin, red).

% Inheritance rule
can_fly(X) :- is_a(X, Y), can_fly(Y).
has_wings(X) :- is_a(X, Y), has_wings(Y).
