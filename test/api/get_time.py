import time

from SingleLog.log import Logger

import PyPtt
import util


def test(ptt_bot: PyPtt.API):
    result = []
    for _ in range(3):
        result.append(ptt_bot.get_time())
        time.sleep(1)

    logger.info('get time result', result)


def func():
    host_list = [
        PyPtt.HOST.PTT1,
        PyPtt.HOST.PTT2]

    for host in host_list:
        ptt_bot = PyPtt.API(
            host=host,
            # log_level=PyPtt.LOG_LEVEL.TRACE,
        )
        util.login(ptt_bot, host)

        test(ptt_bot)

        ptt_bot.logout()


if __name__ == '__main__':
    logger = Logger('TEST')
    func()