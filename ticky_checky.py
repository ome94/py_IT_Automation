#!/usr/bin/env python3

import csv
import operator
import re

error = {}
per_user = {}
with open('syslog.log') as log:
	for line in log:
		line = line.strip()
		err_type = re.search(r"ticky: ERROR ([\w ]* )", line)
		if err_type is not None:
			error[err_type.group(1)] = error.get(err_type.group(1), 0) + 1
		user_log = re.search(r"ticky: (ERROR|INFO) [\w ]*.*\(([\w.]+)\)$", line)
		log_type = user_log.group(1)
		username = user_log.group(2)
		if username not in per_user:
			per_user[username] = {log_type: 0}
		per_user[username][log_type] = per_user[username].get(log_type, 0) + 1

sorted_error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
sorted_user = sorted(per_user.items())

with open('error_message.csv', 'w') as err:
	writer = csv.writer(err)
	writer.writerow(('Error', 'Count'))
	writer.writerows(sorted_error)

with open('user_statistics.csv', 'w') as stat:
	writer = csv.writer(stat)
	writer.writerow(('Username', 'INFO', 'ERROR'))
	for username, user_log in sorted_user:
		writer.writerow([username, user_log.get('INFO', 0), user_log.get('ERROR', 0)])
