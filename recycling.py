import matplotlib.pyplot as plt

def pie_chart():
    numbers = [35, 20, 10, 10, 7, 10, 8]  # numeric values representing percentage in pie chart
    labels = ['Plastic', 'Aluminum', 'Paper', 'Steel', 'Cardboard', "E-Waste",
              "Organic Waste"]  # item labels in respective order to numbers

    fig1, ax1 = plt.subplots()
    ax1.pie(numbers, labels=labels, autopct='%1.1f%%')  #autopct parameter for displaying percentage values
    plt.title("Quantifying Recycling Data Sample ")  # text that represents the title of the pie chart
    plt.show()

if __name__ == '__main__':
    pie_chart()
