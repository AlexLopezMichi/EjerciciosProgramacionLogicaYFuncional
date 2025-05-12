% Peliculas: nombre, [genero, calificacion, director(Director)]
pelicula('Godzilla', [accion, media, director('Gareth Edwards')]).
pelicula('Avengers Endgame', [accion, alta, director('Anthony y Joe Russo')]).
pelicula('Interestelar', [ciencia_ficcion, alta, director('Christopher Nolan')]).
pelicula('El Libro de la Vida', [animacion, media, director('Jorge R. Gutierrez')]).

% Descripciones
descripcion('Godzilla', 'Monstruos gigantes enfrentan a la humanidad en una lucha por la supervivencia.').
descripcion('Avengers Endgame', 'Los Vengadores viajan en el tiempo para revertir el chasquido de Thanos.').
descripcion('Interestelar', 'Exploradores viajan por agujeros de gusano para salvar a la humanidad.').
descripcion('El Libro de la Vida', 'Un cuento animado sobre el Dia de los Muertos y el amor eterno.').

% Coincidencias con respuestas del usuario
coincide(Criterio) :- genero(Criterio).
coincide(Criterio) :- calificacion(Criterio).
coincide(director(D)) :- director(D).

% Cuenta coincidencias
puntaje(Pelicula, Puntaje) :-
    pelicula(Pelicula, Caracteristicas),
    contar_coincidencias(Caracteristicas, 0, Puntaje).

contar_coincidencias([], P, P).
contar_coincidencias([C|R], Acc, Puntaje) :-
    ( coincide(C) -> Acc1 is Acc + 1 ; Acc1 is Acc ),
    contar_coincidencias(R, Acc1, Puntaje).

% Encuentra las mejores peliculas
mejores_peliculas([]) :-  % si todas las puntuaciones son 0, devolver lista vacía
    findall(P, pelicula(P,_), Peliculas),
    forall(member(P, Peliculas), puntaje(P, 0)).

mejores_peliculas(ListaPeliculas) :-
    findall((P,Pt), (pelicula(P,_), puntaje(P,Pt)), Lista),
    max_puntaje(Lista, MaxPuntaje),
    MaxPuntaje > 0,
    findall(P, member((P, MaxPuntaje), Lista), ListaPeliculas).


% Encuentra el puntaje mas alto en una lista
max_puntaje([], 0).
max_puntaje([(_,P)|R], Max) :-
    max_puntaje(R, MaxR),
    Max is max(P, MaxR).

% Preguntas al usuario Y almacenar respuestas
preguntar :-
    write('Que genero prefieres? (accion, animacion, ciencia_ficcion): '), read(G),
    asserta(genero(G)),
    write('Que calificacion buscas? (alta, media, baja): '), read(C),
    asserta(calificacion(C)),
    write('Tienes un director favorito? (usa comillas, por ejemplo "Christopher Nolan"): '), read(D),
    asserta(director(D)).

% Inicio del sistema
iniciar :-
    % Limpiar la base de datos
    retractall(genero(_)), 
    retractall(calificacion(_)),
    retractall(director(_)),
    preguntar,
    mejores_peliculas(Peliculas),
    (   Peliculas \= []
    ->  nl, write('Recomendaciones:'), nl,
        mostrar_peliculas(Peliculas)
    ;   nl, write('No se encontro una pelicula que coincida con tus preferencias.'), nl
    ).

% Mostrar informacion
mostrar_info([]).
mostrar_info([director(D)|R]) :-
    write('Director: '), write(D), nl,
    mostrar_info(R).
mostrar_info([alta|R]) :-
    write('Calificacion: alta'), nl,
    mostrar_info(R).
mostrar_info([media|R]) :-
    write('Calificacion: media'), nl,
    mostrar_info(R).
mostrar_info([baja|R]) :-
    write('Calificacion: baja'), nl,
    mostrar_info(R).
mostrar_info([accion|R]) :-
    write('Genero: accion'), nl,
    mostrar_info(R).
mostrar_info([animacion|R]) :-
    write('Genero: animacion'), nl,
    mostrar_info(R).
mostrar_info([ciencia_ficcion|R]) :-
    write('Genero: ciencia ficcion'), nl,
    mostrar_info(R).

mostrar_peliculas([]).
mostrar_peliculas([P|R]) :-
    pelicula(P, Caracteristicas),
    descripcion(P, Desc),
    nl, write('Pelicula: '), write(P), nl,
    mostrar_info(Caracteristicas),
    write('Sinopsis: '), write(Desc), nl,
    mostrar_peliculas(R).
