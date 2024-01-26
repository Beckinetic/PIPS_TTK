import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
import warnings

# Q3.2P.1 --------------------------------------------------------------------------------------------------------------
np.random.seed(15118738)
data1 = np.random.uniform(low=-10, high=10, size=100)
fig1 = plt.boxplot(data1)

plt.savefig('Q32P1_boxplot')
plt.show()

data2 = np.random.normal(loc=-10, scale=5, size=100)
fig2 = sns.violinplot(data2)
plt.savefig('Q32P1_violinplot')
plt.show()

fig3 = sns.stripplot(data2)
plt.savefig('Q32P1_stripplot')
plt.show()

# The violin plot spells out the most of the statistical characteristics of the dataset. It illustrates clearly the data
# density along the range. The box plot can hardly show it and so is the strip plot.

# Q3.2P.2 --------------------------------------------------------------------------------------------------------------
df_titanic = pd.read_csv('https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv')
df_titanic.head()

x, counts = np.unique(df_titanic['Sex'].values, return_counts=True)
y1 = df_titanic[df_titanic['Survived'] == 1].groupby('Sex').sum()['Survived'].values
y2 = counts - y1

plt.bar(x, y1)
plt.bar(x, y2, bottom=y1)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(["Survived", "Not Survived"])
plt.title("Titanic Survival by Genders")
plt.savefig('Q32P2_stackedplot')
plt.show()

# Q3.2P.3 --------------------------------------------------------------------------------------------------------------
tips = sns.load_dataset('tips')

scatter_plot = sns.regplot(x='total_bill', y='tip', data=tips)
scatter_plot.set_xlabel('Total Bill')
scatter_plot.set_ylabel('Tip')
plt.savefig('Q32P3_tips')
plt.show()

# Q3.2P.4 --------------------------------------------------------------------------------------------------------------
diamonds = sns.load_dataset('diamonds')

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.heatmap(diamonds.corr(), annot=True, ax=axes[0], cmap='coolwarm')
axes[0].set_title('Correlation Heatmap')

sns.kdeplot(data=diamonds, x='carat', y='price', ax=axes[1], cmap='Blues', fill=True)
axes[1].set_title('KDE Plot of Carat vs Price')

plt.tight_layout()
plt.savefig('Q32P4_diamonds')
plt.show()


# Q3.2P.5 --------------------------------------------------------------------------------------------------------------
def my_plots(string):
    if string == "eww":
        x = np.random.rand(100)
        y = np.random.rand(100)
        plt.scatter(x, y)
        plt.title("Confusing Plot")
        plt.xlabel("Some Random Numbers")
        plt.ylabel("Other Random Numbers")
        plt.show()

    elif string == "yay":
        x = np.arange(0., 10., 0.2)
        y = np.cos(x)
        plt.plot(x, y)
        plt.title("Cosine Wave Plot")
        plt.xlabel("x")
        plt.ylabel("cos(x)")
        plt.show()

    else:
        print("Please either use 'eww' for a confusing plot or 'yay' for a clear plot.")


my_plots("eww")
plt.savefig('Q32P5_eww')
my_plots("yay")
plt.savefig('Q32P5_yay')

# Q3.2P.6 --------------------------------------------------------------------------------------------------------------
# Old code from Q2.2P.7
def nthpower(number, n, start=1):
    max_iterations = 10000
    iteration = 0
    tolerance = 1e-6

    x = start
    while iteration < max_iterations:
        iteration = iteration + 1
        f_x = x ** (1 / n) - number
        f_prime_x = (1 / n) * x ** ((1 / n) - 1)

        x_new = x - f_x / f_prime_x
        if abs(x_new - x) < tolerance:
            break
        x = x_new

    return x


# New code
def find_nth_root(number, exponent, initial_guess=1):
    """
    Calculate the nth root of a given number using the Newton method.

    Parameters:
    number (float): The number to find the nth root of.
    exponent (int): The root to be calculated.
    initial_guess (float): Initial guess for the root value.

    Returns:
    float: The estimated nth root of the number.
    """
    max_iterations = 10000
    iteration = 0
    tolerance = 1e-6

    current_estimate = initial_guess
    while iteration < max_iterations:
        iteration += 1
        function_value = current_estimate ** (1 / exponent) - number
        derivative_value = (1 / exponent) * current_estimate ** ((1 / exponent) - 1)

        updated_estimate = current_estimate - function_value / derivative_value
        if abs(updated_estimate - current_estimate) < tolerance:
            break
        current_estimate = updated_estimate

    return current_estimate

