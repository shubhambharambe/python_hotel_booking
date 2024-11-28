1) user is able to login and JWT token generated
2) List of hotels we can get through
3) user is able to book the hotel with the help of JWT token
4) user is able to get the booking on basis of booking id
5) user is able to get all of the booking he has booked
6)throttling concept add in your application
7)only super user can see the list of user 
8)only super user can add room for available hotels 
9)Any one can register user to book hotels

======================================>Add readme<===================================================

===============================>add instructions of to start application<============================






1.open (Hotelbook) folder
2.open CMD in this folder 
3.write command cd (booking_app )
4.after that write command(python manage.py createsuperuser)
5.after that you need to add username,email and password for check Django administration(Database)
6.after that  command( python manage.py runserver)
7.you got this type of link http://127.0.0.1:8000/
8.Open your browser and navigate to:

Application: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
Log in to the admin panel using the credentials of the superuser created earlier to view or manage the database tables.


================================>how to use all API's screenshots of postman API<====================





1. Send a POST request to: " http://127.0.0.1:8000/api/token" and send data in json body
     http://127.0.0.1:8000/api/token/refresh for refresh the token

2.In the JSON body, provide the credentials used for the superuser:
 {
    "username":"", 
    "password":""
}

3.The response will include the access token and refresh token:
    "access": "",  
    "refresh": "ex"
The access token is valid for 30 minutes.
The refresh token is valid for 1 day.
4.Use the access token for authenticated API requests by adding it to the Authorization header:
    Key:Authorization: 
    value:Bearer "put token here"
5.Create a Booking:

Endpoint: POST(http://127.0.0.1:8000/api/bookings/{}
{
    "room": 1,
    "start_date": "2024-12-01",
    "end_date": "2024-12-05"
}

6.Fetch Bookings
GET request to /api/mybookings/
(http://127.0.0.1:8000/)
{
    "room": 1,
    "start_date": "2024-12-01",
    "end_date": "2024-12-05"
}
