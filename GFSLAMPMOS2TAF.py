
#import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re 

station_id = "KDFW" 
short_station_id = station_id[1:4]
short_station_id = station_id[1:4]
      
def metartext_function(): 
    """
    Extracts Raw METAR(s) for the passed 3 hours from the Aviation Weather Center website 
    Returns: Raw METAR(s) Type - List 
    """
    quote_page = "https://www.aviationweather.gov/metar/data?ids="+station_id+"&format=raw&date=&hours=3"
    html = urlopen(quote_page)
    soup = BeautifulSoup(html,"html.parser")
    text = str(soup.find_all('code'))
    def remove_html_tags():
        """Remove html tags from a string"""
        clean = re.compile('<.*?>')
        clean = re.sub(clean, '', text)
        return(clean)
    cleantext=remove_html_tags() 
    cleantext=re.split(",",cleantext)
    return(cleantext)

def linestext_function():  
    """
    Extracts GFS LAMP MOS data 
    Returns: Return GFS LAMP MOS between <PRE> & </PRE>
    """
    quote_page = "http://www.nws.noaa.gov/cgi-bin/lamp/getlav.pl?sta="+station_id
    html = urlopen(quote_page)
    soup = BeautifulSoup(html,"html.parser")
    text = str(soup.find_all('pre'))
    lines=text.splitlines()
    return(lines)

lines = linestext_function()
#print(lines)

def station_info_function(): 
    """
    Extracts Station Info
    Returns: Station Info
    """ 
    station_info = lines[1].split() 
    return(station_info)

def station_name_function(): 
    """
    Extracts Station Name
    Returns: Station Name
    """ 
    station_info = lines[1].split()
    station_name = 'STATION NAME: '+station_info[0]
    return(station_name)

def initalized_time_function(): 
    """
    Extracts Initalized Time
    Returns: Initalized Time
    """ 
    station_info = lines[1].split()
    initalized_time = 'INITIALIZED TIME: ' + station_info[6] +'Z'
    return(initalized_time)

def fm_times_function(): 
    """
    Extracts Time From the GFS LAMP MOS data 
    Returns: XXXXZ (i.e. fm_times)        
    """ 
    time_vector = lines[2].split()
    time_vector = (time_vector[1:len(time_vector)])
    time = [ s + '00' for s in time_vector]
    fm_times=[s +"Z" for s in time]
    return(fm_times)

def times_function(): 
    """
    Extracts Time From the GFS LAMP MOS data 
    Returns: XXXX time 
    """ 
    time_vector = lines[2].split()
    time_vector = (time_vector[1:len(time_vector)])
    time = [ s + '00' for s in time_vector]
    return(time)

def temp_function(): 
    """
    Extracts Temperature From the GFS LAMP MOS data 
    Returns: Temperature M02 or 02 depending on negative and postive integars 
    """ 
    temp=lines[3].split()
    temp=temp[1:len(temp)]
    temp_new=[int(x) for x in temp]
    temp_c=[(round(((y-32)*5.0/9.0))) for y in temp_new]
    results = []
    for values in temp_c:
        res=[]
        v=()
        v=len(str(values))
        if values < 0 and v <= 2:
            res=str(values).replace('-', 'M0')
        elif values>0 and v == 1:
            res='0'+str(values)
        elif values < 0 and v >= 3:
            res=str(values).replace('-', 'M')
        elif values==0:
            res=str(values) + '0'
        elif values>0:
            res=str(values) 
        results.append(res)
    final_temp_c = results        
    return(final_temp_c)    
    
def dewpointtemp_function(): 
    """
    Extracts Dewpoint Temperature from the GFS LAMP MOS data 
    Returns: Dew Point Temperature M02 or 02 depending on negative and postive integars 
    """ 
    dew_point = lines[4].split()
    dew_point = dew_point[1:len(dew_point)]
    dew_point_new = [int(x) for x in dew_point]
    dew_point_c = [(round(((y-32)*5.0/9.0))) for y in dew_point_new]
    results =[]
    for values in dew_point_c:
        res=[]
        v=()
        v=len(str(values))
        if values < 0 and v <= 2:
            res=str(values).replace('-', 'M0')
        elif values>0 and v == 1:
            res='0'+str(values)
        elif values < 0 and v >= 3:
            res=str(values).replace('-', 'M')
        elif values==0:
            res=str(values) + '0'
        elif values>0:
            res=str(values) 
        results.append(res)
    final_dew_point_c = results
    return(final_dew_point_c)  

