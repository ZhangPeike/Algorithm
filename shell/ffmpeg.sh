ffmpeg -f image2 -i $1 -c:v libx264 -r 25 $2/%07d.png
