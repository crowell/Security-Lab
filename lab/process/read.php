<?php

/*
 * Read the data stored in $dataFile if it exists!
 */



$services_json = json_decode(getenv("VCAP_SERVICES"),true);
$contents='';
if(!$services_json) {
	$contents = file_exists($dataFile) ? file_get_contents($dataFile) : '';
} else {
	$mysql_config = $services_json["mysql-5.1"][0]["credentials"];
        $username = $mysql_config["username"];
        $password = $mysql_config["password"];
        $hostname = $mysql_config["hostname"];
        $port = $mysql_config["port"];
        $db = $mysql_config["name"];
        $link = mysql_connect("$hostname:$port", $username, $password);
        $db_selected = mysql_select_db($db, $link);
	
	$contents=mysql_query("SELECT line FROM shout")
}

// If the file does not exits then there is no need to break up any information
if (!empty($contents)) {
    //$lines = explode("\n", $contents);
	
    $lines = mysql_fetch_array($contents)
    $posts = array();
    foreach ($lines as $line) {
        $parts = explode(',', $line);
        // Check to see if the line was more than a single element.
        if (count($parts) > 1) {
            $posts[] = array('postingUser' => $parts[0],
                'postingTime' => date('m/d/Y H:m', $parts[1]),
                'postedMessage' => $parts[2]);
        }
    }
} else {
   $posts = array();
	$line = "ben,".time().",hello";
        $parts = explode(',', $line);
        // Check to see if the line was more than a single element.
        if (count($parts) > 1) {
            $posts[] = array('postingUser' => $parts[0],
                'postingTime' => date('m/d/Y H:m', $parts[1]),
                'postedMessage' => $parts[2]);
        }
    
  

}

