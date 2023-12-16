
ENGINE_VERSION = "0.0.1"


try:
  from eletrixengine.libs import console
except Exception as e:
  print(f"CRITICAL ERROR : {e}")
  exit()
try:
  import sys
  import os
  os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
  import pygame
  from pygame.locals import *
  from OpenGL.GL import *
  from OpenGL.GLU import *


except:
  console.print_error("Failed to load PyGame and PyOpenGL exiting...")
  exit()

# Load assets
  
from eletrixengine.assets.cube import conf as cube_demo_conf

print(f"Hello from EletrixEngine Community {ENGINE_VERSION}")
pygame.display.set_caption(f"EletrixEngine {ENGINE_VERSION} - untitled Window")

class logs():

  def error(text):
    console.print_error(text)

  def warn(text):
    console.print_warning(text)

  def info(text):
    console.print_info(text)

class demo():
  def Cube():
    glBegin(GL_LINES)
    for edge in cube_demo_conf.edges:
        for vertex in edge:
            glVertex3fv(cube_demo_conf.vertices[vertex])
    glEnd()
    
class window_property():
  def set_title(title):
    try:
      pygame.display.set_caption(title)
      return("true")
    except Exception as e:
      console.print_error(f"Error occured in set_title function : {e}")
      return("false")
  def init(width, height):
      try:
          pygame.init()
          pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
          gluPerspective(45, (width / height), 0.1, 50.0)

          glTranslatef(0.0, 0.0, -5)
          running = True

          while running:
              for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      running = False  # Set the running flag to False to exit the loop

              demo.Cube()
              glRotatef(1, 3, 1, 1)
              glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

              pygame.display.flip()
              pygame.time.wait(10)

          pygame.quit()  # Quit pygame before exiting
          return "true"
      except Exception as e:
          console.print_error(f"Failed to init pygame: {e}")
          return "false"

  def set_icon(path):
    try:
      Icon = pygame.image.load(path)
      pygame.display.set_icon(Icon)
      return("true")
    except Exception as e:
      return("false")
