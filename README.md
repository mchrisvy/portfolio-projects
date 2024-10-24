
<h1> Academic Projects (Undergrad) </h1>


<details>

<summary><h2> Analysis of light curves to search for Exoplanets </h2></summary>

Light curves are graphs that show how the brightness of stars changes over a period of time.

This project used the <a href="https://github.com/pmaxted/pycheops">PYCHEOPS </a> package to study binary stars and exoplanets, where it calculates things like the mass, radius, temperature etc.

My individual project was to analyse the accuracy of radii of stars with an ellipsoidal effect calculated by PYCHEOPS. The ellipsoidal effect warps the shape of the star and so must be studued carefully. I used <a href="https://www.physik.uni-hamburg.de/en/hs/group-schmidt/members/wichmann-rainer/nightfall.html"> NIGHTFALL </a>, an astronomy application to simulate the lightcurves of stars, more accurate than PYCHEOPS. I used this program to model the radii obtained by PYCHEOPS and the final output radii by NIGHTFALL were compared.


I found that radii with an ellipsoidal 
effect were within good precision as long as there was an offset of 0.002 on the larger star(r1) and offset of 0.0002 on the smaller star(r2). As the fractional radii of the 
stars grew, the accuracy and precision of PYCHEOPS failed. Only radii at 𝑟1 < 0.26 and 𝑟2 <
0.023 were where the values were accurate.

<img src="visualisations/final%20final%20boy.png">


</details>





<details>

<summary><h2> Gravitational Wave Time Series Analysis </h2></summary>

When two black holes come into close contact, spiral and then merge, it releases such strong energy that it cause ripples in the fabric of space and time. These are called gravitational waves. 

Two short duration signals of the detection of gravitational waves had noises removed using Time series analytical techniques such as, pre-whitening and band pass filters. This isolated the chirp signals of the 
gravitational wave event detected form both sites A and B which was found to have time delay
between each other, 𝑡𝑑𝑒𝑙𝑎𝑦 = 1.46 𝑚𝑠.

<img src="visualisations/Raw%20signals.png">
These were the raw data signals
<img src="visualisations/filtered%20signals.png">
This is the prewhitened and band-passed signal. There is a large spike at around 12s showing the chirp of the gravitaitonal wave
<img src="visualisations/filtered%20signal%20ontop%20closer.png">
At a closer glance, we can see an offset/time delay between the two signals. This was calculated by using crosss correlation technique. It was found to be about 0.0014s
<img src="visualisations/final%20signal.png">
By shifting one of the signals by the offset, it shows that the signals detected by the interferomters were the same and that it indeed is the gravitational wave we have detected!

From this, I was able to calculate at what angle in radians in which the gravitational wave passed through the detectors, 8.42 rad.

</details>





<details>

<summary><h2> Butterfly Effect - Chaos </h2></summary>
something somethings blah blah 

</details>
