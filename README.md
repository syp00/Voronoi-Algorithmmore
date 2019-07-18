# Voronoi-Algorithmmore
# Voronoi Algorithm more
 이 코드는 픽셀을 선택한 후 각자 색상코드를 넣고, 그 외의 픽셀을 가장 가까운 선택된 픽셀의 색상으로 바꿔 이미지를 출력 및 저장한다. 선택된 픽셀은 흰색으로 바꾼다.

 ## 선택된 픽셀 색 변경
 ```python
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

    for i in range(22): # 추가
      image.putpixel((nx[i], ny[i]), (255, 255, 255)) # 색상값 변경 가능
```
