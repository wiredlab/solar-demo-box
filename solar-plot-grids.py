#!/usr/bin/env python3


from matplotlib.pylab import *

interactive(False)
close()


# figure(figsize=(7.5, 10))
figure(figsize=(10, 7.5))
suptitle('''Valpo ECE Solar Panel Load Curve
panel:____________________
lamp:____________________
''')

subplot(1, 1, 1)
plot()
grid(True)

title('Voltage and Power vs Current')
xticks(arange(0, 131, 5), rotation=45)
xlabel('Panel current (mA)')

yticks(arange(0, 22.1, 1))
ylabel('Panel voltage (V)\n and power ($\\times 100$mW)')

tight_layout()


if False:
    subplot(2, 1, 2)
    plot()
    grid(True)

    # title('Load curve _______________')
    xticks(arange(0, 131, 5), rotation=45)
    xlabel('Panel current (mA)')

    yticks(arange(0, 2.11, 0.1))
    ylabel('Panel power (W)')

    # tight_layout()


savefig('solar-plot-grids.pdf')

