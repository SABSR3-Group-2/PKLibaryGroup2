#
# Protocol class
#

import math


class Protocol:

    """A class to describe the dosing protocol for the pharmacokinetic model.
    Protocol can consist of continuous infusion of specified duration,
    or discrete doses at stated time points.
    Creates a dose(t) function to be called in the Solution class.

    Parameters
    :param d_g: total quantity of drug administered (ng)
    :type d_g: float
    :param plan: duration of infusion (continuous); dose timings (discrete)
    :type plan: int or float (continuous); list or tuple (discrete)

    Raises
    :Type error: if the dosing plan is in incorrect input format
    """

    def __init__(self, d_g, plan):
        self.d_g = d_g
        self.plan = plan

    def discrete(self, t, dose_time):
        n_dose = len(self.plan)
        sig = 1 / ((self.d_g / n_dose) * math.sqrt(2 * math.pi))
        return (self.d_g / n_dose) * \
            math.exp(-0.5 * ((t - dose_time) ** 2 / (sig ** 2)))

    def dose(self, t):
        if isinstance(self.plan, list) or isinstance(self.plan, tuple):
            gaus = []
            for dose_time in self.plan:
                gaus.append(self.discrete(t, dose_time))
            return sum(gaus)

        elif isinstance(self.plan, int) or isinstance(self.plan, float):
            if t <= self.plan:
                return self.d_g / self.plan
            else:
                return 0

        else:
            raise TypeError('Incorrect input format')
