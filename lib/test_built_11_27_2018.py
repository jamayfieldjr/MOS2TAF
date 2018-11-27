#import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

class MOS2TAF(object) 
""" MOS to TAF converter """

    def __init__(self,string) 

    """
    Initializes the object with GFS MOS LAMP, NAM MOS, and  report text.
 
        
    Args:
        string: station ID e.g. KMEM (Special Note: Work for US station only)
        
    Raises:
        MalformedTAF: An error parsing the TAF/METAR report
    """

       # Instance variables
        self._raw_taf = None
        self._taf_header = None
        self._raw_weather_groups = []
        self._weather_groups = []
        self._maintenance = None
  
 
station_id = "KIND" 
short_station_id = station_id[1:4]

quote_page = "http://www.nws.noaa.gov/cgi-bin/lamp/getlav.pl?sta="+station_id
quote_page1 = "http://www.nws.noaa.gov/cgi-bin/mos/getmet.pl?sta="+station_id
quote_page2 = "http://www.nws.noaa.gov/cgi-bin/mos/getmav.pl?sta="+station_id
quote_page3 = "https://www.aviationweather.gov/metar/data?ids="+station_id+"&format=raw&date=&hours=3"
quote_page4 = "https://forecast.weather.gov/product.php?site=meg&product=TAF&issuedby="+short_station_id


html = urlopen(quote_page3)
soup = BeautifulSoup(html,"html.parser")
#features = "html.parser"
text = str(soup.find_all('code'))

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

#print(remove_html_tags(text))
cleantext=remove_html_tags(text) 
cleantext=re.split(",",cleantext)

for values in cleantext:
  print(values);

print(' ')
#====================================================================================
#====================================================================================

html = urlopen(quote_page)
#print(html.read())

soup = BeautifulSoup(html,"html.parser")
text = str(soup.find_all('pre'))
lines=text.splitlines()
#print(lines)

#===================================================================================
#STATION INFO
station_info = lines[1].split()
#print(str(station_info))
station_name = 'STATION NAME: '+station_info[0]
#print(str(station_name))
initalized_time = 'INITIALIZED TIME: ' + station_info[6] +'Z'
#print(str(initalized_time))
#===================================================================================
#===================================================================================
#TIME_VECTOR
time_vector = lines[2].split()
#print(time_vector)
time_vector = (time_vector[1:len(time_vector)])
#print(time_vector)
#time = ['']*len(time_vector)
#print(time)
#print(time_vector)
time = [ s + '00' for s in time_vector]
#print(time)
fm_times=["FM" + s for s in time]
#print(fm_times)
#===================================================================================
#===================================================================================
#TEMP_VECTOR
temp = lines[3].split()
#print(temp)
temp = temp[1:len(temp)]
temp_new = [int(x) for x in temp]
#print(type(temp))
temp_c = [(round(((y - 32) * 5.0 / 9.0))) for y in temp_new]
#print(type(temp_c))
temp_c=map(str,temp_c)
final_temp_c=[x.replace('-', 'M') for x in temp_c]
#print(final_temp_c)
#===================================================================================
#===================================================================================
#DEW_POINT_TEMP_VECTOR
dew_point = lines[4].split()
#print(temp)
dew_point = dew_point[1:len(dew_point)]
dew_point_new = [int(x) for x in dew_point]
#print(type(temp))
dew_point_c = [(round(((y - 32) * 5.0 / 9.0))) for y in dew_point_new]
#print(type(dew_point_c))
dew_point_c=map(str,dew_point_c)
final_dew_point_c=[x.replace('-', 'M') for x in dew_point_c]
#print(final_dew_point_c)

[final_temp_c,'/',final_dew_point_c]
full_temp=['/'.join(map(str, i)) for i in zip(final_temp_c, final_dew_point_c)]
#===================================================================================
#===================================================================================
#WIND DIRECTION 
wind_dir = lines[5].split()
wind_dir = wind_dir[1:len(wind_dir)]
wind_dir=list(map(lambda k: k+'0', wind_dir))
#print(wind_dir)
#===================================================================================
#===================================================================================
#WIND SPEED
wind_spd = lines[6].split()
wind_spd = wind_spd[1:len(wind_spd)]
wind_spd=list(map(lambda k: k+'KT', wind_spd))
#print(wind_spd)
#===================================================================================
#===================================================================================
#COMBINING WIND DIRECTION AND WIND SPEED
wind=[''.join(map(str, i)) for i in zip(wind_dir, wind_spd)]
#print(wind)
full_wind=['/'.join(map(str, i)) for i in zip(wind_dir, wind_spd)]
#print(full_wind)
#===================================================================================
#===================================================================================
#CLOUD TYPE  
cloud_type = lines[18].split()
#print(cloud_type)
cloud_type = cloud_type[1:len(cloud_type)]
#print(cloud_type)
#===================================================================================
#===================================================================================
#CLOUD HEIGHT
cloud_height = lines[19].split()
#print(cloud_height)
cloud_height = cloud_height[1:len(cloud_height)]
#print(cloud_height)

