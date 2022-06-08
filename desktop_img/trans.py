import PythonMagick as ma

for i in range(66):
    img = ma.Image('./woozi_img/{point}.png'.format(point=i+1)) 
    img.sample('128x128')
    img.write('./woozi/{point}.ico'.format(point=i+1))
img = ma.Image('/woozi_img/icon.jpeg')
img.sample('128x128')
img.write('./woozi/icon.ico')
img = ma.Image('/woozi_img/icon2.jpeg')
img.sample('128x128')
img.write('./woozi/icon2.ico')