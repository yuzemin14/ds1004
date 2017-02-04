import matplotlib.pyplot as plt
c = [0, 1, 2, 3, 4, 5]
sec = [2.2384, 2.5067, 3.0443, 4.6418, 6.6878, 10.8745]
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(c, sec)

ax.set_xlabel('Numbers of Reducers - log2')
ax.set_ylabel('Seconds')
plt.title('Time Used as Function of Numbers of Reducers')