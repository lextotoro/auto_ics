import datetime 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', help='title of meeting')
parser.add_argument('-d', help='days from now')
parser.add_argument('-s', help='start hour (integer for hour)')
parser.add_argument('-e', help='end hours (integer for hour)')
parser.add_argument('-l', help='location')
parser.add_argument('-c', help='Description\Comment for invite body')
args = parser.parse_args()

def date_by_adding_business_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date

today = datetime.date.today()
print today
meeting_date = date_by_adding_business_days(today, int(args.d))
dt_start = datetime.datetime.combine(meeting_date,datetime.time(int(args.s), 00))
print dt_start
dt_end = datetime.datetime.combine(meeting_date,datetime.time(int(args.e), 00))						  
print dt_end


summary = args.t

f = open("fj_ir_meeting_invite.ics", "w")
f.write("BEGIN:VCALENDAR\n")
f.write("VERSION:2.0\n")
f.write("PRODID:MY COMPANY\n")
f.write("BEGIN:VEVENT\n")
f.write("DTSTAMP:"+str(today)+"\n")
f.write("ORGANIZER;CN=Event Organiser:MAILTO:Event_Organiser@example.com\n")
f.write("DTSTART:"+str(dt_start).replace(' ', 't', 1)+"\n")
f.write("DTEND:"+str(dt_end).replace(' ', 't', 1)+"\n")
f.write("SUMMARY:"+summary+"\n")
f.write("GEO:53.3900;2.5970\n")
f.write("LOCATION:"+args.l+"\n")
f.write("DESCRIPTION:"+args.c+"\n")
f.write("END:VEVENT\n")
f.write("END:VCALENDAR\n")
f.close()
