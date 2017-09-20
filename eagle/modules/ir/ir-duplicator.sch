<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="8.3.1">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="50" name="dxf" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="53" name="tGND_GNDA" color="7" fill="9" visible="no" active="no"/>
<layer number="54" name="bGND_GNDA" color="1" fill="9" visible="no" active="no"/>
<layer number="56" name="wert" color="7" fill="1" visible="no" active="no"/>
<layer number="57" name="tCAD" color="7" fill="1" visible="no" active="no"/>
<layer number="59" name="tCarbon" color="7" fill="1" visible="no" active="no"/>
<layer number="60" name="bCarbon" color="7" fill="1" visible="no" active="no"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
<layer number="99" name="SpiceOrder" color="7" fill="1" visible="yes" active="yes"/>
<layer number="100" name="Muster" color="7" fill="1" visible="no" active="no"/>
<layer number="101" name="Patch_Top" color="12" fill="4" visible="yes" active="yes"/>
<layer number="102" name="Vscore" color="7" fill="1" visible="yes" active="yes"/>
<layer number="103" name="tMap" color="7" fill="1" visible="yes" active="yes"/>
<layer number="104" name="Name" color="16" fill="1" visible="yes" active="yes"/>
<layer number="105" name="tPlate" color="7" fill="1" visible="yes" active="yes"/>
<layer number="106" name="bPlate" color="7" fill="1" visible="yes" active="yes"/>
<layer number="107" name="Crop" color="7" fill="1" visible="yes" active="yes"/>
<layer number="108" name="tplace-old" color="10" fill="1" visible="yes" active="yes"/>
<layer number="109" name="ref-old" color="11" fill="1" visible="yes" active="yes"/>
<layer number="110" name="fp0" color="7" fill="1" visible="yes" active="yes"/>
<layer number="111" name="LPC17xx" color="7" fill="1" visible="yes" active="yes"/>
<layer number="112" name="tSilk" color="7" fill="1" visible="yes" active="yes"/>
<layer number="113" name="IDFDebug" color="4" fill="1" visible="yes" active="yes"/>
<layer number="114" name="Badge_Outline" color="7" fill="1" visible="yes" active="yes"/>
<layer number="115" name="ReferenceISLANDS" color="7" fill="1" visible="yes" active="yes"/>
<layer number="116" name="Patch_BOT" color="9" fill="4" visible="yes" active="yes"/>
<layer number="118" name="Rect_Pads" color="7" fill="1" visible="yes" active="yes"/>
<layer number="121" name="_tsilk" color="7" fill="1" visible="yes" active="yes"/>
<layer number="122" name="_bsilk" color="7" fill="1" visible="yes" active="yes"/>
<layer number="123" name="tTestmark" color="7" fill="1" visible="yes" active="yes"/>
<layer number="124" name="bTestmark" color="7" fill="1" visible="yes" active="yes"/>
<layer number="125" name="_tNames" color="7" fill="1" visible="yes" active="yes"/>
<layer number="126" name="_bNames" color="7" fill="1" visible="yes" active="yes"/>
<layer number="127" name="_tValues" color="7" fill="1" visible="yes" active="yes"/>
<layer number="128" name="_bValues" color="7" fill="1" visible="yes" active="yes"/>
<layer number="129" name="Mask" color="7" fill="1" visible="yes" active="yes"/>
<layer number="131" name="tAdjust" color="7" fill="1" visible="yes" active="yes"/>
<layer number="132" name="bAdjust" color="7" fill="1" visible="yes" active="yes"/>
<layer number="144" name="Drill_legend" color="7" fill="1" visible="yes" active="yes"/>
<layer number="150" name="Notes" color="7" fill="1" visible="yes" active="yes"/>
<layer number="151" name="HeatSink" color="7" fill="1" visible="yes" active="yes"/>
<layer number="152" name="_bDocu" color="7" fill="1" visible="yes" active="yes"/>
<layer number="153" name="FabDoc1" color="7" fill="1" visible="yes" active="yes"/>
<layer number="154" name="FabDoc2" color="7" fill="1" visible="yes" active="yes"/>
<layer number="155" name="FabDoc3" color="7" fill="1" visible="yes" active="yes"/>
<layer number="199" name="Contour" color="7" fill="1" visible="yes" active="yes"/>
<layer number="200" name="200bmp" color="1" fill="10" visible="yes" active="yes"/>
<layer number="201" name="201bmp" color="2" fill="10" visible="yes" active="yes"/>
<layer number="202" name="202bmp" color="3" fill="10" visible="yes" active="yes"/>
<layer number="203" name="203bmp" color="4" fill="10" visible="yes" active="yes"/>
<layer number="204" name="204bmp" color="5" fill="10" visible="yes" active="yes"/>
<layer number="205" name="205bmp" color="6" fill="10" visible="yes" active="yes"/>
<layer number="206" name="206bmp" color="7" fill="10" visible="yes" active="yes"/>
<layer number="207" name="207bmp" color="8" fill="10" visible="yes" active="yes"/>
<layer number="208" name="208bmp" color="9" fill="10" visible="yes" active="yes"/>
<layer number="209" name="209bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="210" name="210bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="211" name="211bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="212" name="212bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="213" name="213bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="214" name="214bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="215" name="215bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="216" name="216bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="217" name="217bmp" color="18" fill="1" visible="no" active="no"/>
<layer number="218" name="218bmp" color="19" fill="1" visible="no" active="no"/>
<layer number="219" name="219bmp" color="20" fill="1" visible="no" active="no"/>
<layer number="220" name="220bmp" color="21" fill="1" visible="no" active="no"/>
<layer number="221" name="221bmp" color="22" fill="1" visible="no" active="no"/>
<layer number="222" name="222bmp" color="23" fill="1" visible="no" active="no"/>
<layer number="223" name="223bmp" color="24" fill="1" visible="no" active="no"/>
<layer number="224" name="224bmp" color="25" fill="1" visible="no" active="no"/>
<layer number="225" name="225bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="226" name="226bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="227" name="227bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="228" name="228bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="229" name="229bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="230" name="230bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="231" name="231bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="248" name="Housing" color="7" fill="1" visible="yes" active="yes"/>
<layer number="249" name="Edge" color="7" fill="1" visible="yes" active="yes"/>
<layer number="250" name="Descript" color="3" fill="1" visible="no" active="no"/>
<layer number="251" name="SMDround" color="12" fill="11" visible="no" active="no"/>
<layer number="254" name="cooling" color="7" fill="1" visible="yes" active="yes"/>
<layer number="255" name="routoute" color="7" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="IoT">
<packages>
<package name="AX-1838HS">
<pad name="GND" x="0" y="0" drill="0.7" shape="octagon"/>
<pad name="OUT" x="-2.54" y="0" drill="0.7" shape="octagon"/>
<pad name="VCC" x="2.54" y="0" drill="0.7" shape="octagon"/>
<wire x1="-3.3" y1="2.25" x2="-3.3" y2="-2.25" width="0.127" layer="21"/>
<wire x1="3.3" y1="2.25" x2="3.3" y2="-2.25" width="0.127" layer="21"/>
<wire x1="3.3" y1="-2.25" x2="2.15" y2="-2.25" width="0.127" layer="21"/>
<wire x1="2.15" y1="-2.25" x2="-2.15" y2="-2.25" width="0.127" layer="21"/>
<wire x1="-2.15" y1="-2.25" x2="-3.3" y2="-2.25" width="0.127" layer="21"/>
<wire x1="-3.3" y1="2.25" x2="3.3" y2="2.25" width="0.127" layer="21"/>
<wire x1="-2.15" y1="-2.25" x2="2.15" y2="-2.25" width="0.127" layer="21" curve="180"/>
</package>
<package name="ESP8266-07">
<pad name="GPIO0" x="10" y="0" drill="1" diameter="1.2" shape="offset" rot="R180"/>
<pad name="GPIO2" x="10" y="-2" drill="1" diameter="1.2" shape="offset" rot="R180"/>
<pad name="GPIO15" x="10" y="-4" drill="1" diameter="1.2" shape="offset" rot="R180"/>
<pad name="GND" x="10" y="-6" drill="1" diameter="1.2" shape="offset" rot="R180"/>
<pad name="GPIO4" x="10" y="2" drill="1" diameter="1.2" shape="offset" rot="R180"/>
<pad name="GPIO5" x="10" y="4" drill="1" diameter="1.2" shape="offset" rot="R180"/>
<pad name="RXD0" x="10" y="6" drill="1" diameter="1.2" shape="offset" rot="R180"/>
<pad name="TXD0" x="10" y="8" drill="1" diameter="1.2" shape="offset" rot="R180"/>
<pad name="RST" x="-6" y="8" drill="1" diameter="1.2" shape="offset"/>
<pad name="ADC" x="-6" y="6" drill="1" diameter="1.2" shape="offset"/>
<pad name="EN" x="-6" y="4" drill="1" diameter="1.2" shape="offset"/>
<pad name="GPIO14" x="-6" y="0" drill="1" diameter="1.2" shape="offset"/>
<pad name="GPIO16" x="-6" y="2" drill="1" diameter="1.2" shape="offset"/>
<pad name="GPIO12" x="-6" y="-2" drill="1" diameter="1.2" shape="offset"/>
<pad name="GPIO13" x="-6" y="-4" drill="1" diameter="1.2" shape="offset"/>
<pad name="VCC" x="-6" y="-6" drill="1" diameter="1.2" shape="offset"/>
<wire x1="-6" y1="-7" x2="10" y2="-7" width="0.127" layer="21"/>
<wire x1="10" y1="-7" x2="10" y2="13" width="0.127" layer="21"/>
<wire x1="10" y1="13" x2="-6" y2="13" width="0.127" layer="21"/>
<wire x1="-6" y1="13" x2="-6" y2="-7" width="0.127" layer="21"/>
<text x="-3.46" y="10.19" size="1.27" layer="1">ESP8266-07</text>
</package>
<package name="ESP8266-07-HEADER">
<pad name="VCC" x="-6.5" y="-7" drill="0.7" diameter="1.5"/>
<pad name="GPIO13" x="-6.5" y="-5" drill="0.7" diameter="1.5"/>
<pad name="GPIO12" x="-6.5" y="-3" drill="0.7" diameter="1.5"/>
<pad name="GPIO14" x="-6.5" y="-1" drill="0.7" diameter="1.5"/>
<pad name="GPIO16" x="-6.5" y="1" drill="0.7" diameter="1.5"/>
<pad name="EN" x="-6.5" y="3" drill="0.7" diameter="1.5"/>
<pad name="ADC" x="-6.5" y="5" drill="0.7" diameter="1.5"/>
<pad name="GND" x="6.5" y="-7" drill="0.7" diameter="1.5"/>
<pad name="GPIO15" x="6.5" y="-5" drill="0.7" diameter="1.5"/>
<pad name="GPIO2" x="6.5" y="-3" drill="0.7" diameter="1.5"/>
<pad name="GPIO0" x="6.5" y="-1" drill="0.7" diameter="1.5"/>
<pad name="GPIO4" x="6.5" y="1" drill="0.7" diameter="1.5"/>
<pad name="GPIO5" x="6.5" y="3" drill="0.7" diameter="1.5"/>
<pad name="RXD0" x="6.5" y="5" drill="0.7" diameter="1.5"/>
<wire x1="-8" y1="-9.5" x2="-8" y2="11.7" width="0.127" layer="21"/>
<wire x1="-8" y1="-9.5" x2="8" y2="-9.5" width="0.127" layer="21"/>
<wire x1="8" y1="-9.5" x2="8" y2="11.7" width="0.127" layer="21"/>
<wire x1="-8" y1="11.7" x2="8" y2="11.7" width="0.127" layer="21"/>
<pad name="RST" x="-6.5" y="7" drill="0.7" diameter="1.5"/>
<pad name="TXD0" x="6.5" y="7" drill="0.7" diameter="1.5"/>
</package>
<package name="MICROUSB">
<wire x1="-4.7" y1="0" x2="-4.7" y2="4.8" width="0.127" layer="21"/>
<wire x1="-4.7" y1="4.8" x2="-4.7" y2="5.05" width="0.127" layer="21"/>
<wire x1="-4.7" y1="5.05" x2="4.7" y2="5.05" width="0.127" layer="21"/>
<wire x1="4.7" y1="5.05" x2="4.7" y2="4.8" width="0.127" layer="21"/>
<smd name="RX" x="0" y="0.675" dx="1.35" dy="0.4" layer="1" rot="R90"/>
<smd name="P$6" x="-3.1" y="0.8" dx="1.6" dy="2.1" layer="1" rot="R90"/>
<wire x1="4.7" y1="4.8" x2="4.7" y2="0" width="0.127" layer="21"/>
<wire x1="-4.7" y1="0" x2="4.7" y2="0" width="0.127" layer="21"/>
<smd name="P$1" x="3.1" y="0.8" dx="1.6" dy="2.1" layer="1" rot="R90"/>
<smd name="P$2" x="3.8" y="3.35" dx="1.9" dy="1.8" layer="1"/>
<smd name="P$3" x="-3.8" y="3.35" dx="1.9" dy="1.8" layer="1"/>
<smd name="P$5" x="-1.2" y="3.35" dx="1.9" dy="1.8" layer="1"/>
<smd name="P$7" x="1.2" y="3.35" dx="1.9" dy="1.8" layer="1"/>
<smd name="TX" x="0.65" y="0.675" dx="1.35" dy="0.4" layer="1" rot="R90"/>
<smd name="VCC" x="1.3" y="0.675" dx="1.35" dy="0.4" layer="1" rot="R90"/>
<smd name="GND" x="-1.3" y="0.675" dx="1.35" dy="0.4" layer="1" rot="R90"/>
<smd name="DEBUG" x="-0.65" y="0.675" dx="1.35" dy="0.4" layer="1" rot="R90"/>
<text x="0" y="1.905" size="0.4064" layer="2" rot="R180" align="center">MICRO USB</text>
<wire x1="-4.7" y1="4.8" x2="4.7" y2="4.8" width="0.127" layer="21"/>
</package>
<package name="SOT-223">
<wire x1="-3.25" y1="-1.75" x2="3.25" y2="-1.75" width="0.127" layer="21"/>
<wire x1="3.25" y1="-1.75" x2="3.25" y2="1.75" width="0.127" layer="21"/>
<wire x1="3.25" y1="1.75" x2="-3.25" y2="1.75" width="0.127" layer="21"/>
<wire x1="-3.25" y1="1.75" x2="-3.25" y2="-1.75" width="0.127" layer="21"/>
<smd name="P$1" x="0" y="3.1" dx="2.2" dy="3.5" layer="1" rot="R90"/>
<smd name="P$2" x="0" y="-3.1" dx="1.2" dy="2.2" layer="1"/>
<smd name="P$3" x="-2.3" y="-3.1" dx="2.2" dy="1.2" layer="1" rot="R90"/>
<smd name="P$4" x="2.3" y="-3.1" dx="1.2" dy="2.2" layer="1"/>
</package>
<package name="AYZ0202AGRL">
<wire x1="-2.5" y1="-2.25" x2="-2.5" y2="2.25" width="0.127" layer="22"/>
<wire x1="2.5" y1="-2.25" x2="2.5" y2="2.25" width="0.127" layer="21"/>
<wire x1="-2.5" y1="2.25" x2="2.5" y2="2.25" width="0.127" layer="21"/>
<wire x1="-2.5" y1="-2.25" x2="2.5" y2="-2.25" width="0.127" layer="21"/>
<smd name="4" x="-2.5" y="-2.25" dx="1.5" dy="1.5" layer="1"/>
<smd name="5" x="0" y="-2.25" dx="1.5" dy="1.5" layer="1"/>
<smd name="6" x="2.5" y="-2.25" dx="1.5" dy="1.5" layer="1"/>
<smd name="3" x="2.5" y="2.25" dx="1.5" dy="1.5" layer="1"/>
<smd name="2" x="0" y="2.25" dx="1.5" dy="1.5" layer="1"/>
<smd name="1" x="-2.5" y="2.25" dx="1.5" dy="1.5" layer="1"/>
<hole x="-1.5" y="0" drill="0.9"/>
<hole x="1.5" y="0" drill="0.9"/>
</package>
</packages>
<symbols>
<symbol name="AX-1838HS">
<wire x1="-2.54" y1="0" x2="7.62" y2="0" width="0.254" layer="94"/>
<wire x1="7.62" y1="0" x2="7.62" y2="12.7" width="0.254" layer="94"/>
<wire x1="7.62" y1="12.7" x2="-2.54" y2="12.7" width="0.254" layer="94"/>
<wire x1="-2.54" y1="12.7" x2="-2.54" y2="0" width="0.254" layer="94"/>
<pin name="OUT" x="0" y="-5.08" visible="pin" length="middle" rot="R90"/>
<pin name="GND" x="2.54" y="-5.08" visible="pin" length="middle" direction="pwr" rot="R90"/>
<pin name="VCC" x="5.08" y="-5.08" visible="pin" length="middle" direction="pwr" rot="R90"/>
<wire x1="1.27" y1="8.89" x2="1.27" y2="11.43" width="0.254" layer="94"/>
<wire x1="1.27" y1="11.43" x2="3.81" y2="11.43" width="0.254" layer="94"/>
<wire x1="3.81" y1="11.43" x2="3.81" y2="8.89" width="0.254" layer="94"/>
<wire x1="3.81" y1="8.89" x2="1.27" y2="8.89" width="0.254" layer="94"/>
<wire x1="1.27" y1="8.89" x2="3.81" y2="11.43" width="0.254" layer="94"/>
<wire x1="1.27" y1="11.43" x2="3.81" y2="8.89" width="0.254" layer="94"/>
</symbol>
<symbol name="ESP8266-07">
<pin name="VCC" x="-12.7" y="-7.62" visible="pin" length="short" direction="pwr"/>
<pin name="GPIO13" x="-12.7" y="-5.08" visible="pin" length="short"/>
<pin name="GPIO12" x="-12.7" y="-2.54" visible="pin" length="short"/>
<pin name="GPIO14" x="-12.7" y="0" visible="pin" length="short"/>
<pin name="GPIO16" x="-12.7" y="2.54" visible="pin" length="short"/>
<pin name="EN" x="-12.7" y="5.08" visible="pin" length="short" direction="in"/>
<pin name="ADC" x="-12.7" y="7.62" visible="pin" length="short" direction="in"/>
<pin name="RST" x="-12.7" y="10.16" visible="pin" length="short" direction="in"/>
<pin name="GND" x="12.7" y="-7.62" visible="pin" length="short" direction="pwr" rot="R180"/>
<pin name="RXD0" x="12.7" y="7.62" visible="pin" length="short" rot="R180"/>
<pin name="TXD0" x="12.7" y="10.16" visible="pin" length="short" rot="R180"/>
<pin name="GPIO5" x="12.7" y="5.08" visible="pin" length="short" rot="R180"/>
<pin name="GPIO4" x="12.7" y="2.54" visible="pin" length="short" rot="R180"/>
<pin name="GPIO0" x="12.7" y="0" visible="pin" length="short" rot="R180"/>
<pin name="GPIO2" x="12.7" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="GPIO15" x="12.7" y="-5.08" visible="pin" length="short" rot="R180"/>
<wire x1="-10.16" y1="-10.16" x2="10.16" y2="-10.16" width="0.254" layer="94"/>
<wire x1="10.16" y1="-10.16" x2="10.16" y2="17.78" width="0.254" layer="94"/>
<wire x1="10.16" y1="17.78" x2="-10.16" y2="17.78" width="0.254" layer="94"/>
<wire x1="-10.16" y1="17.78" x2="-10.16" y2="-10.16" width="0.254" layer="94"/>
<text x="-7.62" y="12.7" size="1.27" layer="94">ESP8266-07</text>
</symbol>
<symbol name="MICROUSB">
<wire x1="-7.62" y1="0" x2="7.62" y2="0" width="0.254" layer="94"/>
<wire x1="-7.62" y1="0" x2="-7.62" y2="2.54" width="0.254" layer="94"/>
<wire x1="-7.62" y1="2.54" x2="-5.08" y2="5.08" width="0.254" layer="94"/>
<wire x1="-5.08" y1="5.08" x2="5.08" y2="5.08" width="0.254" layer="94"/>
<wire x1="5.08" y1="5.08" x2="7.62" y2="2.54" width="0.254" layer="94"/>
<wire x1="7.62" y1="2.54" x2="7.62" y2="0" width="0.254" layer="94"/>
<pin name="GND" x="-5.08" y="-2.54" visible="pin" length="short" direction="pwr" rot="R90"/>
<pin name="DEBUG" x="-2.54" y="-2.54" visible="pin" length="short" rot="R90"/>
<pin name="RX" x="0" y="-2.54" visible="pin" length="short" rot="R90"/>
<pin name="TX" x="2.54" y="-2.54" visible="pin" length="short" rot="R90"/>
<pin name="VCC" x="5.08" y="-2.54" visible="pin" length="short" direction="pwr" rot="R90"/>
</symbol>
<symbol name="AZ1117E">
<wire x1="7.62" y1="0" x2="7.62" y2="7.62" width="0.254" layer="94"/>
<wire x1="7.62" y1="7.62" x2="-7.62" y2="7.62" width="0.254" layer="94"/>
<wire x1="-7.62" y1="7.62" x2="-7.62" y2="0" width="0.254" layer="94"/>
<wire x1="-7.62" y1="0" x2="7.62" y2="0" width="0.254" layer="94"/>
<pin name="GND" x="10.16" y="5.08" visible="pin" length="short" direction="pwr" rot="R180"/>
<pin name="IN" x="-10.16" y="5.08" visible="pin" length="short" direction="in"/>
<pin name="OUT" x="-10.16" y="2.54" visible="pin" length="short" direction="out"/>
</symbol>
<symbol name="AYZ0202AGRL">
<wire x1="0" y1="0" x2="0" y2="10.16" width="0.254" layer="94"/>
<wire x1="0" y1="10.16" x2="7.62" y2="10.16" width="0.254" layer="94"/>
<wire x1="7.62" y1="10.16" x2="7.62" y2="0" width="0.254" layer="94"/>
<wire x1="7.62" y1="0" x2="0" y2="0" width="0.254" layer="94"/>
<pin name="3" x="-2.54" y="7.62" length="short"/>
<pin name="2" x="-2.54" y="5.08" length="short"/>
<pin name="1" x="-2.54" y="2.54" length="short"/>
<pin name="6" x="10.16" y="7.62" length="short" rot="R180"/>
<pin name="5" x="10.16" y="5.08" length="short" rot="R180"/>
<pin name="4" x="10.16" y="2.54" length="short" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="AX-1838HS">
<gates>
<gate name="G$1" symbol="AX-1838HS" x="-2.54" y="-2.54"/>
</gates>
<devices>
<device name="" package="AX-1838HS">
<connects>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="OUT" pad="OUT"/>
<connect gate="G$1" pin="VCC" pad="VCC"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="ESP8266-07">
<gates>
<gate name="G$1" symbol="ESP8266-07" x="-5.08" y="5.08"/>
</gates>
<devices>
<device name="SMD" package="ESP8266-07">
<connects>
<connect gate="G$1" pin="ADC" pad="ADC"/>
<connect gate="G$1" pin="EN" pad="EN"/>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="GPIO0" pad="GPIO0"/>
<connect gate="G$1" pin="GPIO12" pad="GPIO12"/>
<connect gate="G$1" pin="GPIO13" pad="GPIO13"/>
<connect gate="G$1" pin="GPIO14" pad="GPIO14"/>
<connect gate="G$1" pin="GPIO15" pad="GPIO15"/>
<connect gate="G$1" pin="GPIO16" pad="GPIO16"/>
<connect gate="G$1" pin="GPIO2" pad="GPIO2"/>
<connect gate="G$1" pin="GPIO4" pad="GPIO4"/>
<connect gate="G$1" pin="GPIO5" pad="GPIO5"/>
<connect gate="G$1" pin="RST" pad="RST"/>
<connect gate="G$1" pin="RXD0" pad="RXD0"/>
<connect gate="G$1" pin="TXD0" pad="TXD0"/>
<connect gate="G$1" pin="VCC" pad="VCC"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="HEADER" package="ESP8266-07-HEADER">
<connects>
<connect gate="G$1" pin="ADC" pad="ADC"/>
<connect gate="G$1" pin="EN" pad="EN"/>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="GPIO0" pad="GPIO0"/>
<connect gate="G$1" pin="GPIO12" pad="GPIO12"/>
<connect gate="G$1" pin="GPIO13" pad="GPIO13"/>
<connect gate="G$1" pin="GPIO14" pad="GPIO14"/>
<connect gate="G$1" pin="GPIO15" pad="GPIO15"/>
<connect gate="G$1" pin="GPIO16" pad="GPIO16"/>
<connect gate="G$1" pin="GPIO2" pad="GPIO2"/>
<connect gate="G$1" pin="GPIO4" pad="GPIO4"/>
<connect gate="G$1" pin="GPIO5" pad="GPIO5"/>
<connect gate="G$1" pin="RST" pad="RST"/>
<connect gate="G$1" pin="RXD0" pad="RXD0"/>
<connect gate="G$1" pin="TXD0" pad="TXD0"/>
<connect gate="G$1" pin="VCC" pad="VCC"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="MICROUSB">
<gates>
<gate name="G$1" symbol="MICROUSB" x="0" y="2.54"/>
</gates>
<devices>
<device name="609-4613-1-ND" package="MICROUSB">
<connects>
<connect gate="G$1" pin="DEBUG" pad="DEBUG"/>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="RX" pad="RX"/>
<connect gate="G$1" pin="TX" pad="TX"/>
<connect gate="G$1" pin="VCC" pad="VCC"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="AZ1117E">
<description>&lt;b&gt;AZ1117E&lt;/b&gt; - 3.3 volt regulator

