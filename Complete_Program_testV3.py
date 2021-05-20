import random as rand
import pymysql
import time
import seaborn as sns
import matplotlib.pyplot as plt
import pandas
from matplotlib.backends.backend_pdf import PdfPages



'''////////////////////////////////////////////////////////////////'''
#Define Time
def str_time_prop(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def rand_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)

#print(random_date("1/1/2020 1:30 PM", "1/1/2021 4:50 AM", random.random()))

'''////////////////////////////////////////////////////////////////////'''

#Define all variables in the database and upload them
def define_city():
    global city_1 
#Define City
    if city_1 == 1:
        city_1 = 'New York'
    elif city_1 == 2:
        city_1 = 'New York'
    elif city_1 == 3:
        city_1 = 'Madrid'
    elif city_1 == 4:
        city_1 = 'Tokio'
    elif city_1 == 5:
        city_1 = 'Tokio'
    elif city_1 == 6:
        city_1 = 'London'
    elif city_1 == 7:
        city_1 = 'London'
    elif city_1 == 8:
        city_1 = 'Buenos Aires'
    elif city_1 == 9:
        city_1 = 'Buenos Aires'
    elif city_1 == 10:
        city_1 = 'Buenos Aires'
        
def define_event():
    global event_1, month
    if city_1 == 'New York':
        event_1 = ('Murder','Murder','Theft','Theft','Theft','Fraud','Assault','Arson','Robbery','Vandalism')
        event_1 = rand.choice(event_1)
        if event_1 == 'Theft':
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','H_August','I_September','J_October','K_November','l_December')
            month = rand.choice(month)
        else:
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','J_October','K_November','l_December')
            month = rand.choice(month)            
            
        '''////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
    elif city_1 == 'Madrid':
        event_1 = ('Murder','Theft','Fraud','Fraud','Assault','Arson','Robbery','Vandalism','Vandalism','Vandalism','Vandalism','Vandalism')
        event_1 = rand.choice(event_1)
        if event_1 == 'Vandalism':
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','I_September','J_October','K_November','l_December')
            month = rand.choice(month)
        else:
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','J_October','K_November','l_December')
            month = rand.choice(month)        
        
            '''////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
    elif city_1 == 'Tokio':
        event_1 = ('Murder','Theft','Fraud','Fraud','Fraud','Fraud','Fraud','Fraud','Assault','Arson','Robbery','Vandalism')
        event_1 = rand.choice(event_1)
        if event_1 == 'Fraud':
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','I_September','J_October','K_November','l_December')
            month = rand.choice(month)
        else:
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','J_October','K_November','l_December')
            month = rand.choice(month)
            
            
            '''////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
    elif city_1 == 'London':
        event_1 = ('Murder','Theft','Fraud','Assault','Assault','Assault','Arson','Robbery','Robbery','Robbery','Vandalism','Vandalism','Vandalism')
        event_1 = rand.choice(event_1)  
        if event_1 == 'Assault':
            month = ('A_January','B_Febuary','C_March','C_March','D_April','E_May','F_June','G_July','H_August','I_September','J_October','K_November','l_December')
            month = rand.choice(month)
        else:
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','J_October','K_November','l_December')
            month = rand.choice(month)
            
            
            '''////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
    elif city_1 == 'Buenos Aires':    
        event_1 = ('Murder','Murder','Murder','Murder','Murder','Theft','Fraud','Fraud','Assault','Arson','Robbery','Robbery','Robbery','Robbery','Vandalism')
        event_1 = rand.choice(event_1)
        if event_1 == 'Murder':
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','J_October','K_November','l_December','l_December','l_December')
            month = rand.choice(month)
        else:
            month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','J_October','K_November','l_December')
            month = rand.choice(month)
            '''////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
            
            
def define_month():
    global month
    month = ('A_January','B_Febuary','C_March','D_April','E_May','F_June','G_July','H_August','I_September','J_October','K_November','l_December','l_December')
    month = rand.choice(month)
    
'''define_Month was merged to define_event so its not used right now'''
        
'''//////////////////////////////////////////////////////////////////////'''

'''----------------------Define Individual data for Database Func-----------------'''
def city_random_beta():
    define_city()
    print(city_1)
    define_event()
    print(event_1)
#    define_month()
    print(month)
