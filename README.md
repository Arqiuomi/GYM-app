# GYM-app
This is an app for smb, who wants to organize his training plan
## Main folders 
There is **MVC** pattern are used.
### module
This is the folder with main functional of the app.

| class                 | file                        | description                                                                                                                     |  
|-----------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| DB                    | work_with_DB.py             | This is the class for working with data.                                                                                        |
| User, User_char       | class_about_user.py         | Create a user profile and virtual avatar of the user.                                                                           |
| Plan, Train, Exercise | train.py, class_exercise.py | Descript the behaviour of the app, while user are training.<br/> Classes implement the following user's personal training plan. |

### controller 
This is the folder with common logical chains, which are used
during the program realisation.
### view 
This is the folder with program interface. We used KiVy GUI 
to create the general view of the app. 
You  can look for more information and principals of work on their 
official web-site: 
[Kivy framework](https://kivy.org/doc/stable/api-kivy.html).

![](Schwarz.jpeg)

