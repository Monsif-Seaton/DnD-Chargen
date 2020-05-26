# D&D Character sheet platform

In fulfillment of the week 5 CRUD application project

# Contents
* Requirements
* Solution
* Planning
* Architecture
* Testing
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

# Planning
![](http://puu.sh/FOVGe/8809d2b4e9.png)

Initially my risk assesment was fairly simple as shown above. The risks were largely relating to malfunctioning hardware and project time management


![](http://puu.sh/FOVGx/f376462898.png)

After learning more about security concerns and Jenkins I was able to identify and add a few more areas of risk

**trello**

![](https://puu.sh/FOW12/d87f154013.jpg)

The initial scope of my app was a bit different because I assumed a login system rather than this being an app for one. My understanding of the requirements and difficulty of each task was also not perfect because this was made before work on the code of the project had started

![](https://puu.sh/FOW1x/fb566d3ab3.jpg)

The updated design reflects the requirements and is more simple due to knowing the difficulty of tasks and the time constraints

# Architecture

Initial design

![](https://puu.sh/FOVmC/23e70c7dcc.png)

The Characters table was to act as the central link in a chain of tables dependant on each other. I did not include the (at this time planned) users table because it would distract from the design of the main app and because I was on the fence about including a login system at all

final design

![](https://puu.sh/FOVnT/cf4fd1b441.png)

As the timeframe and the technologies to be used became more clear, I changed direction on the design to be a little less complex. The subraces and subclasses were dropped due to the complexity of the logic and amount of data input required to set up the relationships between the tables

**system level design**
![](http://puu.sh/FOVt1/8d0fbcac37.jpg)

The source code for this project was written in Python using the Flask framework. HTML and CSS were used for the front end website. Github was used as the source control platform and Jenkins pulled from this as thr CI server. Builds were deployed to google cloud platform using gunicorn

# Testing
I achieved a 93% testing coverage. The missing 7% is due to a couple of one line debugging functions and a bug in a test for my sheets page that I couldn't resolve. This bug is related to my use of dynamic urls, but tests with the same structure work for other dynamic url pages in the app

![](https://puu.sh/FOVAX/a4d1df3105.png)

# Future improvements
I would like to add a Tools page with a dice roller app that I made the functions for but didn't have time to implement. I would also like to make the character sheet more detailed with subraces, subclasses and skills. Finally, I would like to make the website better looking through use of Flexbox and Bootstrap

# Authors
Monsif Seaton
