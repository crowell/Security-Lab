<?php

/*
 * Read the data stored in $dataFile if it exists!
 */
$contents = file_exists($dataFile) ? file_get_contents($dataFile) : '';

// If the file does not exits then there is no need to break up any information
if (!empty($contents)) {
    $lines = explode("\n", $contents);

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
}

