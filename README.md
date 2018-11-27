# MOS2TAF

This module is supposed to make it easy for Operational Meteorologists to output MOS data in a TAF format. 

For example: 


 	KIND   INDIANAPOLIS          GFS LAMP GUIDANCE  11/27/2018  0600 UTC            
	UTC  07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 00 01 02 03 04 05 06 07
	TMP  25 24 24 23 23 23 21 21 22 22 22 22 22 22 22 22 21 21 21 21 21 20 20 20 19 
 	DPT  20 19 19 19 18 18 17 17 16 16 15 15 16 16 16 15 15 15 15 15 15 15 15 14 14 
 	WDR  27 27 27 27 27 27 27 27 27 27 28 28 28 28 28 29 29 29 29 29 29 28 28 28 28 
 	WSP  13 13 12 11 11 11 10 10 10 11 12 12 13 13 13 13 13 13 12 11 11 10 10 09 08 
 	WGS  NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG 
 	PPO  36 25 17 33 29 24  4 17 15 10 11  3  2  1  1  0  0  0  0  0  1  2  3  9  7 
 	PCO   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N 
 	P06                 18                 9                 1                 1    
 	LP1   0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 
 	LC1   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N 
 	CP1   0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 
 	CC1   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N 
 	POZ   5  6  7  7  8  8  9  9  9  9  8  8  8  7  8  8  8  9 10  1  1  0  0  0  0 
 	POS  95 95 93 93 92 92 91 91 91 91 92 92 92 92 92 91 91 90 89 99 99100100100100 
 	TYP   S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S 
 	CLD  OV OV OV OV OV OV OV OV OV OV BK BK BK BK BK BK BK OV OV OV OV OV OV OV OV 
 	CIG   4  4  4  4  4  4  4  4  4  4  5  5  5  5  5  5  5  5  6  5  5  5  5  5  5 
 	CCG   4  4  4  4  4  4  4  4  4  4  5  5  5  5  5  5  5  5  6  6  5  5  6  6  6 
 	VIS   7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7 
 	CVS   6  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  7  7  7  7  7  7  7  7 
 	OBV   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N 
	
	where the variables definated by the NWS 
	
	UTC Hour of the day in UTC time. This is the hour at which the forecast is valid, or if the forecast is valid for a period, the end of the forecast period.
	TMP surface temperature valid at that hour.
	DPT surface dewpoint valid at that hour.
	WDR forecasts of the 10-meter wind direction at the hour, given in tens of degrees.
	WSP forecasts of the 10-meter wind speed at the hour, given in knots.
	WGS forecasts of the 10-meter wind gust at the hour, given in knots.  "NG" means that no gust is forecast.
	PPO probability of precipitation occurring on the hour.  The precipitation need not be measurable.
	P06 probability of measurable precipitation (PoP) during a 6-h period ending at that time.
	PCO categorical forecast of yes (Y) or no (N) indicating if precipitation, not necessarily measurable, will occur on the hour.
	LP1 probability of lightning (at least one total lightning flash) occurring during the 1-hr period ending at the indicated time.
	LC1 categorical forecast of no (N), low (L), medium (M), or high (H) potential for lightning (at least one total lightning flash) occurring during the 1-hr period ending at the indicated time.
	CP1 probability of convection (at least one total lightning flash and/or radar reflectivity of 40dBZ or higher) occurring during the 1-hr period ending at the indicated time.
	CC1 categorical forecast of no (N), low (L), medium (M), or high (H) potential for convection (at least one total lightning flash and/or radar reflectivity of 40dBZ or higher) occurring during the 1-hr period ending at the indicated time.
	POZ* conditional probability of freezing pcp occurring at the hour.  This probability is conditional on precipitation occurring.
	POS* conditional probability of snow occurring at the hour.  This probability is conditional on precipitation occurring.
	TYP* conditional precipitation type at the hour.  This category forecast is conditional on precipitation occurring.
	CLD forecast categories of total sky cover valid at that hour.
	CIG ceiling height categorical forecasts at the hour.
	CCG conditional ceiling height categorical forecasts at the hour.   This category forecast is conditional on precipitation occurring.
	VIS visibility categorical forecasts at the hour.
	CVS conditional visibility categorical forecasts at the hour.   This category forecast is conditional on precipitation occurring.
	OBV obstruction to vision categorical forecasts at the hour.
