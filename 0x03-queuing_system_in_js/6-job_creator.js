import kue from 'kue';

const queue = kue.createQueue();

const myObject = { phoneNumber: '0340584759', message: 'Hello world' };
let job = queue.create(myObject).save((error) => {
	if (!error) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
