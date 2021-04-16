import pafy
from prettytable import PrettyTable
import colorama
import sys
import os

try:
	os.mkdir('YoutubeDownloader')
except:
	pass

fuente = colorama.Fore
estilo = colorama.Style

azul = fuente.BLUE
rojo = fuente.RED
verde = fuente.GREEN
amarillo = fuente.YELLOW
celeste = fuente.CYAN
morado = fuente.MAGENTA
reset = estilo.RESET_ALL

celesteNegrita = "\x1b[1;36m"

print(verde, "**************************************************")
print(verde, "*", " YOUTUBE DOWNLOADER".center(46), "*")
print(verde, "**************************************" + celesteNegrita +" @MiguelRG " + reset + verde + "*")

respuesta = "si"
while respuesta == "si":
	url = input(verde + " URL: " + celeste)
	video = pafy.new(url)
	titulo = video.title
	visualisaciones = video.viewcount
	autor = video.author
	categoria = video.category
	duracion = video.duration
	meGusta = video.likes
	noMeGusta = video.dislikes

	print("")
	print(verde, "------------- Informacion del 	archivo ------------")
	print(verde, "Título:", celeste, titulo)
	print(verde, "Autor:", celeste, autor)
	print(verde, "Categoria:", celeste, 			categoria)
	print(verde, "Visualisaciones:", celeste,  visualisaciones)
	print(verde, "Duracion:", celeste, duracion)
	print(verde, "Me gusta:", celeste, meGusta, verde, "No me gusta:", celeste, noMeGusta)
	print(verde, "--------------------------------------------------")
	print("")

	tabla = PrettyTable()
	formatos = video.allstreams
	print(" ------ Formatos disponibles para descargar -------\n")

	a = azul
	b = amarillo
	c = rojo
	d = celeste
	e = morado

	tabla.field_names = [c+"Opcion"+a, c+"Tipo"+a, c+"Extensión"+a, c+"Calidad"+a, c+"Tamaño"+a]
	n = 0
	for f in formatos:
		tamaño = f"{e} {f.get_filesize()/(10**6):.2f} {b} MB {a}"
		formato = [b+str(n)+a, d+f.mediatype+a, d+f.extension+a, e+f.quality+a, tamaño]
		n += 1
		tabla.add_row(formato)
	print(a)
	print(tabla)
	
	print("")
	print(verde, "Seleccione una opcion para descargar: \n")
	opcion = int(input(verde + " __/¬> " + celeste))
	extension = formatos[opcion].extension
	nombreArchivo = f"{sys.path[0]}/{video.title}.{extension}"
	print(verde, f"Guardando el archivo '{titulo}.{extension}' en {sys.path[0]}/YoutubeDownloader ...\n", amarillo)
	formatos[opcion].download(filepath=f"{sys.path[0]}/YoutubeDownloader")
	print("")
	print(verde, f"'{titulo}.{extension}' a sido descargado correctamente", reset)
	print(rojo, "Desea seguir descargando? si/no :")
	respuesta = input(verde + " __/¬> " + celeste).lower()
	
else:
	print(verde, "Hasta pronto! ", reset)