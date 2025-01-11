import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
	console.log(
		`Sending notification to ${phoneNumber}, with message: ${message}`
	);
}
const jobOn = `push_notification_code`;
const myObject = { phoneNumber: '0340584759', message: 'Hello world' };

queue.create(jobOn, (myObject, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message);
	done();
});

//job.on('complete', () => console.log('Notification job completed'));
//job.on('failed', () => console.log('Notification job failed'));
