# Logs Analysis
A small project for udacity web-developer course

A project to analyse a databank and extract some useful information


# Requisites of the code
1. Find the 3 most popular article in the databank 

2. Find the most popular authors

3. Which days more than 1% of the requests had an error status

# What is needed to run
 
1. Python version 2 or 3 : https://realpython.com/installing-python/

2. Virtual box, a tool that allows the creation and usage of virtual machines: https://www.virtualbox.org/wiki/Downloads

3. Vagrant, https://www.vagrantup.com/downloads.html

3.1 Once you download the vagrant you will need to configure a virtual machine, download the following link and extract into a file of    your computer: https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip ,after extracting, put the **news.py** of this project in the same file as the others and download https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip and once again extract the **newsdata.sql** to the same file

3.2 Use the comand prompt of your machine to navigate to the file and run the command : **Vagrant up** it will set up the virtual machine to the configuration of the file once its done run **Vagrant ssh** to connect to the virtual machine

3.3 When you connect to the virtual machine, used **cd /vagrant** to acess the folders and then run **psql -d news -f newsdata.sql** to create the database nes in the virtual machine, after created it will automatically enter in database mode so type **\q to leave

3.4 Run the code with **python news.py** it will print the answers both in the screen and in the log.txt


# How to execute

run python news.py when connected to vagrant, the output will be printed both in the comand screen and in a log.txt file that the program create
