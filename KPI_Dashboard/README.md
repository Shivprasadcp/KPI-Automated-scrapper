just make sure you have import error : Pandas requires version '2.0.1' or newer of 'xlrd'
if you encounter this error then : pip install --upgrade xlrd



Scheduling with Task Scheduler (Windows)
To schedule your script on Windows using Task Scheduler:

Open Task Scheduler:

Press Windows + R, type taskschd.msc, and hit Enter.
Create a new task:

In the right panel, click Create Task.
General Tab:

Name the task (e.g., KPI Dashboard Script).
Set the task to run whether the user is logged in or not.
Triggers Tab:

Click New to create a trigger.
Choose when you want to run the script (e.g., daily, weekly, at a specific time).
Set the desired schedule (e.g., daily at midnight).
Actions Tab:

Click New, and choose Start a program.
In the "Program/script" field, browse and select python.exe (typically found in C:/Users/yourusername/AppData/Local/Programs/Python/Python311/).
In the "Add arguments (optional)" field, put the path to your script:
text
Copy code
"D:\Pilgrims\KPI_Dashboard\kpi_dashboard.py"
Ensure that the "Start in" field points to the folder where your script is located (e.g., D:\Pilgrims\KPI_Dashboard\).
Conditions and Settings Tabs:

Adjust settings like "Allow task to run on demand" and "Stop the task if it runs longer than..." as needed.
Finish and Save:

Click OK to save the task.
Now, your script will run according to the schedule you set up.