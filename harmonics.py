import matplotlib.pyplot as plt
from numpy import arange, sin, cos
from math import pi
from config import PATH, author, preset, params


class Parser:
    def __init__(self, title, time, wave, color, label, amplitude, ax, bw):
        self.title = title
        self.time = time
        self.wave = wave
        self.color = color
        self.label = label
        self.amplitude = amplitude
        self.ax = ax
        self.bw = bw


def plotter(func):
    def wrapper(**kwargs):

        extract = func(**kwargs)
        plt.style.use('bmh')
        plt.rcParams.update(params)
        plt.title(
            f'${extract.label}$ ${extract.ax}$\n${extract.title}$', style=preset)
        plt.ylabel(f'$amplitude({extract.amplitude})$', style=preset)
        plt.xlabel(f'$time(t)$\n${author}$', style=preset)
        plt.xticks([x for x in range(0, extract.bw+1)])
        plt.axhline(color='#fff', linewidth=1)
        # plt.savefig(f'{PATH}//Figure_{pos}.png', dpi=400)

        plt.plot(extract.time, extract.wave, color=extract.color)
        plt.show()

    return wrapper


@plotter
def gen_shm(A=1, T=8, tm=10, pos=1):
    t = arange(0, tm, 0.1)
    omega = (2*pi)/T
    n = 1/T

    displacement_m = A*(sin(omega*t))
    velocity_m = (A*omega)*(cos(omega*t))
    acc_m = -(A*(omega**2))*(sin(omega*t))

    displacement_e = A*(cos(omega*t))
    velocity_e = -(A*omega)*(sin(omega*t))
    acc_e = -(A*(omega**2))*(cos(omega*t))

    m = '(mean-position)'
    e = '(extreme-position)'
    title = f'A={A}m, T={T}s, ω={omega:.2f} rad/s, t={tm} s, n={n:.2f} Hz'

    waves = [displacement_m, velocity_m, acc_m,
             displacement_e, velocity_e, acc_e]
    colors = ['#1f77b4', '#e5ae38', '#67b551']
    labels = ['displacement', 'velocity', 'acceleration']
    amps = ['A', 'Aω', 'Aω^2']

    i = pos if pos <= 3 else pos - 3
    ax = m if pos <= 3 else e

    return Parser(title, t, waves[pos-1], colors[i-1], labels[i-1], amps[i-1], ax, tm)


a = gen_shm(pos=2)
