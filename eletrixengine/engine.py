ENGINE_VERSION = "0.0.1"

if __name__ == "__main__":
   raise RuntimeError("Please run the main.py file !")

try:
  from eletrixengine.libs import console
except Exception as e:
  print(f"CRITICAL ERROR : {e}")
  exit(-1)
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
  exit(-1)

# Load assets
  
from eletrixengine.assets.cube import conf as cube_demo_conf

print(f"Hello from EletrixEngine Community {ENGINE_VERSION}")
pygame.display.set_caption(f"EletrixEngine {ENGINE_VERSION} - untitled Window")

class Logs(object):

  def error(self, text):
    console.print_error(text)

  def warn(self, text):
    console.print_warning(text)

  def info(self, text):
    console.print_info(text)

class Demo(object):
  def cube(self):
    glBegin(GL_LINES)
    for edge in cube_demo_conf.edges:
        for vertex in edge:
            glVertex3fv(cube_demo_conf.vertices[vertex])
    glEnd()


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.coord = (x, y, z)
      
    def translation(self, vector):
        self.x += vector.self.coord_x
        self.y += vector.self.coord_y

class Vector(object):
    def __init__(self, origine_pt, extrem_pt):
        self.origine = origine_pt
        self.extremity = extrem_pt

        self.coord_x = self.extremity.x - self.origine.x
        self.coord_y = self.extremity.y - self.origine.y


class Object3D(object):
   def __init__(self, pts_list:list, texture=None):
        self.list_pts = pts_list
        self.texture = texture

        




    
class WindowProperty():
  def set_title(self, title):
    try:
      pygame.display.set_caption(title)
      return("true")
    except Exception as e:
      console.print_error(f"Error occured in set_title function : {e}")
      return("false")
    

  def init(self, width, height):
      # FewerElk note : you should not name a fct like this. It is confusing.
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

              Demo().cube()
              glRotatef(1, 3, 1, 1)
              glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

              pygame.display.flip()
              pygame.time.wait(10)

          pygame.quit()  # Quit pygame before exiting
          return "true"
      except Exception as e:
          console.print_error(f"Failed to init pygame: {e}")
          return "false"

  def set_icon(self, path):
    try:
      Icon = pygame.image.load(path)
      pygame.display.set_icon(Icon)
      return("true")
    except Exception as e:
      return("false")
