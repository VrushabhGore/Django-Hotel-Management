## Project Idea
Hotel Reservation System with chat support and Two-factor authentication functionality.

You can view the app here: http://b239c491.ngrok.io

## Team Members
1. Kabir Singh Mann - Two Factor, Port Forwarding, User profiles and app integration
2. Navin Rai - Reservation System, Database management and app integration
3. Vrushabh Gore -  Hotel App, Chat app, Deployment server and app integration, Port Forwarding.

## Date 15/03/2019

1. Created a new README File.

## Date 19/03/2019

1. Django Project Created Named Hotel django_hotel_management

2. Django App Added to the Project named hotel

3. Created 2 HTML pages with bootstrap and used blocked coding to show how things will look once they are done.

4. Used a migration to create the basic auth_user table and created an Admin Panel

5. Unable to write database in the DateField through shell will check with Carl Later.

## Date 24/03/2019

1. Login page created.

2. UserProfile Added to the Project named hotel.

3. Model created for users.

## Date 26/03/2019

1. Connected Database with reservation

2. Created a Authentication Application to seperate Authentication and Hotel App(This will help us make changes to Login and Registration when we add 2 Factor Authentication)

3. Created Registration Form Using Django UserCreationForm

4. Added Crispy-Forms for styling the UserCreationForm

5. Everyone Registered using the User Creation Form would have User Status

6. Staff and Admin Status can be added from the Admin Panel.

7. Profile Page added which takes images and displays user name and email ID

8. Signals used to automatically create a new Profile for a newly registered user.

## Date 30/03/2019

1. Tunneling complete

2. ngrok portforwarding active

## Date 2/04/2019

1. Added a ChatApp which will use Django Channel

2. Created a routing pattern for the chat app.

3. Implemented WebSockets to send and recieve connections

4. Created django layers over ReDIS server for backend purpose

5. Implemented AsyncWebsocket instead of Syncronous connection.

## Date 07/04/2019

1. Two factor Authentication added

2. Token Generator and Yubikey component added.

3. Two factor added in admin panel.

4. Google Authenticator support added.

## Date 25/04/2019
1. Integration and merging of 2FA complete with chat app.

2. Reservation System Complete.

## Date 26/04/2019
1. Integration of all the apps and the reservation system

2. Merged into Master.

3. Heat template added for production server deployment.

4. README.md merged and updated with markdown format.

5. Database integration.

6. Ngrok build and production server running.

# Tools

- Using SQL Database for development
- Using SQL Database for Production

# References
1. [Bootstrap Starter Template](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
2. [Templating and Rendering](https://docs.djangoproject.com/en/2.1/topics/templates/)
3. [Admin Interface](https://www.tutorialspoint.com/django/django_admin_interface.htm)
4. [Model Creation](https://www.tutorialspoint.com/django/django_models.htm)
5. [Extending Templates from a base](https://www.youtube.com/watch?v=tyFmF_v3z8c)
6. [Form Styling Using Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms)
7. [Registration Form Creation](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/)
8. [Allow only authenticated users to view contents of the app - login_required](https://www.youtube.com/watch?v=fqDTZA5P1EE)
9. [How to Implement a ChatApp Using Django Layers](https://channels.readthedocs.io/en/latest/tutorial/part_1.html)
10. [How to Build a Functioning Login Page in ONE Video! (Django Tutorial) | Part 8](https://www.youtube.com/watch?v=p_n7g6tVloU)
11. [Django Login/Logout Tutorial (Part 1)](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/)
12. [Extending Templates from a base](https://www.youtube.com/watch?v=tyFmF_v3z8c)
13. [Django local host accessible from public domain using Ngrock](https://www.youtube.com/watch?v=GCIW-2RTcFY)
14. [Set up and Installation](https://dashboard.ngrok.com/get-started)
15. [django-two-factor-auth](https://github.com/Bouke/django-two-factor-auth)
16. [Django Two-Factor Authentication Documentation](https://django-two-factor-auth.readthedocs.io/en/stable/index.html)
17. [Integrating 2 factor authentication into your project](https://www.youtube.com/watch?v=7Z8cDOCH5fM)
18. [Django Forms](https://www.journaldev.com/22424/django-forms)
19. [A SQLite Tutorial with Python](https://stackabuse.com/a-sqlite-tutorial-with-python/)