def full_temp_function():
    """
    Extracts Full Temperature from the GFS LAMP MOS data 
    Returns: Full Temperature XX/XX if single digit or negative will add M for negative and 0 for single digit for format
    """ 
    full_temp=['/'.join(map(str, i)) for i in zip(temp_function(),dewpointtemp_function())]
    return(full_temp)

def wind_dir_function(): 
    """
    Extracts Wind Direction from the GFS LAMP MOS data 
    Returns: Wind Direction DIR
    """ 
    wind_dir = lines[5].split()
    wind_dir = wind_dir[1:len(wind_dir)]
    wind_dir=list(map(lambda k: k+'0', wind_dir))
    return(wind_dir)

def wind_spd_function():
    """
    Extracts Wind Speed from the GFS LAMP MOS data Line 6 ***See Reference*** 
    Returns: Wind Speed XX or XXX
    """ 
    wind_spd = lines[6].split()
    wind_spd = wind_spd[1:len(wind_spd)]
    return(wind_spd)

def wind_gusts_function():
    """
    Extracts Wind Gusts from the GFS LAMP MOS data Line 7 ***See Reference*** 
    Returns: Wind Speed XX or XXX
    """ 
    wind_gusts = lines[7].split()
    wind_gusts = wind_gusts[1:len(wind_gusts)]
    wind_gusts=[x.replace('NG', '//') for x in wind_gusts]
    wind_gusts=list(map(lambda k: 'G'+k+'KT', wind_gusts))
    return(wind_gusts)

def full_wind_function():
    """
    Inputs wind_spd_function, wind_gusts_function, & wind_dir_function from the GFS LAMP MOS data ***See Reference*** 
    Returns: Full Wind DIRXXGXXKT
    """ 
    wind=[''.join(map(str, i)) for i in zip(wind_dir_function(), wind_spd_function(),wind_gusts_function())]
    full_wind=[''.join(map(str, i)) for i in zip(wind_dir_function(), wind_spd_function(),wind_gusts_function())]
    return(full_wind)

def split(s, n):
    if len(s) < n:
        return []
    else:
        return [s[:n]] + split(s[n:], n) 

def precip_prob_function():
    """
    Extracts Precipitation Probability from the GFS LAMP MOS data from Line 9  ***See Reference*** 
    Returns: PXXX if x=100 or x>=99 then P XX
    """ 
    precip_prob=lines[8]
    precip_prob = precip_prob [5:len(precip_prob )]
    precip_prob = split(precip_prob ,3)
    pcp = ['P']*len(precip_prob)
    zipped_precip_prob = [''.join(map(str, i)) for i in zip(pcp, precip_prob)]
    return(zipped_precip_prob)

def snow_precip_prob_function():
    """
    Extracts Snow Precipitation Probability from the GFS LAMP MOS data from Line 16 ***See Reference*** 
    Returns: SXXX if x=100 or x>=99 then S XX
    """ 
    lol = lines[16]
    lol = lol[5:len(lol)]
    snow_prob = split(lol, 3)
    pcp = ['S ']*len(snow_prob)
    zipped_snow_prob = [''.join(map(str, i)) for i in zip(pcp, snow_prob)]
    return(zipped_snow_prob)

def ice_precip_prob_function():
    """
    Extracts Snow Precipitation Probability from the GFS LAMP MOS data from Line 15 ***See Reference*** 
    Returns: IXXX if x=100 or x>=99 then I XX
    """ 
    lol = lines[15]
    lol = lol[5:len(lol)]
    ice_prob = split(lol, 3)
    pcp = ['I ']*len(ice_prob)
    zipped_ice_prob =[''.join(map(str, i)) for i in zip(pcp, ice_prob)]
    return(zipped_ice_prob)

