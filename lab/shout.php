<?php
/* Configuration */
$dataFile = './data/data.csv';

/* Required Files */
require_once './process/write.php';
require_once './process/read.php';
?>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Shout Box | Guest Book Simple Script</title>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
        <link rel="stylesheet" type="text/css" href="/styles/styles.css">
    </head>
    <body>
        <?php
        if ($error !== false):
            ?>
            <div id="error"><?php echo $error; ?></div>
            <?php
        endif;
        ?>
        <div id="listing">
            <?php
            if (!empty($contents)) {
                foreach ($posts as $post):
                    ?>
                    <p class="post">
                        <b><?php echo $post['postingUser']; ?> </b> 
                        (@<?php echo $post['postingTime']; ?>)<br>
                        <?php echo $post['postedMessage']; ?>
                    </p>
                    <?php
                endforeach;
            } else {
                echo 'Nothing has been Posted. Be the first to post!';
            }
            ?>
        </div>
        <div id="form">
            <form action="<?php echo basename(__FILE__); ?>" method="post">
                <label for="posting_user">Username</label>
                <input type="text" name="posting_user" size="20" <?php if (isset($_POST['posting_user']))
                echo 'value="' . $_POST['posting_user'] . '"';
            ?>> 
                <label for="posting_site">Site (Without http://)</label>
                <input type="text" name="posting_site" size="20" <?php if (isset($_POST['posting_user']))
                           echo 'value="' . $_POST['posting_site'] . '"';
            ?>> 
                <label for="posting_message">Message</label>
                <textarea name="posting_message" rows="5" cols="20"> <?php if (isset($_POST['posting_user']))
                           echo $_POST['posting_message'];
            ?></textarea>
                <input type="submit" name="submit" value="Post!">
            </form>
        </div>
    </body>
</html>

