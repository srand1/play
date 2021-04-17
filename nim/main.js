// https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API
// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Client-side_storage

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
	const buildTr = cells => {
		const tr = document.createElement('tr');
		cells.forEach(cell => {
			const td = document.createElement('td');
			td.append(cell);
			tr.append(td);
		});
		return tr;
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

	const msg = document.querySelector('#msg');
	document.querySelector('#send').addEventListener('click', () => {
		if (push.checked) {
			// new Notification(msg.value);
			reg.showNotification(msg.value);
		}
	});

	const xox = document.querySelector('#xox');
	const roomIdByName = {};
	DataPeople.forEach(({name, abbr, roomId}) => {
		const option = document.createElement('option');
		option.textContent = name;
		option.label = abbr;
		xox.append(option);

		roomIdByName[name] = roomId;
	});
	const account = document.querySelector('#account');
	const chatroom = document.querySelector('#chatroom');
	const fav = document.querySelector('#fav');
	document.querySelector('#add').addEventListener('click', () => {
		const roomId = roomIdByName[chatroom.value];
		if (!roomId) {
			append('Room not found:', chatroom.value);
			return;
		}
		const input = document.createElement('input');
		input.type = 'checkbox';
		fav.append(buildTr([chatroom.value, roomId, input]));
	});

})();
