import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.axis([0, 20, 0, 20])
fig.suptitle("cat SherKhan")
usiki_x = [11.29,11.74,11.10,8.61,8,8.45]
usiki_y = [7.58,8.14,8.61,7.71,8.14,8.35]
Usiki_x1 = [8.23,5]
Usiki_y1 = [8.31,9]
Usiki_x2 = [8.32,5]
Usiki_y2 = [8.01,7]
Usiki_x3 = [8.42,6.30]
Usiki_y3 = [7.71,6.30]
Usiki_x4 = [11.35,14]
Usiki_y4 = [8.40,9]
Usiki_x5 = [11.42,14.77]
Usiki_y5 = [8.05,7.75]
Usiki_x6 = [11.48,14]
Usiki_y6 = [7.71,6.30]
c1=plt.Circle ((10, 10), radius= 6,color = 'yellow')
c2=plt.Circle ((7.87, 11.04), radius= 1.3,color = 'black')
c3=plt.Circle ((11.81, 11.04), radius= 1.3 ,color = 'black')
c4=plt.Circle ((8, 10.95), radius= 0.2,color = 'white')
c5=plt.Circle ((12.29, 10.87), radius= 0.2 ,color = 'white')
c_nose=plt.Circle ((9.84, 9.44), radius= 1,color = 'orange')
plt.gca ().add_artist (c1)
plt.gca ().add_artist (c2)
plt.gca ().add_artist (c3)
plt.gca ().add_artist (c4)
plt.gca ().add_artist (c5)
plt.gca ().add_artist (c_nose)
plt.scatter(7.48,16.41,marker='^',s=4000,c="yellow")
plt.scatter(11.81,16.41,marker='^',s=4000,c="yellow")
plt.scatter(usiki_x,usiki_y,s=2,c="black")
plt.plot(Usiki_x1,Usiki_y1,c='black')
plt.plot(Usiki_x2,Usiki_y2,c='black')
plt.plot(Usiki_x3,Usiki_y3,c='black')
plt.plot(Usiki_x4,Usiki_y4,c='black')
plt.plot(Usiki_x5,Usiki_y5,c='black')
plt.plot(Usiki_x6,Usiki_y6,c='black')
plt.show()