#    define_date =rand_date("1/1/2020", "1/1/2021", rand.random())
#    print(define_date)
    connection = pymysql.connect(host='localhost',
                             user='localhost',
                             password='123456',
                             database='sys',
                             charset='utf8mb4', 
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor();
    insert_query = """insert into main_table(month,city,crime) values('%s','%s','%s')""" \
        %(month, city_1, event_1 );
        
    cursor.execute(insert_query);
    connection.commit();
    connection.close();
    
for city_define in range(10000):
    city_1 = rand.randint(1,10)
    city_random_beta()
    
    
    
'''
////////////////////////////////////////////////////////////////////////////////////////////////////////
INSERT INTO MAIN_TOTAL TABLE
'''
    
def insert_total():
    connection = pymysql.connect(host='localhost',
                             user='localhost',
                             password='123456',
                             database='sys',
                             charset='utf8mb4', 
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor();
 #   insert_query = """INSERT INTO main_total"""
        
    cursor.execute("""INSERT INTO main_total SELECT City,Month,Crime,COUNT(*) as TOTAL FROM main_table group by crime,month,city""");
    connection.commit();
    connection.close();
    
insert_total()

'''
////////////////////////////////////////////////////////////////////////////////////////////////////////
--------------------DATA ANALYSIS-----------------------------------------------------
'''

    
pp = PdfPages('Crime_report.pdf')
#plt.savefig(pp, format='pdf')
#pp.savefig()

    # create a PdfPages object
#pdf = PdfPages('out.pdf')

# define here the dimension of your figure
#fig = plt.figure()



connection = pymysql.connect(host='localhost',
                             user='localhost',
                             password='123456',
                             database='sys',
                             charset='utf8mb4', 
                             cursorclass=pymysql.cursors.DictCursor)
cursor= connection.cursor();


''' TEST TEST TEST'''


cursor.execute("""TRUNCATE TABLE main_statistics""");
cursor.execute("""INSERT INTO main_statistics SELECT City, Month,Crime,SUM(Total) \
               as Total FROM main_total WHERE City = 'Buenos Aires' \
                   and crime = 'Murder' group by month,crime order by Month""");
connection.commit();

s = "SELECT MAX(Total) FROM main_statistics"
cursor.execute(s)
s = cursor.fetchone()
#s = pandas.read_sql("SELECT MAX(Total) FROM main_statistics", connection)
newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(s))
s = [int(i) for i in newstr.split()]
print(type(s))
def print_and_return(value,sep=''):
    print(value)
    return value
    
s= print_and_return(*s)
print(type(s))
print(s)

print(s)
'''AVG'''



avg = "SELECT AVG(Total) FROM main_statistics"
cursor.execute(avg)
avg = cursor.fetchone()
#s = pandas.read_sql("SELECT MAX(Total) FROM main_statistics", connection)
newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(avg))
avg = [int(i) for i in newstr.split()]
print(type(avg))
def print_and_return(value,sep=''):
    print(value)
    return value
    
avg= print_and_return(*avg)
print(type(avg))
print(avg)

print(s)
if s > avg*2:
    print('Seguir estudio')
elif s <avg*2:
    print('No hacer estudio')
else:
    print('No hacer estudio2')


'''AVG IGUALAR A MEAN, CALCULAR DESVIO STANDARD, CALCULARDIST NORMAL'''









''''end end end'''





'''
(0)
 ----------------------------------INDEX------------------------------------------
//////////////////////////////////////////////////////////////////////////////////
'''


firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt = 'Index\n \n\
        \nHeatmaps-----------------------------------------------------------------------------2\
        \n  -  London Heatmap---------------------------------------------------------------3\
        \n  -  Buenos Aires Heatmap-------------------------------------------------------4\
        \n  -  New York Heatmap------------------------------------------------------------5\
        \n  -  Madrid Heatmap----------------------------------------------------------------6\
        \n  -  Tokio Heatmap------------------------------------------------------------------7\
        \nOther Analysis-----------------------------------------------------------------------8\
        \n  -  Arsonist per month in London-----------------------------------------------9\
        \n  -  Vandalism in London Compared to Total crime------------------------10\
        \n  -  Comparison per month of Murders in Tokio-BsAs---------------------11\
        \n  -  SUM of all  Theft in BsAs-Tokio-New York-Madrid--------------------12\
        \n  -  Buenos Aires Robbery-Murder-Assault-----------------------------------13\
        \n  -  Crimes in April-------------------------------------------------------------------14'
        
        
firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=22, ha="left")
plt.savefig(pp, format='pdf')

'''
(0)
 ----------------------------------Heatmap Page------------------------------------------
//////////////////////////////////////////////////////////////////////////////////
'''


firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt = 'HEATMAPS'
        
        
firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=30, ha="center")
plt.savefig(pp, format='pdf')


''' 
(7)
London Heatmap
//////////////////////////////////////////////////////////////////////////////////
'''


sns.set_theme()

# Load the example flights dataset and convert to long-form
d_7 = pandas.read_sql("SELECT City, Month,Crime,SUM(Total) as Total FROM main_total WHERE City = 'London' group by month,crime order by Crime", connection)
d_7 = d_7.pivot("Month", "Crime", "Total")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(d_7, annot=True,cmap='Blues', fmt="", linewidths=.9, ax=ax)


#plt.savefig('London_Heatmap.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()

''' 
(8)
Buenos Aires Heatmap
//////////////////////////////////////////////////////////////////////////////////
'''


sns.set_theme()

# Load the example flights dataset and convert to long-form
d_8 = pandas.read_sql("SELECT City, Month,Crime,SUM(Total) as Total FROM main_total WHERE City = 'Buenos Aires' group by month,crime order by Month", connection)
d_8 = d_8.pivot("Month", "Crime", "Total")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(d_8, annot=True,cmap='Blues', fmt="", linewidths=.9, ax=ax)


#plt.savefig('BsAs_Heatmap.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()

''' 
(9)
New York Heatmap
//////////////////////////////////////////////////////////////////////////////////
'''


sns.set_theme()

# Load the example flights dataset and convert to long-form
d_9 = pandas.read_sql("SELECT City, Month,Crime,SUM(Total) as Total FROM main_total WHERE City = 'London' group by month,crime order by Crime", connection)
d_9 = d_9.pivot("Month", "Crime", "Total")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(d_9, annot=True,cmap='Blues', fmt="", linewidths=.9, ax=ax)


#plt.savefig('NewYork_Heatmap.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()

''' 
(10)
Madrid Heatmap
//////////////////////////////////////////////////////////////////////////////////
'''


sns.set_theme()

# Load the example flights dataset and convert to long-form
d_10 = pandas.read_sql("SELECT City, Month,Crime,SUM(Total) as Total FROM main_total WHERE City = 'Madrid' group by month,crime order by Crime", connection)
d_10 = d_10.pivot("Month", "Crime", "Total")

# Draw a heatmap with the numeric values in each cell


f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(d_10, annot=True,cmap='Blues', fmt="", linewidths=.9, ax=ax)

#plt.savefig('Madrid_Heatmap.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()

''' 
(12)
Tokio Heatmap
//////////////////////////////////////////////////////////////////////////////////
'''


sns.set_theme()

# Load the example flights dataset and convert to long-form
d_11 = pandas.read_sql("SELECT City, Month,Crime,SUM(Total) as Total FROM main_total WHERE City = 'Tokio' group by month,crime order by Crime", connection)
d_11 = d_11.pivot("Month", "Crime", "Total")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(d_11, annot=True,cmap='Blues', fmt="", linewidths=.9, ax=ax)


#plt.savefig('Tokio_Heatmap.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()


'''
(0)
 ----------------------------------Other Analysis------------------------------------------
//////////////////////////////////////////////////////////////////////////////////
'''


firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt = 'Other Analysis'
        
        
firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=30, ha="center")
plt.savefig(pp, format='pdf')



'''
(1)
 Arsonist per month in London
//////////////////////////////////////////////////////////////////////////////////
'''

d_1 = pandas.read_sql("SELECT city,month,SUM(total) as total FROM main_total WHERE city = 'london' and crime = 'arson' GROUP BY month ORDER BY total DESC", connection)
d_1

sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(7, 3))

sns.set_color_codes("pastel")
sns.barplot(x="total", y="month", data=d_1,
            label="Arson Freq. in London ", color="g")


ax.legend(ncol=1, loc="lower right", frameon=True)
ax.set(xlim=(0,70), ylabel="",
       xlabel="")
sns.despine(left=True, bottom=True)



