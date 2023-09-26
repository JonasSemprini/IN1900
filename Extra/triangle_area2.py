#Oppgave

def triangle_area(v):
  x1, y1 = v[0]; x2,y2 = v[1]; x3,y3 = v[2]
  return 0.5*(abs((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)+(x2*y1)))

  corners = {1:(0,0), 2:{1,0}, 3:(0,2)}

  print(triangle_area(corners))
