import graphics.threeD_graphics.cuboid as cb
from graphics.threeD_graphics.sphere import sphere_circum as sp
from graphics.threeD_graphics.sphere import sphere_area
from graphics import rectungle
from graphics import circle as cr
r=int(input("Enter the radius of circle "))
cr.cir_area(r)
cr.cir_perimeter(r)
l=int(input("Enter the length of rectungle "))
b=int(input("Enter the breadth of rectungle "))
rectungle.rect_area(l,b)
rectungle.rect_perimeter(l,b)
s=int(input("Enter the radius of sphere "))
sp(s)
sphere_area(s)
lc=int(input("Enter the length of cuboid "))
wc=int(input("Enter the width of cuboid "))
hc=int(input("Enter the height of cuboid "))
cb.cuboid_area(lc,wc,hc)
cb.cuboid_perimeter(lc,wc,hc)