def all_precip_prob_function():
    """
    Input Any Preciptation, Snow Precipitation, and Ice Precipitation Probability from the GFS LAMP MOS data ***See Reference*** 
    Returns: PXXX SXXX IXXX if x=100 or x>=99 then P XX S XX I XX
    """ 
    zippy_precip_prob = [' '.join(map(str, i)) for i in zip(precip_prob_function(),snow_precip_prob_function(),ice_precip_prob_function())]
    return(zippy_precip_prob)

def cloud_type_function():
    """
    Extracts Cloud Type from the GFS LAMP MOS data 
    Returns: Cloud Type SKC,FEW,SCT,BKN,OVC
    """ 
    cloud_type = lines[18].split()
    cloud_type = cloud_type[1:len(cloud_type)]
    return(cloud_type)

def cloud_height_function():
    """
    Extracts Cloud Height from the GFS LAMP MOS data 
    Returns: Cloud Height XXX
    """ 
    cloud_height = lines[19].split()
    cloud_height = cloud_height[1:len(cloud_height)]
    return(cloud_height)

def full_cloud_function():
    """
    Extracts Full Cloud from the GFS LAMP MOS data 
    Returns: Full Cloud XXX
    """ 
    zipped_height_types=[''.join(map(str, i)) for i in zip(cloud_type_function(), cloud_height_function())]
    cloud_type_hash={ 'CL':'SKC', 'FW':'FEW', 'SC':'SCT', 'BK':'BKN', 'OV':'OVC' }
    cloud_height_hash={ '1': ' 200       ', '2' : ' 200-400   ', '3' : ' 500-900   ', '4' : ' 1000-1900 ', '5' : ' 2000-3000 ','6' : ' 3100-6500 ', '7' : ' 6600-12000', '8' : ' 12000     ' }
    results = []
    for ht in zipped_height_types:
        htype = ht[:2]
        val = ht[2:]
        res = cloud_type_hash[htype] + cloud_height_hash[val]
        results.append(res)
    clouds_results=[x.replace('SKC 12000', 'CLR      ') for x in results]
    return(clouds_results)

def full_vis_function():
    """
    Extracts Full Cloud from the GFS LAMP MOS data 
    Returns: Visibility i.e. P6SM, 5SM-3SM BR, 3SM-1SM BR
    """ 
    vis = lines[21].split()
    vis = vis[1:len(vis)]
    visibility_hash={ '1':'M1/2SM FG      ', '2':'1/2SM-1SM FG/BR', '3':'1SM-2SM BR     ', '4':'2SM-3SM BR     ', '5':'3SM-5SM BR     ', '6':'6SM BR         ', '7':'P6SM           '}
    visresults = []
    for v in vis:
        val = v[:2]
        res = visibility_hash[val] 
        visresults.append(res)
    return(visresults)

def final_taf_format():
    """
    Extracts Final TAF Format from the GFS LAMP MOS data 
    Returns: TAF FORMAT 24 hours 
    """ 
    x = list(zip(fm_times_function(),full_wind_function(),full_vis_function(),full_cloud_function(), full_temp_function(), all_precip_prob_function()))
    new_data = list(' '.join(w) for w in x)
    onepiece = str(station_info_function())
    twopiece = ' FT GFS LAMP '
    elevenpiece =  datetime.datetime.today().strftime('%H%M')
    elevenpiece = [elevenpiece,'Z']
    elevenpiece = ''.join(elevenpiece)
    threepiece =  datetime.datetime.today().strftime('%d')
    time=times_function()
    fourpiece = (time[0][:2])
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
    print(' ')
    print('REQUESTED:',elevenpiece)
    print('GFS LAMP TERMINAL AERODROME FORECAST ***', station_id, '*** WITH CURRENT PAST THREE HOUR ROUTINE AND SPECI METAR(s)')
    print(' ')
    
    raw_metars = metartext_function()
    raw_metars=reversed(raw_metars)

    for values_00 in raw_metars:
        values_00 = values_00[8:]
        values_00 = values_00.replace(station_id, "")
        values_00= re.split("[A-Za-z][0-9]{4}",values_00)
        print(values_00[0])

    print(' ')
    new_data = new_data[0:len(new_data)] 

    for values in new_data:
        print(values);

final_taf_format() 
