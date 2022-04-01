# FlareList
This repository contains a list of solar flare events obtained with a new detection algorithm.
You will have access to CSV files containing the list of events. 

<pre>
Guide to labels:
  singleID - it is a progressive number which counts the events 
  multipleID - events with the same multipleID are overlapping in time, therefore can be studied as part of the same event
  tstart - flare event starting time [UTC]
  tpeak - flare event peak time [UTC]  (reaches its maximum value) 
  tend - flare event endtime [UTC]
  BG_flux - local average flux at the beginning of the event [Wm^{-2}]
  peak_flux - value of flux at tpeak [Wm^{-2}]
  flux_integral - time integral of flux over the period from tstart to tend [Wm^{-2} s]
</pre>
