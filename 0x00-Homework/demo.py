import matplotlib.pyplot as plt
import numpy as nmpi

bars = plt.bar(['January', 'February', 'March', 'April', 'May', 
                      'June', 'July', 'August', 'September', 
                      'October', 'November', 'December'],  [35000, 42000, 38000, 41000, 38000, 
                                                            39000, 45000, 47000, 43000, 42000, 48000, 51000])
bars[0].set_color('green')
bars[1].set_color('black')
bars[2].set_color('yellow')
bars[3].set_color('blue')
bars[4].set_color('red')
bars[5].set_color('orange')
bars[6].set_color('pink')
bars[7].set_color('brown')
bars[8].set_color('purple')
bars[9].set_color('gray')
bars[10].set_color('indigo')
bars[11].set_color('violet')

plt.show()