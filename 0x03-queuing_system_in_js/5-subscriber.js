import { createClient } from 'redis';

const client = createClient();

client.on('error', error => console.log('Redis client not connected to the server:', error));
client.on('connect', () => console.log('Redis client connected to the server'));

const channel = "holberton school channel";
client.subscribe(channel);
client.on('message', (chan, mess) => {
	if (chan === channel) console.log(message);
	if (message === "KILL_SERVER") {
		client.unsubscribe(channel);
		client.quit();
	}
});
