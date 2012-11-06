<?php 

 // Connects to your Database 

// mysql_connect("127.0.0.1", "root", "toor") or die(mysql_error()); 
 //mysql_select_db("securelab") or die(mysql_error()); 

#Connect to AppFog MYSQL service
$services_json = json_decode(getenv("VCAP_SERVICES"),true);
$mysql_config = $services_json["mysql-5.1"][0]["credentials"];
$username = $mysql_config["username"];
$password = $mysql_config["password"];
$hostname = $mysql_config["hostname"];
$port = $mysql_config["port"];
$db = $mysql_config["name"];
$link = mysql_connect("$hostname:$port", $username, $password);
$db_selected = mysql_select_db($db, $link);

 //checks cookies to make sure they are logged in 

 if(isset($_COOKIE['ID_my_site'])) 

 { 

 		$username = $_COOKIE['ID_my_site']; 

 		$pass = md5($_COOKIE['Key_my_site']); 

 	 	$check = mysql_query("SELECT * FROM users WHERE username = '$username' AND password = '$pass'")or die(mysql_error()); 
		if(mysql_num_rows($check) == 0)
		{
			die('NICE TRY :P, It\'s not that easy!');
		}

 		while($info = mysql_fetch_array( $check )) 	 
 		{ 
			//if the cookie has the wrong password, they are taken to the login page 
 			if ($pass != $info['password']) 
			{
 				header("Location: login.php"); 
 			} 
                	//otherwise they are shown the admin area	 
 	        	else 
 			{ 
 	         		echo "USER Area<p>"; 
 		 		echo "Your Content<p>"; 
		 		echo "<a href=shout.php>Shoutbox</a>"; 
				if($username == "admin")
				{
					echo("<p>congrats, you're admin! you win!");
				}
			} 
		} 
 } 
 else //if the cookie does not exist, they are taken to the login screen 
 {			 
 	header("Location: login.php"); 
 } 
?> 
