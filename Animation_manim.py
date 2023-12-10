from manim import *

def irrational_sketch(t):
            return np.array([np.cos(t) + np.cos(np.pi*t), np.sin(t) + np.sin(np.pi*t), 0])

class Irrational2(Scene):
    def construct(self):
        fun = ParametricFunction(irrational_sketch, t_range=[0, 20*TAU]).set_stroke(width=1)

        self.play(Create(fun, run_time=30, rate_func=linear))
        self.wait(5)   