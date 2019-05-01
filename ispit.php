<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>DWA ispit</title>
  <meta name="description" content="DWA ispit">
  <meta name="author" content="DWA">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.3.0/milligram.css">
  <style>
    body {
        padding: 40px;
    }
  </style>
</head>

<body>
  <img src="fipu_logo.png" width="200"/>
  <h1>Dinamičke web aplikacije</h1>
  <p>Ovo je tvoja aplikacija za potrebe ispita. Izvorni kod nalazi se u fajlu <code>index.php</code> kojeg možeš mijenjati pomoću online VSCode editora na adresi <a href='http://<?php echo $_SERVER['SERVER_ADDR']; ?>:9000'>http://<?php echo $_SERVER['SERVER_ADDR']; ?>:9000</a></p>
  <p><code>phpMyAdmin</code> se nalazi na <a target="blank" href="/phpmyadmin">ovdje</a>, korisničko ime / šifra za pristup bazi je <code>dwa / dwa</code></p>
  <p>Sretno na ispitu!</p>
</body>
</html>