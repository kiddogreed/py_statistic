# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import statistics

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



    score = [89, 90, 91, 90, 85, 91, 88, 80, 77, 81, 76, 85, 87, 88, 83, 95, 88, 82, 85, 84]

    mean = statistics.mean(score)
    mode = statistics.mode(score)
    median = statistics.median(score)

    print(f"MEAN:{mean}")
    print(f"MODE:{mode}")
    print(f"MEADIAN:{median}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
