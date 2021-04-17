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
	const addFav = chatroomVal => {
		const roomId = roomIdByName[chatroomVal] || parseInt(chatroomVal);
		if (!roomId) {
			append('Room not found: ' + chatroomVal);
			return;
		}
		const input = document.createElement('input');
		input.type = 'checkbox';
		let conn = null;
		input.addEventListener('change', () => {
			if (input.checked) {
				console.assert(conn === null);
				conn = NimUtils.getConn(account.value, roomId);
			} else {
				console.assert(conn !== null);
				conn.destroy();
				conn = null;
			}
		});
		fav.append(buildTr([chatroomVal, roomId, input]));
	};
	document.querySelector('#add').addEventListener('click', () => {
		addFav(chatroom.value);
		localStorage.setItem('config-fav', JSON.stringify(
			JSON.parse(localStorage.getItem('config-fav') || '[]').concat(chatroom.value)
		));
	});
	JSON.parse(localStorage.getItem('config-fav') || '[]').forEach(addFav);

	const count = document.querySelector('#count');
	const latest = document.querySelector('#latest');
	const updateMsg = () => {
		count.value = localStorage.length;
		latest.value = Date();
	};
	const showLatest = msg => {
		if (msg.custom.messageType !== 'TEXT') return;
		reg.showNotification(msg.custom.user.nickName, {
			tag: msg.chatroomId,
			renotify: true,
			body: msg.custom.text,
		});
	};
	UI = {updateMsg, showLatest, reg};

	const dumpStorage = storage => {
		const ans = {};
		const l = storage.length;
		for (let i = 0; i < l; i++) {
			const key = storage.key(i);
			const val = storage.getItem(key);
			ans[key] = val;
		}
		return ans;
	};

})();
