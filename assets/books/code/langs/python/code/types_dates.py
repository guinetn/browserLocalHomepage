#%%
# python.exe xxxx.py

import datetime   # datetime module helps in handling dates, times

 
cur_date = datetime.datetime.now()
 
# extract values from the date
print(cur_date)
print(cur_date.year)
print(cur_date.day)
print(cur_date.weekday())
print(cur_date.month)
print(cur_date.time())


# Differences between two times or two dates
import datetime
time1 = datetime.datetime.now()
time2 = datetime.datetime.now()
timediff = time2 - time1            # object of type timedelta
print(timediff.microseconds())


time1 = datetime.datetime.now()
time2 = datetime.timedelta(days=3)
time3=time1+time2
print(time3.date())


# FORMAT DATE AND TIME
import datetime
date1 = datetime.datetime.now()
print(date1.strftime('%Y%m%d')) # YYYYMMDD


print(date1.strftime('%d. %B %Y %I:%M%p'))
#			  \
#			   \___ Format specification
#
#						%a   locale abbreviated name of the weekday
#						%A	 weekday
#						%w	 day of the week as a number
#						%d	 day of the month as a zero-padded number
#						%b	 month as locale abbreviated name
#						%B	 month as locale full name
#						%m	 month as a zero-padded number
#						%y	 year as a zero-padded two-digit number
#						%Y	 year as a zero-padded four-digit number
#						%H	 hour (24-hour clock) as a zero-padded number
#						%I	 hour (12-hour clock) as a zero-padded number
#						%p   AM or PM
#						%M	 minute as a zero-padded number
#						%S	 second as a zero-padded number


# CREATE DATE FROM STRING

date1 = datetime.datetime.strptime("2015-11-21", "%Y-%m-%d")
date1 = datetime.datetime(year=2015, month=11, day=21)


# PARSING Dates

class Birthday: 
    def init (self, year = 0, month = 0, day = 0): 
        self.year = year 
        self.month = month 
        self.day = day 
    def out_date(self): 
        return "year %d, month: %d, day: %d" %(self.year, self.month, self.day)         
    @classmethod 
    def pre_out(cls, date_string): 
        year, month, day = map(int, date_string.split("-")) 
        return cls(year, month, day) 
        
date = "2319-3-23" 
Birthday = Birthday.pre_out(date) 
print(Birthday.out_date()) # output 



"""Dates and Times.

@see: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times

The datetime module supplies classes for manipulating dates and times in both simple and complex
ways. While date and time arithmetic is supported, the focus of the implementation is on efficient
member extraction for output formatting and manipulation. The module also supports objects that
are timezone aware.
"""

from datetime import date


def test_datetime():
    """Dates and Times"""

    real_now = date.today()
    assert real_now

    fake_now = date(2018, 8, 29)

    assert fake_now.day == 29
    assert fake_now.month == 8
    assert fake_now.year == 2018
    assert fake_now.ctime() == 'Wed Aug 29 00:00:00 2018'
    assert fake_now.strftime(
        '%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'
    ) == '08-29-18. 29 Aug 2018 is a Wednesday on the 29 day of August.'

    # Dates support calendar arithmetic.
    birthday = date(1964, 7, 31)
    age = fake_now - birthday

    assert age.days == 19752
