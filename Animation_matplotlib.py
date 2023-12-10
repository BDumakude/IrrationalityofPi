import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from matplotlib.animation import FFMpegWriter
from matplotlib.animation import FuncAnimation

# The next (commented) line is if ffmpeg isn't added to your PATH and you have to specify its location form matplotlib 
# plt.rcParams['animation.ffmpeg_path'] = "C:\\{Your Full path}\\ffmpeg.exe"

fig = plt.figure(figsize=(8, 8), facecolor="black")

l, = plt.plot([], [], "white")

plt.xlim(-3, 3)
plt.ylim(-3, 3)

plt.axis("off")

def x_comp(t):
    return np.cos(t) + np.cos(np.pi * t)

def y_comp(t):
    return np.sin(t) + np.sin(np.pi * t)

t_list = np.linspace(0, 40*np.pi, 10000)

metadata = dict(title="Movie", artist="B.Dumakude")
writer = FFMpegWriter(fps = 15, metadata=metadata)

x_list = []
y_list = []

with writer.saving(fig, "The Irrationality of Pi 2.mp4", 100):
    for tval in t_list:
        x_list.append(x_comp(tval))
        y_list.append(y_comp(tval))

        l.set_data(x_list, y_list)

        writer.grab_frame()
    
plt.show()