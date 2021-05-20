

import pymysql
import seaborn as sns
import matplotlib.pyplot as plt
import pandas
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import scipy.stats as stats
import pylab as pl
from scipy.stats import norm, kurtosis


city_select = 'Buenos Aires'
crime_select = 'Murder'

connection = pymysql.connect(host='localhost',
                             user='localhost',
                             password='123456',
                             database='sys',
                             charset='utf8mb4', 
                             cursorclass=pymysql.cursors.DictCursor)
cursor= connection.cursor();



''' Set Power Point Settings '''
pp = PdfPages('Crime_report2.pdf')

''' Set Power Plotting Settings '''
sns.set_theme(style="whitegrid")
sns.set_color_codes("pastel")
sns.despine(left=True, bottom=True)

''' Get Ammount of rows '''
count = "SELECT Count(crime) FROM main_table"
cursor.execute(count)
count = cursor.fetchone()
#s = pandas.read_sql("SELECT MAX(Total) FROM main_statistics", connection)
newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(count))
count = [int(i) for i in newstr.split()]
print(type(count))
def print_and_return(value,sep=''):
    print(value)
    return value
    
count= print_and_return(*count)
print(type(count))
print(count)

print(count)



''' //////////////////////////////////////////////////////////
-----------------------Reprot Starts Here-------------------------
///////////////////////////////////////////////////////////////'''

'(1)Index'
firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt = 'Index\n \n\
        \n  -  Index-----------------------------------------------------------------------------1\
        \n  -  This project---------------------------------------------------------------2\
        \n  -  Technical report-------------------------------------------------------3\
        \n  -  Descriptive Analysis------------------------------------------------------------4\
        \n  -  Symmetry and Kurtosis----------------------------------------------------------------11\
        \n  -  Regression------------------------------------------------------------------13\
        \n  -  Tools used in this project-----------------------------------------------14\n\n\n\n\n\n'
        
        
firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=22, ha="left")
plt.savefig(pp, format='pdf')

'(2)This Project'
firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt = 'This program has the objective of creating a statistical report\
        \nfrom data provided by a big database.\
        \n\nIn order to do it, it will have to order and analyze the\
        \ninformation.  \
        \n\nThis is done by connecting to a database and running queries\
        \nuntil the information has been filtered and tailored to the \
        \npoint where it can be used for this report.\
        \n\nPython will also give you the option to select the target\
        \nof the analysis and with that in mind will create a path of\
        \ncommands where, depending on the quality of the data, it will\
        \ndecide the outcome of the analysis (for example, if a variable\
        \nneeds to be normalized\n\n\n\n'
        
        
firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
plt.savefig(pp, format='pdf')

'(2)Technical Report'
firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt_1=('Technical Report\n\
    \nThis report has been done with academical purposes only\
    \nThe database information was created by a module of this program\
    \nthat works with the creation of tendencies in mind.\n\
    \nFor practical purposes, we are going to define this database\
    \nfree of any bias that may incur while extracting the sample and its\
    \ndependencies\n\
    \nThe sample contains a list of different types of crime that were\
    \nrecorded in 5 different important cities during the period of one\
    \nyear,divided by months.This report will select one city and type \
    \nof crime and perform a statistical analysis of its data.\
    \n\nAny extreme value will be normalized.  \
    \nIt is correct to assume that there might be crimes that were not\
    \nrecorded during this period of time. Therefore its important to\
    \ndefine that this sample is representative of the population\n\n'\
    +'City Selected: '+ city_select \
    +'\nCrime Selected: '+ crime_select \
    +'\nIndividual entries in the sample: '+str(count))
    
txt = txt_1
        
        
firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
plt.savefig(pp, format='pdf')
plt.clf()

'(3)Descriptive Analysis'
firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt_1=('Descriptive analysis\n\
    \n\nThe first step in this report is to evaluate the \
    \nfrequency te data repeats itself.\
    \n\nIn this report, each individual case will be grouped by\
    \ntheir month of ocurrence.\
    \n\nThe next page will show how the data is classified by\
    \nthe time it happened, it will be also compare the frequency of '\
    +crime_select +'s' \
    '\nwith the other crime types in the database\
    \n\n\n\n\n')
    
txt = txt_1
        
        
firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
plt.savefig(pp, format='pdf')
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

''' //////////////////////////////////////////////////////////
-----------------------TEST TEST TEST-------------------------
///////////////////////////////////////////////////////////////'''


cursor.execute("""TRUNCATE TABLE main_statistics""");
cursor.execute("""INSERT INTO main_statistics SELECT City, Month,Crime,SUM(Total) \
               as Total FROM main_total WHERE City = 'Buenos Aires' \
                   and crime = 'Murder' group by month,crime order by Month""");
