///////////////////////////////////////////////////////////////////////////////////////////////

1-This Program

2-Tools used

3-Notes


////////////////////////////////////////////////////////////////////////////////////////////////

1-This Program:
	
	The objective of this program is to analyse the data in a database and 
	visualize the information in a really simple way to understand ir more easily.
	No matter how big the database is, it will get it done. 
	This program is compatible with AWS services such as Redshift or a database set in 
	an EC2 Instance, in case you want to try it you will have to adjust the credentials 
	at the beggining of each program.
	It was also made with the use of visualization tools in mind, such as Spyder IDE or 
	Jupyter Notebook.
	It also saves the analysis in a PDF called 'Crime_report.pdf'.
	
	This program comes in 3 differen variants:

		-Analysis: Only runs the Visual analysis on the database and 
		saves the result on a pdf. 
		It is available as a python script (ideally with a visual IDE such as Spyder)
		and as a Jupyter Notebook.

		-Fill Database and Analysis: There is also the option to fill the database
		before running the visual analysis. This is done with the creation of tendencies 
		in mind. Ex: In Buenos Aires, The most common crime will always be 'Murder'.
		After filling the database it will automatically run the analysis.
		There is no limits to how many rows of data it can create, right now it is set
		to 10.000 Rows.

		-Truncate table: This small script will empty the database so you can try new 
		results with the other parts of the program.


2- Tools Used:

	Python Libraries:
		-Matplotlib and Pdfpages
		-Seaborn
		-Pandas
		-Random
		-Time 
		-Pymysql
		-Numpy

	Programs Used:
		-Jupyter Notebook
		-AWS EC2 Services
		-MYSQL
		-Python EDE (Spyder4)

	Topics Covered:
		-Programming
		-Statistics
		-SQL databases
		-Multiple Queries
		-ETL
		
		
	
3 -Notes:
	-This program also can save each plot in a single PDF.
	-For security reasons, the published program will be config. to work on a localhost database
	instead of my AWS EC2. If you want to see a program working on an AWS Instance please
	check my other project 'Discord Bot'
	