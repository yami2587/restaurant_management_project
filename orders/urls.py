<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Restaurent Menu</title>
</head>
<body>
 <h1> Welecome to our Restaurent!</h1>
 <div id="menu"></div>
 <script>
  fetch("/api/menu/")
  .then(res => res.json())
  .then(data =>{
    document.getElementById('menu').innerHtml=data.map(
        item => '<div><b>${item.name}</b>: ${item.price} <br>${item.description}<hr></div>').join('');

    )
  })
  .catch(() => {
    document.getElementById("menu").innerHtml = "Couldn't load menu";
  });
  </script>
  </body>
  </html>
  