#====================================================================================

 	KIND   GFS MOS GUIDANCE   11/27/2018  0000 UTC                      
 	DT /NOV  27            /NOV  28                /NOV  29          /  
 	HR   06 09 12 15 18 21 00 03 06 09 12 15 18 21 00 03 06 09 12 18 00 
 	X/N                    26          17          34          25    45 
 	TMP  25 21 19 22 23 23 21 21 20 19 18 23 31 33 29 27 27 27 27 41 42 
 	DPT  21 18 14 15 14 14 14 15 15 14 13 15 16 16 17 17 18 19 21 27 32 
 	CLD  OV OV OV BK BK OV OV OV OV SC CL CL FW OV OV OV OV OV OV OV OV 
 	WDR  28 28 27 28 28 28 29 29 28 28 26 25 25 23 19 17 15 12 13 17 16 
 	WSP  12 10 11 10 12 13 13 10 09 07 05 06 07 07 05 05 05 07 07 08 07 
 	P06         0     0     0     0     0     0     0     3    11 13 12 
 	P12                     0           1           0          11    24 
 	Q06         0     0     0     0     0     0     0     0     0  0  0 
 	Q12                     0           0           0           0     0 
 	T06      0/ 0  0/ 0  0/ 0  0/ 0  0/ 0  0/ 4  0/ 0  0/ 0  1/ 0  1/ 4 
 	T12            0/ 0        0/ 2        0/ 4        0/ 6     1/ 1    
 	POZ   0  0  2  1  0  1  2  1  0  0  0  0  0  0  2  4 11  9 18 11  1 
 	POS 100100 98 99100 99 96 98 98 98100 99100 95 98 92 75 75 46 20  0 
 	TYP   S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  R  R 
 	SNW                                 0                       0       
 	CIG   4  4  5  6  6  6  6  6  6  8  8  8  8  8  7  7  7  7  6  4  3 
 	VIS   7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  5 
 	OBV   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N BR 		
	
	 KIND   NAM MOS GUIDANCE   11/27/2018  0000 UTC                      
 	DT /NOV  27            /NOV  28                /NOV  29          /  
	 HR   06 09 12 15 18 21 00 03 06 09 12 15 18 21 00 03 06 09 12 18 00 
 	X/N                    31          16          34          27    42 
 	TMP  24 23 22 27 29 28 25 21 20 19 18 26 31 33 31 30 29 29 29 39 38 
	 DPT  18 18 17 17 16 15 15 14 14 13 13 15 15 15 16 18 20 22 24 29 32 
 	CLD  OV OV OV OV OV OV OV OV BK FW CL CL SC BK OV OV OV OV OV OV OV 
 	WDR  28 28 28 28 28 28 28 28 28 27 26 25 25 24 20 19 17 14 14 19 21 
 	WSP  14 11 12 11 13 13 11 11 10 08 07 07 08 08 05 06 06 06 07 08 07 
 	P06         1     1     0     0     0     0     2    10    12 29 19 
 	P12                     1           0           2          13    36 
 	Q06         0     0     0     0     0     0     0     0     0  0  0 
 	Q12                     0           0           0           0     0 
 	T06      0/ 0  0/ 2  0/ 1  1/ 1  0/ 3  0/ 2  0/ 0  1/ 1  1/ 0  1/ 9 
 	T12            0/ 2        1/ 1        0/ 3        1/ 1     1/ 0    
 	POZ   3  1  4  0  0  2  1  2  1  1  0  0  2  1  6  3 11 12 20 19  6 
 	POS  94 99 96 98 99 98 99 97 97 98 99 98 97 97 94 94 77 74 44 16 13 
 	TYP   S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  S  R  R 
 	SNW                                 0                       0       
 	CIG   5  5  5  5  5  5  6  6  6  8  8  8  8  8  8  7  7  7  6  3  5 
 	VIS   7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  5  6 
 	OBV   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N BR BR 
			
			
	where the variables definated by the NWS 
			
	DT = The day of the month, denoted by the standard three or four letter abbreviation 
	HR = Hour of the day in UTC time. This is the hour at which the forecast is valid, or if the forecast is valid for a period, the end of the forecast period. 
	N/X = nighttime minimum/daytime maximum surface temperatures. 
	TMP = surface temperature valid at that hour. 
	DPT = surface dewpoint valid at that hour. 
	CLD = forecast categories of total sky cover valid at that hour. 
	WDR = forecasts of the 10-meter wind direction at the hour, given in tens of degrees. 
	WSP = forecasts of the 10-meter wind speed at the hour, given in knots. 
	P06 = probability of precipitation (PoP) during a 6-h period ending at that time. 
	P12 = PoP during a 12-h period ending at that time. 
	Q06 = quantitative precipitation forecast (QPF) category for liquid equivalent precipitation amount during a 6-h period ending at that time. 
	Q12 = QPF category for liquid equivalent precipitation amount during a 12-h period ending at the indicated time. 
	SNW = snowfall categorical forecasts during a 24-h period ending at the indicated time. 
	T06 = probability of thunderstorms/conditional probability of severe thunderstorms during the 6-hr period ending at the indicated time. 
	T12 = probability of thunderstorms/conditional probability of severe thunderstorms during the 12-hr period ending at the indicated time. 
	POZ = conditional probability of freezing pcp occurring at the hour. 
	POS = conditional probability of snow occurring at the hour. 
	TYP = conditional precipitation type at the hour. 
	CIG = ceiling height categorical forecasts at the hour. 
	VIS = visibility categorical forecasts at the hour. 
	OBV = obstruction to vision categorical forecasts at the hour. 
						
	KIND FT GFS MOS 2706/3006 0723Z 280/12KT OVC 1000-1900 P6SM M4/M6
	FM0900 280/10KT OVC 1000-1900 P6SM M6/M8
	FM1200 270/11KT OVC 2000-3000 P6SM M7/M10
	FM1500 280/10KT BKN 3100-6500 P6SM M6/M9
	FM1800 280/12KT BKN 3100-6500 P6SM M5/M10
	FM2100 280/13KT OVC 3100-6500 P6SM M5/M10
	FM0000 290/13KT OVC 3100-6500 P6SM M6/M10
	FM0300 290/10KT OVC 3100-6500 P6SM M6/M9
	
	KIND FT NAM MOS 2706/3006 0723Z 280/14KT OVC 2000-3000 P6SM M4/M8
	FM0900 280/11KT OVC 2000-3000 P6SM M5/M8
	FM1200 280/12KT OVC 2000-3000 P6SM M6/M8
	FM1500 280/11KT OVC 2000-3000 P6SM M3/M8
	FM1800 280/13KT OVC 2000-3000 P6SM M2/M9	
	FM2100 280/13KT OVC 2000-3000 P6SM M2/M9
	FM0000 280/11KT OVC 3100-6500 P6SM M4/M9
	FM0300 280/11KT OVC 3100-6500 P6SM M6/M10