#===================================================================================
#===================================================================================
#probability of precipitation
precip_prob=lines[8]
precip_prob = precip_prob [5:len(precip_prob )]

def split(s, n):
    if len(s) < n:
        return []
    else:
        return [s[:n]] + split(s[n:], n) 

precip_prob  =  split(precip_prob ,3)
pcp = ['PRECIP:']*len(precip_prob)
precentage = ['% ']*len(precip_prob)
zipped_precip_prob =[''.join(map(str, i)) for i in zip(pcp, precip_prob, precentage)]
#===================================================================================
#===================================================================================
#Conditional Probability of snow occurring at the hour.
lol = lines[16]
lol = lol[5:len(lol)]
snow_prob  =  split(lol, 3)
pcp = ['SN: ']*len(snow_prob)
precentage = ['% ']*len(snow_prob)
zipped_snow_prob =[''.join(map(str, i)) for i in zip(pcp, snow_prob, precentage)]
#===================================================================================
#===================================================================================
#Conditional Probability of ice occurring at the hour.
lol= lines[15]
lol = lol[5:len(lol)]
ice_prob  =  split(lol, 3)
pcp = ['IC: ']*len(ice_prob)
precentage = ['% ']*len(ice_prob)
zipped_ice_prob =[''.join(map(str, i)) for i in zip(pcp, ice_prob, precentage)]
#===================================================================================
#===================================================================================

#probability of lightning 
lgt_prob = lines[11]
lol = lol[4:len(lol)]
lgt_prob  =  split(lol, 3)
pcp = ['LGT: ']*len(lgt_prob)
precentage = ['% ']*len(lgt_prob)
zipped_lgt_prob =[''.join(map(str, i)) for i in zip(pcp, lgt_prob, precentage)]
#===================================================================================
#===================================================================================
#COMBINING CLOUD TYPE AND CLOUD HEIGHT
zipped_height_types=[''.join(map(str, i)) for i in zip(cloud_type, cloud_height)]
#print(zipped_height_types)

cloud_type_hash={ 'CL':'SKC', 'FW':'FEW', 'SC':'SCT', 'BK':'BKN', 'OV':'OVC' }

cloud_height_hash={ '1': ' 200', '2' : ' 200-400', '3' : ' 500-900', '4' : ' 1000-1900', '5' : ' 2000-3000','6' : ' 3100-6500', '7' : ' 6600-12000', '8' : ' 12000' }
results = []
for ht in zipped_height_types:
 htype = ht[:2]
 val = ht[2:]
 res = cloud_type_hash[htype] + cloud_height_hash[val]
 results.append(res)
 #print(zipped_full_clouds)
 #print(type(zipped_full_clouds))
#print(results) 

#===================================================================================
#===================================================================================

#very low instrument flight rules	VLIFR	< 200 feet	< 0.5 mile
#low instrument flight rules	LIFR	> 200 feet and < 500 feet	> 0.5 mile and < 1 mile
#instrument flight rules	IFR	> 500 and < 1000 feet	> 1 and < 3 miles
#marginal visual flight rules	MVFR	> 1000 and < 3000 feet	> 3 and <5 miles
#visual flight rules	VFR	> 3000 feet	> 5 miles

#'BK':'BKN', 'OV':'OVC' 


#===================================================================================
#===================================================================================
#VISIBILITY
vis = lines[21].split()
vis = vis[1:len(vis)]

visibility_hash={ '1':'M1/2SM FG', '2':'1/2SM-1SM FG/BR', '3':'1SM-2SM BR', '4':'2SM-3SM BR', '5':'3SM-5SM BR', '6':'6SM BR', '7':'P6SM'}
visresults = []
for v in vis:
 val = v[:2]
 res = visibility_hash[val] 
 visresults.append(res)

#===================================================================================
#===================================================================================

#print(vis)
#print(fm_times)
x = zip(fm_times, full_wind, results, visresults, full_temp, zipped_precip_prob, zipped_snow_prob, zipped_ice_prob, zipped_lgt_prob)
#for values in x:
#  print(values);

new_data = list(' '.join(w) for w in x)
#print(new_data)

