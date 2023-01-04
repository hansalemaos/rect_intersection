# Checks if two rectangles intersect 


```python
# Tested with:
# Python 3.9.13
# Windows 10

from rect_intersection import intersects

# Allowed formats for box1/box2 
format_1x4 = (0, 0, 100, 200)
format_4x2 = [(0, 0), (100, 0), (100, 200), (0, 200)]
format_2x2 = [(0, 0), (100, 200)]

box1 = (0, 0, 100, 200)


box2 = (1000, 1000, 2000, 2000)
print(intersects(box1, box2))
box2 = (50, 20, 2000, 2000)
print(intersects(box1, box2))
box2 = [(50, 20), (2000, 20), (2000, 2000), (50, 2000)]
print(intersects(box1, box2))
box2 = [(50, 20), (2000, 2000)]
print(intersects(box1, box2))


box2 = (1000, 1000, 2000, 2000)
print(intersects(box1, box2))
box2 = (50, 20, 2000, 2000)
print(intersects(box1, box2))
box2 = [(50, 20), (2000, 20), (2000, 2000), (50, 2000)]
print(intersects(box1, box2))
box2 = [(50, 20), (2000, 2000)]
print(intersects(box1, box2))

box2 = (1000, 1000, 2000, 2000)
print(intersects(box1, box2))
box2 = (50, 20, 2000, 2000)
print(intersects(box1, box2))
box2 = [(50, 20), (2000, 20), (2000, 2000), (50, 2000)]
print(intersects(box1, box2))
box2 = [(50, 20), (2000, 2000)]
print(intersects(box1, box2))



False
True
True
True
False
True
True
True
False
True
True
True

	
```




