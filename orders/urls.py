<!DOCKTYPE html>
<html><head> 
    <title> {{restaurant_name}} </title>
    <style> 
     body {font-family: Arial, sans-serif; text-align: center; color:black;}
     h1{color: red; margin-top: 50px}
     p {font-size: 18px;margin:10px 0;}
     img.logo{
        width: 200px;
        margin: 20px auto;
        display: block;
     }
    </head>
<body>
    <div class="contact-box">
     <img src= "{% static 'image/logo.png' % }" alt= "Logo" class = "logo">
     <h1> Contact Us </h1>
     <p> Email: support@demo.com </p>
     <p> Phone: +91 000000000</p>
     <p> Address: 123 Food street , jingu bingu talllalal</p>
 </body>
</html>