FORMAT: CCCC TTTT/TTTT HHHHZ WWWDDKT CIG hhhh-hhhh

	KIND FT GFS LAMP 2707/2808 0723Z 270/13KT OVC 1000-1900 P6SM M4/M7
	FM0800 270/13KT OVC 1000-1900 P6SM M4/M7 PRECIP: 25%  SN:  95%  IC:   6%  LGT:  7 %
	FM0900 270/12KT OVC 1000-1900 P6SM M4/M7 PRECIP: 17%  SN:  93%  IC:   7%  LGT:  7 %
	FM1000 270/11KT OVC 1000-1900 P6SM M5/M7 PRECIP: 33%  SN:  93%  IC:   7%  LGT:  8 %
	FM1100 270/11KT OVC 1000-1900 P6SM M5/M8 PRECIP: 29%  SN:  92%  IC:   8%  LGT:  8 %
	FM1200 270/11KT OVC 1000-1900 P6SM M5/M8 PRECIP: 24%  SN:  92%  IC:   8%  LGT:  9 %
	FM1300 270/10KT OVC 1000-1900 P6SM M6/M8 PRECIP:  4%  SN:  91%  IC:   9%  LGT:  9 %
	FM1400 270/10KT OVC 1000-1900 P6SM M6/M8 PRECIP: 17%  SN:  91%  IC:   9%  LGT:  9 %
	FM1500 270/10KT OVC 1000-1900 P6SM M6/M9 PRECIP: 15%  SN:  91%  IC:   9%  LGT:  9 %
	FM1600 270/11KT OVC 1000-1900 P6SM M6/M9 PRECIP: 10%  SN:  91%  IC:   9%  LGT:  8 %
	FM1700 280/12KT BKN 2000-3000 P6SM M6/M9 PRECIP: 11%  SN:  92%  IC:   8%  LGT:  8 %
	FM1800 280/12KT BKN 2000-3000 P6SM M6/M9 PRECIP:  3%  SN:  92%  IC:   8%  LGT:  8 %
	FM1900 280/13KT BKN 2000-3000 P6SM M6/M9 PRECIP:  2%  SN:  92%  IC:   8%  LGT:  7 %
	FM2000 280/13KT BKN 2000-3000 P6SM M6/M9 PRECIP:  1%  SN:  92%  IC:   7%  LGT:  8 %
	FM2100 280/13KT BKN 2000-3000 P6SM M6/M9 PRECIP:  1%  SN:  92%  IC:   8%  LGT:  8 %
	FM2200 290/13KT BKN 2000-3000 P6SM M6/M9 PRECIP:  0%  SN:  91%  IC:   8%  LGT:  8 %
	FM2300 290/13KT BKN 2000-3000 P6SM M6/M9 PRECIP:  0%  SN:  91%  IC:   8%  LGT:  9 %
	FM0000 290/13KT OVC 2000-3000 P6SM M6/M9 PRECIP:  0%  SN:  90%  IC:   9%  LGT: 10 %
	FM0100 290/12KT OVC 3100-6500 P6SM M6/M9 PRECIP:  0%  SN:  89%  IC:  10%  LGT:  1 %
	FM0200 290/11KT OVC 2000-3000 P6SM M6/M9 PRECIP:  0%  SN:  99%  IC:   1%  LGT:  1 %
	FM0300 290/11KT OVC 2000-3000 P6SM M6/M9 PRECIP:  1%  SN:  99%  IC:   1%  LGT:  0 %
	FM0400 280/10KT OVC 2000-3000 P6SM M7/M9 PRECIP:  2%  SN: 100%  IC:   0%  LGT:  0 %
	FM0500 280/10KT OVC 2000-3000 P6SM M7/M9 PRECIP:  3%  SN: 100%  IC:   0%  LGT:  0 %
	FM0600 280/09KT OVC 2000-3000 P6SM M7/M10 PRECIP:  9%  SN: 100%  IC:   0%  LGT:  0 %
