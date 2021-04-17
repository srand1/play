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

	NimUtils = {getDummyLogger};
})();