#https://stackoverflow.com/questions/1815316/why-cant-i-join-this-tuple-in-python

onepiece = station_info[0]
twopiece = ' FT GFS LAMP '

elevenpiece =  datetime.datetime.today().strftime('%H%M')
elevenpiece = [elevenpiece,'Z']
elevenpiece = ''.join(elevenpiece)
#print(elevenpiece)

threepiece =  datetime.datetime.today().strftime('%d')
fourpiece = time[0][:2]
fivepiece = [threepiece,fourpiece]
fivepiece=''.join(fivepiece)

sixpiece = str(datetime.date.today() + datetime.timedelta(days=1))
sevenpiece = sixpiece[-2:] 
eightpiece = int(time[len(time)-1][:2])+1
eightpiece = ''.join(['0',str(eightpiece)])
ninepiece = [sevenpiece,eightpiece]
ninepiece =''.join(ninepiece)

tenpiece = [fivepiece,ninepiece]
tenpiece ='/'.join(tenpiece)

tenpiece = [onepiece,twopiece,tenpiece,' ',elevenpiece,new_data[0][6:]]
tenpiece =''.join(tenpiece)
print(tenpiece)
new_data = new_data[1:len(new_data)] 

for values in new_data:
  print(values);

print(' ')

html = urlopen(quote_page1)
#print(html.read())

soup = BeautifulSoup(html,"html.parser")
text = str(soup.find_all('pre'))
lines=text.splitlines()
#print(lines)

#===================================================================================
#STATION INFO
station_info = lines[1].split()
#print(str(station_info))
station_name = 'STATION NAME: '+station_info[0]
#print(str(station_name))
initalized_time = 'INITIALIZED TIME: ' + station_info[6] +'Z'
#print(str(initalized_time))
#===================================================================================
#===================================================================================
#TIME_VECTOR
time_vector = lines[3].split()
#print(time_vector)
time_vector = (time_vector[1:9])
#print(time_vector)
#time = ['']*len(time_vector)
#print(time)
#print(time_vector)
time = [ s + '00' for s in time_vector]
#print(time)
fm_times=["FM" + s for s in time]
#print(fm_times)
#===================================================================================
#===================================================================================
#TEMP_VECTOR
temp = lines[5].split()
#print(temp)
temp = temp[1:9]
temp_new = [int(x) for x in temp]
#print(type(temp))
temp_c = [(round(((y - 32) * 5.0 / 9.0))) for y in temp_new]
#print(type(temp_c))
temp_c=map(str,temp_c)
final_temp_c=[x.replace('-', 'M') for x in temp_c]
#print(final_temp_c)
#===================================================================================
#===================================================================================
#DEW_POINT_TEMP_VECTOR
dew_point = lines[6].split()
#print(temp)
dew_point = dew_point[1:9]
dew_point_new = [int(x) for x in dew_point]
#print(type(temp))
dew_point_c = [(round(((y - 32) * 5.0 / 9.0))) for y in dew_point_new]
#print(type(dew_point_c))
dew_point_c=map(str,dew_point_c)
final_dew_point_c=[x.replace('-', 'M') for x in dew_point_c]
#print(final_dew_point_c)

[final_temp_c,'/',final_dew_point_c]
full_temp=['/'.join(map(str, i)) for i in zip(final_temp_c, final_dew_point_c)]
#===================================================================================
#===================================================================================
#WIND DIRECTION 
wind_dir = lines[8].split()
wind_dir = wind_dir[1:9]
wind_dir=list(map(lambda k: k+'0', wind_dir))
#print(wind_dir)
#===================================================================================
#===================================================================================
#WIND SPEED
wind_spd = lines[9].split()
wind_spd = wind_spd[1:9]
wind_spd=list(map(lambda k: k+'KT', wind_spd))
#print(wind_spd)
#===================================================================================
#===================================================================================
#COMBINING WIND DIRECTION AND WIND SPEED
wind=[''.join(map(str, i)) for i in zip(wind_dir, wind_spd)]
#print(wind)
full_wind=['/'.join(map(str, i)) for i in zip(wind_dir, wind_spd)]
#print(full_wind)
#===================================================================================
#===================================================================================
#CLOUD TYPE  
cloud_type = lines[7].split()
#print(cloud_type)
cloud_type = cloud_type[1:9]
#print(cloud_type)
#===================================================================================
#===================================================================================
#CLOUD HEIGHT
cloud_height = lines[20].split()
#print(cloud_height)
cloud_height = cloud_height[1:9]
#print(cloud_height)
#===================================================================================
#===================================================================================
#COMBINING CLOUD TYPE AND CLOUD HEIGHT
zipped_height_types=[''.join(map(str, i)) for i in zip(cloud_type, cloud_height)]
#print(zipped_height_types)

