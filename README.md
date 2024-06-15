# Pixel steak

<hr>
Pixel steak - is the restaurant booking application.
It allows customer to browse company news, restaurant menu
and provides functionality to book a table or few.

## Features

- ### Homepage
It introduces user the upcoming events and special offers.
Designed as moving slides with titles and description,
it also allows user to manipulate with slides by clicking on
news list items on the left sidebar.
The site owner can add, delete or edit slides to show,
using administration panel. The website fetch them automatically
from the cloud based data base


- ### Menu
Shows user available dishes, short description and pricing.
Also provides additional information about vegan and spicy
dishes using icons.
The site owner can add, edit or delete categories and dishes
in these categories. The web application show only categories
which have dishes. When adding a new dish, site owner can specify
is it vegan and hot spicy is it.

- ### Booking system
Provides customer the form to fill out and book a table.
Based on for how many people customer books places, the system 
automatically assign available tables. It tries to fit in everyone
and avoid wasting tables at the same time. The system also
checks the other reservations to prevent double booking.
To make booking the user should be registered and logged in.

- ### Responsive design
Using Bootstrap and custom CSS make the web application look good
both on mobile devices and desktop screens.

- ## Admin Features

The admin (super user) of the web site can easily manage it's content directly from the web page.
This features are available to the admin only and not visible for the site users

- ### News section

