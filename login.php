<?php
$servername = "localhost";
$username = "root";
$password = "";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully ". "<br>";

// Use database
$sql2 = "use project";
if ($conn->query($sql2) === TRUE) {
    echo "Database used successfully ". "<br>";
} else {
    echo "Error using database: " . $conn->error;
}

//get data of user from url
$nam=$_GET['name'];
echo "$nam ". "<br>";

//$sql1 = "INSERT INTO people (name) VALUES ('$nam')";

$sql1 = "INSERT INTO people (name) SELECT * FROM (SELECT '$nam') AS tmp WHERE NOT EXISTS (     SELECT name FROM people WHERE name = '$nam' ) LIMIT 1";

if ($conn->query($sql1) === TRUE) {
    echo "New record created successfully". "<br>";
} else {
    echo "Error: " . $sql1 . "<br>" . $conn->error;
}

$sql = "SELECT name FROM people";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "Online: " . $row["name"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();

?> 