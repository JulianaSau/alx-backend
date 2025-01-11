import express from 'express';
import redis, { createClient } from 'redis';
import { promisify } from 'util';

const listProducts = [
	{ Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
	{ Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
	{ Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
	{ Id: 4, name: "Suitcase 1050", price: 550, stock: 5 }
]
/* handling redis connection */
function getItemById(id) {
	return (listProducts.filter((item) => item.Id == id)[0]);
}

const client = createClient();
const getClient = promisify(client.get).bind(client);

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', error => console.log('Redis client not connected to the server:', error));

/* implementing redis */
function reserveStockById(itemId, stock) {
	client.set(`item.${itemId}`);
}

async function getCurrentReservedStockById(itemId) {
	const stock = await getClient(`item..${itemId}`);
	return (stock);
}

/* starting an express server */
const app = express();
const port = 1245;


app.get('/list_products', (req, res) => {
	res.json(listProducts);
})


app.get('/list_products/:itemId', async (req, res) => {
	const itemId = Number(req.params.Id);
	const item = getItemById(itemId);
	if (!item) {
		return res.json({ "status": "Product not found" });
	}
	const reservedStock = await getCurrentReservedStockById(itemId);
	const stock = reservedStock !== null ? reservedStock : item.stock;
	item.currentQuantity = stock;
	res.json(item);
})


app.get('/reserve_product/:itemId', async (req, res) => {
	const itemId = Number(req.params.Id);
	const item = getItemById(itemId);
	if (!item) {
		return res.json({ "status": "Product not found" });
	}
	const reservedStock = await getCurrentReservedStockById(itemId);
	if (reservedStock === null) reservedStock = item.stock;
	//const stock = reservedStock !== null ? reservedStock : item.stock;
	if (reservedStock < 1) {
		res.json({ "status": "Not enough stock available", "itemId": itemId });
		return;
	}
	reserveStockById(itemId, Number(reservedStock) - 1);
	res.json({ "status": "Reservation confirmed", "itemId": itemId });
})

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`);
});
