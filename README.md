Pistachio is a projection system for the computer game Out of the Park Baseball.

It projects:

wOBA and WAR by position for position players

'Pitching wOBA' and WAR for starter and reliever pitchers

Once successfully run the projections will output in three html pages:

pitchers.html shows pitchers and pitching prospects

hitters.html shows hitters

hit_prospects.html shows hitter prospects

These projections are now built ground-up based on OOTP 26 - the testing method is not perfect but it does attempt to be rigorous. 

The underlying testing data and method is posted in detail here: https://docs.google.com/spreadsheets/d/19f0pZUqyonjDa2AwHckd8Al9H-wmBC6nvM-Y0RzzhSs/edit?gid=202842399#gid=202842399

In order to configure the code to your OOTP save you need to update config.py to reflect:

filepath <- this is the filepath that your csv files from OOTP are saved in, that this code reads

export_filepath <- this is the folder into which the code saves its html outputs

pistachio_filepath <- this is the folder that main.py and the other related scripts lives in

ID = 3332 <- this is your scout's coach_id taken from coaches.csv

team_managed = 'CHC'  <- this is the team you manage in game

You need to update these before you try to run main.py else it won't work.

Some other things you can update in config.py if helpful include:

club_lookup which is a map of the team numbers to their abbreviations (i.e. 6 = CHC) - this is set to MLB defaults

POSITION_THRESHOLDS which is minimum fielding ratings by position

Pitcher thresholds that determine whether a pitcher is a starter or a reliever

The code is expecting your ratings to be set on the 20-80 scale in increments of 5 and needs this in order to work.

Pull requests and feedback welcomed.

OOTP forums post (I am the username 'Squirrel' in this post): https://forums.ootpdevelopments.com/showthread.php?t=361580

Player ID numbers saved in 'flagged.txt' can be found in the outputs by typing 'flag' in the search box at the top of the html or using the 'custom search builder' at the top of the html output pages. This can be used for eg draft prospects, or any other shortlist of players created in-game.

I've left example html outputs in the 'outputs' folder but once you run main.py successfully you will overwrite it with the outputs from your OOTP save.