import math

def is_up_day(daily_info):
	 close = daily_info.get('Close', None)
	 open_p = daily_info.get('Open', None)
	 if close > open_p:
	 	return True
	 else:
	 	return False

def get_bar_size(daily_info):
	high = daily_info.get('High', None)
	low = daily_info.get('Low', None)

	return math.ceil((high - low) * 10000)

def get_upper_wick_length(daily_info):
	if is_up_day(daily_info):
		high = daily_info.get('High', None)
		close = daily_info.get('Close', None)
		return math.ceil((high - close) * 10000)
	else:
		high = daily_info.get('High', None)
		open_p = daily_info.get('Open', None)
		return math.ceil((high - open_p) * 10000)

def get_lower_wick_length(daily_info):
	if is_up_day(daily_info):
		low = daily_info.get('Low', None)
		open_p = daily_info.get('Open', None)
		return math.ceil((open_p - low) * 10000)
	else:
		low = daily_info.get('Low', None)
		close = daily_info.get('Close', None)
		return math.ceil((close - low) * 10000)

def get_body_size(daily_info):
	open_p = daily_info.get('Open', None)
	close = daily_info.get('Close', None)
	if is_up_day(daily_info):
		return math.ceil((close - open_p) * 10000)
	else:
		return math.ceil((open_p - close) * 10000)