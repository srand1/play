// https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API
// 
(async () => {
	console.log('hello');

	const reg = await navigator.serviceWorker.register('worker.js');
	console.log('reg', reg);

	const log = document.querySelector('#log');
	const append = str => {
		const li = document.createElement('li');
		li.textContent = str;
		log.append(li);
	};

	const push = document.querySelector('#push');
	push.addEventListener('change', async () => {
		if (push.checked) {
			if (Notification.permission !== 'granted') {
				const perm = await Notification.requestPermission();
				if (perm !== 'granted') {
					push.checked = false;
					console.log(perm);
					return;
				}
			}
		} else {
		}
	});
	document.querySelector('#request').addEventListener('click', async () => {
			if (Notification.permission !== 'granted') {
				const perm = await Notification.requestPermission();
				if (perm !== 'granted') {
					push.checked = false;
					console.log(perm);
					return;
				}
			}
	});

	const msg = document.querySelector('#msg');
	document.querySelector('#send').addEventListener('click', () => {
		if (push.checked) {
			// new Notification(msg.value);
			reg.showNotification(msg.value);
		}
	});

	const interval = document.querySelector('#interval');
	const close = noti => {noti.close();};
	const job = after => {
		const now = Date();
		append(now);
		if (push.checked) {
			// const noti = new Notification(now);
			// setTimeout(close, after, noti);
			reg.showNotification(now);
		}
	};
	let timer = null;
	document.querySelector('#start').addEventListener('click', () => {
		if (timer !== null) {
			console.log('already running', timer);
			return;
		}
		append('starting');
		const after = parseInt(interval.value);
		timer = setInterval(job, after, after*5);
	});
	document.querySelector('#stop').addEventListener('click', () => {
		if (timer === null) {
			console.log('already stopped');
			return;
		}
		append('stopping');
		clearInterval(timer);
		timer = null;
	});

})();
