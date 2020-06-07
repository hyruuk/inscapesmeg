import mne_bids
import mne
import os
import os.path as op
import numpy as np
from mne_bids import make_bids_folders, make_bids_basename, write_raw_bids


'''
This script create a BIDS folder structure from the raw files acquired at the UDEM MEG center (CTF-275 system).
To use it, just put the session files (the folder named by the date of recording) in the specified acquisition folder.
Run the script again for each new subject to add.
'''



BIDS_PATH = '/home/hyruuk/pCloudDrive/science/neuromod/inscapes_MEG/BIDS'
ACQ_PATH = '/home/hyruuk/pCloudDrive/science/neuromod/inscapes_MEG/raw'
EVENT_ID = {'TaskStart': 2, 'TaskStop': 4}
EVENT_ID_EYEMVT = {
    'sacc_left': int('10000000', 2),
    'sacc_right': int('01000000', 2),
    'sacc_up': int('00100000', 2),
    'sacc_down': int('00010000', 2),
    'SP_left': int('10000001', 2),
    'SP_right': int('01000001', 2),
    'SP_up': int('00100001', 2),
    'SP_down': int('00010001', 2)
}


# check if BIDS_PATH exists, if not, create it
if not os.path.isdir(BIDS_PATH):
    os.mkdir(BIDS_PATH)
    print('BIDS folder created at : {}'.format(BIDS_PATH))
else:
    print('{} already exists.'.format(BIDS_PATH))

# list folders in acquisition folder
recording_folders = os.listdir(ACQ_PATH)

# loop across recording folders (folder containing the recordings of the day)
for rec_date in recording_folders: # folders are named by date in format YYYYMMDD
    for file in os.listdir(op.join(ACQ_PATH, rec_date)):
        # Create emptyroom BIDS if doesn't exist already
        if 'NOISE_noise' in file:
            if not op.isdir(op.join(BIDS_PATH, 'sub-emptyroom', 'ses-{}'.format(rec_date))):
                er_bids_basename = make_bids_basename(subject='emptyroom', task='noise', session=rec_date)
                er_raw_fname = op.join(ACQ_PATH, rec_date, file)
                er_raw = mne.io.read_raw_ctf(er_raw_fname)
                write_raw_bids(er_raw, er_bids_basename, BIDS_PATH)
        # Rewrite in BIDS format if doesn't exist yet
        if 'NEUROMOD' in file and '.ds' in file and not 'procedure' in file:
            subject = file[1:3]
            run = file[-5:-3]
            session = 'recording'
            if run == '02' or run == '05':
                task = 'RS'
            elif run == '01':
                task = 'EyeMvt'
            elif run == '03' or run == '06':
                task = 'Inscapes'
            elif run == '04' or run == '07':
                task = 'Oceans'
            bids_basename = make_bids_basename(subject=subject, session=session, task=task, run=run)
            if not op.isdir(op.join(BIDS_PATH, 'sub-{}'.format(subject), 'ses-{}'.format(session), 'meg', bids_basename + '_meg.ds')):
                raw_fname = op.join(ACQ_PATH, rec_date, file)
                raw = mne.io.read_raw_ctf(raw_fname, preload=False)
                try:
                    events = mne.find_events(raw)
                    if task == 'EyeMvt':
                        write_raw_bids(raw, bids_basename, BIDS_PATH, events_data=events, event_id=EVENT_ID_EYEMVT, overwrite=True)
                    else:
                        write_raw_bids(raw, bids_basename, BIDS_PATH, events_data=events, event_id=EVENT_ID, overwrite=True)
                except:
                    write_raw_bids(raw, bids_basename, BIDS_PATH, overwrite=True)
