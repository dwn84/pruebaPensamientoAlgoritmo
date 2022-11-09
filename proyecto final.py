import pygame
import sys
import numpy as np
from numpy.random import default_rng

class Hospital():
# Método constructor de la clase
  def __init__(self, nombre):
    self.nombre = nombre
    self.posicion_x = 0
    self.posicion_y = 0
    self.especializacion = "Pediatria"
  def mostrar_nombre_gerente(self):
      print("XYZ")
  def conocer_posicion(self):
    print("cfgsdfgd del", self.nombre, ":\n x:",
    self.posicion_x, "\n y:", self.posicion_y)

class Emergencia():
  def __init__(self):
    self.posicion_x = round(30*np.random.rand())
    self.posicion_y = round(30*np.random.rand())
  def calcular_distancia(self, coordenada_x, coordenada_y):
    distancia = round(((self.posicion_x - coordenada_x) ** 2 + (self.posicion_y - coordenada_y)**2)**(1/2), 1)
    return distancia



def conocer_posicion(self):
  print("------------------------------------------------------------------------")
  print("CCCCCC de la llamada de emergencia:\n x:",
  self.posicion_x, "\n y:", self.posicion_y)

def crearHospitales(numero_hospitales = 5):
  rng = default_rng()
  X = rng.choice(30, size = numero_hospitales)
  Y = rng.choice(30, size = numero_hospitales)
  Hospitales = []
  for i in range(numero_hospitales):
    indice = str(i+1)
    nuevo_Hospital = Hospital("Hospital "+indice)
    mi_super_hospital = Hospital("Sagrado Corazon")
    nuevo_Hospital.posicion_x = X[i] + 1
    nuevo_Hospital.posicion_y = Y[i] + 1
    nuevo_Hospital.conocer_posicion()
    Hospitales.append(nuevo_Hospital)
  return Hospitales

def crearEmergencia():
  emergencia = Emergencia()
  emergencia.conocer_posicion()
  return emergencia

cantidad_hospitales = 5

pygame.init()

# Definimos el tamaño de la pantalla y el margen
margen = 10 # Margen en pixeles
width = 600 # Ancho de la pantalla en pixeles
height = 600 # Largo de la pantalla en pixeles
surface = pygame.display.set_mode((width, height)) # Creamos una superficie enpantalla para graficar

pygame.display.set_caption('Llamada de Emergencia') #Indicamos un título a la ventana
# Asignamos un ícono para la ventana
icon = pygame.image.load("icono.png")
pygame.display.set_icon(icon)
# Cargamos un sonido de fondo
pygame.mixer.music.load("Cosmonkey - Hold Me.mp3", "mp3")
# Iniciamos un sonido de fondo
pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0)
# Definimos los colores con códigos RGB
red = pygame.Color(255, 0, 0) # 0 - 255
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
# Creamos una variable para controlar las imágenes
gen_hospitales = False
graf_hospitales = False
gen_emergencia = False
graf_emergencia = False

print("------------------------------------------------------------------------")
print("Tamaño de pantalla: ", width, "x", height, "px")
print("El área ocuparda por cada hospital y llamada de emergencia es de(20x20)px")
# Le decimos al usuario por consola la tecla que debe presionar para continuar
print("------------------------------------------------------------------------")
print("Presiona -barra espaciadora- para crear los hospitales aleatoriamente")
print("------------------------------------------------------------------------")
print("Presiona la tecla -e- para crear una llamada de emergencia y calcular la distancia al hospital más cercano")
print("------------------------------------------------------------------------")
print("Para reiniciar las ubicaciones y los cálculos de distancia, presione las teclas nuevamente")

while True:
  surface.fill(black)
  # Creamos un marco
  pygame.draw.line(surface, blue, (0, 0), (width, 0), 3)
  pygame.draw.line(surface, blue, (width, 0), (width, height), 3)
  pygame.draw.line(surface, blue, (width, height), (0, height), 3)
  pygame.draw.line(surface, blue, (0, height), (0, 0), 3)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        gen_hospitales = True
      if event.key == pygame.K_e:
        gen_emergencia = True
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_SPACE:
        graf_hospitales = True
      if event.key == pygame.K_e:
        graf_emergencia = True

  if gen_hospitales:
    Hospitales = crearHospitales(
    numero_hospitales=cantidad_hospitales)
    gen_hospitales = False
  
  if graf_hospitales:
    for i in range(cantidad_hospitales):
      hospital = Hospitales[i]
      pos_x = (hospital.posicion_x - 1)*((width)/30) + margen
      pos_y = (hospital.posicion_y - 1)*((height)/30) + margen
      pygame.draw.circle(surface, green, (pos_x, pos_y), 10)
  if gen_emergencia:
    distancias = []
    llamada_emergencia = crearEmergencia()
    for i in range(len(Hospitales)):
      hospital = Hospitales[i]
      posh_x = hospital.posicion_x
      posh_y = hospital.posicion_y
      if posh_x == llamada_emergencia.posicion_x and posh_y == llamada_emergencia.posicion_y:
        break
      distancia = llamada_emergencia.calcular_distancia(posh_x, posh_y)
      distancias.append(distancia)
    if posh_x == llamada_emergencia.posicion_x and posh_y == llamada_emergencia.posicion_y:
      print("¡Llamada de emergencia encima de un hospital! - Por favor revise otra Emergencia.")
    else:
      menor_distancia = min(distancias)
      ubicacion_hospital_cercano = distancias.index(min(distancias)) #Este es el índice del hospital más cercano para buscar en el array
      hospital_cercano = Hospitales[ubicacion_hospital_cercano] #Este es el hospital más cercano
      nombre_hospital = hospital_cercano.nombre
      print("El", nombre_hospital + " es el más cercano su distancia hasta la Emergencia es de "+str(menor_distancia))

    gen_emergencia = False

    if graf_emergencia:
      pos_emergencia_x = (llamada_emergencia.posicion_x - 1)*(width/30) + margen
      pos_emergencia_y = (llamada_emergencia.posicion_y - 1)*(height/30) + margen
      pos_hospital_cercano_x = (hospital_cercano.posicion_x - 1)*(width/30) + margen
      pos_hospital_cercano_y = (hospital_cercano.posicion_y - 1)*(height/30) + margen
      pygame.draw.circle(surface, red, (pos_emergencia_x, pos_emergencia_y), 10)


      if posh_x != llamada_emergencia.posicion_x:
        pygame.draw.line(surface, white, (pos_emergencia_x,pos_emergencia_y), (pos_hospital_cercano_x, pos_hospital_cercano_y), 2)

    pygame.display.update()