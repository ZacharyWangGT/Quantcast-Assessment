def cookies_per_day(csv):
    cookie_per_day = {}
    for line in csv:
        line_split = line.split(',')
        cookie = line_split[0]
        date = line_split[1].split('T')[0]
        if date not in cookie_per_day:
            cookie_per_day[date] = [cookie]
        else:
            cookie_per_day[date].append(cookie)
    return cookie_per_day

def most_frequent_cookies(date, cookie_per_day):
    most_frequent = []
    cookie_freq = {}
    cookies = cookie_per_day[date]

    for cookie in cookies:
        cookie_freq[cookie] = cookie_freq.get(cookie, 0) + 1
    highest_freq = max(cookie_freq.values())

    for cookie in cookie_freq:
        if cookie_freq[cookie] == highest_freq:
            most_frequent.append(cookie)

    return most_frequent