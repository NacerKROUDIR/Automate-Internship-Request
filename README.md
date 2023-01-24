# How I Automated 🤖 The Task of Looking for an Internship as Data Scientist
As a data science enthusiast, I found it challenging to keep track of potential internship opportunities and to efficiently reach out to companies. I decided to automate this process by using Google Sheets, Python programming language. This allowed me to efficiently and effectively reach out to companies and increased my chances of finding an internship opportunity. In this Repository, you will find the code I used to set up my system to automate the task of searching for an internship as a data scientist.

## In Google Sheets
The first step in my process was to gather data on potential internship opportunities. I used LinkedIn to search for companies that have data science positions or internships available. I manually collected information such as the company’s name, email address, and the name of the hiring manager. I then added this information to a Google Sheet, which served as my database.

The next step in my process was to generate the emails that would be sent to the companies on my list. To do this, I used the ARRAYFORMULA function in Google Sheets to automatically generate the email subject and body for each company in my database.

The first column in my Google Sheet was the Enterprise column, and the second column was the Contact column which is the Hiring Manager Name. I used these columns to create the email subject and body using the ARRAYFORMULA function to create two new columns, one for the Email Subject and one for the Email Body.

[Screenshot of Example Table with Data](Google Sheet Example Table.png)

The rest of the work is done in the code in this repository in Python programming language. I used [gspread] to import the data from google sheets directly into python and [smtplib] to automate sending the emails

**For more information about this project, including a detailed explanation and demonstration of the code, check out my Medium blog post [How I Automated 🤖 The Task of Looking for an Internship as Data Scientist] where I go over the process step-by-step.**
