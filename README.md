# DryAsBone

Scrape and process pixels of a solar irradiance map

Specifically built for scraping the SERIS website for research on solar irradiance and intermittency  

main.py will run every 30s, which is when image updates on website

data.csv will contain both solar data (districts) and area weather (not related to districts).
Each point in scrape.py corresponds to each district in Singapore

Row[0] = datetime (YYMMDDHHMM format, Singaprore time)

Row[1-30] = Districts 1-30

Row[31-77] = Areas 1-47

<ol>
<li>1389,1120: D1
<li>1313,1141: D2
<li>1212,1082: D3
<li>1179,1149: D4
<li>990,1049: D5
<li>1338,1036: D6
<li>1389,1015: D7
<li>1368,952: D8
<li>1292,986: D9
<li>1128,948: D10
<li>1208,877: D11
<li>1397,868: D12
<li>1502,826: D13
<li>1590,919: D14
<li>1569,1011: D15
<li>1871,872: D16
<li>2039,726: D17
<li>1783,684: D18
<li>1527,654: D19
<li>1191,742: D20
<li>977,885: D21
<li>570,847: D22
<li>881,747: D23
<li>583,583: D24
<li>906,499: D25
<li>1107,591: D26
<li>1162,310: D27
<li>1405,541: D28
<li>444,1233: Jurong Island
<li>1254,1267: Sentosa
</ol>

weather is split into the following areas(+30 to index):
<ol>
<li>Ang Mo Kio
<li>Bedok
<li>Bishan
<li>Boon Lay
<li>Bukit Batok
<li>Bukit Merah
<li>Bukit Panjang
<li>Bukit Timah
<li>Central Water Catchment
<li>Changi
<li>Choa Chu Kang
<li>Clementi
<li>City
<li>Geylang
<li>Hougang
<li>Jalan Behar
<li>Jurong East
<li>Jurong Island
<li>Jurong West
<li>Kallang
<li>Lim Chu Kang
<li>Mandai
<li>Marine Parade
<li>Novena
<li>Pasir Ris
<li>Paya Lebar
<li>Pioneer
<li>Pulau Tekong
<li>Pulau Ubin
<li>Punggol
<li>Queenstown
<li>Selatar
<li>Sembawang
<li>Sengkang
<li>Sentosa
<li>Serangoon
<li>Southern Islands
<li>Sungei
<li>Tampines
<li>Tanglin
<li>Tengah
<li>Toa Payoh
<li>Tuas
<li>Western Islands
<li>Western Water Catchment
<li>Woodlands
<li>Yishun
</ol>

Weather codes are

<ol>
<li>fair
<li>fair & warm
<li>partly cloudy
<li>cloudy
<li>hazy
<li>slightly hazy
<li>windy
<li>mist
<li>light rain
<li>moderate rain
<li>heavy rain
<li>passing showers
<li>light showers
<li>showers
<li>heavy showers
<li>thundery showers
<li>heavy thundery showers
<li>heavy thundery showers with gusty winds
</ol>