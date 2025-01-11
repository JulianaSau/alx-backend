import { createClient } from 'redis';
const { promisify } = require('util');

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
	await setAsync(schoolName, value);
}

async function displaySchoolValue(schoolName) {
	const res = await getAsync(schoolName);
	console.log(res);
}

(async () => {
	await setNewSchool('Holberton', '100');
	await displaySchoolValue('Holberton');

	await setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
})();