#plt.savefig('Arson_london_month.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()

'''
(2)
 Vandalism in London Compared to Total crime
//////////////////////////////////////////////////////////////////////////////////
'''


d_2a = pandas.read_sql("SELECT city,month,SUM(total) as total FROM main_total WHERE city = 'london' and crime = 'vandalism' GROUP BY month ORDER BY total DESC", connection)
d_2a

d_2b = pandas.read_sql("SELECT city,month,SUM(total) as total FROM main_total WHERE city = 'london'  GROUP BY month ORDER BY total DESC", connection)
d_2b

f, ax = plt.subplots(figsize=(7, 3))
sns.set_color_codes("pastel")
sns.barplot(x="total", y="month", data=d_2b,
            label="Total Crime in London ", color="r")


sns.set_color_codes("pastel")
sns.barplot(x="total", y="month", data=d_2a,
            label="Total Vandalism in London", color="g")

# Add a legend and informative axis label
ax.legend(ncol=1, loc="lower right", frameon=True)
ax.set(xlim=(0,590), ylabel="",
       xlabel="")
sns.despine(left=True, bottom=True)



sns.set_theme(style="whitegrid")

#plt.savefig('Vandalism_London_TotalCrime.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()

''' 
(3)
Comparison per month of Murders in Tokio-BsAs
//////////////////////////////////////////////////////////////////////////////////
'''
d_3 = pandas.read_sql("SELECT crime,month ,city,Count(*) as total FROM sys.main_table  where city='Buenos Aires' and crime='murder' or city='Tokio' and crime='murder' group by city,crime,month ORDER BY total;", connection)
d_3


g = sns.catplot(
    data=d_3, kind="bar",
    x="month", y="total", hue="city",
    ci="sd", palette="dark", alpha=.6, height=10)
g.despine(left=True)
g.set_axis_labels("", "Murders")
g.legend.set_title("")

#plt.savefig('Month_Comp_Murder_tokio_BsAs.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()

''' 
(4)
SUM of all  Theft in BsAs-Tokio-New York-Madrid
//////////////////////////////////////////////////////////////////////////////////
'''
d_4 = pandas.read_sql("SELECT crime,month ,city,Count(*) as total FROM sys.main_table  where city='Buenos Aires' and crime='Theft' or city='Tokio' and crime='Theft'or city='Madrid' and crime='Theft'or city='New York' and crime='Theft' group by city,crime,month ORDER BY total;", connection)
d_4


g = sns.catplot(
    data=d_4, kind="bar",
    x="month", y="total", hue="city",
    ci="sd", palette="dark", alpha=.6, height=15)
g.despine(left=True)
g.set_axis_labels("", "Murders")
g.legend.set_title("")


#plt.savefig('Total_Theft_BsAs_Tokio_NewTork_Madrid.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()

''' 
(5)
Buenos Aires Robbery-Murder-Assault
//////////////////////////////////////////////////////////////////////////////////
'''


d_5 = pandas.read_sql("SELECT crime,month ,city,Count(*) as total FROM sys.main_table  WHERE City='Buenos Aires' and crime= 'Murder' or crime= 'Assault' and City='Buenos Aires'or crime='Robbery' and City='Buenos Aires' group by city,crime,month ORDER BY total;", connection)
d_5

g = sns.catplot(
    data=d_5, kind="bar",
    x="month", y="total", hue="crime",
    ci="sd", palette="muted", alpha=.6, height=15)
g.despine(left=True)
g.set_axis_labels("", "Top Buenos aires Problems")
g.legend.set_title("")

#plt.savefig('Robbery_Assault_Murder_BsAs.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()


''' 
(6)
Crimes in April
//////////////////////////////////////////////////////////////////////////////////
'''

d_6 = pandas.read_sql("SELECT crime,city,month,count(*) as total from main_table where month = 'D_April' group by month,city,crime ORDER BY total", connection)
d_6

g = sns.catplot(
    data=d_6, kind="bar",
    x="city", y="total", hue="crime",
    ci="sd", palette="muted", alpha=.6, height=15)
g.despine(left=True)
g.set_axis_labels("", "Top Buenos aires Problems")
g.legend.set_title("")


#plt.savefig('April_Crimes.pdf')
plt.savefig(pp, format='pdf')
#pp.savefig()

plt.clf()





connection.close();

pp.close()
