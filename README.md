# Introduction

The aim of this project is the creation of a modular Internet of Things (IoT) system that enables an interface between DIY IoT devices and consumer grade products such as Google Home or Amazon Alexa. The end software product will be focused on household tasks and behaviors, with functionality resembling a combination of IFTTT (used for interacting different web services) and Tasker (used for automating actions on a phone). Currently, most solutions to this problem function only with off-the-shelf products. This project seeks to allow users to use both off-the-shelf products and DIY solutions seamlessly. The program OpenHAB aligns most closely with this project’s end objectives, but functions using data pipelines instead of event driven actions.

I became interested in this area while working on an Honors Contract where I developed in internet connected Door Sensor. This thesis will serve as a continuation and expansion of that project. I am interested in this topic because it revolves around the interface between Software Engineering and Electrical Engineering. This project will demonstrate my programming capabilities and electrical systems understanding in a useful package, serving as a capstone for the focus areas that are not directly under my major or my diploma. 

The overall goal for this project is the design and production of a number of IoT PCB components and a modular software system that integrates them with off-the-shelf, consumer-available IoT products. Users will be able to integrate their own components with the software using a simple user interface. The components will then be able to be utilized by configuring event-driven actions with a web-based GUI. Examples of events include time of day, Google Home/Amazon Alexa voice commands, and open/closing of doors.

Modules to be created:
* Door Open/Close Sensor (already developed but revising is necessary)
* IR blaster/receiver - Send IR signals to TV (with ability to record and reproduce remote signals)
* HDMI CEC adapter - Detect HDMI CEC signals and interface with IR blaster to add CEC functionality to older TVs)
* Digital Thermostat
* Light Sensor (under consideration)
* Motion Sensor (under consideration)
* Vehicle Key Fob signal blaster/receiver (under consideration)
		
Core features of the software will include:
* Ability to utilize and integrate all created PCB modules
* Ability to interface modules together to create useful actions
* Ability to add DIY modules with an easy to use interface
* Interface with Google Home
* Interface with Philips Hue

The end product should be cheap (compared to other smart home solutions) and easy to set up and use. Experienced users could create their own PCBs and then integrate them into the system seamlessly.

Resources will be needed in order to ensure completion of the project. The modules will require frequent use of the PCB mill in the Peralta Labs.  I have experience developing and printing PCBs, and the lab manager has granted me after hours access, as well as training for the mill. This will allow me to print boards on my own schedule, as my design necessitates. Additionally, the boards will require electrical components and the lab has a large supply of free parts (e.g. resistors, capacitors, regulators), allowing me to prototype cheaply and develop rapidly. Git and Github will be used for version control for the PCB files and software. Files will be checked in routinely to keep the repository up to date.

This project will require understanding of both software and electrical engineering, as well as IoT systems. As such, the director for this project is from the Software department, and the second committee member is from the Engineering department with a background in IoT. 

Because this is a project-based thesis, the end objective is a report on what I will have accomplished, not what others have done. As such, there will not be a strict requirement for citations. This is not to say that I will not be performing research, it will just be focused on my own work. Technical articles will be cited as is appropriate, although the focus of research will be on market research and comparison.

Meetings will be conducted once per week ‒ more often if necessary ‒ starting at beginning of the Fall 2017 semester. Meetings will be used for conceptual guidance and progress reports. In advance for each meeting, I will prepare the necessary things I wish to talk about.

The first semester of work will be mainly focused on PCB module development. Creating functional boards is a prerequisite for integrating them together. The second semester will focus on software design and integration with the first semester’s work. Schedules for both semesters are found below.


## Semester 1 - R&D and PCB Modules
|       Week          |            Task            
| ------------------- | --------------------------
Week 01 \| 2017-08-13 | Component research and initial planning
Week 02 \| 2017-08-20 | Complete work on Door Sensing PCB
Week 03 \| 2017-08-27 | Develop IR blaster/receiver PCB
Week 04 \| 2017-09-03 | Develop IR blaster/receiver PCB
Week 05 \| 2017-09-10 | Develop HDMI CEC PCB
Week 06 \| 2017-09-17 | Develop HDMI CEC PCB
Week 07 \| 2017-09-24 | Develop HDMI CEC PCB
Week 08 \| 2017-10-01 | Basic integration of HDMI and IR modules
Week 09 \| 2017-10-08 | Basic integration of HDMI and IR modules
Week 10 \| 2017-10-15 | Develop Thermometer PCB
Week 11 \| 2017-10-22 | Develop Thermometer PCB
Week 12 \| 2017-10-29 | Develop Thermometer PCB
Week 13 \| 2017-11-05 | Develop Thermometer PCB
Week 14 \| 2017-11-12 | Add ability to control single module with Google Home
Week 15 \| 2017-11-19 | Add ability to control Philips Hue with command line
Week 16 \| 2017-11-26 | Link module to Philips Hue for testing
Week 17 \| 2017-12-03 | Refinement of current work and preparation for 2nd semester. Continues through winter break

## Semester 2 - Integration and Software Design
|       Week          |            Task            
| ------------------- | --------------------------
Week 01 \| 2018-01-07 | Component research and initial planning
Week 02 \| 2018-01-14 | Local module database (list of modules attached to network)
Week 03 \| 2018-01-21 | Viewing status of modules attached to network
Week 04 \| 2018-01-28 | Event handling and tasks
Week 05 \| 2018-02-04 | Event handling and tasks
Week 06 \| 2018-02-11 | Integration with Philips Hue
Week 07 \| 2018-02-18 | Integration with Google Home
Week 08 \| 2018-02-25 | User interface
Week 09 \| 2018-03-04 | User interface refinement
Week 10 \| 2018-03-11 | Module PCB refinement
Week 11 \| 2018-03-18 | Create Report
Week 12 \| 2018-03-25 | Create Report
Week 13 \| 2018-04-01 | Thesis Defense
Week 14 \| 2018-04-08 | Revising of Report
Week 15 \| 2018-04-15 | Final submission due April 20 (signed signature title page, abstract, and digital submission)


