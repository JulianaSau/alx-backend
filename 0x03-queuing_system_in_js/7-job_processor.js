import kue from 'kue';

const blackList = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
	const tracker = 100;
	job.progress(0, tracker);
	if (blackList.includes(phoneNumber)) {
		done(Error(`Phone number ${phoneNumber} is blacklisted`));
		return;
	}
	job.progress(50, tracker);
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
	done();
}

const queue = kue.createQueue();
const jobName = `push_notification_code_2`;

queue.process(jobName, 2, (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message, job, done);
});
