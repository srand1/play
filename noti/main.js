// https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API
// 
(async () => {
	console.log('hello');

	const reg = await navigator.serviceWorker.register('worker.js');
	console.log('reg', reg);

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
			new Notification(msg.value);
		}
	});

})();
