from random import Random


class BirthdayParadox:
    """
    A class to simulate and test the Birthday Paradox.

    The Birthday Paradox states that in a group of just 23 people,
    there is more than a 50% chance that at least two people
    share the same birthday.

    This class allows simulation of the paradox for any number
    of people and multiple trials to estimate the probability.
    """

    def __init__(self, people_count, testing_range=1000):
        """
        Initialize the BirthdayParadox simulation.

        :param people_count: Number of people in the group.
        :param testing_range: Number of trials/experiments to run (default=1000).
        """
        self.__people_count, self.__testing_range = self._input_validation(
            people_count, testing_range
        )
        self.__r = Random()  # Random number generator instance

    def _input_validation(self, people_count, testing_range):
        if not isinstance(people_count, int):
            raise TypeError("people_count must be an integer")
        elif not isinstance(testing_range, int):
            raise TypeError("testing_range must be an integer")
        else:
            return people_count, testing_range

    # ---- Properties for people count ----
    @property
    def people_count(self):
        """Return the number of people in the simulation."""
        return self.__people_count

    @people_count.setter
    def people_count(self, new_people_count: int):
        """Set a new number of people for the simulation."""
        self.__people_count = new_people_count

    # ---- Properties for testing range ----
    @property
    def testing_range(self):
        """Return the number of trials in the simulation."""
        return self.__testing_range

    @testing_range.setter
    def testing_range(self, new_range):
        """Set a new number of trials for the simulation."""
        self.__testing_range = new_range

    # ---- Generate birthdays ----
    def _generate_birthdays(self):
        """
        Generate random birthdays for one trial.

        Process:
        - For each person in the group, pick a random integer between 1 and 365.
          (We assume a year has 365 equally likely birthdays, ignoring leap years.)
        - Store all birthdays in a list.

        :return: A list of integers representing birthdays for all people in this trial.
        """
        birthdays = []
        for _ in range(self.__people_count):
            # Pick a random day of the year (1 to 365)
            bd = self.__r.randint(1, 365)
            birthdays.append(bd)
        return birthdays

    # ---- Perform multiple trials ----
    def _birthday_trials(self):
        """
        Run multiple experiments to generate groups of birthdays.

        :return: A list of birthday lists, one for each trial.
        """
        all_birthdays = []
        for _ in range(self.__testing_range):
            generate_birthday = self._generate_birthdays()
            all_birthdays.append(generate_birthday)
        return all_birthdays

    # ---- Count paradox cases ----
    def _count_paradoxes(self):
        """
        Count the number of trials where at least two people
        share the same birthday.

        Process:
        - For each trial (list of birthdays):
            - Keep a temporary list of seen birthdays.
            - As we go through each birthday:
                - If the birthday is already in the list → we found a match → count it as a paradox trial.
                - Stop checking further for that trial (since one match is enough).
            - If no duplicates are found, this trial is NOT counted as a paradox.
        - Repeat for all trials.

        :return: The total number of trials where a birthday match occurred.
        """
        all_birthdays = self._birthday_trials()
        paradox_count = 0
        for bd_list in all_birthdays:
            temp_birthday_list = []
            for birthday in bd_list:
                # Found a duplicate in this trial
                if birthday in temp_birthday_list:
                    paradox_count += 1
                    break  # no need to check further for this trial
                temp_birthday_list.append(birthday)

        return paradox_count

    def paradox_percentage(self):
        """
        Calculate the percentage of trials where at least one birthday match occurred.

        Formula:
        probability = (number of paradox trials / total number of trials) * 100

        :return: Probability (as a percentage) rounded to 2 decimal places.
        """
        paradox_count = self._count_paradoxes()
        percentage = round((paradox_count / self.__testing_range) * 100, 2)
        return percentage

    def __str__(self):
        """
        Return a human-readable summary of the BirthdayParadox simulation.
        """
        return f"""BirthdayParadox Simulation:
- People in group: {self.people_count}
- Trials: {self.testing_range}
- Estimated probability of shared birthday: {self.paradox_percentage()}%"""
