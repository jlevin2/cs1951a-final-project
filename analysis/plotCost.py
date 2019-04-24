import sqlite3
import matplotlib.pyplot as plt

COLORS = ['RED','ORANGE','YELLOW','GREEN','BLUE','INDIGO']

'''
x: list of data for x axis
y: list of data for y axis
x_axis_label: string
y_axis_label: string
'''
def plotPoints(x, y, x_axis_label, y_axis_label, color, legend_label=""):
    plt.scatter(x, y, alpha=0.3, s=1, c=color, label=legend_label)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)

"Year is a string from : 'six','seven','eight','nine','ten'"
def cost_vs_year_earnings(year):
    conn = sqlite3.connect('earnings.db')
    c = conn.cursor()
    c.execute('SELECT {0}_year_mean, cost_estimate_pri FROM earnings WHERE cost_estimate_pri IS NOT NULL and {0}_year_mean IS NOT NULL'.format(year))
    private =  list(filter(lambda x: not isinstance(x[0], str) and not isinstance(x[1], str), c.fetchall()))
    c.execute('SELECT {0}_year_mean, cost_estimate_pub FROM earnings WHERE cost_estimate_pub IS NOT NULL and {0}_year_mean IS NOT NULL'.format(year))
    public = list(filter(lambda x: not isinstance(x[0], str) and not isinstance(x[1], str), c.fetchall()))

    private_earnings = [row[0] for row in private]
    private_costs = [row[1] for row in private]
    public_earnings = [row[0] for row in public]
    public_costs = [row[1] for row in public]

    plotPoints(private_costs,private_earnings,"Costs of Attendance","Expected Earnings", "red", "Private Institutions")
    plotPoints(public_costs,public_earnings,"Costs","Expected Earnings", "blue", "Public Institutions")
    plt.title('Costs of Attendance vs Expected Earnings')
    plt.legend()

def cost_vs_earnings_over_time():
    conn = sqlite3.connect('earnings.db')
    c = conn.cursor()
    years = [9,11,12,13,14]
    for index,year in enumerate(years):
        c.execute('SELECT six_year_mean, cost_estimate_pri FROM earnings WHERE cost_estimate_pri IS NOT NULL and six_year_mean IS NOT NULL and year={0}'.format(year))
        private =  list(filter(lambda x: not isinstance(x[0], str) and not isinstance(x[1], str), c.fetchall()))
        c.execute('SELECT six_year_mean, cost_estimate_pub FROM earnings WHERE cost_estimate_pub IS NOT NULL and six_year_mean IS NOT NULL')
        public = list(filter(lambda x: not isinstance(x[0], str) and not isinstance(x[1], str), c.fetchall()))
        private_earnings = [row[0] for row in private]
        private_costs = [row[1] for row in private]
        public_earnings = [row[0] for row in public]
        public_costs = [row[1] for row in public]

        plotPoints(private_costs + public_costs,private_earnings + public_earnings,"Costs of Attendance","Expected Earnings", COLORS[index], str(year))

    plt.title('Costs of Attendance vs Expected Earnings')
    plt.legend()



cost_vs_year_earnings('six')
plt.show()
