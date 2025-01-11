import express from 'express';
import redis { createClient } from 'redis';
import { promisify } from 'util';


const app = express();
const client = createClient();
const getClient = promisify(client.get).bind(client);
const port = 1245;
const available = 50;

function reserveSeat(number, available_seats){
	available_seats["numberOfAvailableSeats"] = number;
}

async function getCurrentAvailableSeats(itemId){
	const available = await getClient(itemId);
	return (available[numberOfAvailableSeats]);
}
})
app.get('/', () => {
	res.json()
	
app.listen(port, () => {
	console.log(`App listening to port ${port}`);
})
