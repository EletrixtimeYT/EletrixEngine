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
        x = self.x + vector.self.coord_x
        y = self.y + vector.self.coord_y
        z = self.z + vector.self.coord_z

        return Point(x, y, z)

class Vector(object):
    def __init__(self, origine_pt, extrem_pt):
        self.origine = origine_pt
        self.extremity = extrem_pt

        self.coord_x = self.extremity.x - self.origine.x
        self.coord_y = self.extremity.y - self.origine.y
        self.coord_z = self.extremity.z - self.origine.z
        
    def multiply(self, factor:float):
        """Multiply this vector. Return a new vector"""
        ncx = self.coord_x * factor
        ncy = self.coord_y * factor
        ncz = self.coord_z * factor

        nx = self.origine.x + ncx
        ny = self.origine.y + ncz
        nz = self.origine.z + ncx
        return Vector(Point(nx, ny, nz))
        
    def addition(self, vector):
        #get new vec coord
        x2 = self.coord_x + vector.coord_x
        y2 = self.coord_y + vector.coord_y
        z2 = self.coord_z + vector.coord_z
        
        #get new ext pt coord
        ptx = self.origine.x + x2
        pty = self.origine.y + y2
        ptz = self.origine.z + z2
        
        #create the pt for the ext
        extr = Point(ptx, pty, ptz)
        
        #the final vector
        sum = Vector(self.origine, extr)
        return sum
    
class Face(object):
   def __init__(self, list_pts, texture=None):
      texture = texture

      self.list_pts = list_pts


class Object3D(object):
    def __init__(self, pts_list:list, texture=None):
        raise DeprecationWarning("Don't use now. Maybe later")
        self.list_pts = pts_list
        self.texture = texture
      
    def build(self):
       ...

class Cube(object):
  def __init__(self, size:float, origine:Point, texture=None):
      self.origine = origine
      self.texture = texture
      self.size = size

      self.list_pts = [origine]
      
  def build(self):
     pt1 = Point(self.origine.x + self.size, self.origine.y, self.origine.z)
     pt2 = Point(self.origine.x, self.origine.y + self.size, self.origine.z)
     pt3= Point(self.origine.x, self.origine.y, self.origine.z + self.size)

     pt4 = Point(self.origine.x + self.size, self.origine.y, self.origine.z + self.size)
     pt5 = Point(self.origine.x + self.size, self.origine.y + self.size, self.origine.z + self.size)
     pt6 = Point(self.origine.x + self.size, self.origine.y + self.size, self.origine.z)
     pt7 = Point(self.origine.x, self.origine.y + self.size, self.origine.z + self.size)

     self.list_pts.append(pt1, pt2, pt3, pt4, pt5, pt6, pt7)
    
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
