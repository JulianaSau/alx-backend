import { createClient } from 'redis';

const client = createClient();

client.on('error', error => console.log('Redis client not connected to the server:', error));
client.connect();
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
	client.set(schoolName, value);
}

function displaySchoolValue(schoolName) {
	client.get(schoolName)
		.then(value => console.log(value));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
//client.disconnect();
