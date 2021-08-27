import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import islice
import csv


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 7
plt.rcParams["figure.figsize"] = fig_size
x = "Q6N7PT68V"
phq = 12
gad = 8

plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [2, 1, 2, 5, 12, 3, 9, 9, 2, 16, 13, 6, 16, 7], color="black", linewidth = 2.5, alpha = 0.75, marker = "D", markersize = 6)
plt.title("Incoming Texts", fontsize = 18)
plt.xlabel("Days Prior to Data Submission", fontsize = 15)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], ("","13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"), fontsize = 12)
plt.ylim(0,32)
plt.ylabel("Number of Texts", fontsize = 15)


#Change for graph type and aggregation interval
plt.savefig("Q6N7PT68V_incoming_texts" + ".png", dpi = 300)


#plt.show()
plt.close()
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 7
plt.rcParams["figure.figsize"] = fig_size
x = "Q6N7PT68V"
phq = 12
gad = 8

plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [4,7,6,8,16,4,17,9,7,30,15,14,20,11], color="black", linewidth = 2.5, alpha = 0.75, marker = "D", markersize = 6)
plt.title("Outgoing Texts", fontsize = 18)
plt.xlabel("Days Prior to Data Submission", fontsize = 15)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], ("","13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"), fontsize = 12)
plt.ylim(0,32)
plt.ylabel("Number of Texts", fontsize = 15)

#Change for graph type and aggregation interval
plt.savefig("Q6N7PT68V_outgoing_texts" + ".png", dpi = 300)


#plt.show()
plt.close()

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 7
plt.rcParams["figure.figsize"] = fig_size
x = "Q6N7PT68V"
phq = 12
gad = 8

plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [119, 3374,9253,5617,11194,7619,248,1712,5244,9372,4208,13179,5094,354], color="black", linewidth = 2.5, alpha = 0.75, marker = "D", markersize = 6)
plt.title("Incoming Calls", fontsize = 18)
plt.xlabel("Days Prior to Data Submission", fontsize = 15)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], ("","13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"), fontsize = 12)
plt.ylim(0,14000)
plt.ylabel("Seconds on Call", fontsize = 15)


#Change for graph type and aggregation interval
plt.savefig("Q6N7PT68V_incoming_calls" + ".png", dpi = 300)


#plt.show()
plt.close()

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 7
plt.rcParams["figure.figsize"] = fig_size
x = "Q6N7PT68V"
phq = 12
gad = 8

plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [704,12248,1026,3356,952,2801,3207,885,3333,7521,1058,1035,524,50], color="black", linewidth = 2.5, alpha = 0.75, marker = "D", markersize = 6)
plt.title("Outgoing Calls", fontsize = 18)
plt.xlabel("Days Prior to Data Submission", fontsize = 15)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], ("","13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"), fontsize = 12)
plt.ylim(0,14000)
plt.ylabel("Seconds on Call", fontsize = 15)

#Change for graph type and aggregation interval
plt.savefig("Q6N7PT68V_outgoing_calls" + ".png", dpi = 300)


#plt.show()
plt.close()
