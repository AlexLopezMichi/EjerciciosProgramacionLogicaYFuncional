% Reglas del Sistema de Riego

% 1 El sistema considera que la hora es adecuada si es entre las 10 am o despues de las 6 pm
% 2 el riego se activa automaticamente si:
% - La humedad del suelo es baja
% - No se pronostica lluvia
% - Y es una hora adecuada para regar

% 3 Si el riego esta activado, se registra como "Activado"; si no, como "No Activado"

% 4 Alerta por condiciones extremas:
% - Si la temperatura es mayor a 32 grados, se activa una alerta por calor extremo.
% Si el riego se activa bajo estas condiciones, el sistema emite una recomendación:

% "Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo."

% 5 En caso contrario, indica:

% "Sin recomendaciones especiales para el riego."

% --- Zonas del sistema de riego ---
% zona(Nombre, Humedad, Temperatura, Hora, Lluvia).
zona(este, baja, 33, 21, true).
zona(oeste, baja, 30, 17, false).
zona(norte, baja, 35, 19, false).
zona(sur, alta, 33, 8, false).

% --- Reglas generales ---

% Regla: ¿Es una hora adecuada para regar?
hora_adecuada(Hora) :- Hora < 10 ; Hora > 18.

% Regla para alerta de temperatura extrema
alerta_calor(T) :- T >= 32.
alerta_humedad_alta(alta).
alerta_lluvia(true).

% --- Activación del riego ---

% Regla principal: ¿Cuando se debe activar el sistema de riego?
activar_riego(Zona) :-
    zona(Zona, Humedad, _, Hora, Lluvia),
    Humedad = baja,
    Lluvia = false,
    hora_adecuada(Hora).

% --- Estado del riego como valor de texto ---
estado_riego(Zona, 'Activado') :- activar_riego(Zona), !.
estado_riego(_, 'No Activado').

% --- Recomendación con salida en variable ---
recomendacion(Zona, 'No se recomienda riego: lluvia esperada.') :-
    zona(Zona, _, _, _, true), !.

recomendacion(Zona, 'No se recomienda riego: humedad del suelo alta.') :-
    zona(Zona, H, _, _, _),
    alerta_humedad_alta(H), !.

recomendacion(Zona, 'Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo.') :-
    activar_riego(Zona),
    zona(Zona, _, Temp, _, _),
    alerta_calor(Temp), !.

recomendacion(_, 'Sin recomendaciones especiales para el riego.').

% --- Nivel de riesgo ---
nivel_riesgo(Zona, alto) :-
    activar_riego(Zona),
    zona(Zona, _, Temp, _, _),
    alerta_calor(Temp), !.

nivel_riesgo(Zona, medio) :-
    activar_riego(Zona), !.

nivel_riesgo(_, bajo).

% --- Explicación del sistema ---
explicacion(Zona, 'No se activa riego: la humedad no es baja.') :-
    zona(Zona, H, _, _, _),
    H \= baja, !.

explicacion(Zona, 'No se activa riego: se espera lluvia.') :-
    zona(Zona, _, _, _, true), !.

explicacion(Zona, 'No se activa riego: no es una hora adecuada.') :-
    zona(Zona, _, _, Hora, _),
    \+ hora_adecuada(Hora), !.
explicacion(_, 'Se activa el riego: condiciones adecuadas.').

% Consulta si la hora en la zona es adecuada para regar
hora_adecuada_zona(Zona) :-
    zona(Zona, _, _, Hora, _),
    (Hora < 10 ; Hora > 18).

% Consulta si hay probabilidad de lluvia en la zona (true/false)
probabilidad_lluvia(Zona, Lluvia) :-
    zona(Zona, _, _, _, Lluvia).

% Consulta si la humedad del suelo es baja en la zona (true/false)
humedad_baja(Zona, Humedad) :-
    zona(Zona, Humedad, _, _, _),
    Humedad = baja.