connection.commit();





'''----------------Extract Max Value--------------------'''
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



'''----------------AVG/MEAN--------------------'''
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


'''----------------Standard Dev--------------------'''
std = "SELECT STD(Total) FROM main_statistics"
cursor.execute(std)
std = cursor.fetchone()
#s = pandas.read_sql("SELECT MAX(Total) FROM main_statistics", connection)
newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(std))
std = [int(i) for i in newstr.split()]
print(type(std))
def print_and_return(value,sep=''):
    print(value)
    return value
    
std= print_and_return(*std)
print(type(std))
print(std,avg)

'(5)Descriptive Analysis2'
firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt_1=('As shown in the histogram, we can organize the data\
      \nto make understanding it easier.\
        \n\nThe data can be studied further, we can calculate\
        \ndifferent variables from the information that will help\
        \nthis study\
        \n\nVariables:\
        \n\nMean: '+str(avg)+ \
        '\n\nStandard Deviation: '+ str(std)+ \
        '\n\nHighest Value: '+str(s)+
        '\n\n\n\n\n')
    
txt = txt_1
        
        
firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
plt.savefig(pp, format='pdf')
plt.clf()





'''AVG IGUALAR A MEAN, CALCULAR DESVIO STANDARD, CALCULARDIST NORMAL'''



'''///////////////////////////////////////////////////////////////////
-------------------Second Graphs----------------------------------
//////////////////////////////////////////////////////////////////////'''


