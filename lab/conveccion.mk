plots.pdf : plots.py datos.txt
	python plots.py
datos.txt : a.out 
	./a.out > datos.txt
a.out : conveccion.c
	gcc conveccion.c -lm

