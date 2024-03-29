(() => {
	const appKey = '632feff1f4c838541ab75195d1ceb3fa';
	const account = '100000';
	const chatroomAddresses = ['chatweblink01.netease.im:443'];

	const getDummyLogger = (() => {
		const loggers = {};
		return name => {
			if (!(name in loggers)) {
				loggers[name] = (...args) => {
					const now = (new Date()).toISOString();
					console.log(now, name, args);
				};
			}
			return loggers[name];
		};
	})();

	const appendMsg = msg => {
		msg.custom = JSON.parse(msg.custom);
		if (!parseInt(msg.custom.sessionRole)) return;
		const key = 'xoxmsg-' + localStorage.length;
		localStorage.setItem(key, JSON.stringify(msg));
		UI.showLatest(msg);
		UI.updateMsg();
	};
	const onmsgs = msgs => msgs.forEach(appendMsg);
	const onconnect = (roomInfo, ...args) => {
		console.log((new Date()).toISOString(), 'connect', roomInfo.chatroom.id, roomInfo.chatroom.name, roomInfo.chatroom.onlineMemberNum, roomInfo, args);
	};
	const ondisconnectWithRoomId = roomId => ((evt, ...args) => {
		console.log((new Date()).toISOString(), 'disconnect', roomId, evt.code, evt, args);
	});

	const all = [];
	const getConn = (account, roomId) => {
		const conn = SDK.Chatroom.getInstance({
			appKey: appKey,
			isAnonymous: true,
			chatroomNick: 'RO',
			// account: account,
			// token: account,
			chatroomId: roomId,
			chatroomAddresses: chatroomAddresses,
			// onconnect: getDummyLogger('connect'),
			onconnect,
			onwillreconnect: getDummyLogger('willreconnect'),
			// ondisconnect: getDummyLogger('disconnect'),
			ondisconnect: ondisconnectWithRoomId(roomId),
			onerror: getDummyLogger('error'),
			// onmsgs: getDummyLogger('msgs'),
			onmsgs,
			// onmsgs: function(arr){console.log('msg', JSON.parse(arr[0].custom))},
		});
		all.push(conn);
		return conn;
	};
	const getHist = (conn, opts) => new Promise((resolve, reject) => {
		// return of current func / getHistoryMsgs / reject / resolve useless
		console.log({
			done: (err, obj) => err ? reject(err) : resolve(obj),
			...opts,
		});
		conn.getHistoryMsgs({
			done: (err, obj) => err ? reject(err) : resolve(obj),
			...opts,
		});
	});

	NimUtils = {
		getDummyLogger,
		getConn,
		all,
		getHist,
	};
})();
