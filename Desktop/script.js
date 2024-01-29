function validate()
{
 var x=document.getElementByld("login").value;
 var y=document.getElementByld("pass").value;
 if(x==")
  {
     alert("please fill out login  return false;ID");
  }
 elseif(x!='abc@abc.com')
{
 alert("INVALID login ID");
 return false;
}
if(y==")
{
alert("PLEASE FILL OUT PASSWORD ");
return false;
}
if(x=='abc@abc.com'&& y=='123')
{
  alert("successfully logged in ");
return false;
}
}