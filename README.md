# where2charge
Course project for CSE583 Software Development for Data Scientists 

Team members: Arsalan Esmaili, Soheil Keshavarz

Goal: Suggesting reliable charging for EV owners

Components: 

- manager 

- analysis module

- front module

- google api module


## User stories:


- Suzi is an EV owner. She wants to charge her car every morning before
 showing up at work. She wants to use this tool to quickly navigate herself
 to an available charging station in middle of her commute route. 

- Brandon: Brandon is an EV owner who wants to look at different charging stations on the map and review their main attributes of reliability. Specifically, he wants to understand their reviews in just few words.

- Susan: Susan is an EV owner who wants to drive to a shopping mall with a EV charger close to her. She wants to get the best suggestion based on the location she wants to go. 

- Leo: Leo is a researcher who wants to analyse trip information of the users (anonymous), and check differences between travel time and see how travel time would be different based on different attributes and investigate equity.

- Joe is an employee in SDOT. He want to see number of EV trips from each traffic analysis zone (TAZ) to better understand the generated demand. He wants to see a summary and a csv file for trips generated. 

- Dave is the system admin. He wants to communicate with app users. He needs a specific interface where he
can see each user usage, subscription, feedbacks, etc., and send notification to all or a group of users.

- Rob is a hacker. He wants to access location information of users. 
He made a bot to decode admin credentials. 

* The user's data in this app should be encrypted and the location information needs to be masked in
 a more aggregated level.
This will be clearly indicated to users. 
The application should assure users that there is no way for use of their accurate information and all analysis will be used anonymously.
 This is necessary to meet the criteria for data ethics.


## Components:

1. Control logic
- It provides the calculation of the input data for the interface.
- The input is one to multiple origin/destination locations that user specifies, type of plugs and other preferences that user determine.
- Time, distance, and other trip components for the suggested routes.
- It uses user interface, navigation system, database, analysis component
- Side effect: risk of data leakage, crashing risk as it need to handle multiple users, it needs maintenance

2. User interface
- Gets the input from the user and provide the requested task and visualize them. The main goal is to provide user-friendly 
environment for EV riders to be able to benefit from the provided analysis.
- Input: Type of plug, origin/destination locations, and other user preferences for selecting EV charging station
- Output: Visualization of the suggested route and their differences (e.g., review summary, time, distance, etc.)
- It should be connected to the control logic and get instructinos, including map, from it.
- side effects: 

3. navigation system:


4. analysis component


5. request component:
-using OOP, it is a clean way to keep track of each request from the user interface. If we keep each request as an object with user inputs as 
attributes of that object, writing the control logic and handling multiple requests will be simpler.

6. Database