cloud_type_hash={ 'CL':'SKC', 'FW':'FEW', 'SC':'SCT', 'BK':'BKN', 'OV':'OVC' }

cloud_height_hash={ '1': ' 200', '2' : ' 200-400', '3' : ' 500-900', '4' : ' 1000-1900', '5' : ' 2000-3000','6' : ' 3100-6500', '7' : ' 6600-12000', '8' : ' 12000' }
results = []
for ht in zipped_height_types:
 htype = ht[:2]
 val = ht[2:]
 res = cloud_type_hash[htype] + cloud_height_hash[val]
 results.append(res)
 #print(zipped_full_clouds)
 #print(type(zipped_full_clouds))
#print(results) 
#===================================================================================
#===================================================================================
#VISIBILITY
vis = lines[21].split()
vis = vis[1:len(vis)]

visibility_hash={ '1':'M1/2SM FG', '2':'1/2SM-1SM FG/BR', '3':'1SM-2SM BR', '4':'2SM-3SM BR', '5':'3SM-5SM BR', '6':'6SM BR', '7':'P6SM'}
visresults = []
for v in vis:
 val = v[:2]
 res = visibility_hash[val] 
 visresults.append(res)

#print(vis)

x = zip(fm_times, full_wind, results, visresults, full_temp)
#for values in x:
#  print(values);

new_data = list(' '.join(w) for w in x)
#print(new_data)

#https://stackoverflow.com/questions/1815316/why-cant-i-join-this-tuple-in-python

onepiece = station_info[0]
twopiece = ' FT NAM MOS '

elevenpiece =  datetime.datetime.today().strftime('%H%M')
elevenpiece = [elevenpiece,'Z']
elevenpiece = ''.join(elevenpiece)
#print(elevenpiece)

threepiece =  datetime.datetime.today().strftime('%d')
fourpiece = time[0][:2]
fivepiece = [threepiece,fourpiece]
fivepiece=''.join(fivepiece)

sixpiece = str(datetime.date.today() + datetime.timedelta(days=3))
sevenpiece = sixpiece[-2:] 
eightpiece = int(time[len(time)-1][:2])+3
eightpiece = ''.join(['0',str(eightpiece)])
ninepiece = [sevenpiece,eightpiece]
ninepiece =''.join(ninepiece)

tenpiece = [fivepiece,ninepiece]
tenpiece ='/'.join(tenpiece)

tenpiece = [onepiece,twopiece,tenpiece,' ',elevenpiece,new_data[0][6:]]
tenpiece =''.join(tenpiece)
print(tenpiece)
new_data = new_data[1:len(new_data)] 

for values in new_data:
  print(values);

print(' ')
#===================================================================================
#===================================================================================
#===================================================================================

html = urlopen(quote_page2)
#print(html.read())

soup = BeautifulSoup(html,"html.parser")
text = str(soup.find_all('pre'))
lines=text.splitlines()
#print(lines)

#===================================================================================
#STATION INFO
station_info = lines[1].split()
#print(str(station_info))
station_name = 'STATION NAME: '+station_info[0]
#print(str(station_name))
initalized_time = 'INITIALIZED TIME: ' + station_info[6] +'Z'
#print(str(initalized_time))
#===================================================================================
#===================================================================================
#TIME_VECTOR
time_vector = lines[3].split()
#print(time_vector)
time_vector = (time_vector[1:9])
#print(time_vector)
#time = ['']*len(time_vector)
#print(time)
#print(time_vector)
time = [ s + '00' for s in time_vector]
#print(time)
fm_times=["FM" + s for s in time]
#print(fm_times)
#===================================================================================
#===================================================================================
#TEMP_VECTOR
temp = lines[5].split()
#print(temp)
temp = temp[1:9]
temp_new = [int(x) for x in temp]
#print(type(temp))
temp_c = [(round(((y - 32) * 5.0 / 9.0))) for y in temp_new]
#print(type(temp_c))
temp_c=map(str,temp_c)
final_temp_c=[x.replace('-', 'M') for x in temp_c]
#print(final_temp_c)
#===================================================================================
#===================================================================================
#DEW_POINT_TEMP_VECTOR
dew_point = lines[6].split()
#print(temp)
dew_point = dew_point[1:9]
dew_point_new = [int(x) for x in dew_point]
#print(type(temp))
dew_point_c = [(round(((y - 32) * 5.0 / 9.0))) for y in dew_point_new]
#print(type(dew_point_c))
dew_point_c=map(str,dew_point_c)
final_dew_point_c=[x.replace('-', 'M') for x in dew_point_c]
#print(final_dew_point_c)

