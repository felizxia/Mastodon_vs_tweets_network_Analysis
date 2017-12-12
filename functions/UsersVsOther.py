import csv
import string
import matplotlib.pyplot as plt

users = []
Connections = []
degree = []
separation = []
Diameter = []
Components = []
Density = []
AverageDegree = []
index = 0
with open('final.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        index += 1
        if index == 1:
            continue
        else:
            users.append(row[2])
            Connections.append(row[3])
            degree.append(row[7])
            separation.append(row[8])
            Diameter.append(row[9])
            Components.append(row[10])
            Density.append(row[11])
            AverageDegree.append(row[12])

######################################################################################################################
# userVsseparation = zip(users,separation)
# sorted(userVsseparation, key=lambda x: x[0])
# # print(userVsseparation)
# users_X = []
# separation_Y = []
# for i in reversed(userVsseparation):
#     users_X.append(int(i[0]))
#     separation_Y.append(float(i[1]))
# print users_X
# print separation_Y
#
# plt.plot(users_X,separation_Y,'ro')
# # plt.yscale('log')
# plt.xscale('log')
# plt.xlabel('# of users(log)')
# plt.ylabel('separation')
# plt.show()

# ######################################################################################################################
# userVsDegree = zip(users,degree)
# sorted(userVsDegree, key=lambda x: x[0])
# # print(userVsseparation)
# users_X = []
# Degree_Y = []
# for i in reversed(userVsDegree):
#     users_X.append(int(i[0]))
#     Degree_Y.append(float(i[1]))
# print users_X
# print Degree_Y
#
# plt.plot(users_X,Degree_Y,'ro')
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel('# of users(log)')
# plt.ylabel('Degree(log)')
# plt.show()

# ######################################################################################################################
# userVsDiameter = zip(users,Diameter)
# sorted(userVsDiameter, key=lambda x: x[0])
# # print(userVsseparation)
# users_X = []
# Diameter_Y = []
# for i in reversed(userVsDiameter):
#     users_X.append(int(i[0]))
#     Diameter_Y.append(float(i[1]))
# print users_X
# print Diameter_Y
#
# plt.plot(users_X,Diameter_Y,'ro')
# # plt.yscale('log')
# plt.xscale('log')
# plt.xlabel('# of users(log)')
# plt.ylabel('Diameter')
# plt.show()

# ######################################################################################################################
# userVsComponents = zip(users,Components)
# sorted(userVsComponents, key=lambda x: x[0])
# # print(userVsseparation)
# users_X = []
# Components_Y = []
# for i in reversed(userVsComponents):
#     users_X.append(int(i[0]))
#     Components_Y.append(float(i[1]))
# print users_X
# print Components_Y
#
# plt.plot(users_X,Components_Y,'ro')
# # plt.yscale('log')
# plt.xscale('log')
# plt.xlabel('# of users(log)')
# plt.ylabel('Components')
# plt.show()

# ######################################################################################################################
# userVsDensity = zip(users,Density)
# sorted(userVsDensity, key=lambda x: x[0])
# # print(userVsseparation)
# users_X = []
# Density_Y = []
# for i in reversed(userVsDensity):
#     users_X.append(int(i[0]))
#     Density_Y.append(float(i[1]))
# print users_X
# print Density_Y
#
# plt.plot(users_X,Density_Y,'ro')
# # plt.yscale('log')
# plt.xscale('log')
# plt.xlabel('# of users(log)')
# plt.ylabel('Density')
# plt.show()

######################################################################################################################
userVsAverageDegree = zip(users,AverageDegree)
sorted(userVsAverageDegree, key=lambda x: x[0])
# print(userVsseparation)
users_X = []
AverageDegree_Y = []
for i in reversed(userVsAverageDegree):
    users_X.append(int(i[0]))
    AverageDegree_Y.append(float(i[1]))
print users_X
print AverageDegree_Y

plt.plot(users_X,AverageDegree_Y,'ro')
# plt.yscale('log')
plt.xscale('log')
plt.xlabel('# of users(log)')
plt.ylabel('AverageDegree')
plt.show()