![image of admin tools at the home page](https://i.ibb.co/K2RNvHw/2024-06-15-18-24-09.png)
By clicking on the arrow at the right part of the News banners an admin can open the management panel.
It's simple and pretty straight-forward, allowing to add, edit, and delete news from the home page


- ### Menu section

![image of admin panel at the menu page](https://i.ibb.co/y5N0sY6/2024-06-15-18-28-22.png)

'Admin panel' allows the admin to add new categories to the menu and new dishes (items). 
The bottom part represents the empty categories, that are not visible for the site users.
The admin can delete them by clicking on the cross sign next to each category

![image of admin tools at the menu page](https://i.ibb.co/23LT9R0/2024-06-15-18-31-17.png)

The other admin tools are located nest to the corresponding elements. For example 'Rename' and
'Delete' buttons bellow each category name, or 'Edit' and 'Delete' buttons on each card with a dish.

By clicking on these buttons the admin can edit and delete items from the menu.

- ### Bookings section

The navigation panel provides 'My bookings' menu item for the site users, where they can book a table, 
view their upcoming bookings and cancel them.
But if the admin is logged in, 'Bookings' menu item will be there instead of 'My bookings', providing the
admin with a table, containing all the bookings made by users.

![image of bookings table](https://i.ibb.co/FHk7NSp/2024-06-15-18-34-47.png)

From this page admin can create a new booking (e.g. the customer contacting the admin by the phone) or delete
the existing one by clicking on the button with a cross in the last column. 

For the better user experience all the past bookings are dimmed. 

If the user cancels his booking it will be represented in the table by marking its background red, changing the
reference number to the text 'CANCELLED' and revealing booked tables. This bright marking is required to show the admin, 
that the booking has been cancelled, so the restaurant staff can perform the required actions. Therefore, if the
cancelled booking is old, it won't have the red background. 

## Testing

### Code validation
<hr>

- ### HTML
For HTML validation I have used [W3C Validator](https://validator.w3.org/)



| Result for page                                                                                  | Errors           |
|--------------------------------------------------------------------------------------------------|------------------|
| [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpixel-steak-5f7f6955f42e.herokuapp.com%2F) | No errors        |
| [Menu page](https://pixel-steak-5f7f6955f42e.herokuapp.com/menu/)                                | Error in href attribute (cannot contain spaces). The links are for the same page, so it works as expected.
| [Booking](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpixel-steak-5f7f6955f42e.herokuapp.com%2Fbooking%2Fall%2F) | No errors. But this page is not visible for unregistered users
| [Sign Up](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpixel-steak-5f7f6955f42e.herokuapp.com%2Faccounts%2Fsignup%2F) | No errors |
| [Log In](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpixel-steak-5f7f6955f42e.herokuapp.com%2Faccounts%2Flogin%2F) | No errors |

- ### CSS
For CSS valiadtion I have used [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

No errors found
[Result](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpixel-steak-5f7f6955f42e.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)


- ### Python
All python files passed CI Python Linter with no issues.

<hr>

## Manual Testing

<hr>

### Home page

- user role

| Action                                                      | Before                                | After                                              | Result  |
|-------------------------------------------------------------|---------------------------------------|----------------------------------------------------|---------|
| Click on logo                                               | Any page of website                   | Homepage renders                                   | Test Success |
| Click on 'Home' at the navbar                               | Any page of website                   | Homepage renders                                   | Test Success |
| Hover over the news headings at the left part of the page   | Grey background                       | Brown background                                   | Test Success |
| Click the news heading at the left part of the page         | News banners change change each other | The banner with the same heading and image appears | Test Success |
| Click on 'My bookings' at the navbar (unregistered)         | Any page of website                   | Sign Up page renders                               | Test Success |

- admin role

| Action                                                   | Before                           | After                                                            | Result  |
|----------------------------------------------------------|----------------------------------|------------------------------------------------------------------|---------|
| Click on the arrow at the right part of the news heading | No admin tools                   | Appears collapsed admin tool pannel below                        | Test Success |
| Hover on 'Add New' button                                | White background and brown text  | Brown background and wihte text                                  | Test Success |
| Hover on 'Edit' button                                   | White background and brown text  | Brown background and wihte text                                  | Test Success |
| Hover on 'Delete' button                                 | White background and brown text  | Brown background and wihte text                                  | Test Success |
| Click on 'Add New' button                                | Home page rendered               | Add news page rendered with the form to fill                     | Test Success |
| Click on 'Back' button                                   | Add news page rendered           | Homepage renders, no new records in database                     | Test Success |
| Click on 'Add' button ('title' isn't filled)             | Add news page rendered           | Notification shows up that the field should not be empty         | Test Success |
| Click on 'Add' button ('text' isn't filled)              | Add news page rendered           | Notification shows up that the field should not be empty         | Test Success |
| Click on 'Add' button ('image' isn't filled)             | Add news page rendered           | Homepage renders with a freshly added news and default image     | Test Success |
| Click on 'Edit' button                                   | Home page rendered               | Edit news page rendered with the form to fill and prefilled data | Test Success |
| Click on 'Back' button                                   | Edit news page rendered          | Homepage renders, no new records in database                     | Test Success |
| Click on 'Save' button                                   | Edit news page rendered          | Homepage renders, the edited news has been updated               | Test Success |
| Click on 'Delete' button                                 | Home page rendered with the news | The deleted news disappeared frmom the homepage                  | Test Success |


### Menu page

- user role

|  Action                                                   | Before                                | After                                              | Result  |
|-----------------------------------------------------------|---------------------------------------|----------------------------------------------------|---------|
| Click on 'Menu' at the navbar                             | Any page of website                   | Menu page renders                                  | Test Success |
| Hover over the news headings at the left part of the page | Grey background                       | Brown background                                   | Test Success |
| Click the menu categories at the left part of the page    | Any location of the page              | The page scrolls to the clicked category           | Test Success |

- admin role

| Action                                                                      | Before                          | After                                                                             | Result  |
|-----------------------------------------------------------------------------|---------------------------------|-----------------------------------------------------------------------------------|---------|
| Hover on 'Add category' button on the admin panel                           | White background and brown text | Brown background and wihte text                                                   | Test Success |
| Hover on 'Add item' button on the admin panel                               | White background and brown text | Brown background and wihte text                                                   | Test Success |
| Click on 'Add category' button on the admin panel                           | Menu page rendered              | Add new category page renders                                                     | Test Success |
| Click on 'Back' button at the bottom of the page                            | Add new category page rendered  | Menu page renders, no new records to the database have been made                  | Test Success |
| Click on 'Add category' button with 'Name' empty                            | Add new category page rendered  | Notification shows up that the field is required                                  | Test Success |
| Click on 'Add category' button with 'Name' filled                           | Add new category page rendered  | Menu page renders, the new category is visible only in admin pannel as it's empty | Test Success |
| Click on 'Add item' button on the admin panel                        | Menu page rendered   | Add new dish page renders with the form to fill | Test Success |
| Click on 'Back' button at the bottom of the page                            | Add new dish page rendered  | Menu page renders, no new records to the database have been made                  | Test Success |
| Click on 'Add' button with the empty required field                           | Add new dish page rendered  | The page scrolls to the empty field                  | Test Success |
| Click on 'Add' button with the form filled correct                          | Add new dish page rendered  | The menu page renders with a new dish added                  | Test Success |
| Hover on 'Rename' button at the bottom of the category name                 | White background and brown text | Brown background and wihte text                                                   | Test Success |
| Click on 'Rename' button at the bottom of the category name                 | Menu page rendered              | Rename the category page renders with the prefilled name                          |Test Success |
| Click on 'Back' button at the bottom of the rename page                     | Rename category page rendered   | Menu page renders, no changes to the database have been made                      | Test Success |
| Click on 'Confirm' button at the bottom of the rename page                  | Rename category page rendered   | Menu page renders, the name of the category has been updated                      | Test Success |
| Hover on 'Delete' button at the bottom of the category name                 | White background and brown text | Brown background and wihte text                                                   | Test Success |
| Click on 'Delete' button at the bottom of the category name                 | Menu page is rendered           | The category disappears from the page                                             | Test Success |
| Hover on 'Edit' button at the bottom of the menu item                       | White background and brown text | Brown background and wihte text                                                   | Test Success |
| Click on 'Edit' button at the bottom of the menu item                       | Menu page rendered              | Edit item page renders with the prefilled form                                    | Test Success |
| Click on 'Cancel' button at the bottom of the page                          | Edit item page rendered         | Menu page renders, no changes to the database have been made                      | Test Success |
| Click on 'Save' button                                                      | Edit item page rendered         | Menu page renders, the dish from the menu has been updated                        | Test Success |
| Hover on 'Delete' button at the bottom of the menu item                     | White background and brown text | Brown background and wihte text                                                   | Test Success |
| Click on 'Delete' button at the bottom of the menu item                     | Menu page rendered              | The dish disappears from the menu                                                 | Test Success |
| Click on the cross sign after the category name in Empty categories section | Menu page rendered              | The empty category disappears from the list                                       |


### My Bookings page

- user role

| Action                                                         | Before                                | After                                                                  | Result  |
|----------------------------------------------------------------|---------------------------------------|------------------------------------------------------------------------|---------|
| Click on 'My bookings' at the navbar (loged in as a user)      | Any page of website                   | Booking page renders with booking form and history                     | Test Success |
| Click on 'Book table' button without filling required fields   | Book a table page rendered | Notification appears which field should be filled                      | Test Success |
| Click on 'Book table' button with the form filled correctly    | Book a table page rendered | Booking confirmation page renders                                      | Test Success |
| Click on Ref.number of the booking in history section          | Book a table page rendered | Booking details page renders                                           | Test Success |
| Hover on 'Back to booking' button at the bottom of the page    | White background and brown text | Brown background and wihte text                                        | Test Success |
| Click on 'Back to booking' button at the bottom of the page    | Booking details page rendered              | Book a table page renders                                              | Test Success |
| Click on 'Cancel Booking' button at the right part of the page | Booking details page rendered              | Notification appearts that the field is required                       | Test Success |
| Click on 'Cancel Booking' button with the last name filled     | Booking details page rendered              | Book a table page renders, the booking becomes cancelled (not deleted) | Test Success |

- admin role

| Action                                                       | Before                     | After                                                       | Result  |
|--------------------------------------------------------------|----------------------------|-------------------------------------------------------------|---------|
| Click on 'Bookings' at the navbar                            | Any page of website        | Booking page renders with the all restaurant bookings       | Test Success |
| Click on 'Create New' button at the top of the table         | Bookings page rendered     | Book a table page renders with the booking form and history | Test Success |
| Click on 'Book table' button without filling required fields | Book a table page rendered | Notification appears which field should be filled           | Test Success |
| Click on 'Book table' button with the form filled correctly  | Book a table page rendered | Booking confirmation page appears                           | Test Success |
| Click on 'X' button in the last collumn                      | Bookings page rendered  | The booking disappears                                      | Test Success |



## Deployment

<hr>

### ElephantSQL Database

For the database I have used [ElephantSQL](https://www.elephantsql.com/) cloud service.
It uses PostgreSQL 13.12 version

### Cloudinary media hosting
For images I have used [Cloudinary](https://cloudinary.com/) which provides cloud based sollution

### Heroku Deployment
The web application was deployed on Heroku, service providing cloud based server for the web-application running.
Deployment steps are as follows, after account setup:

- Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
- From the new app Settings, click Reveal Config Vars, and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `CLOUDINARY_URL` | user's own value |


Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

Connect the git repository to Heroku and deploy from branch.

## Improvement

<hr>
The project represents basic functionality however the structure
allows to scale it dramatically and add more features

- ### Booking from the news slides
On the homepage the button book a table can be placed on each
slide and redirect user to the booking page with the date filled
already. 

- ### Menu sorting and filters
The menu structure allows to add filters (e.g. "vegan only"), and
order by feature. It also can add special styling to highlight 
price drops

- ### Booking searching system for admin
In case of multiple bookings, adding a search bar allowing to find the booking using reference number, last name or
phone number will be a good idea, allowing finding of the booking easy and fast.
