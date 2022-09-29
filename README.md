
<h1> Portfolio Projects </h1>


<details>

<summary><h3> Gravitational Wave Time Series Analysis </h3></summary>

Two short duration signals of the detection of gravitational waves had noises removed using Time series analytical techniques such as, pre-whitening and band pass filters. This isolated the chirp signals of the 
gravitational wave event detected form both sites A and B which was found to have time delay
between each other, 𝑡𝑑𝑒𝑙𝑎𝑦 = 1.46 𝑚𝑠.

<img src="visualisations/Raw%20signals.png">
<img src="visualisations/filtered%20signals.png">
<img src="visualisations/filtered%20signal%20ontop%20closer.png">
<img src="visualisations/final%20signal.png">

</details>




<details>

<summary><h3> Analysis of light curves </h3></summary>

Light curves are graphs that show how the brightness of stars changes over a period of time.

This project used the <a href="https://github.com/pmaxted/pycheops">PYCHEOPS </a> package to study binary stars and exoplanets, where it calculates things like the mass, radius, temperature etc.

My individual project was to analyse the accuracy of radii of stars with an ellipsoidal effect calculated by PYCHEOPS. The ellipsoidal effect warps the shape of the star and so must be studued carefully. I used <a href="https://www.physik.uni-hamburg.de/en/hs/group-schmidt/members/wichmann-rainer/nightfall.html"> NIGHTFALL </a>, an astronomy application to simulate the lightcurves of stars, more accurate than PYCHEOPS. I used this program to model the radii obtained by PYCHEOPS and the final output radii by NIGHTFALL were compared.


I found that radii with an ellipsoidal 
effect were within good precision as long as there was an offset. As the fractional radii of the 
stars grew, the accuracy and precision of PYCHEOPS failed. Only radii at 𝑟1(larger stars) < 0.26 and 𝑟2(smaller star) <
0.023 were where the values were accurate.

<img src="visualisations/final%20final%20boy.png">


</details>






<details>

<summary><h3> Butterfly Effect - Chaos </h3></summary>
something somethings jssjvs

</details>
