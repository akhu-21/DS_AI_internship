
import random
random.seed(1)

actions = ["Click", "Scroll", "Exit"]

sample_space = [(a1, a2) for a1 in actions for a2 in actions]

print("Sample Space:")
print(sample_space)
print("Total outcomes:", len(sample_space))

event_E = [outcome for outcome in sample_space if "Click" in outcome]

print("\nEvent E (At least one Click):")
print(event_E)

probability_E = len(event_E) / len(sample_space)
print("Theoretical Probability of at least one Click:", probability_E)

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("\nExperimental Probability of Sum = 7 (1000 rolls):")
print(experimental_probability)





print("\nTask 2: The Logic of Dependency (Independent vs. Dependent)\n")

print("\nout put for Independent Events\n")

coin_tossed_head = 1/2
dice_rolling_6 = 1/6
print(f'P(A) * P(B) : {coin_tossed_head * dice_rolling_6 :.3f}')

print("\nout put for Dependent Events\n")

red = 5
blue = 5
picking_1st_marble = red / (red+blue)
picking_2st_marble = (red-1)/(red+blue-1)

prob = picking_1st_marble * picking_2st_marble
print(f'probability that both are Red without Replacement : {prob:.2f}')





print("\nTask 3: The Bayesian Filter (Conditional Probability & Bayes’ Theorem)\n")
spam = 0.1
free_spam = 0.9
ham = 0.9
free_ham = 0.05

spams = spam * free_spam
hams = ham * free_ham
free = (spams) + (hams)
print(f'\nP(free) : {free}\n')

spam_free = (free_spam * spam) / free
print(f'\nemail with the word  "Free", probability it is actually Spam  : {spam_free:.2f}\n')




















































