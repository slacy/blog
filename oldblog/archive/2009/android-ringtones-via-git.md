Title: Android Ringtones via git 
Date: 2009-12-18 15:48
Author: slacy
Category: General
Status: published

To download all Android ringtones via git, type the following:

    $ git clone git://android.git.kernel.org/platform/frameworks/base.git

And then, look in **base/data/sounds** for the ringtones.  I like to
just copy this whole tree over to my SD card, since many of those
ringtones aren't installed by default.  Here's a directory listing of
what you get:

    data/sounds/:
    total 856
    -rw-r----- 1 slacy eng 16130 Dec 18 15:46 Alarm_Beep_01.ogg
    -rw-r----- 1 slacy eng  5898 Dec 18 15:46 Alarm_Beep_02.ogg
    -rw-r----- 1 slacy eng 21153 Dec 18 15:46 Alarm_Beep_03.ogg
    -rw-r----- 1 slacy eng 11368 Dec 18 15:46 Alarm_Buzzer.ogg
    -rw-r----- 1 slacy eng 73946 Dec 18 15:46 Alarm_Classic.ogg
    -rw-r----- 1 slacy eng 10316 Dec 18 15:46 Alarm_Rooster_01.ogg
    -rw-r----- 1 slacy eng 11160 Dec 18 15:46 Alarm_Rooster_02.ogg
    -rw-r----- 1 slacy eng  7531 Dec 18 15:46 AudioPackage2.mk
    -rw-r----- 1 slacy eng  7127 Dec 18 15:46 AudioPackage3.mk
    -rw-r----- 1 slacy eng  7028 Dec 18 15:46 AudioPackage4.mk
    -rw-r----- 1 slacy eng 11950 Dec 18 15:46 F1_MissedCall.ogg
    -rw-r----- 1 slacy eng 18653 Dec 18 15:46 F1_NewVoicemail.ogg
    -rw-r----- 1 slacy eng 20983 Dec 18 15:46 F1_New_MMS.ogg
    -rw-r----- 1 slacy eng 11941 Dec 18 15:46 F1_New_SMS.ogg
    -rw-r----- 1 slacy eng  5349 Dec 18 15:46 OriginalAudio.mk
    -rw-r----- 1 slacy eng 53097 Dec 18 15:46 Ring_Classic_01.ogg
    -rw-r----- 1 slacy eng 59024 Dec 18 15:46 Ring_Classic_02.ogg
    -rw-r----- 1 slacy eng 31085 Dec 18 15:46 Ring_Classic_03.ogg
    -rw-r----- 1 slacy eng 28745 Dec 18 15:46 Ring_Classic_04.ogg
    -rw-r----- 1 slacy eng 12746 Dec 18 15:46 Ring_Classic_05.ogg
    -rw-r----- 1 slacy eng 28256 Dec 18 15:46 Ring_Digital_01.ogg
    -rw-r----- 1 slacy eng 21007 Dec 18 15:46 Ring_Digital_02.ogg
    -rw-r----- 1 slacy eng 23456 Dec 18 15:46 Ring_Digital_03.ogg
    -rw-r----- 1 slacy eng 30844 Dec 18 15:46 Ring_Digital_04.ogg
    -rw-r----- 1 slacy eng 21003 Dec 18 15:46 Ring_Digital_05.ogg
    -rw-r----- 1 slacy eng 26852 Dec 18 15:46 Ring_Synth_01.ogg
    -rw-r----- 1 slacy eng 52809 Dec 18 15:46 Ring_Synth_02.ogg
    -rw-r----- 1 slacy eng 23269 Dec 18 15:46 Ring_Synth_03.ogg
    -rw-r----- 1 slacy eng 43965 Dec 18 15:46 Ring_Synth_04.ogg
    -rw-r----- 1 slacy eng 35187 Dec 18 15:46 Ring_Synth_05.ogg
    drwxr-x--- 2 slacy eng  4096 Dec 18 15:46 effects
    drwxr-x--- 2 slacy eng  4096 Dec 18 15:46 newwavelabs
    drwxr-x--- 2 slacy eng  4096 Dec 18 15:46 notifications
    -rw-r----- 1 slacy eng 16991 Dec 18 15:46 ring3.ogg
    -rw-r----- 1 slacy eng 32466 Dec 18 15:46 ringer.ogg
    drwxr-x--- 2 slacy eng  4096 Dec 18 15:46 ringtones
    drwxr-x--- 2 slacy eng  4096 Dec 18 15:46 testfiles

    data/sounds/effects:
    total 280
    -rw-r----- 1 slacy eng  3994 Dec 18 15:46 Effect_Tick.ogg
    -rw-r----- 1 slacy eng  6193 Dec 18 15:46 KeypressDelete.ogg
    -rw-r----- 1 slacy eng 29892 Dec 18 15:46 KeypressDelete.wav
    -rw-r----- 1 slacy eng  7972 Dec 18 15:46 KeypressReturn.ogg
    -rw-r----- 1 slacy eng 64320 Dec 18 15:46 KeypressReturn.wav
    -rw-r----- 1 slacy eng  7392 Dec 18 15:46 KeypressSpacebar.ogg
    -rw-r----- 1 slacy eng 49400 Dec 18 15:46 KeypressSpacebar.wav
    -rw-r----- 1 slacy eng  5194 Dec 18 15:46 KeypressStandard.ogg
    -rw-r----- 1 slacy eng 17992 Dec 18 15:46 KeypressStandard.wav
    -rw-r----- 1 slacy eng  5582 Dec 18 15:46 VideoRecord.ogg
    -rw-r----- 1 slacy eng 33728 Dec 18 15:46 VideoRecord.wav
    -rw-r----- 1 slacy eng  4851 Dec 18 15:46 camera_click.ogg
    -rw-r----- 1 slacy eng 13030 Dec 18 15:46 camera_click.wav

    data/sounds/newwavelabs:
    total 31052
    -rw-r----- 1 slacy eng   36049 Dec 18 15:46 Backroad.ogg
    -rw-r----- 1 slacy eng  636676 Dec 18 15:46 Backroad.wav
    -rw-r----- 1 slacy eng   28433 Dec 18 15:46 BeatPlucker.ogg
    -rw-r----- 1 slacy eng   30759 Dec 18 15:46 BentleyDubs.ogg
    -rw-r----- 1 slacy eng   46673 Dec 18 15:46 Big_Easy.ogg
    -rw-r----- 1 slacy eng  846768 Dec 18 15:46 Big_Easy.wav
    -rw-r----- 1 slacy eng   41828 Dec 18 15:46 BirdLoop.ogg
    -rw-r----- 1 slacy eng   39174 Dec 18 15:46 Bollywood.ogg
    -rw-r----- 1 slacy eng  742784 Dec 18 15:46 Bollywood.wav
    -rw-r----- 1 slacy eng   48968 Dec 18 15:46 BussaMove.ogg
    -rw-r----- 1 slacy eng  864048 Dec 18 15:46 BussaMove.wav
    -rw-r----- 1 slacy eng   19121 Dec 18 15:46 CaffeineSnake.ogg
    -rw-r----- 1 slacy eng   37672 Dec 18 15:46 Cairo.ogg
    -rw-r----- 1 slacy eng  736324 Dec 18 15:46 Cairo.wav
    -rw-r----- 1 slacy eng   38875 Dec 18 15:46 Calypso_Steel.ogg
    -rw-r----- 1 slacy eng  705644 Dec 18 15:46 Calypso_Steel.wav
    -rw-r----- 1 slacy eng   30615 Dec 18 15:46 CaribbeanIce.ogg
    -rw-r----- 1 slacy eng   39921 Dec 18 15:46 Champagne_Edition.ogg
    -rw-r----- 1 slacy eng  769792 Dec 18 15:46 Champagne_Edition.wav
    -rw-r----- 1 slacy eng   37179 Dec 18 15:46 Club_Cubano.ogg
    -rw-r----- 1 slacy eng  705620 Dec 18 15:46 Club_Cubano.wav
    -rw-r----- 1 slacy eng   48373 Dec 18 15:46 CousinJones.ogg
    -rw-r----- 1 slacy eng   37952 Dec 18 15:46 CrayonRock.ogg
    -rw-r----- 1 slacy eng  627248 Dec 18 15:46 CrayonRock.wav
    -rw-r----- 1 slacy eng  206809 Dec 18 15:46 CrazyDream.ogg
    -rw-r----- 1 slacy eng   30925 Dec 18 15:46 CurveBall.ogg
    -rw-r----- 1 slacy eng   61434 Dec 18 15:46 DancinFool.ogg
    -rw-r----- 1 slacy eng 1016108 Dec 18 15:46 DancinFool.wav
    -rw-r----- 1 slacy eng   18659 Dec 18 15:46 DearDeer.ogg
    -rw-r----- 1 slacy eng   15476 Dec 18 15:46 Ding.ogg
    -rw-r----- 1 slacy eng  264848 Dec 18 15:46 Ding.wav
    -rw-r----- 1 slacy eng   50545 Dec 18 15:46 DonMessWivIt.ogg
    -rw-r----- 1 slacy eng  910496 Dec 18 15:46 DonMessWivIt.wav
    -rw-r----- 1 slacy eng   16985 Dec 18 15:46 DontPanic.ogg
    -rw-r----- 1 slacy eng  175423 Dec 18 15:46 DreamTheme.ogg
    -rw-r----- 1 slacy eng   50578 Dec 18 15:46 Eastern_Sky.ogg
    -rw-r----- 1 slacy eng  940844 Dec 18 15:46 Eastern_Sky.wav
    -rw-r----- 1 slacy eng   31563 Dec 18 15:46 EtherShake.ogg
    -rw-r----- 1 slacy eng   46425 Dec 18 15:46 FriendlyGhost.ogg
    -rw-r----- 1 slacy eng   39738 Dec 18 15:46 Funk_Yall.ogg
    -rw-r----- 1 slacy eng  723740 Dec 18 15:46 Funk_Yall.wav
    -rw-r----- 1 slacy eng   49978 Dec 18 15:46 GameOverGuitar.ogg
    -rw-r----- 1 slacy eng   38688 Dec 18 15:46 Gimme_Mo_Town.ogg
    -rw-r----- 1 slacy eng  705644 Dec 18 15:46 Gimme_Mo_Town.wav
    -rw-r----- 1 slacy eng   54923 Dec 18 15:46 Glacial_Groove.ogg
    -rw-r----- 1 slacy eng  898884 Dec 18 15:46 Glacial_Groove.wav
    -rw-r----- 1 slacy eng   51164 Dec 18 15:46 Gotcha.ogg
    -rw-r----- 1 slacy eng  951416 Dec 18 15:46 Gotcha.wav
    -rw-r----- 1 slacy eng   41094 Dec 18 15:46 Growl.ogg
    -rw-r----- 1 slacy eng   68588 Dec 18 15:46 HalfwayHome.ogg
    -rw-r----- 1 slacy eng 1254448 Dec 18 15:46 HalfwayHome.wav
    -rw-r----- 1 slacy eng   18442 Dec 18 15:46 Highwire.ogg
    -rw-r----- 1 slacy eng   15146 Dec 18 15:46 InsertCoin.ogg
    -rw-r----- 1 slacy eng   50625 Dec 18 15:46 Jump_Up.ogg
    -rw-r----- 1 slacy eng  898884 Dec 18 15:46 Jump_Up.wav
    -rw-r----- 1 slacy eng   15619 Dec 18 15:46 KzurbSonar.ogg
    -rw-r----- 1 slacy eng   27761 Dec 18 15:46 Lectro_Beat.ogg
    -rw-r----- 1 slacy eng  607296 Dec 18 15:46 Lectro_Beat.wav
    -rw-r----- 1 slacy eng   38307 Dec 18 15:46 LoopyLounge.ogg
    -rw-r----- 1 slacy eng   34627 Dec 18 15:46 LoveFlute.ogg
    -rw-r----- 1 slacy eng   42684 Dec 18 15:46 Miami_Twice.ogg
    -rw-r----- 1 slacy eng  723740 Dec 18 15:46 Miami_Twice.wav
    -rw-r----- 1 slacy eng   28124 Dec 18 15:46 MidEvilJaunt.ogg
    -rw-r----- 1 slacy eng   34864 Dec 18 15:46 MildlyAlarming.ogg
    -rw-r----- 1 slacy eng   41355 Dec 18 15:46 Nairobi.ogg
    -rw-r----- 1 slacy eng  705644 Dec 18 15:46 Nairobi.wav
    -rw-r----- 1 slacy eng   44104 Dec 18 15:46 Nassau.ogg
    -rw-r----- 1 slacy eng  769792 Dec 18 15:46 Nassau.wav
    -rw-r----- 1 slacy eng   15563 Dec 18 15:46 NewPlayer.ogg
    -rw-r----- 1 slacy eng   32933 Dec 18 15:46 No_Limits.ogg
    -rw-r----- 1 slacy eng  631928 Dec 18 15:46 No_Limits.wav
    -rw-r----- 1 slacy eng   36287 Dec 18 15:46 Noises1.ogg
    -rw-r----- 1 slacy eng   39025 Dec 18 15:46 Noises2.ogg
    -rw-r----- 1 slacy eng   26662 Dec 18 15:46 Noises3.ogg
    -rw-r----- 1 slacy eng   23053 Dec 18 15:46 NoiseyDing.ogg
    -rw-r----- 1 slacy eng   20052 Dec 18 15:46 OnTheHunt.ogg
    -rw-r----- 1 slacy eng   32640 Dec 18 15:46 OrganDub.ogg
    -rw-r----- 1 slacy eng   39199 Dec 18 15:46 Paradise_Island.ogg
    -rw-r----- 1 slacy eng  729976 Dec 18 15:46 Paradise_Island.wav
    -rw-r----- 1 slacy eng   56616 Dec 18 15:46 Playa.ogg
    -rw-r----- 1 slacy eng 1032632 Dec 18 15:46 Playa.wav
    -rw-r----- 1 slacy eng   52536 Dec 18 15:46 Revelation.ogg
    -rw-r----- 1 slacy eng 1048480 Dec 18 15:46 Revelation.wav
    -rw-r----- 1 slacy eng   49108 Dec 18 15:46 Road_Trip.ogg
    -rw-r----- 1 slacy eng  967732 Dec 18 15:46 Road_Trip.wav
    -rw-r----- 1 slacy eng   31641 Dec 18 15:46 RomancingTheTone.ogg
    -rw-r----- 1 slacy eng   42220 Dec 18 15:46 Safari.ogg
    -rw-r----- 1 slacy eng  705620 Dec 18 15:46 Safari.wav
    -rw-r----- 1 slacy eng   39138 Dec 18 15:46 Savannah.ogg
    -rw-r----- 1 slacy eng  705644 Dec 18 15:46 Savannah.wav
    -rw-r----- 1 slacy eng   44422 Dec 18 15:46 Seville.ogg
    -rw-r----- 1 slacy eng  846768 Dec 18 15:46 Seville.wav
    -rw-r----- 1 slacy eng   39413 Dec 18 15:46 Shes_All_That.ogg
    -rw-r----- 1 slacy eng  736324 Dec 18 15:46 Shes_All_That.wav
    -rw-r----- 1 slacy eng   44186 Dec 18 15:46 SilkyWay.ogg
    -rw-r----- 1 slacy eng  736324 Dec 18 15:46 SilkyWay.wav
    -rw-r----- 1 slacy eng   28898 Dec 18 15:46 SitarVsSitar.ogg
    -rw-r----- 1 slacy eng   26144 Dec 18 15:46 SpringyJalopy.ogg
    -rw-r----- 1 slacy eng   37847 Dec 18 15:46 Steppin_Out.ogg
    -rw-r----- 1 slacy eng  705620 Dec 18 15:46 Steppin_Out.wav
    -rw-r----- 1 slacy eng   36620 Dec 18 15:46 Terminated.ogg
    -rw-r----- 1 slacy eng   36539 Dec 18 15:46 Third_Eye.ogg
    -rw-r----- 1 slacy eng  705644 Dec 18 15:46 Third_Eye.wav
    -rw-r----- 1 slacy eng   46049 Dec 18 15:46 Thunderfoot.ogg
    -rw-r----- 1 slacy eng  846768 Dec 18 15:46 Thunderfoot.wav
    -rw-r----- 1 slacy eng   26298 Dec 18 15:46 TwirlAway.ogg
    -rw-r----- 1 slacy eng   28691 Dec 18 15:46 VeryAlarmed.ogg
    -rw-r----- 1 slacy eng   16487 Dec 18 15:46 Voila.ogg
    -rw-r----- 1 slacy eng   31136 Dec 18 15:46 World.ogg

    data/sounds/notifications:
    total 1704
    -rw-r----- 1 slacy eng  34601 Dec 18 15:46 Beat_Box_Android.ogg
    -rw-r----- 1 slacy eng  59135 Dec 18 15:46 Bees_Knees.ogg
    -rw-r----- 1 slacy eng  19392 Dec 18 15:46 Cheeper.ogg
    -rw-r----- 1 slacy eng  38517 Dec 18 15:46 Heaven.ogg
    -rw-r----- 1 slacy eng  28944 Dec 18 15:46 IM_Me.ogg
    -rw-r----- 1 slacy eng   6652 Dec 18 15:46 Plastic_Pipe.ogg
    -rw-r----- 1 slacy eng  69856 Dec 18 15:46 Plastic_Pipe.wav
    -rw-r----- 1 slacy eng  16562 Dec 18 15:46 ShortCircuit.ogg
    -rw-r----- 1 slacy eng  50350 Dec 18 15:46 Star_Struck.ogg
    -rw-r----- 1 slacy eng  43522 Dec 18 15:46 TaDa.ogg
    -rw-r----- 1 slacy eng  18858 Dec 18 15:46 Tinkerbell.ogg
    -rw-r----- 1 slacy eng  16243 Dec 18 15:46 moonbeam.ogg
    -rw-r----- 1 slacy eng 359980 Dec 18 15:46 moonbeam.wav
    -rw-r----- 1 slacy eng  16905 Dec 18 15:46 pixiedust.ogg
    -rw-r----- 1 slacy eng 332032 Dec 18 15:46 pixiedust.wav
    -rw-r----- 1 slacy eng  18884 Dec 18 15:46 pizzicato.ogg
    -rw-r----- 1 slacy eng 384592 Dec 18 15:46 pizzicato.wav
    -rw-r----- 1 slacy eng  10421 Dec 18 15:46 tweeters.ogg
    -rw-r----- 1 slacy eng 151368 Dec 18 15:46 tweeters.wav

    data/sounds/ringtones:
    total 2300
    -rw-r----- 1 slacy eng  113055 Dec 18 15:46 FreeFlight.ogg
    -rw-r----- 1 slacy eng 2229120 Dec 18 15:46 FreeFlight.wav

    data/sounds/testfiles:
    total 4
    -rwxr-x--- 1 slacy eng 2956 Dec 18 15:46 test.mid
