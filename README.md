# BIC01: Primer Taller

Implemente un programa para investigar el crecimiento poblacional. El programa
debe realizar lo siguiente:

1. Solicitar al usuario el ingreso de la población actual, en miles de millones.
2. Solicite al usuario el ingreso de la tasa de crecimiento anual, el porcentaje.
3. Muestre en pantalla la población por los siguientes 100 años. La información mostrada 
   debe incluir el año, la población al final de dicho año, y el incremento poblacional.
   Los numeros mostrados en pantalla deben redondearse a dos decimales.
4. Muestre en pantalla dentro de cuantos años se duplicará la población actual (ingresada por el
   usuario en el paso 1).
5. Muestre en pantalla dentro de cuantos años se cuadruplicará la población actual (ingresada por el
   usuario en el paso 1).

Asuma que la tasa de crecimiento anual, ingresada por el usuario en el paso 2, se mantiene constante
a traves del tiempo.

La implementación debe realizarse en el archivo `poblacion.py`, entre las líneas marcadas como `#INICIO` y `#FIN`. 
No remueva o modifique el código base.

Los mensajes en consola deben tener el siguiente formato:

```
Ingrese poblacion actual (en miles de millones): 7.9
Ingrese tasa de crecimiento (en porcentaje): 1.05
CRECIMIENTO POBLACIONAL ANUAL
1) Poblacion: 7.98 Incremento: 0.08
2) Poblacion: 8.07 Incremento: 0.08
3) Poblacion: 8.15 Incremento: 0.08
4) Poblacion: 8.24 Incremento: 0.09
5) Poblacion: 8.32 Incremento: 0.09
6) Poblacion: 8.41 Incremento: 0.09
7) Poblacion: 8.5 Incremento: 0.09
8) Poblacion: 8.59 Incremento: 0.09
9) Poblacion: 8.68 Incremento: 0.09
10) Poblacion: 8.77 Incremento: 0.09
11) Poblacion: 8.86 Incremento: 0.09
12) Poblacion: 8.95 Incremento: 0.09
13) Poblacion: 9.05 Incremento: 0.09
14) Poblacion: 9.14 Incremento: 0.1
15) Poblacion: 9.24 Incremento: 0.1
16) Poblacion: 9.34 Incremento: 0.1
17) Poblacion: 9.44 Incremento: 0.1
18) Poblacion: 9.53 Incremento: 0.1
19) Poblacion: 9.63 Incremento: 0.1
20) Poblacion: 9.74 Incremento: 0.1
21) Poblacion: 9.84 Incremento: 0.1
22) Poblacion: 9.94 Incremento: 0.1
23) Poblacion: 10.05 Incremento: 0.1
24) Poblacion: 10.15 Incremento: 0.11
25) Poblacion: 10.26 Incremento: 0.11
26) Poblacion: 10.37 Incremento: 0.11
27) Poblacion: 10.47 Incremento: 0.11
28) Poblacion: 10.58 Incremento: 0.11
29) Poblacion: 10.69 Incremento: 0.11
30) Poblacion: 10.81 Incremento: 0.11
31) Poblacion: 10.92 Incremento: 0.11
32) Poblacion: 11.04 Incremento: 0.11
33) Poblacion: 11.15 Incremento: 0.12
34) Poblacion: 11.27 Incremento: 0.12
35) Poblacion: 11.39 Incremento: 0.12
36) Poblacion: 11.51 Incremento: 0.12
37) Poblacion: 11.63 Incremento: 0.12
38) Poblacion: 11.75 Incremento: 0.12
39) Poblacion: 11.87 Incremento: 0.12
40) Poblacion: 12.0 Incremento: 0.12
41) Poblacion: 12.12 Incremento: 0.13
42) Poblacion: 12.25 Incremento: 0.13
43) Poblacion: 12.38 Incremento: 0.13
44) Poblacion: 12.51 Incremento: 0.13
45) Poblacion: 12.64 Incremento: 0.13
46) Poblacion: 12.77 Incremento: 0.13
47) Poblacion: 12.91 Incremento: 0.13
48) Poblacion: 13.04 Incremento: 0.14
49) Poblacion: 13.18 Incremento: 0.14
50) Poblacion: 13.32 Incremento: 0.14
51) Poblacion: 13.46 Incremento: 0.14
52) Poblacion: 13.6 Incremento: 0.14
53) Poblacion: 13.74 Incremento: 0.14
54) Poblacion: 13.89 Incremento: 0.14
55) Poblacion: 14.03 Incremento: 0.15
56) Poblacion: 14.18 Incremento: 0.15
57) Poblacion: 14.33 Incremento: 0.15
58) Poblacion: 14.48 Incremento: 0.15
59) Poblacion: 14.63 Incremento: 0.15
60) Poblacion: 14.78 Incremento: 0.15
61) Poblacion: 14.94 Incremento: 0.16
62) Poblacion: 15.1 Incremento: 0.16
63) Poblacion: 15.26 Incremento: 0.16
64) Poblacion: 15.42 Incremento: 0.16
65) Poblacion: 15.58 Incremento: 0.16
66) Poblacion: 15.74 Incremento: 0.16
67) Poblacion: 15.91 Incremento: 0.17
68) Poblacion: 16.07 Incremento: 0.17
69) Poblacion: 16.24 Incremento: 0.17
70) Poblacion: 16.41 Incremento: 0.17
71) Poblacion: 16.58 Incremento: 0.17
72) Poblacion: 16.76 Incremento: 0.17
73) Poblacion: 16.93 Incremento: 0.18
74) Poblacion: 17.11 Incremento: 0.18
75) Poblacion: 17.29 Incremento: 0.18
76) Poblacion: 17.47 Incremento: 0.18
77) Poblacion: 17.66 Incremento: 0.18
78) Poblacion: 17.84 Incremento: 0.19
79) Poblacion: 18.03 Incremento: 0.19
80) Poblacion: 18.22 Incremento: 0.19
81) Poblacion: 18.41 Incremento: 0.19
82) Poblacion: 18.6 Incremento: 0.19
83) Poblacion: 18.8 Incremento: 0.2
84) Poblacion: 19.0 Incremento: 0.2
85) Poblacion: 19.2 Incremento: 0.2
86) Poblacion: 19.4 Incremento: 0.2
87) Poblacion: 19.6 Incremento: 0.2
88) Poblacion: 19.81 Incremento: 0.21
89) Poblacion: 20.02 Incremento: 0.21
90) Poblacion: 20.23 Incremento: 0.21
91) Poblacion: 20.44 Incremento: 0.21
92) Poblacion: 20.65 Incremento: 0.21
93) Poblacion: 20.87 Incremento: 0.22
94) Poblacion: 21.09 Incremento: 0.22
95) Poblacion: 21.31 Incremento: 0.22
96) Poblacion: 21.53 Incremento: 0.22
97) Poblacion: 21.76 Incremento: 0.23
98) Poblacion: 21.99 Incremento: 0.23
99) Poblacion: 22.22 Incremento: 0.23
100) Poblacion: 22.45 Incremento: 0.23
Poblacion duplicada en: 67
Poblacion cuadruplicada en: 133
```