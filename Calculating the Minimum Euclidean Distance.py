def euclidean_distance(x,y):
    x1=x[0]
    x2=y[0]
    y1=x[1]
    y2=y[1]
    d=(((x2-x1)**2+(y2-y1)**2)**0.5)
    if d!=0:
        return d


points=[(4,5),(8,7),(10,2),(3,15)]
distances=[]
for x in points:
    for y in points:
        if x!=y:
            a=euclidean_distance(x,y)
            if a not in distances:
                distances.append(a)
      

print(f'the minimum distance between two points is equal to {min(distances)}')

        
        
    
    
    
    