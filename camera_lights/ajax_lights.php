<?php
include_once '../vars.php';

$light_id=$_POST["light_id"];
$state=$_POST["state"];

if ($state=='1') $state='dh';
else $state='dl';

if ($light_id=="camlight"){
	system("sudo raspi-gpio set $cameralight $state");
}

if ($light_id=="headlight"){
	system("sudo raspi-gpio set $headlight_right $state");
	system("sudo raspi-gpio set $headlight_left $state");
}

if ($light_id=="LaUp"){
	system("sudo raspi-gpio set $LaUp $state");
	
}

if ($light_id=="LaDown"){
	system("sudo raspi-gpio set $LaDown $state");

}

if ($light_id=="TiltUp"){
	system("sudo raspi-gpio set $TiltUp $state");

}

if ($light_id=="TiltDown"){
	system("sudo raspi-gpio set $TiltDown $state");

}

if ($light_id=="shutdown"){
	system("sudo shutdown");
}

echo"$light_id, $state";
/*
$myFile = "testFile.txt";
$fh = fopen($myFile, 'w') or die("can't open file");
fwrite($fh, $light_id.$state);
fclose($fh);
*/
?>
