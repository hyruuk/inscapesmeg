# MEG

## Recording system and hardware

### MEG center
<img src="./_static/mri/mri.jpg" alt="UNF MRI" width="350" align="right" hspace="10"/> Magnetoencephalographic (MEG) data acquisition for the Courtois neuromod project is taking place at the [MEG laboratory](https://www.webdepot.umontreal.ca/Usagers/jolicop/MonDepotPublic/MEG-english.html) of University of Montreal's [Psychology Department](https://psy.umontreal.ca/english/home/). The MEG system is a CTF-275 dewar equipped with 275 SQUID sensor gradiometers which are distributed over the whole cortex (approx. 2.2 cm between sensors). Because of SQUID sensor's sensitivty, the dewar is protected from environmental noise by a 5x3m(?) magnetically shielded room. The MEG center also include a high speed processing cluster to handle the high volume of data, and is newly equipped with a helium recycling system to better face the worldwide helium shortage.

### Head localization
In order to allow for an efficient source reconstruction, three head localization coils are attached to the subject's nasion and left/right pre-auriculars, the position of which are tracked throughout the recording session. This step is required in order to co-register the MEG data with an anatomical MRI scan of the subjects head, a key step in estimating solutions of the MEG inverse problem. Additionally, the subject's head shape is scanned using the [Polhemus Fastrack 3D digitizer](https://polhemus.com/_assets/img/FASTRAK_Brochure_1.pdf) to help with the precise monitoring the head's position relative to the MEG's sensors.

### Personalized head cases
<img src="./_static/mri/headcase.png" alt="head case" width="200" align="right" hspace="10"/> In order to minimize movement, each participant wears a custom-designed, personalized headcase during scanning, built by [Caseforge](https://caseforge.co). The headcases are milled based on a head scan of each participant generated using a handheld 3D scanner, and the shape of the MEG dewar. Caseforge mills the personalized headcases in polystyrene foam blocks.

## BIDS formating

All functional and anatomical data has been formated in [BIDS](https://bids.neuroimaging.io/) using [MNE-BIDS](https://github.com/mne-tools/mne-bids), for more information visit the Brain Imaging Data Structure documentation [site](https://bids-specification.readthedocs.io/en/stable/).

## Stimuli

### Visual presentation

The visual stimuli are projected on a transparent screen inside of the shielded room (default : 1m distance between the screen and the subject's eyes), using a high definition short-range projector (ref?) and a set of mirrors.

### Auditory system

-----

### Stimuli presentation

For the HCP-trt dataset, Eprime scripts provided by the Human Connectome project were adapted for our presentation system, and run using Eprime 2.0. For all other tasks, a custom overlay on top of the [psychopy library](https://www.psychopy.org/) was used to present the different tasks and synchronize task with the scanner trigger pulses.
This software also allowed to trigger the start of the eyetracking system, and onset the stimuli presentation. Trigger pulses were also recorded in the [AcqKnowledge software](https://www.biopac.com/product/acqknowledge-software/). All task stimuli scripts are available through [github](https://github.com/courtois-neuromod/task_stimuli).

## Physiological measures

### Biopac
During all sequences, electrophysiological signals were recorded using a Biopac M160  MRI compatible systems and amplifiers. Measurements were acquired at 1000 Hz. Recodings were synchronized to the MRI scans via trigger pulses. All measurements were recorded and monitored using Biopac's AcqKnowledge sofware.

### Plethysmograph
Participant cardiac pulse was measured using an MRI compatible plethysmograph. A Biopac TSD200-MRI photoplethysmogram transducer was  placed on the foot or toe of the participants to obtain beat-by-beat estimates of heart rate.

### Skin conductance
Skin conductance, was measured using two electrodes, one applied to the sole of the foot and the other to the ankle, to record the participant electrodermal response.

### Electrocardiogram
An electrocardiogram (ECG) was used to  measure the electrical activity generated by the heart. The ECG was recorded using three MRI compatible electrodes that were placed adjacent to one aother, on the lower left rib cage, just under the heart.

### Respiration
Participant’s respiration was measured using a custom MRI compatible respiration belt.  The respiration system consisted of: a pressure cuff taken from a blood pressure monitor (PhysioLogic blood), a pressure sensor (MPXV5004GC7U, NXP USA Inc), and flexible tubing. The cuff was attached to the participant upper abdomen using Velcro strap, and then connected to the pressure sensor, located outside the scanner room, using tubing passed through a waveguide. The pressure signal was recorded using an analog input on the Biopac system, and monitored using AcqKnowledge software.