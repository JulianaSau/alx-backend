import redis, { createClient, print } from 'redis';

const client = createClient();

client.on('error', error => {
	console.log(`Redis clientnt not connected to the server: ${error.message}`);
});

client.on('connect', () => {
	console.log('Redis clientnt connected to the server');
});


const HASHKEY = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
	client.hset(HASHKEY, key, values[index], print);
});

client.hgetall(HASHKEY, (err, value) => {
	console.log(value);
});
