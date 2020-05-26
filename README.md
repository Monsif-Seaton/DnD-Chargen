# D&D Character sheet platform

In fulfillment of the week 5 CRUD application project

# Contents
* Requirements
* Solution
* Architecture
* Testing
* Planning
* Future Improvements

# Requirements
To create a CRUD application of our choice that uses the technologies and methods we have learned up to this point namely:
*A Kanban board
*A relational database to store at least two tables persistently and a model of their relationship
*Clear documentation and a risk assesment
*A python based CRUD application made using best practices such as TDD
*Test suites and automated tests for the application. Must have a high coverage with consistent reports and evidence
*A functioning front end
*A version control system using the Feature-Branch model
*Code built through a CI server and deployed to a cloud based VM

**Solution**
I settled on making a simple d&d character sheet platform that allows the user to create, read, update and delete characters based on the d&d 5E ruleset. It will also have an admin function to allow for the dungeon master to view the character sheets of their players for the purpose of session planning

# Architecture
Initial design
![erd1](https://puu.sh/FOVmC/23e70c7dcc.png)
I did not include the (at this time planned) users table because it would distract from the design of the main app and because I was on the fence about including a login system at all

final design
![erd2](https://puu.sh/FOVnT/cf4fd1b441.png)
As the timeframe and the technologies to be used became more clear, I changed direction on the design to be a little less complex. The subraces and subclasses were dropped due to the complexity of the logic and amount of data input required to set up the relationships between the tables

**system level design**
![system level pic](http://puu.sh/FOVt1/8d0fbcac37.jpg)
The source code for this project was written in Python using the Flask framework. HTML and CSS were used 

# Testing
I achieved a 93% testing coverage. The missing 7% is due to a couple of debugging functions and a bug in a test for my sheets page that I couldn't resolve
[insert pic]

# Planning
initial
[insert pic]
discuss
final
[pic]
discuss


# Future improvements
discuss

# Authors
Monsif Seaton
