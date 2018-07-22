Para que las imágenes de la web no ocupen tanto espacio (ya que la
idea es solo tener un registro de los eventos) las achiqué un poco
utilizando ImageMagick.

Escalar todas las imágenes a máximo 2048 en cualquiera de sus
dimensiones (se conserva el aspecto)

http://www.imagemagick.org/script/command-line-processing.php#geometry

$ mkdir -p resized; \
  for IMG in `ls GOPR*.JPG DSC*.JPG DSC_*.jpg DSCF*.JPG IMG_*.jpg IMG_*.JPG *_n.jpg`; do { \
    convert -resize 2048x2048 ${IMG} resized/${IMG}; \
  } ; done


Para corregir la fecha EXIF de las fotografías utilizo:

$ sudo apt-get install jhead

Restar 2 horas

$ jhead -ta-2:00 imagen.jpg

Sumar 2 horas

$ jhead -ta+2:00 imagen_000*.jpg

Asignar una fecha específica

$ jhead -ds2015:11:12 imagein.jpg
