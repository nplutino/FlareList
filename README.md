# FlareList
This repository accompanies the article "A new catalog of solar flare events from soft x-ray GOES signal in the period 1986-2020" by N. Plutino et al.
It contains a list of solar flare events obtained with a new detection algorithm working on GOES data. You will have access to CSV files containing the list of events.
When used for publications, please acknowledge the authors' work by citing the paper and including the url of this repository.

<pre>
Guide to labels:
  singleID - it is a progressive number which counts the events 
  multipleID - events with the same multipleID are overlapping in time, therefore can be studied as part of the same event
  tstart - flare event starting time [UTC]
  tpeak - flare event peak time [UTC]  (reaches its maximum value) 
  tend - flare event endtime [UTC]
  BG_flux - local average flux at the beginning of the event [Wm^{-2}]
  peak_flux - value of flux at tpeak [Wm^{-2}]
  fclass - flare class associated to the peak flux 
  flux_integral - time integral of flux over the period from tstart to tend [Wm^{-2} s]
</pre>

In order to obtain absolute intensities for peak fluxes you can use the following expression: <pre> peak_flux - BG_flux </pre>
