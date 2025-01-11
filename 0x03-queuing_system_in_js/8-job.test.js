import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const jobs = [{
	phoneNumber: '092832938247',
	message: "Hello world"
}];

describe('createPushNotificationsJobs', () => {
	before(() => {
		queue.testMode.enter();
	});
	afterEach(() => {
		queue.testMode.clear();
	});
	after(() => {
		queue.testMode.exit();
	});
	it('checks if jobs is an array', () => {
		expect(() => {
			createPushNotificationsJobs(0, queue);
		}).to.throw('Jobs is not an array');
	});
	it('checks if jobs is an array', () => {
		expect(() => {
			createPushNotificationsJobs("passing a string", queue);
		}).to.throw('Jobs is not an array');
	});
	it('checks if jobs is an array', () => {
		expect(() => {
			createPushNotificationsJobs({ hello: "world" }, queue);
		}).to.throw('Jobs is not an array');
	});
	it('checks if jobs is an array', () => {
		expect(
			createPushNotificationsJobs([], queue)
		).to.equal(undefined);
	});
	it('creates  new jobs sucessfully', () => {
		queue.createJob('job1', { key: 'value' }).save();
		queue.createJob('job2', { key: 'value' }).save();
		expect(queue.testMode.jobs.length).to.equal(2);
		expect(queue.testMode.jobs[0].type).to.equal('job1');
		expect(queue.testMode.jobs[0].data).to.eql({ key: 'value' });
		expect(queue.testMode.jobs[1].type).to.equal('job2');
		expect(queue.testMode.jobs[1].data).to.eql({ key: 'value' });
	});
});
