#Cameron Dennis 
#used some chatgpt and google for the vitrual enviornment. 
import numpy as np

np.random.seed(1)
rand_list = np.random.uniform(0, 1, 10)

mean = np.mean(rand_list)
median = np.median(rand_list)
std = np.std(rand_list)

print('Mean: ', mean)
print('Median: ', median)
print('Standard Deviation: ', std)