# Improvements:
# (1) Changed the function and argument name to find_nth_root making it more clear.
# (2) Added descriptive comments about function detail
# (3) Used clearer variable names

# Q3.2P.7 --------------------------------------------------------------------------------------------------------------
# One of the controversies about Python coding style is the maximum line length of 79 characters (docstrings or comments
# are limited even further to 72).
# Source: https://pythonsway.it/pep8-style-controversy/
# My opinion: I would loosen the constraint and make it 90~110.
# (1) The screen resolution has improved significantly since the birth of PEP8;
# (2) A strict 72 character cut-off can in some cases impede readability of the code;
# (3) The easiness for code comparison is tempting, but don't people tend to use two monitors now?

# Q3.2P.8 --------------------------------------------------------------------------------------------------------------

# Simulate diffusion models slowly with intrinsic trial-to-trial variability in parameters
def simul_ratcliff_slow(N=100, Alpha=1, Tau=.4, Nu=1, Beta=.5, rangeTau=0, rangeBeta=0, Eta=.3, Varsigma=1, nsteps=300,
                        step_length=.01):
    """
    SIMUL_RATCLIFF_SLOW  Generates data according to a drift diffusion model with optional trial-to-trial variability

    Parameters
    ----------
    N: a integer denoting the size of the output vector
    (defaults to 100 experimental trials)

    Alpha: the mean boundary separation across trials  in evidence units
    (defaults to 1 evidence unit)

    Tau: the mean non-decision time across trials in seconds
    (defaults to .4 seconds)

    Nu: the mean drift rate across trials in evidence units per second
    (defaults to 1 evidence units per second, restricted to -5 to 5 units)

    Beta: the initial bias in the evidence process for choice A as a proportion of boundary Alpha
    (defaults to .5 or 50% of total evidence units given by Alpha)

    rangeTau: Non-decision time across trials is generated from a uniform
    distribution of Tau - rangeTau/2 to  Tau + rangeTau/2 across trials
    (defaults to 0 seconds)

    rangeZeta: Bias across trials is generated from a uniform distribution
    of Zeta - rangeZeta/2 to Zeta + rangeZeta/2 across trials
    (defaults to 0 evidence units)

    Eta: Standard deviation of the drift rate across trials
    (defaults to 3 evidence units per second, restricted to less than 3 evidence units)

    Varsigma: The diffusion coefficient, the standard deviation of the
    evidence accumulation process within one trial. It is recommended that
    this parameter be kept fixed unless you have reason to explore this parameter
    (defaults to 1 evidence unit per second)

    Returns
    -------
    Numpy array with reaction times (in seconds) multiplied by the response vector
    such that negative reaction times encode response B and positive reaction times
    encode response A
    """

    if (Nu < -5) or (Nu > 5):
        Nu = np.sign(Nu) * 5
        warnings.warn('Nu is not in the range [-5 5], bounding drift rate to %.1f...' % (Nu))

    if (Eta > 3):
        warnings.warn('Standard deviation of drift rate is out of bounds, bounding drift rate to 3')
        eta = 3

    if (Eta == 0):
        Eta = 1e-16

    # Initialize output vectors
    rts = np.zeros(N)
    choice = np.zeros(N)

    for n in range(0, N):
        random_walk = np.empty(nsteps)
        start_point = np.random.uniform(Beta - rangeBeta / 2,
                                        Beta + rangeBeta / 2)
        ndt = np.random.uniform(Tau - rangeTau / 2, Tau + rangeTau / 2)
        drift = stats.norm.rvs(loc=Nu, scale=Eta)
        random_walk[0] = start_point * Alpha
        for s in range(1, nsteps):
            random_walk[s] = random_walk[s - 1] + stats.norm.rvs(loc=drift * step_length,
                                                                 scale=Varsigma * np.sqrt(step_length))
            if random_walk[s] >= Alpha:
                random_walk[s:] = Alpha
                rts[n] = s * step_length + ndt
                choice[n] = 1
                break
            elif random_walk[s] <= 0:
                random_walk[s:] = 0
                rts[n] = s * step_length + ndt
                choice[n] = -1
                break
            elif s == (nsteps - 1):
                rts[n] = np.nan
                choice[n] = np.nan
                break
    result = rts * choice
    return result