&lt;p&gt;Technical Specifications:
&lt;ul&gt;
&lt;li&gt;Max Current 1.3 A&lt;/li&gt;
&lt;/ul&gt;
&lt;/p&gt;

&lt;p&gt;Connect 1.0 uF cap from GND to IN&lt;br/&gt;
Connect 1.0 uF cap from GND to OUT&lt;/p&gt;</description>
<gates>
<gate name="G$1" symbol="AZ1117E" x="-2.54" y="-2.54"/>
</gates>
<devices>
<device name="" package="SOT-223">
<connects>
<connect gate="G$1" pin="GND" pad="P$3" route="any"/>
<connect gate="G$1" pin="IN" pad="P$4"/>
<connect gate="G$1" pin="OUT" pad="P$1 P$2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="AYZ0202AGRL">
<gates>
<gate name="G$1" symbol="AYZ0202AGRL" x="0" y="-2.54"/>
</gates>
<devices>
<device name="" package="AYZ0202AGRL">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="6" pad="6"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="SparkFun-LED">
<description>&lt;h3&gt;SparkFun LEDs&lt;/h3&gt;
This library contains discrete LEDs for illumination or indication, but no displays.
&lt;br&gt;
&lt;br&gt;
We've spent an enormous amount of time creating and checking these footprints and parts, but it is &lt;b&gt; the end user's responsibility&lt;/b&gt; to ensure correctness and suitablity for a given componet or application. 
&lt;br&gt;
&lt;br&gt;If you enjoy using this library, please buy one of our products at &lt;a href=" www.sparkfun.com"&gt;SparkFun.com&lt;/a&gt;.
&lt;br&gt;
&lt;br&gt;
&lt;b&gt;Licensing:&lt;/b&gt; Creative Commons ShareAlike 4.0 International - https://creativecommons.org/licenses/by-sa/4.0/ 
&lt;br&gt;
&lt;br&gt;
You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to sell your device using our footprint, you email us with a link to the product being sold. We want bragging rights that we helped (in a very small part) to create your 8th world wonder. We would like the opportunity to feature your device on our homepage.</description>
<packages>
<package name="LED_5MM">
<description>&lt;B&gt;LED 5mm PTH&lt;/B&gt;&lt;p&gt;
5 mm, round
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 2&lt;/li&gt;
&lt;li&gt;Pin pitch: 0.1inch&lt;/li&gt;
&lt;li&gt;Diameter: 5mm&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;LED-IR-THRU&lt;/li&gt;</description>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="1.905" width="0.2032" layer="22"/>
<wire x1="-1.143" y1="0" x2="0" y2="1.143" width="0.1524" layer="51" curve="-90" cap="flat"/>
<wire x1="0" y1="-1.143" x2="1.143" y2="0" width="0.1524" layer="51" curve="90" cap="flat"/>
<wire x1="-1.651" y1="0" x2="0" y2="1.651" width="0.1524" layer="51" curve="-90" cap="flat"/>
<wire x1="0" y1="-1.651" x2="1.651" y2="0" width="0.1524" layer="51" curve="90" cap="flat"/>
<wire x1="-2.159" y1="0" x2="0" y2="2.159" width="0.1524" layer="51" curve="-90" cap="flat"/>
<wire x1="0" y1="-2.159" x2="2.159" y2="0" width="0.1524" layer="51" curve="90" cap="flat"/>
<pad name="A" x="-1.27" y="0" drill="0.8128" diameter="1.8796"/>
<pad name="K" x="1.27" y="0" drill="0.8128" diameter="1.8796"/>
<text x="0" y="3.3909" size="0.6096" layer="25" font="vector" ratio="20" align="bottom-center">&gt;NAME</text>
<text x="0.0254" y="-3.3909" size="0.6096" layer="27" font="vector" ratio="20" align="top-center">&gt;VALUE</text>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="1.905" width="0.2032" layer="21"/>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="1.905" width="0.254" layer="21" curve="-286.260205" cap="flat"/>
<circle x="0" y="0" radius="2.54" width="0.1524" layer="21"/>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="1.905" width="0.2032" layer="51"/>
</package>
<package name="LTE-302">
<description>&lt;h3&gt;IR Emitter/Detector&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 2&lt;/li&gt;
&lt;li&gt;Pin pitch: 2.54mm&lt;/li&gt;
&lt;li&gt;Area: 2.25 x 4.4 mm&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;b&gt;Datasheet referenced for footprint&lt;/b&gt;&lt;a href="https://www.sparkfun.com/datasheets/Components/LTE-302.pdf"&gt; LTE-302&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;LTE-302&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;</description>
<wire x1="2.159" y1="0.762" x2="2.159" y2="-0.762" width="0.127" layer="21"/>
<wire x1="2.159" y1="-0.762" x2="0.762" y2="-0.762" width="0.127" layer="21"/>
<wire x1="0.762" y1="-0.762" x2="0.381" y2="-0.762" width="0.127" layer="21"/>
<wire x1="0.381" y1="-0.762" x2="-0.381" y2="-0.762" width="0.127" layer="21"/>
<wire x1="-0.381" y1="-0.762" x2="-0.762" y2="-0.762" width="0.127" layer="21"/>
<wire x1="-0.762" y1="-0.762" x2="-2.159" y2="-0.762" width="0.127" layer="21"/>
<wire x1="-2.159" y1="-0.762" x2="-2.159" y2="0.762" width="0.127" layer="21"/>
<wire x1="-2.159" y1="0.762" x2="-0.381" y2="0.762" width="0.127" layer="21"/>
<wire x1="-0.381" y1="0.762" x2="0.381" y2="0.762" width="0.127" layer="21"/>
<wire x1="0.381" y1="0.762" x2="2.159" y2="0.762" width="0.127" layer="21"/>
<wire x1="-0.381" y1="0" x2="0.381" y2="0.762" width="0.127" layer="21"/>
<wire x1="0.381" y1="0.762" x2="0.381" y2="-0.762" width="0.127" layer="21"/>
<wire x1="0.381" y1="-0.762" x2="-0.381" y2="0" width="0.127" layer="21"/>
<wire x1="-0.381" y1="0" x2="-0.381" y2="0.762" width="0.127" layer="21"/>
<wire x1="-0.381" y1="0" x2="-0.381" y2="-0.762" width="0.127" layer="21"/>
<wire x1="0.762" y1="-0.762" x2="-0.762" y2="-0.762" width="0.127" layer="21" curve="-180"/>
<pad name="A" x="1.27" y="0" drill="0.8"/>
<pad name="C" x="-1.27" y="0" drill="0.8"/>
<text x="-1.27" y="0.9525" size="0.6096" layer="25" font="vector" ratio="20">&gt;NAME</text>
<text x="-1.27" y="-1.5875" size="0.6096" layer="27" font="vector" ratio="20" align="top-left">&gt;VALUE</text>
<wire x1="0.762" y1="-0.762" x2="-0.762" y2="-0.762" width="0.127" layer="51" curve="-180"/>
</package>
</packages>
<symbols>
<symbol name="LED">
<description>&lt;h3&gt;LED&lt;/h3&gt;
&lt;p&gt;&lt;/p&gt;</description>
<wire x1="1.27" y1="0" x2="0" y2="-2.54" width="0.254" layer="94"/>
<wire x1="0" y1="-2.54" x2="-1.27" y2="0" width="0.254" layer="94"/>
<wire x1="1.27" y1="-2.54" x2="0" y2="-2.54" width="0.254" layer="94"/>
<wire x1="0" y1="-2.54" x2="-1.27" y2="-2.54" width="0.254" layer="94"/>
<wire x1="1.27" y1="0" x2="-1.27" y2="0" width="0.254" layer="94"/>
<wire x1="-2.032" y1="-0.762" x2="-3.429" y2="-2.159" width="0.1524" layer="94"/>
<wire x1="-1.905" y1="-1.905" x2="-3.302" y2="-3.302" width="0.1524" layer="94"/>
<text x="-3.429" y="-4.572" size="1.778" layer="95" font="vector" rot="R90">&gt;NAME</text>
<text x="1.905" y="-4.572" size="1.778" layer="96" font="vector" rot="R90" align="top-left">&gt;VALUE</text>
<pin name="C" x="0" y="-5.08" visible="off" length="short" direction="pas" rot="R90"/>
<pin name="A" x="0" y="2.54" visible="off" length="short" direction="pas" rot="R270"/>
<polygon width="0.1524" layer="94">
<vertex x="-3.429" y="-2.159"/>
<vertex x="-3.048" y="-1.27"/>
<vertex x="-2.54" y="-1.778"/>
</polygon>
<polygon width="0.1524" layer="94">
<vertex x="-3.302" y="-3.302"/>
<vertex x="-2.921" y="-2.413"/>
<vertex x="-2.413" y="-2.921"/>
</polygon>
</symbol>
</symbols>
<devicesets>
<deviceset name="LED-IR" prefix="D">
<description>&lt;h3&gt;Infrared LED (IR)&lt;/h3&gt;
&lt;p&gt;&lt;li&gt;&lt;b&gt; Wavelength: &lt;/b&gt; 940nm&lt;/li&gt;

