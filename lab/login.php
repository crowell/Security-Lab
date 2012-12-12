<?php 

#check if we are running on AppFog with a MySQL service
$services_json = json_decode(getenv("VCAP_SERVICES"),true);
if(!$services_json) {
    #connect to local Database
    mysql_connect("127.0.0.1", "root", "toor") or die(mysql_error());
    mysql_select_db("securelab") or die(mysql_error());
} else {
    #connect to AppFog MYSQL DB
    $mysql_config = $services_json["mysql-5.1"][0]["credentials"];
    $username = $mysql_config["username"];
    $password = $mysql_config["password"];
    $hostname = $mysql_config["hostname"];
    $port = $mysql_config["port"];
    $db = $mysql_config["name"];
    $link = mysql_connect("$hostname:$port", $username, $password);
    $db_selected = mysql_select_db($db, $link);
}

 //Checks if there is a login cookie

 if(isset($_COOKIE['ID_my_site']))
 //if there is, it logs you in and directes you to the members page
 { 
 	$username = $_COOKIE['ID_my_site']; 
 	$pass = md5($_COOKIE['Key_my_site']);
        $check = mysql_query("SELECT * FROM users WHERE username = '$username'")or die(mysql_error());
	while($info = mysql_fetch_array( $check )) 	
 	{
          if ($pass != $info['password']) 
 	  {
 	  }
          else
	  {
              header("Location: members.php");
	  }
	}
 }


 //if the login form is submitted 

 if (isset($_POST['submit'])) { // if form has been submitted
 // makes sure they filled it in
 if(!$_POST['username'] | !$_POST['pass']) 
 {
	die('You did not fill in a required field.');
 }
 // checks it against the database
 if (!get_magic_quotes_gpc()) 
 {
	//REMOVE SAFETY by commenting out the next line.  Makes SQLi too easy
	$_POST['email'] = addslashes($_POST['email']);

 }
 $uname = $_POST['username'];
 $pword = (md5($_POST['pass']));
 $check = mysql_query("SELECT * FROM users WHERE username = '$uname'")or die(mysql_error());



 //Gives error if user dosen't exist

 $check2 = mysql_num_rows($check);

 if ($check2 == 0) 
 {	
    die('That user does not exist in our database. <a href=index.php>Click Here to Register</a>');
 }

$query = "SELECT * FROM users WHERE username = '$uname' AND password = '$pword'";
if(stristr($query, "drop table") !== false) {
	die('Nice Try');
}
if(stristr($query, "create table") !== false) {
        die('Nice Try');
}	
$check = mysql_query($query) or die(mysql_error()); 
if(mysql_num_rows($check) == 0)
{
	die('invalid password. <a href=login.php>Try again</a>');
}

 while($info = mysql_fetch_array( $check )) 	
 {
    $_POST['pass'] = stripslashes($_POST['pass']);
    $noMD5 = ($_POST['pass']);
    //$info['password'] = stripslashes($info['password']);
    $_POST['pass'] = (md5($_POST['pass']));
    //gives error if the password is wrong
    //This is for safety.  Removing it might make this too hard for students...
    //So, I'll comment it out.  We need to then do checks for admin shit then
    if ($_POST['pass'] != $info['password']) 
    {
      //this is a simple check for making sure that the password from the db
      //is the same as the password that we get
      //preventing simple manual sqli.  make sure that they use tools! >:)
      die('Nice Try. It\'s not that easy though >:)');
    }

    if(!(1==1))
    {
	die('lolhax');
    } //stupid check because of the commented out checks
    else 
    { 
	// if login is ok then we add a cookie 
	$_POST['username'] = stripslashes($_POST['username']); 
	$_POST['username'] = mysql_real_escape_string($_POST['username']); 
	$hour = time() + 3600; 
//	setcookie(ID_my_site, $info['username'], $hour); 
	setcookie(ID_my_site, $_POST['username'], $hour); 
//	setcookie(Key_my_site, $info['password'], $hour);	 
	setcookie(Key_my_site, $noMD5, $hour);
	 //then redirect them to the members area 
 	header("Location: members.php"); 

     }  

   } 

 } 
else 
{	 
 // if they are not logged in 
 ?> 

 <form action="<?php echo $_SERVER['PHP_SELF']?>" method="post"> 

 <table border="0"> 

 <tr><td colspan=2><h1>Login</h1></td></tr> 

 <tr><td>Username:</td><td> 

 <input type="text" name="username" maxlength="40"> 

 </td></tr> 

 <tr><td>Password:</td><td> 

 <input type="password" name="pass" maxlength="50"> 

 </td></tr> 

 <tr><td colspan="2" align="right"> 

 <input type="submit" name="submit" value="Login"> 

 </td></tr> 

 </table> 

 </form> 
 <a href=register.php>Not Registered?</a><br>
 <a href=members.php>Already Logged In?</a><br>
 <a href=logout.php>Log Out</a>

 <?php 

 } 

 ?> 
