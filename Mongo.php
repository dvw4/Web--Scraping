<!DOCTYPE html>
<html>
<body>
<?php
require 'vendor/autoload.php';
$usr = get_current_user();
$client = new MongoDB\Client("mongodb://{$usr}:${usr}@localhost:27017/{$usr}");
$db = $client->$usr;
$collection = $db->Stocks;
$result = $collection->find( [] );
echo "<table border='1'>\n";
echo "<thead>\n";
echo "<tr>\n";
echo "<th>Symbol</th><th>Name</th><th>Price</th><th>Change</th><th>Volume</th>";
echo "</tr>\n";
echo "</thead>\n";
echo "<tbody>\n";
foreach ($result as $doc) {
	echo "<tr>\n  ";
	foreach ($doc as $key => $value) {
		if ($key!='_id'){
			echo "<td>";
			echo "{$value}";
			echo "</td>";
		}
	}
	echo "\n</tr>\n";
}
echo "</tbody>\n";
echo "</table>\n";
?>
</body>
</html>
