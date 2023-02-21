function required()
{
var FName = document.forms["regform"]["FName"].value;
var LName = document.forms["regform"]["LName"].value;
var Gender = document.forms["regform"]["Gender"].value;
var Mobile = document.forms["regform"]["Mobile"].value;
var Email = document.forms["regform"]["Email"].value;
var Password = document.forms["regform"]["Password"].value;

if (FName == "")
{
alert("Enter The First Name");
}

else if (LName == "")
{
alert("Enter The Last Name");
}

else if (Gender == "")
{
alert("Choose Gender ");
}

else if (Mobile == "")
{
alert("Enter the Mobile Number ");
}

else if (Email== "")
{
alert("Enter the Email ");
}

else if (Password == "")
{
alert("Set The Password");
}

else 	
{
alert('Registration Sucessfull...!');
}
}