print(std)
if s > avg*2:
    print('Seguir estudio')
    
    '(6)Descriptive Analysis2'
    firstPage = plt.figure(figsize=(12.69,7.27))
    firstPage.clf()
    txt_1=('If we look at the histogram one more time, its clear that\
          \nthe highes value does not help this statistical analysis\
        \nand it stands as a problem because it si not epresentative of \
        \nthe population for being and isolated result\
        \n\nAs we dont expect it to repeat again in the future we will\
        \nnormalize the value, by bringing it close to the Mean\
        \nAn histogram in the next page will show graphically why this\
        \nextreme value is not representative the population\
        \n\n\n\n\n\n\n')
        
    txt = txt_1
            
            
    firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
    plt.savefig(pp, format='pdf')
    plt.clf()

    
    '''----------------Normal Dist.--------------------'''
    '''----------------Plotting 1--------------------'''
    '''AVG IGUALAR A MEAN, CALCULAR DESVIO STANDARD, CALCULARDIST NORMAL'''
    
    h = pandas.read_sql('SELECT TOTAL FROM main_statistics order by Total',connection)
    #connection.close();
    fit = stats.norm.pdf(h, avg, std)  #this is a fitting indeed
    
    pl.plot(h,fit,'-o')
    plt.tick_params(labelleft=False) 
    pl.hist(h,density=True)      #use this to draw histogram of your data
    plt.savefig(pp, format='pdf')
    plt.clf()
    pl.show()                   #use may also need add this 
    
    #h.sort()
    hmean = np.mean(h)
    hstd = np.std(h)
    pdf = stats.norm.pdf(h, hmean, hstd)
    #plt.plot(h, pdf) # including h here is crucial
    #plt.savefig(pp, format='pdf')
    #plt.clf()
    
    #connection.close();
    cursor= connection.cursor();
    
    
    '''----------------Ingresar pagina de por que seguimos--------------------'''
    
    
    
    '''----------------Extract Max Value--------------------'''
    test= """UPDATE main_statistics Set Total= %s ORDER BY Total Desc LIMIT 1 """ \
        %(avg);
    cursor.execute(test);  
    connection.commit();
    s = "SELECT MAX(Total) FROM main_statistics"
    cursor.execute(s)
    s = cursor.fetchone()
    #s = pandas.read_sql("SELECT MAX(Total) FROM main_statistics", connection)
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(s))
    s = [int(i) for i in newstr.split()]
        
    s= print_and_return(*s)
    print(type(s))
    print(s)
    
    
    '''----------------AVG/MEAN--------------------'''
    
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
    
    
    '''----------------Standard Dev.--------------------'''
    std = "SELECT STD(Total) FROM main_statistics"
    cursor.execute(std)
    std = cursor.fetchone()
    #s = pandas.read_sql("SELECT MAX(Total) FROM main_statistics", connection)
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(std))
    std = [int(i) for i in newstr.split()]
    print(type(std))       
    std= print_and_return(*std)
    print(type(std))
    print(std,avg)
    
    '(5)Descriptive Analysis2'
    firstPage = plt.figure(figsize=(12.69,7.27))
    firstPage.clf()
    txt_1=('After normalizing the extreme values, we can calculate the\
           \nvariables again and see how the data is shown in the new plot.\
            \n\nVariables:\
            \n\nMean: '+str(avg)+ \
            '\n\nStandard Deviation: '+ str(std)+ \
            '\n\nHighest Value: '+str(s)+
            '\n\nComparing this new values with the ones we got earlier might not seem much\
            \nbut if we look at the next histogram, the result will be much more\
            \nhomogeneous.\
            \n\n\n\n\n')
        
    txt = txt_1
            
            
    firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
    plt.savefig(pp, format='pdf')
    plt.clf()

    
    
    '''----------------Normal Dist.--------------------'''
    '''----------------Plotting 2--------------------'''
    
    '''AVG IGUALAR A MEAN, CALCULAR DESVIO STANDARD, CALCULARDIST NORMAL'''
    h = pandas.read_sql('SELECT TOTAL FROM main_statistics order by Total',connection)
    #connection.close();
    plt.figtext(0.5, 0.01, "Normal Distribution", ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    fit = stats.norm.pdf(h, avg, std)  #this is a fitting indeed
    
    pl.plot(h,fit,'--o')
    pl.hist(h,density=True)      #use this to draw histogram of your data
    #pl.axis('off')
    plt.tick_params(labelleft=False) 
    plt.savefig(pp, format='pdf')
    plt.clf()

    pl.show()                   #use may also need add this 
    
    #h.sort()
    ''' Only line'''
    hmezan = np.mean(h)
    hstd = np.std(h)
    pdf = stats.norm.pdf(h, hmean, hstd)
    plt.figtext(0.5, 0.01, "Normal Distribution", ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    #plt.plot(h, pdf) 
    #plt.savefig(pp, format='pdf')
    #plt.clf()
    pl.show()    
    
    
    '''----------------Kurtosis--------------------'''
    d_8 = pandas.read_sql("SELECT Total FROM main_statistics ", connection)        
    kur= kurtosis(d_8)
    kur= print_and_return(*kur)
    kur=float("{:.2f}".format(kur))
    if kur < 0:
        kur_status='Platykurtic'
        kur_sent='the kurtosis is flatter (less peaked) when compared with the normal distribution.\
            \nThe lower the value, the less we can rely on the frequency distribution variables.'
    elif kur == 0:
        kur_status='Mesokurtic'
        kur_sent='the kurtosis is the same as the normal distribution'
    elif kur > 0:
        kur_status='Leptokurtic'
        kur_sent='the kurtosis has a higher peak and taller (i.e. fatter and heavy) tails than a normal distribution'
        
    '(7)Descriptive Analysis3'
    firstPage = plt.figure(figsize=(12.69,7.27))
    firstPage.clf()
    txt_1=('Symmetry \
           \n\nIf we compare this f(x) with Gauss Bell curve, our data will be skewed to the left.\
          \nThis means that from all the frequency series, the mean should be the most suited for this study.\
        \n\nKurtosis\
        \n\nThe Kurtosis we get from the data is '+str(kur)+' this means that the curve is '+str(kur_status)+'.\
            \nWhen we talk about a '+kur_status+' curve, it meants that \n '+kur_sent+'\
            \n\n\n\n\n')
        
    txt = txt_1
            
            
    firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
    plt.savefig(pp, format='pdf')
    plt.clf()
elif s <avg*2 or s==avg*2:
    print('No hacer estudio3')
    s = "SELECT MAX(Total) FROM main_statistics"
    cursor.execute(s)
    s = cursor.fetchone()
    #s = pandas.read_sql("SELECT MAX(Total) FROM main_statistics", connection)
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(s))
    s = [int(i) for i in newstr.split()]
        
    s= print_and_return(*s)
    print(type(s))
    print(s)
    
    
    '''----------------AVG/MEAN--------------------'''
    
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
    
    
    '''----------------Standard Dev.--------------------'''
    std = "SELECT STD(Total) FROM main_statistics"
    cursor.execute(std)
    std = cursor.fetchone()
    #s = pandas.read_sql("SELECT MAX(Total) FROM main_statistics", connection)
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(std))
    std = [int(i) for i in newstr.split()]
    print(type(std))       
    std= print_and_return(*std)
    print(type(std))
    print(std,avg)
    
    '(5)Descriptive Analysis2'
    firstPage = plt.figure(figsize=(12.69,7.27))
    firstPage.clf()
    txt_1=(' COMPLETAR')
        
    txt = txt_1
            
            
    firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
    plt.savefig(pp, format='pdf')
    plt.clf()

    
    
    '''----------------Normal Dist.--------------------'''
    '''----------------Plotting 2--------------------'''
    
    '''AVG IGUALAR A MEAN, CALCULAR DESVIO STANDARD, CALCULARDIST NORMAL'''
    h = pandas.read_sql('SELECT TOTAL FROM main_statistics order by Total',connection)
    #connection.close();
    plt.figtext(0.5, 0.01, "Normal Distribution", ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    fit = stats.norm.pdf(h, avg, std)  #this is a fitting indeed
    
    pl.plot(h,fit,'--o')
    pl.hist(h,density=True)      #use this to draw histogram of your data
    #pl.axis('off')
    plt.tick_params(labelleft=False) 
    plt.savefig(pp, format='pdf')
    plt.clf()

    pl.show()                   #use may also need add this 
    
    #h.sort()
    ''' Only line'''
    hmezan = np.mean(h)
    hstd = np.std(h)
    pdf = stats.norm.pdf(h, hmean, hstd)
    plt.figtext(0.5, 0.01, "Normal Distribution", ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    #plt.plot(h, pdf) 
    #plt.savefig(pp, format='pdf')
    #plt.clf()
    pl.show()    
    
    
    '''----------------Kurtosis--------------------'''
    d_8 = pandas.read_sql("SELECT Total FROM main_statistics ", connection)        
    kur= kurtosis(d_8)
    kur= print_and_return(*kur)
    kur=float("{:.2f}".format(kur))
    if kur < 0:
        kur_status='Platykurtic'
        kur_sent='the kurtosis is flatter (less peaked) when compared with the normal distribution.\
            \nThe lower the value, the less we can rely on the frequency distribution variables.'
    elif kur == 0:
        kur_status='Mesokurtic'
        kur_sent='the kurtosis is the same as the normal distribution'
    elif kur > 0:
        kur_status='Leptokurtic'
        kur_sent='the kurtosis has a higher peak and taller (i.e. fatter and heavy) tails than a normal distribution'
        
    '(7)Descriptive Analysis3'
    firstPage = plt.figure(figsize=(12.69,7.27))
    firstPage.clf()
    txt_1=('Symmetry \
           \n\nIf we compare this f(x) with Gauss Bell curve, our data will be skewed to the left.\
          \nThis means that from all the frequency series, the mean should be the most suited for this study.\
        \n\nKurtosis\
        \n\nThe Kurtosis we get from the data is '+str(kur)+' this means that the curve is '+str(kur_status)+'.\
            \nWhen we talk about a '+kur_status+' curve, it meants that \n '+kur_sent+'\
            \n\n\n\n\n')
        
    txt = txt_1
            
            
    firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
    plt.savefig(pp, format='pdf')
    plt.clf()
else:
    print('No hacer estudio2')
''' 
(5)
Regression
//////////////////////////////////////////////////////////////////////////////////
'''    

'(5)Regression and tendency'
firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt_1=('Regression\
       \n\nIn the next page there is a plot explaining the relation between the variable\
          \ntime and the total of crimes in that month.\
        \n\nThis is important not only to decision making, but it also help ups to forecast\
        \nthe near future. The tendency we can see is the line that connects these variables and\
        \n\n\n\n\n\n\n\n\n\n\n\n')
    
txt = txt_1
        
        
firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=19, ha="left")
plt.savefig(pp, format='pdf')
plt.clf()






bro = [1,2,3,4,5,6,7,8,9,10,11,12]
import seaborn as sns; sns.set_theme(color_codes=True)
tips = pandas.read_sql('SELECT * FROM main_statistics order by Month',connection)
plt.figtext(0.5, 0.01, "Regression & Tendency in the last 12 Months", ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
ax = sns.regplot(x=bro, y='Total', data=tips)
plt.savefig(pp, format='pdf')
plt.clf()


'''
(n)
Tools used
//////////////////////////////////////////////////////////////////////////////////
'''    

'(n)Tools usedy'
firstPage = plt.figure(figsize=(12.69,7.27))
firstPage.clf()
txt_1=('Tools Used in this project\
      \n\n-Python\n--Python Libraries\n----Pymysql\n----Seaborn\n----Matplotlib\n----Pandas\n----Numpy\
          \n----Scipy.stats\n----Random\n----Time\n----Pdfpages\
    \n\n-MySql\n\n-Aws Cloud Services\n\n-Jupyter Notebook\
        \n\n-Knowledge Required\n--SQL Query\n--ETL\n--Statistics\n--Programming')
                      
txt = txt_1
        
        
firstPage.text(0.1,0.1,txt, transform=firstPage.transFigure, size=16, ha="left")
plt.savefig(pp, format='pdf')
plt.clf()

connection.close();  
pp.close()

