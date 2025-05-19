import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# The function allows to choose a statistic for sampling and population distributions
def choose_statistic(x, sample_stat_text):
  # calculate mean if the text is "Mean"
  if str.lower(sample_stat_text) == "mean":
    return np.mean(x)
  # calculate minimum if the text is "Minimum"
  elif str.lower(sample_stat_text) == "minimum":
    return np.min(x)
  # calculate maximum if the text is "Maximum"
  elif str.lower(sample_stat_text) == "maximum":
    return np.max(x)
  # calculate variance if the text is "Variance"
  elif str.lower(sample_stat_text) == "variance":
    return np.var(x)
  # raise error if sample_stat_text is not "mean", "minimum", or "variance"
  else:
    raise Exception('Make sure to input "mean", "minimum", "maximum", or "variance"')

# The function allows to plot the population distribution and sampling distribution
def plot_population_distribution(population_data):
  # plot the population distribution
  sns.histplot(population_data, stat='density')
  # informative title for the distribution 
  plt.title(f"Population Distribution")
  # remove None label
  plt.xlabel('')
  plt.show()
  plt.clf()

# The function allows to plot a simulated sampling distribution of a statistic
def sampling_distribution(population_data, samp_size, stat):
  # list that will hold all the sample statistics
  sample_stats = []
  for i in range(500):
    # get a random sample from the population of size samp_size
    samp = np.random.choice(population_data, samp_size, replace = False)
    # calculate the chosen statistic (mean, minimum, maximum or variance) of the sample
    sample_stat = choose_statistic(samp, stat)
    # add sample_stat to the sample_stats list
    sample_stats.append(sample_stat)
  
  pop_statistic = round(choose_statistic(population_data, stat),2)
  
  # plot the sampling distribution
  sns.histplot(sample_stats, stat='density')
  # informative title for the sampling distribution
  plt.title(f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n Population {stat}: {pop_statistic}")
  plt.axvline(pop_statistic,color='g',linestyle='dashed', label=f'Population {stat}')
  # plot the mean of the chosen sample statistic for the sampling distribution
  plt.axvline(np.mean(sample_stats),color='orange',linestyle='dashed', label=f'Mean of the Sample {stat}s')
  plt.legend()
  plt.show()
  plt.clf()