[final_temp_c,'/',final_dew_point_c]
full_temp=['/'.join(map(str, i)) for i in zip(final_temp_c, final_dew_point_c)]
#===================================================================================
#===================================================================================
#WIND DIRECTION 
wind_dir = lines[8].split()
wind_dir = wind_dir[1:9]
wind_dir=list(map(lambda k: k+'0', wind_dir))
#print(wind_dir)
#===================================================================================
#===================================================================================
#WIND SPEED
wind_spd = lines[9].split()
wind_spd = wind_spd[1:9]
wind_spd=list(map(lambda k: k+'KT', wind_spd))
#print(wind_spd)
#===================================================================================
#===================================================================================
#COMBINING WIND DIRECTION AND WIND SPEED
wind=[''.join(map(str, i)) for i in zip(wind_dir, wind_spd)]
#print(wind)
full_wind=['/'.join(map(str, i)) for i in zip(wind_dir, wind_spd)]
#print(full_wind)
#===================================================================================
#===================================================================================
#CLOUD TYPE  
cloud_type = lines[7].split()
#print(cloud_type)
cloud_type = cloud_type[1:9]
#print(cloud_type)
#===================================================================================
#===================================================================================
#CLOUD HEIGHT
cloud_height = lines[20].split()
#print(cloud_height)
cloud_height = cloud_height[1:9]
#print(cloud_height)
#===================================================================================
#===================================================================================
#COMBINING CLOUD TYPE AND CLOUD HEIGHT
zipped_height_types=[''.join(map(str, i)) for i in zip(cloud_type, cloud_height)]
#print(zipped_height_types)

cloud_type_hash={ 'CL':'SKC', 'FW':'FEW', 'SC':'SCT', 'BK':'BKN', 'OV':'OVC' }

cloud_height_hash={ '1': ' 200', '2' : ' 200-400', '3' : ' 500-900', '4' : ' 1000-1900', '5' : ' 2000-3000','6' : ' 3100-6500', '7' : ' 6600-12000', '8' : ' 12000' }
results = []
for ht in zipped_height_types:
 htype = ht[:2]
 val = ht[2:]
 res = cloud_type_hash[htype] + cloud_height_hash[val]
 results.append(res)
 #print(zipped_full_clouds)
 #print(type(zipped_full_clouds))
#print(results) 
#===================================================================================
#===================================================================================
#VISIBILITY
vis = lines[21].split()
vis = vis[1:len(vis)]

visibility_hash={ '1':'M1/2SM FG', '2':'1/2SM-1SM FG/BR', '3':'1SM-2SM BR', '4':'2SM-3SM BR', '5':'3SM-5SM BR', '6':'6SM BR', '7':'P6SM'}
visresults = []
for v in vis:
 val = v[:2]
 res = visibility_hash[val] 
 visresults.append(res)


#print(vis)

x = zip(fm_times, full_wind, results, visresults, full_temp)
#for values in x:
#  print(values);

new_data = list(' '.join(w) for w in x)
#print(new_data)

#https://stackoverflow.com/questions/1815316/why-cant-i-join-this-tuple-in-python

onepiece = station_info[0]
twopiece = ' FT GFS MOS '

elevenpiece =  datetime.datetime.today().strftime('%H%M')
elevenpiece = [elevenpiece,'Z']
elevenpiece = ''.join(elevenpiece)
#print(elevenpiece)

threepiece =  datetime.datetime.today().strftime('%d')
fourpiece = time[0][:2]
fivepiece = [threepiece,fourpiece]
fivepiece=''.join(fivepiece)

sixpiece = str(datetime.date.today() + datetime.timedelta(days=3))
sevenpiece = sixpiece[-2:] 
eightpiece = int(time[len(time)-1][:2])+3
eightpiece = ''.join(['0',str(eightpiece)])
ninepiece = [sevenpiece,eightpiece]
ninepiece =''.join(ninepiece)

tenpiece = [fivepiece,ninepiece]
tenpiece ='/'.join(tenpiece)

tenpiece = [onepiece,twopiece,tenpiece,' ',elevenpiece,new_data[0][6:]]
tenpiece =''.join(tenpiece)
print(tenpiece)
new_data = new_data[1:len(new_data)] 

for values in new_data:
  print(values);

print(' ')
#===================================================================================
#===================================================================================
#===================================================================================
