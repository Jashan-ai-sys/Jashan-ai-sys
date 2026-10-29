import sys, glob
from PIL import Image
q = int(sys.argv[2])
frames = [Image.open(f).convert("RGBA") for f in sorted(glob.glob("frames/*.png"))]
frames[0].save(sys.argv[1], save_all=True, append_images=frames[1:], duration=round(1000/24), loop=0, quality=q, method=6)
print(len(frames), frames[0].size)
