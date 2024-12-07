# `pages` Folder

Overview: 
The pages folder contains the core components of NUConnects routing structure. Each file in this folder represents a page of the application, and the folder hierarchy mirrors the URL paths of your application. Each Subpage is placed under the persona. The buttons of the home persona pages route to the seperate pages that a specific to each user persona. Each page allows the user to interact with the databse specific to their experience. 

The following is the list of pages that are available to each user:

Pages accessible to Dao (student):
00_Student_Home
- 02_Profile
- 01_View_Programs
- 23_View_All_Post
- 03_Application_Stat

Pages accessible to Cooper (professor):
10_Professor_Home.py
- 16_Uni_All_Programs
- 02_Profile
- 03_Application_Stat

Pages accessible to Jennie (the other university Admin):
15_University_Home
- 23_View_All_Post
- 21_Manage_My_Programs
- View_All_Schools.py
- 18_Uni_All_Users
- 22_View_All_Roles

Pages accessible to Lisa (the NEU Admin)
20_Admin_Home
- 23_View_All_Post
- 16_Uni_All_Programs
- View_All_Schools
- 8_Uni_All_Users
- 22_View_All_Roles