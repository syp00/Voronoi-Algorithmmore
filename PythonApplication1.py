from PIL import Image
import random
import math
 
def generate_voronoi_diagram(width, height): #, num_cells):
  image = Image.new("RGB", (width, height))
  putpixel = image.putpixel
  imgx, imgy = image.size
  nx = []
  ny = []   
  nr = []
  ng = []
  nb = []
  
  nx = [20, 40, 40, 40, 40, 60, 60, 60, 60, 80, 80, 120, 120, 140, 140, 140, 140, 160, 160, 160, 160, 180]
  ny = [50, 20, 40, 60, 80, 20, 40, 60, 80, 40, 60, 40, 60, 20, 40, 60, 80, 20, 40, 60, 80, 50]
  nr = [0, 43, 100, 232, 0, 45, 73, 65, 233, 112, 213, 0, 43, 100, 232, 0, 45, 73, 65, 233, 112, 213]
  nb = [45, 33, 0, 0, 0, 241, 155, 214, 12, 156, 222, 45, 33, 0, 0, 0, 241, 155, 214, 12, 156, 222]
  ng = [90, 43, 100, 232, 0,  100, 232, 0, 45, 73, 65, 90, 43, 100, 232, 0,  100, 232, 0, 45, 73, 65]
  
  num_cells = len(nx)

  print(nx,"\n",ny)
  print(imgx, imgy)

  for y in range(imgy):
    for x in range(imgx):
      dmin = math.hypot(imgx, imgy)
      j = -1
      for i in range(num_cells):
        d = math.hypot(nx[i]-x, ny[i]-y)
        if d < dmin:
          dmin = d
          j = i
      putpixel((x, y), (nr[j], ng[j], nb[j]))

    for i in range(22):
      image.putpixel((nx[i], ny[i]), (255, 255, 255))
   
  image.save("VoronoiDiagram.png", "PNG")
  image.show()


if __name__== "__main__":
  generate_voronoi_diagram(200, 100) 