&lt;/p&gt;

&lt;p&gt;
&lt;li&gt;&lt;b&gt;Packages:&lt;/b&gt;&lt;/li&gt;
&lt;ul&gt;&lt;li&gt;&lt;b&gt;TSAL6100&lt;/b&gt; &lt;/li&gt;
&lt;li&gt;&lt;b&gt; LTE302&lt;/b&gt; - Side firing. Check SparkFun-Sensors.lbr for the receiver&lt;/li&gt; 
&lt;ul&gt;&lt;/p&gt;

&lt;p&gt;&lt;b&gt;SparkFun Products:&lt;/b&gt;
&lt;ul&gt;&lt;li&gt;&lt;a href=”[https://www.sparkfun.com/products/12780]”&gt;ZX Distance and Gesture Sensor&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href=”https://www.sparkfun.com/products/241”&gt;Infrared Emitters and Detectors&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;</description>
<gates>
<gate name="G$1" symbol="LED" x="0" y="2.54"/>
</gates>
<devices>
<device name="TSAL6100" package="LED_5MM">
<connects>
<connect gate="G$1" pin="A" pad="A"/>
<connect gate="G$1" pin="C" pad="K"/>
</connects>
<technologies>
<technology name="">
<attribute name="PROD_ID" value="DIO-12058"/>
</technology>
</technologies>
</device>
<device name="SIDE_EMITTER" package="LTE-302">
<connects>
<connect gate="G$1" pin="A" pad="A"/>
<connect gate="G$1" pin="C" pad="C"/>
</connects>
<technologies>
<technology name="">
<attribute name="PROD_ID" value="DIO-10904" constant="no"/>
<attribute name="SF_ID" value="SEN-00241" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="SparkFun-Capacitors">
<description>&lt;h3&gt;SparkFun Capacitors&lt;/h3&gt;
This library contains capacitors. 
&lt;br&gt;
&lt;br&gt;
We've spent an enormous amount of time creating and checking these footprints and parts, but it is &lt;b&gt; the end user's responsibility&lt;/b&gt; to ensure correctness and suitablity for a given componet or application. 
&lt;br&gt;
&lt;br&gt;If you enjoy using this library, please buy one of our products at &lt;a href=" www.sparkfun.com"&gt;SparkFun.com&lt;/a&gt;.
&lt;br&gt;
&lt;br&gt;
&lt;b&gt;Licensing:&lt;/b&gt; Creative Commons ShareAlike 4.0 International - https://creativecommons.org/licenses/by-sa/4.0/ 
&lt;br&gt;
&lt;br&gt;
You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to sell your device using our footprint, you email us with a link to the product being sold. We want bragging rights that we helped (in a very small part) to create your 8th world wonder. We would like the opportunity to feature your device on our homepage.</description>
<packages>
<package name="0603">
<description>&lt;p&gt;&lt;b&gt;Generic 1608 (0603) package&lt;/b&gt;&lt;/p&gt;
&lt;p&gt;0.2mm courtyard excess rounded to nearest 0.05mm.&lt;/p&gt;</description>
<wire x1="-1.6" y1="0.7" x2="1.6" y2="0.7" width="0.0508" layer="39"/>
<wire x1="1.6" y1="0.7" x2="1.6" y2="-0.7" width="0.0508" layer="39"/>
<wire x1="1.6" y1="-0.7" x2="-1.6" y2="-0.7" width="0.0508" layer="39"/>
<wire x1="-1.6" y1="-0.7" x2="-1.6" y2="0.7" width="0.0508" layer="39"/>
<wire x1="-0.356" y1="0.432" x2="0.356" y2="0.432" width="0.1016" layer="51"/>
<wire x1="-0.356" y1="-0.419" x2="0.356" y2="-0.419" width="0.1016" layer="51"/>
<smd name="1" x="-0.85" y="0" dx="1.1" dy="1" layer="1"/>
<smd name="2" x="0.85" y="0" dx="1.1" dy="1" layer="1"/>
<text x="0" y="0.762" size="0.6096" layer="25" font="vector" ratio="20" align="bottom-center">&gt;NAME</text>
<text x="0" y="-0.762" size="0.6096" layer="27" font="vector" ratio="20" align="top-center">&gt;VALUE</text>
<rectangle x1="-0.8382" y1="-0.4699" x2="-0.3381" y2="0.4801" layer="51"/>
<rectangle x1="0.3302" y1="-0.4699" x2="0.8303" y2="0.4801" layer="51"/>
<rectangle x1="-0.1999" y1="-0.3" x2="0.1999" y2="0.3" layer="35"/>
</package>
<package name="0402">
<description>&lt;p&gt;&lt;b&gt;Generic 1005 (0402) package&lt;/b&gt;&lt;/p&gt;
&lt;p&gt;0.2mm courtyard excess rounded to nearest 0.05mm.&lt;/p&gt;</description>
<wire x1="-0.2704" y1="0.2286" x2="0.2704" y2="0.2286" width="0.1524" layer="51"/>
<wire x1="0.2704" y1="-0.2286" x2="-0.2704" y2="-0.2286" width="0.1524" layer="51"/>
<wire x1="-1.2" y1="0.65" x2="1.2" y2="0.65" width="0.0508" layer="39"/>
<wire x1="1.2" y1="0.65" x2="1.2" y2="-0.65" width="0.0508" layer="39"/>
<wire x1="1.2" y1="-0.65" x2="-1.2" y2="-0.65" width="0.0508" layer="39"/>
<wire x1="-1.2" y1="-0.65" x2="-1.2" y2="0.65" width="0.0508" layer="39"/>
<smd name="1" x="-0.58" y="0" dx="0.85" dy="0.9" layer="1"/>
<smd name="2" x="0.58" y="0" dx="0.85" dy="0.9" layer="1"/>
<text x="0" y="0.762" size="0.6096" layer="25" font="vector" ratio="20" align="bottom-center">&gt;NAME</text>
<text x="0" y="-0.762" size="0.6096" layer="27" font="vector" ratio="20" align="top-center">&gt;VALUE</text>
<rectangle x1="-0.554" y1="-0.3048" x2="-0.254" y2="0.3048" layer="51"/>
<rectangle x1="0.2588" y1="-0.3048" x2="0.5588" y2="0.3048" layer="51"/>
<rectangle x1="-0.1999" y1="-0.3" x2="0.1999" y2="0.3" layer="35"/>
</package>
<package name="0805">
<description>&lt;p&gt;&lt;b&gt;Generic 2012 (0805) package&lt;/b&gt;&lt;/p&gt;
&lt;p&gt;0.2mm courtyard excess rounded to nearest 0.05mm.&lt;/p&gt;</description>
<smd name="1" x="-0.9" y="0" dx="0.8" dy="1.2" layer="1"/>
<smd name="2" x="0.9" y="0" dx="0.8" dy="1.2" layer="1"/>
<text x="0" y="0.889" size="0.6096" layer="25" font="vector" ratio="20" align="bottom-center">&gt;NAME</text>
<text x="0" y="-0.889" size="0.6096" layer="27" font="vector" ratio="20" align="top-center">&gt;VALUE</text>
<wire x1="-1.5" y1="0.8" x2="1.5" y2="0.8" width="0.0508" layer="39"/>
<wire x1="1.5" y1="0.8" x2="1.5" y2="-0.8" width="0.0508" layer="39"/>
<wire x1="1.5" y1="-0.8" x2="-1.5" y2="-0.8" width="0.0508" layer="39"/>
<wire x1="-1.5" y1="-0.8" x2="-1.5" y2="0.8" width="0.0508" layer="39"/>
</package>
<package name="1206">
<description>&lt;p&gt;&lt;b&gt;Generic 3216 (1206) package&lt;/b&gt;&lt;/p&gt;
&lt;p&gt;0.2mm courtyard excess rounded to nearest 0.05mm.&lt;/p&gt;</description>
<wire x1="-2.4" y1="1.1" x2="2.4" y2="1.1" width="0.0508" layer="39"/>
<wire x1="2.4" y1="-1.1" x2="-2.4" y2="-1.1" width="0.0508" layer="39"/>
<wire x1="-2.4" y1="-1.1" x2="-2.4" y2="1.1" width="0.0508" layer="39"/>
<wire x1="2.4" y1="1.1" x2="2.4" y2="-1.1" width="0.0508" layer="39"/>
<wire x1="-0.965" y1="0.787" x2="0.965" y2="0.787" width="0.1016" layer="51"/>
<wire x1="-0.965" y1="-0.787" x2="0.965" y2="-0.787" width="0.1016" layer="51"/>
<smd name="1" x="-1.4" y="0" dx="1.6" dy="1.8" layer="1"/>
<smd name="2" x="1.4" y="0" dx="1.6" dy="1.8" layer="1"/>
<text x="0" y="1.143" size="0.6096" layer="25" font="vector" ratio="20" align="bottom-center">&gt;NAME</text>
<text x="0" y="-1.143" size="0.6096" layer="27" font="vector" ratio="20" align="top-center">&gt;VALUE</text>
<rectangle x1="-1.7018" y1="-0.8509" x2="-0.9517" y2="0.8491" layer="51"/>
<rectangle x1="0.9517" y1="-0.8491" x2="1.7018" y2="0.8509" layer="51"/>
<rectangle x1="-0.1999" y1="-0.4001" x2="0.1999" y2="0.4001" layer="35"/>
</package>
</packages>
<symbols>
<symbol name="CAP">
<wire x1="0" y1="2.54" x2="0" y2="2.032" width="0.1524" layer="94"/>
<wire x1="0" y1="0" x2="0" y2="0.508" width="0.1524" layer="94"/>
<text x="1.524" y="2.921" size="1.778" layer="95" font="vector">&gt;NAME</text>
<text x="1.524" y="-2.159" size="1.778" layer="96" font="vector">&gt;VALUE</text>
<rectangle x1="-2.032" y1="0.508" x2="2.032" y2="1.016" layer="94"/>
<rectangle x1="-2.032" y1="1.524" x2="2.032" y2="2.032" layer="94"/>
<pin name="1" x="0" y="5.08" visible="off" length="short" direction="pas" swaplevel="1" rot="R270"/>
<pin name="2" x="0" y="-2.54" visible="off" length="short" direction="pas" swaplevel="1" rot="R90"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="1.0UF" prefix="C">
<description>&lt;h3&gt;1µF ceramic capacitors&lt;/h3&gt;
&lt;p&gt;A capacitor is a passive two-terminal electrical component used to store electrical energy temporarily in an electric field.&lt;/p&gt;</description>
<gates>
<gate name="G$1" symbol="CAP" x="0" y="0"/>
</gates>
<devices>
<device name="-0603-16V-10%" package="0603">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="PROD_ID" value="CAP-00868"/>
<attribute name="VALUE" value="1.0uF"/>
</technology>
</technologies>
</device>
<device name="-0402-16V-10%" package="0402">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="PROD_ID" value="CAP-12417"/>
<attribute name="VALUE" value="1.0uF"/>
</technology>
</technologies>
</device>
<device name="-0805-25V-(+80/-20%)" package="0805">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="PROD_ID" value="CAP-11625"/>
<attribute name="VALUE" value="1.0uF"/>
</technology>
</technologies>
</device>
<device name="-1206-50V-10%" package="1206">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="PROD_ID" value="CAP-09822"/>
<attribute name="VALUE" value="1.0uF"/>
</technology>
</technologies>
</device>
<device name="-0805-25V-10%" package="0805">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="PROD_ID" value="CAP-08064"/>
<attribute name="VALUE" value="1.0uF"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U$1" library="IoT" deviceset="AX-1838HS" device=""/>
<part name="U$2" library="IoT" deviceset="ESP8266-07" device="SMD"/>
<part name="U$4" library="IoT" deviceset="MICROUSB" device="609-4613-1-ND"/>
<part name="U$5" library="IoT" deviceset="AZ1117E" device=""/>
<part name="D1" library="SparkFun-LED" deviceset="LED-IR" device="TSAL6100"/>
<part name="U$3" library="IoT" deviceset="AYZ0202AGRL" device=""/>
<part name="C1" library="SparkFun-Capacitors" deviceset="1.0UF" device="-0805-25V-10%" value="1.0uF"/>
<part name="C2" library="SparkFun-Capacitors" deviceset="1.0UF" device="-0805-25V-10%" value="1.0uF"/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U$1" gate="G$1" x="7.62" y="63.5"/>
<instance part="U$2" gate="G$1" x="38.1" y="50.8"/>
<instance part="U$4" gate="G$1" x="-5.08" y="101.6"/>
<instance part="U$5" gate="G$1" x="-5.08" y="55.88" rot="R270"/>
<instance part="D1" gate="G$1" x="20.32" y="35.56"/>
<instance part="U$3" gate="G$1" x="58.42" y="45.72"/>
<instance part="C1" gate="G$1" x="-5.08" y="88.9" rot="R90"/>
<instance part="C2" gate="G$1" x="-5.08" y="78.74" rot="R90"/>
</instances>
<busses>
</busses>
<nets>
<net name="N$1" class="0">
<segment>
<pinref part="U$5" gate="G$1" pin="IN"/>
<pinref part="U$4" gate="G$1" pin="VCC"/>
<wire x1="0" y1="66.04" x2="0" y2="88.9" width="0.1524" layer="91"/>
<pinref part="C1" gate="G$1" pin="2"/>
<wire x1="0" y1="88.9" x2="0" y2="99.06" width="0.1524" layer="91"/>
<wire x1="-2.54" y1="88.9" x2="0" y2="88.9" width="0.1524" layer="91"/>
<junction x="0" y="88.9"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="U$5" gate="G$1" pin="GND"/>
<wire x1="0" y1="45.72" x2="0" y2="43.18" width="0.1524" layer="91"/>
<pinref part="U$4" gate="G$1" pin="GND"/>
<wire x1="0" y1="43.18" x2="-10.16" y2="43.18" width="0.1524" layer="91"/>
<wire x1="-10.16" y1="43.18" x2="-10.16" y2="78.74" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="GND"/>
<wire x1="-10.16" y1="78.74" x2="-10.16" y2="88.9" width="0.1524" layer="91"/>
<wire x1="-10.16" y1="88.9" x2="-10.16" y2="99.06" width="0.1524" layer="91"/>
<wire x1="10.16" y1="58.42" x2="10.16" y2="43.18" width="0.1524" layer="91"/>
<wire x1="10.16" y1="43.18" x2="0" y2="43.18" width="0.1524" layer="91"/>
<junction x="0" y="43.18"/>
<pinref part="U$2" gate="G$1" pin="GND"/>
<wire x1="50.8" y1="43.18" x2="53.34" y2="43.18" width="0.1524" layer="91"/>
<wire x1="53.34" y1="43.18" x2="53.34" y2="25.4" width="0.1524" layer="91"/>
<wire x1="20.32" y1="25.4" x2="-10.16" y2="25.4" width="0.1524" layer="91"/>
<wire x1="-10.16" y1="25.4" x2="-10.16" y2="43.18" width="0.1524" layer="91"/>
<junction x="-10.16" y="43.18"/>
<pinref part="D1" gate="G$1" pin="C"/>
<wire x1="20.32" y1="30.48" x2="20.32" y2="25.4" width="0.1524" layer="91"/>
<wire x1="20.32" y1="25.4" x2="53.34" y2="25.4" width="0.1524" layer="91"/>
<junction x="53.34" y="25.4"/>
<pinref part="U$2" gate="G$1" pin="GPIO15"/>
<wire x1="50.8" y1="45.72" x2="53.34" y2="45.72" width="0.1524" layer="91"/>
<wire x1="53.34" y1="45.72" x2="53.34" y2="43.18" width="0.1524" layer="91"/>
<junction x="53.34" y="43.18"/>
<junction x="20.32" y="25.4"/>
<pinref part="U$3" gate="G$1" pin="2"/>
<wire x1="55.88" y1="50.8" x2="53.34" y2="50.8" width="0.1524" layer="91"/>
<wire x1="53.34" y1="50.8" x2="53.34" y2="45.72" width="0.1524" layer="91"/>
<junction x="53.34" y="45.72"/>
<pinref part="C2" gate="G$1" pin="1"/>
<junction x="-10.16" y="78.74"/>
<pinref part="C1" gate="G$1" pin="1"/>
<junction x="-10.16" y="88.9"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="OUT"/>
<wire x1="7.62" y1="58.42" x2="7.62" y2="48.26" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="GPIO12"/>
<wire x1="7.62" y1="48.26" x2="25.4" y2="48.26" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$8" class="0">
<segment>
<pinref part="D1" gate="G$1" pin="A"/>
<wire x1="20.32" y1="38.1" x2="20.32" y2="45.72" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="GPIO13"/>
<wire x1="20.32" y1="45.72" x2="25.4" y2="45.72" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$4" class="0">
<segment>
<pinref part="U$2" gate="G$1" pin="GPIO4"/>
<pinref part="U$3" gate="G$1" pin="3"/>
<wire x1="50.8" y1="53.34" x2="55.88" y2="53.34" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$6" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="TX"/>
<wire x1="-2.54" y1="99.06" x2="-2.54" y2="96.52" width="0.1524" layer="91"/>
<wire x1="-2.54" y1="96.52" x2="55.88" y2="96.52" width="0.1524" layer="91"/>
<wire x1="55.88" y1="96.52" x2="55.88" y2="58.42" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="RXD0"/>
<wire x1="55.88" y1="58.42" x2="50.8" y2="58.42" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$7" class="0">
<segment>
<pinref part="U$4" gate="G$1" pin="RX"/>
<wire x1="-5.08" y1="99.06" x2="-5.08" y2="93.98" width="0.1524" layer="91"/>
<wire x1="-5.08" y1="93.98" x2="53.34" y2="93.98" width="0.1524" layer="91"/>
<wire x1="53.34" y1="93.98" x2="53.34" y2="60.96" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="TXD0"/>
<wire x1="53.34" y1="60.96" x2="50.8" y2="60.96" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$5" class="0">
<segment>
<wire x1="-2.54" y1="78.74" x2="20.32" y2="78.74" width="0.1524" layer="91"/>
<pinref part="U$5" gate="G$1" pin="OUT"/>
<wire x1="-2.54" y1="66.04" x2="-2.54" y2="78.74" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="VCC"/>
<pinref part="U$2" gate="G$1" pin="EN"/>
<wire x1="12.7" y1="55.88" x2="12.7" y2="43.18" width="0.1524" layer="91"/>
<wire x1="25.4" y1="55.88" x2="20.32" y2="55.88" width="0.1524" layer="91"/>
<wire x1="20.32" y1="55.88" x2="12.7" y2="55.88" width="0.1524" layer="91"/>
<wire x1="12.7" y1="55.88" x2="12.7" y2="58.42" width="0.1524" layer="91"/>
<wire x1="20.32" y1="78.74" x2="20.32" y2="55.88" width="0.1524" layer="91"/>
<junction x="20.32" y="55.88"/>
<junction x="12.7" y="55.88"/>
<pinref part="U$2" gate="G$1" pin="VCC"/>
<wire x1="12.7" y1="43.18" x2="25.4" y2="43.18" width="0.1524" layer="91"/>
<pinref part="C2" gate="G$1" pin="2"/>
<junction x="-2.54" y="78.74"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
