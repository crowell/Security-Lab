<?php

$error = false;
if (isset($_POST['posting_user'])) {
    $postUser = trim($_POST['posting_user']);
    $postURL = trim($_POST['posting_site']);
    $postMessage = trim($_POST['posting_message']);
    if((strpos($postMessage,'<script>') !== false)||(stripos($postMessage,'src')!== false)||(strpos($postMessage,'<SCRIPT>') !== false))
    {
        $postMessage = 'Nice Try :P';
    }

    if (($postUser != '') AND ($postMessage != '')) {
        $postUser = str_replace(',', '&#44;', htmlentities($postUser));
        if (!empty($postURL)) {
            $postingUser = '<a href="http://' . urlencode($postURL) . '" target="_blank">' . $postUser . '</a>';
        } else {
            $postingUser = $postUser;
        }

        $postingTime = time();
        //$postedMessage = str_replace(array(','), '&#44;',($postMessage));
        $postedMessage = $postMessage;
        $line = $postingUser . ',' . $postingTime . ',' . $postedMessage ."\n";
	$services_json = json_decode(getenv("VCAP_SERVICES"),true);
	if(!$services_json) {	
	        $fileHandle = fopen($dataFile, 'a');
	        if (!fwrite($fileHandle, $line)) {
	            $error = 'Could not write to file, try again.';
	        }
        	fclose($fileHandle);
	} else {
		$mysql_config = $services_json["mysql-5.1"][0]["credentials"];
	        $username = $mysql_config["username"];
	        $password = $mysql_config["password"];
	        $hostname = $mysql_config["hostname"];
	        $port = $mysql_config["port"];
	        $db = $mysql_config["name"];
	        $link = mysql_connect("$hostname:$port", $username, $password);
	        $db_selected = mysql_select_db($db, $link);

		$results = mysql_query("SELECT * FROM shout");
		if (!$results) {
			mysql_query("CREATE TABLE shout (ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, line VARCHAR(200))");
		}
		$insert="INSERT INTO shout (line) VALUES ('".$line."')";
		mysql_query($insert);
	}

        // Delete post data so that fields do no populate again
        unset($_POST);
    } else {
        $error = 'Username and message are required!';
    }
}
