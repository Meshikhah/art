# -*- coding: utf-8 -*-
'''
This function get a string as input if input is one digit add a zero
:param input_string: input digit az string
:type input_string:str
:return: modified output as str
>>> import os
>>> import random
>>> import sys
>>> from art import *
>>> font_list()
3-d :
   **                     **
  /**                    /**
 ******  *****   ****** ******
///**/  **///** **//// ///**/
  /**  /*******//*****   /**
  /**  /**////  /////**  /**
  //** //****** ******   //**
   //   ////// //////     //
<BLANKLINE>
3x5 :
<BLANKLINE>
 #           #
### ###  ## ###
 #  ##   #   #
 ## ### ##   ##
<BLANKLINE>
<BLANKLINE>
5lineoblique :
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
 __  ___     ___        ___     __  ___
  / /      //___) )   ((   ) )   / /
 / /      //           \ \      / /
/ /      ((____     //   ) )   / /
<BLANKLINE>
acrobatic :
  o                               o
 <|>                             <|>
 < >                             < >
  |        o__  __o       __o__   |
  o__/_   /v      |>     />  \    o__/_
  |      />      //      \o       |
  |      \o    o/         v\      |
  o       v\  /v __o       <\     o
  <\__     <\/> __/>  _\o__</     <\__
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
alligator :
  :::::::::::       ::::::::::       ::::::::   :::::::::::
     :+:           :+:             :+:    :+:      :+:
    +:+           +:+             +:+             +:+
   +#+           +#++:++#        +#++:++#++      +#+
  +#+           +#+                    +#+      +#+
 #+#           #+#             #+#    #+#      #+#
###           ##########       ########       ###
<BLANKLINE>
alligator2 :
::::::::::: ::::::::::  ::::::::  :::::::::::
    :+:     :+:        :+:    :+:     :+:
    +:+     +:+        +:+            +:+
    +#+     +#++:++#   +#++:++#++     +#+
    +#+     +#+               +#+     +#+
    #+#     #+#        #+#    #+#     #+#
    ###     ##########  ########      ###
<BLANKLINE>
alphabet :
 t           t
 t           t
ttt eee  ss ttt
 t  e e  s   t
 tt ee  ss   tt
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
avatar :
 _____  _____ ____  _____
/__ __\/  __// ___\/__ __\
  / \  |  \  |    \  / \
  | |  |  /_ \___ |  | |
  \_/  \____\\____/  \_/
<BLANKLINE>
<BLANKLINE>
banner :
<BLANKLINE>
##### ######  ####  #####
  #   #      #        #
  #   #####   ####    #
  #   #           #   #
  #   #      #    #   #
  #   ######  ####    #
<BLANKLINE>
<BLANKLINE>
banner3 :
######## ########  ######  ########
   ##    ##       ##    ##    ##
   ##    ##       ##          ##
   ##    ######    ######     ##
   ##    ##             ##    ##
   ##    ##       ##    ##    ##
   ##    ########  ######     ##
<BLANKLINE>
banner3-d :
'########:'########::'######::'########:
... ##..:: ##.....::'##... ##:... ##..::
::: ##:::: ##::::::: ##:::..::::: ##::::
::: ##:::: ######:::. ######::::: ##::::
::: ##:::: ##...:::::..... ##:::: ##::::
::: ##:::: ##:::::::'##::: ##:::: ##::::
::: ##:::: ########:. ######::::: ##::::
:::..:::::........:::......::::::..:::::
<BLANKLINE>
banner4 :
.########.########..######..########
....##....##.......##....##....##...
....##....##.......##..........##...
....##....######....######.....##...
....##....##.............##....##...
....##....##.......##....##....##...
....##....########..######.....##...
<BLANKLINE>
barbwire :
  ><<                     ><<
  ><<                     ><<
><>< ><   ><<     ><<<< ><>< ><
  ><<   ><   ><< ><<      ><<
  ><<  ><<<<< ><<  ><<<   ><<
  ><<  ><            ><<  ><<
   ><<   ><<<<   ><< ><<   ><<
<BLANKLINE>
<BLANKLINE>
basic :
d888888b d88888b .d8888. d888888b
`~~88~~' 88'     88'  YP `~~88~~'
   88    88ooooo `8bo.      88
   88    88~~~~~   `Y8b.    88
   88    88.     db   8D    88
   YP    Y88888P `8888Y'    YP
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
bell :
  .                   .
 _/_     ___    ____ _/_
  |    .'   `  (      |
  |    |----'  `--.   |
  \__/ `.___, \___.'  \__/
<BLANKLINE>
<BLANKLINE>
big :
 _               _
| |             | |
| |_   ___  ___ | |_
| __| / _ \/ __|| __|
| |_ |  __/\__ \| |_
 \__| \___||___/ \__|
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
bigchief :
_________________________
<BLANKLINE>
<BLANKLINE>
--_/_-----__----__---_/_-
  /     /___)  (_ `  /
_(_ ___(___ __(__)__(_ __
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
binary :
01110100 01100101 01110011 01110100
<BLANKLINE>
block :
<BLANKLINE>
 .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |  _________   | || |    _______   | || |  _________   | |
| | |  _   _  |  | || | |_   ___  |  | || |   /  ___  |  | || | |  _   _  |  | |
| | |_/ | | \_|  | || |   | |_  \_|  | || |  |  (__ \_|  | || | |_/ | | \_|  | |
| |     | |      | || |   |  _|  _   | || |   '.___`-.   | || |     | |      | |
| |    _| |_     | || |  _| |___/ |  | || |  |`\____) |  | || |    _| |_     | |
| |   |_____|    | || | |_________|  | || |  |_______.'  | || |   |_____|    | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'
<BLANKLINE>
block2 :
<BLANKLINE>
  _|                            _|
_|_|_|_|    _|_|      _|_|_|  _|_|_|_|
  _|      _|_|_|_|  _|_|        _|
  _|      _|            _|_|    _|
    _|_|    _|_|_|  _|_|_|        _|_|
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
bubble :
  _    _    _    _
 / \  / \  / \  / \
( t )( e )( s )( t )
 \_/  \_/  \_/  \_/
<BLANKLINE>
bulbhead :
 ____  ____  ___  ____
(_  _)( ___)/ __)(_  _)
  )(   )__) \__ \  )(
 (__) (____)(___/ (__)
<BLANKLINE>
calgphy2 :
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
    #                              #
   ##                             ##
   ##                             ##
 ########    /##       /###     ########
########    / ###     / #### / ########
   ##      /   ###   ##  ###/     ##
   ##     ##    ### ####          ##
   ##     ########    ###         ##
   ##     #######       ###       ##
   ##     ##              ###     ##
   ##     ####    /  /###  ##     ##
   ##      ######/  / #### /      ##
    ##      #####      ###/        ##
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
caligraphy :
<BLANKLINE>
<BLANKLINE>
    *                              *
   **                             **
   **                             **
 ********              ****     ********
********     ***      * **** * ********
   **       * ***    **  ****     **
   **      *   ***  ****          **
   **     **    ***   ***         **
   **     ********      ***       **
   **     *******         ***     **
   **     **         ****  **     **
   **     ****    * * **** *      **
    **     *******     ****        **
            *****
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
catwalk :
  _//                     _//
  _//                     _//
_/_/ _/   _//     _//// _/_/ _/
  _//   _/   _// _//      _//
  _//  _///// _//  _///   _//
  _//  _/            _//  _//
   _//   _////   _// _//   _//
<BLANKLINE>
<BLANKLINE>
chunky :
 __                  __
|  |_ .-----..-----.|  |_
|   _||  -__||__ --||   _|
|____||_____||_____||____|
<BLANKLINE>
<BLANKLINE>
coinstak :
  O))                     O))
  O))                     O))
O)O) O)   O))     O)))) O)O) O)
  O))   O)   O)) O))      O))
  O))  O))))) O))  O)))   O))
  O))  O)            O))  O))
   O))   O))))   O)) O))   O))
<BLANKLINE>
<BLANKLINE>
colossal :
888                      888
888                      888
888                      888
888888  .d88b.  .d8888b  888888
888    d8P  Y8b 88K      888
888    88888888 "Y8888b. 888
Y88b.  Y8b.          X88 Y88b.
 "Y888  "Y8888   88888P'  "Y888
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
computer :
<BLANKLINE>
eeeee eeee eeeee eeeee
  8   8    8   "   8
  8e  8eee 8eeee   8e
  88  88      88   88
  88  88ee 8ee88   88
<BLANKLINE>
<BLANKLINE>
contessa :
 ,        ,
-+- _  __-+-
 | (/,_)  |
<BLANKLINE>
<BLANKLINE>
contrast :
.%%%%%%..%%%%%%...%%%%...%%%%%%.
...%%....%%......%%........%%...
...%%....%%%%.....%%%%.....%%...
...%%....%%..........%%....%%...
...%%....%%%%%%...%%%%.....%%...
................................
<BLANKLINE>
cyberlarge :
 _______ _______ _______ _______
    |    |______ |______    |
    |    |______ ______|    |
<BLANKLINE>
<BLANKLINE>
cybermedium :
___ ____ ____ ___
 |  |___ [__   |
 |  |___ ___]  |
<BLANKLINE>
<BLANKLINE>
cygnet :
<BLANKLINE>
 .       .
-|-.-,.--|-
 '-`'--' '-
<BLANKLINE>
<BLANKLINE>
diamond :
  /\\                     /\\
  /\\                     /\\
/\/\ /\   /\\     /\\\\ /\/\ /\
  /\\   /\   /\\ /\\      /\\
  /\\  /\\\\\ /\\  /\\\   /\\
  /\\  /\            /\\  /\\
   /\\   /\\\\   /\\ /\\   /\\
<BLANKLINE>
<BLANKLINE>
digital :
+-++-++-++-+
|t||e||s||t|
+-++-++-++-+
<BLANKLINE>
doh :
<BLANKLINE>
<BLANKLINE>
         tttt                                                        tttt
      ttt:::t                                                     ttt:::t
      t:::::t                                                     t:::::t
      t:::::t                                                     t:::::t
ttttttt:::::ttttttt        eeeeeeeeeeee        ssssssssss   ttttttt:::::ttttttt
t:::::::::::::::::t      ee::::::::::::ee    ss::::::::::s  t:::::::::::::::::t
t:::::::::::::::::t     e::::::eeeee:::::eess:::::::::::::s t:::::::::::::::::t
tttttt:::::::tttttt    e::::::e     e:::::es::::::ssss:::::stttttt:::::::tttttt
      t:::::t          e:::::::eeeee::::::e s:::::s  ssssss       t:::::t
      t:::::t          e:::::::::::::::::e    s::::::s            t:::::t
      t:::::t          e::::::eeeeeeeeeee        s::::::s         t:::::t
      t:::::t    tttttte:::::::e           ssssss   s:::::s       t:::::t    tttttt
      t::::::tttt:::::te::::::::e          s:::::ssss::::::s      t::::::tttt:::::t
      tt::::::::::::::t e::::::::eeeeeeee  s::::::::::::::s       tt::::::::::::::t
        tt:::::::::::tt  ee:::::::::::::e   s:::::::::::ss          tt:::::::::::tt
          ttttttttttt      eeeeeeeeeeeeee    sssssssssss              ttttttttttt
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
doom :
 _               _
| |             | |
| |_   ___  ___ | |_
| __| / _ \/ __|| __|
| |_ |  __/\__ \| |_
 \__| \___||___/ \__|
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
dotmatrix :
    _                                                    _
   (_)                                                  (_)
 _ (_) _  _        _  _  _  _         _  _  _  _      _ (_) _  _
(_)(_)(_)(_)      (_)(_)(_)(_)_     _(_)(_)(_)(_)    (_)(_)(_)(_)
   (_)           (_) _  _  _ (_)   (_)_  _  _  _        (_)
   (_)     _     (_)(_)(_)(_)(_)     (_)(_)(_)(_)_      (_)     _
   (_)_  _(_)    (_)_  _  _  _        _  _  _  _(_)     (_)_  _(_)
     (_)(_)        (_)(_)(_)(_)      (_)(_)(_)(_)         (_)(_)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
drpepper :
   _               _
 _| |_  ___  ___ _| |_
  | |  / ._><_-<  | |
  |_|  \___./__/  |_|
<BLANKLINE>
<BLANKLINE>
eftifont :
<BLANKLINE>
||  _  _ ||
| ]/o\(c'| ]
L| \( \_)L|
<BLANKLINE>
<BLANKLINE>
eftirobot :
 _            _
( )          ( )
| |  ___  __ | |
( _)( o_)(_' ( _)
/_\  \(  /__)/_\
<BLANKLINE>
<BLANKLINE>
eftitalic :
<BLANKLINE>
  /7  __  __  /7
 /_7,'o/ (c' /_7
//  |_( /__)//
<BLANKLINE>
<BLANKLINE>
eftiwater :
 _        _
 )L __ __ )L
(( (('_))((
<BLANKLINE>
epic :
_________ _______  _______ _________
\__   __/(  ____ \(  ____ \\__   __/
   ) (   | (    \/| (    \/   ) (
   | |   | (__    | (_____    | |
   | |   |  __)   (_____  )   | |
   | |   | (            ) |   | |
   | |   | (____/\/\____) |   | |
   )_(   (_______/\_______)   )_(
<BLANKLINE>
<BLANKLINE>
fourtops :
 |       |
~|~/~/(~~|~
 | \/__) |
<BLANKLINE>
<BLANKLINE>
fuzzy :
 .-.              .-.
.' `.            .' `.
`. .' .--.  .--. `. .'
 : : ' '_.'`._-.' : :
 :_; `.__.'`.__.' :_;
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
goofy :
_        __        ___       ___        __
(__    __) \    ___)  )  ____) (__    __)
   |  |     |  (__   (  (___      |  |
   |  |     |   __)   \___  \     |  |
   |  |     |  (___   ____)  )    |  |
___|  |____/       )_(      (_____|  |____
<BLANKLINE>
<BLANKLINE>
graffiti :
  __                     __
_/  |_   ____    _______/  |_
\   __\_/ __ \  /  ___/\   __\
 |  |  \  ___/  \___ \  |  |
 |__|   \___  >/____  > |__|
            \/      \/
<BLANKLINE>
hollywood :
<BLANKLINE>
         /'                               /'
     --/'--                           --/'--
     /'         ____      ____        /'
   /'         /'    )   /'    )--   /'
 /'         /(___,/'   '---,      /'
(__        (________ (___,/      (__
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
invita :
<BLANKLINE>
<BLANKLINE>
_/_   _  _  _/_
(__ _(/_/_)_(__
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
isometric1 :
      ___           ___           ___           ___
     /\  \         /\  \         /\  \         /\  \
     \:\  \       /::\  \       /::\  \        \:\  \
      \:\  \     /:/\:\  \     /:/\ \  \        \:\  \
      /::\  \   /::\~\:\  \   _\:\~\ \  \       /::\  \
     /:/\:\__\ /:/\:\ \:\__\ /\ \:\ \ \__\     /:/\:\__\
    /:/  \/__/ \:\~\:\ \/__/ \:\ \:\ \/__/    /:/  \/__/
   /:/  /       \:\ \:\__\    \:\ \:\__\     /:/  /
   \/__/         \:\ \/__/     \:\/:/  /     \/__/
                  \:\__\        \::/  /
                   \/__/         \/__/
<BLANKLINE>
isometric2 :
                    ___           ___
                   /\__\         /\__\
      ___         /:/ _/_       /:/ _/_         ___
     /\__\       /:/ /\__\     /:/ /\  \       /\__\
    /:/  /      /:/ /:/ _/_   /:/ /::\  \     /:/  /
   /:/__/      /:/_/:/ /\__\ /:/_/:/\:\__\   /:/__/
  /::\  \      \:\/:/ /:/  / \:\/:/ /:/  /  /::\  \
 /:/\:\  \      \::/_/:/  /   \::/ /:/  /  /:/\:\  \
 \/__\:\  \      \:\/:/  /     \/_/:/  /   \/__\:\  \
      \:\__\      \::/  /        /:/  /         \:\__\
       \/__/       \/__/         \/__/           \/__/
<BLANKLINE>
isometric3 :
                  ___           ___
      ___        /  /\         /  /\          ___
     /  /\      /  /:/_       /  /:/_        /  /\
    /  /:/     /  /:/ /\     /  /:/ /\      /  /:/
   /  /:/     /  /:/ /:/_   /  /:/ /::\    /  /:/
  /  /::\    /__/:/ /:/ /\ /__/:/ /:/\:\  /  /::\
 /__/:/\:\   \  \:\/:/ /:/ \  \:\/:/~/:/ /__/:/\:\
 \__\/  \:\   \  \::/ /:/   \  \::/ /:/  \__\/  \:\
      \  \:\   \  \:\/:/     \__\/ /:/        \  \:\
       \__\/    \  \::/        /__/:/          \__\/
                 \__\/         \__\/
<BLANKLINE>
isometric4 :
                    ___           ___
      ___          /  /\         /  /\          ___
     /__/\        /  /::\       /  /::\        /__/\
     \  \:\      /  /:/\:\     /__/:/\:\       \  \:\
      \__\:\    /  /::\ \:\   _\_ \:\ \:\       \__\:\
      /  /::\  /__/:/\:\ \:\ /__/\ \:\ \:\      /  /::\
     /  /:/\:\ \  \:\ \:\_\/ \  \:\ \:\_\/     /  /:/\:\
    /  /:/__\/  \  \:\ \:\    \  \:\_\:\      /  /:/__\/
   /__/:/        \  \:\_\/     \  \:\/:/     /__/:/
   \__\/          \  \:\        \  \::/      \__\/
                   \__\/         \__\/
<BLANKLINE>
italic :
<BLANKLINE>
_/  _   _ _/
/  (- _)  /
<BLANKLINE>
<BLANKLINE>
jazmine :
<BLANKLINE>
  o                  o
  8                  8
 o8P .oPYo. .oPYo.  o8P
  8  8oooo8 Yb..     8
  8  8.       'Yb.   8
  8  `Yooo' `YooP'   8
::..::.....::.....:::..:
::::::::::::::::::::::::
::::::::::::::::::::::::
<BLANKLINE>
larry3d :
 __                       __
/\ \__                   /\ \__
\ \ ,_\     __     ____  \ \ ,_\
 \ \ \/   /'__`\  /',__\  \ \ \/
  \ \ \_ /\  __/ /\__, `\  \ \ \_
   \ \__\\ \____\\/\____/   \ \__\
    \/__/ \/____/ \/___/     \/__/
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
lcd :
<BLANKLINE>
  |                 |
 -+-   -       -   -+-
  |   |/       \    |
   -   --      -     -
<BLANKLINE>
<BLANKLINE>
lean :
<BLANKLINE>
   _/                                   _/
_/_/_/_/       _/_/         _/_/_/   _/_/_/_/
 _/         _/_/_/_/     _/_/         _/
_/         _/               _/_/     _/
 _/_/       _/_/_/     _/_/_/         _/_/
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
letters :
tt                 tt
tt      eee   sss  tt
tttt  ee   e s     tttt
tt    eeeee   sss  tt
 tttt  eeeee     s  tttt
              sss
<BLANKLINE>
lockergnome :
 :|             :|
:::| :~~/ <::< :::|
 :|  :::, >::>  :|
<BLANKLINE>
madrid :
|-         |-
|  /=\ /== |
\= \=  ==/ \=
<BLANKLINE>
<BLANKLINE>
marquee :
  .::                     .::
  .::                     .::
.:.: .:   .::     .:::: .:.: .:
  .::   .:   .:: .::      .::
  .::  .::::: .::  .:::   .::
  .::  .:            .::  .::
   .::   .::::   .:: .::   .::
<BLANKLINE>
<BLANKLINE>
maxfour :
 |       |
~|~/~/(~~|~
 | \/__) |
<BLANKLINE>
<BLANKLINE>
mike :
  _   _     _
   | |/ //   |
<BLANKLINE>
<BLANKLINE>
mini :
<BLANKLINE>
_|_  _   _ _|_
 |_ (/_ _>  |_
<BLANKLINE>
<BLANKLINE>
nancyj :
  dP                       dP
  88                       88
d8888P .d8888b. .d8888b. d8888P
  88   88ooood8 Y8ooooo.   88
  88   88.  ...       88   88
  dP   `88888P' `88888P'   dP
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
nancyj-fancy :
  dP                       dP
  88                       88
d8888P .d8888b. .d8888b. d8888P
  88   88ooood8 Y8ooooo.   88
  88   88.  ...       88   88
  dP   `88888P' `88888P'   dP
<BLANKLINE>
<BLANKLINE>
nancyj-underlined :
  dP                       dP
  88                       88
d8888P .d8888b. .d8888b. d8888P
  88   88ooood8 Y8ooooo.   88
  88   88.  ...       88   88
  dP   `88888P' `88888P'   dP
oooooooooooooooooooooooooooooooo
<BLANKLINE>
<BLANKLINE>
nipples :
  {__                     {__
  {__                     {__
{_{_ {_   {__     {____ {_{_ {_
  {__   {_   {__ {__      {__
  {__  {_____ {__  {___   {__
  {__  {_            {__  {__
   {__   {____   {__ {__   {__
<BLANKLINE>
<BLANKLINE>
o8 :
  o8                             o8
o888oo  ooooooooo8  oooooooo8  o888oo
 888   888oooooo8  888ooooooo   888
 888   888                 888  888
  888o   88oooo888 88oooooo88    888o
<BLANKLINE>
<BLANKLINE>
ogre :
 _               _
| |_   ___  ___ | |_
| __| / _ \/ __|| __|
| |_ |  __/\__ \| |_
 \__| \___||___/ \__|
<BLANKLINE>
<BLANKLINE>
pawp :
<BLANKLINE>
 _                 _
(_)_   ____  ____ (_)_
(___) (____)(____)(___)
(_)  (_)_(_)(_)__ (_)
(_)_ (__)__  _(__)(_)_
 (__) (____)(____) (__)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
peaks :
  /^^                     /^^
  /^^                     /^^
/^/^ /^   /^^     /^^^^ /^/^ /^
  /^^   /^   /^^ /^^      /^^
  /^^  /^^^^^ /^^  /^^^   /^^
  /^^  /^            /^^  /^^
   /^^   /^^^^   /^^ /^^   /^^
<BLANKLINE>
<BLANKLINE>
pebbles :
<BLANKLINE>
<BLANKLINE>
  O                 O
 oOo               oOo
  o   .oOo. .oOo    o
  O   OooO' `Ooo.   O
  o   O         O   o
  `oO `OoO' `OoO'   `oO
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
pepper :
<BLANKLINE>
_/_ _   __/_
/  /_'_\ /
<BLANKLINE>
<BLANKLINE>
poison :
<BLANKLINE>
@@@@@@@  @@@@@@@@   @@@@@@   @@@@@@@
@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@
  @@!    @@!       !@@         @@!
  !@!    !@!       !@!         !@!
  @!!    @!!!:!    !!@@!!      @!!
  !!!    !!!!!:     !!@!!!     !!!
  !!:    !!:            !:!    !!:
  :!:    :!:           !:!     :!:
   ::     :: ::::  :::: ::      ::
   :     : :: ::   :: : :       :
<BLANKLINE>
<BLANKLINE>
puffy :
 _                 _
( )_              ( )_
| ,_)   __    ___ | ,_)
| |   /'__`\/',__)| |
| |_ (  ___/\__, \| |_
`\__)`\____)(____/`\__)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
pyramid :
  ^    ^    ^    ^
 /t\  /e\  /s\  /t\
<___><___><___><___>
<BLANKLINE>
rectangles :
<BLANKLINE>
 _              _
| |_  ___  ___ | |_
|  _|| -_||_ -||  _|
|_|  |___||___||_|
<BLANKLINE>
<BLANKLINE>
roman :
    .                          .
  .o8                        .o8
.o888oo  .ooooo.   .oooo.o .o888oo
  888   d88' `88b d88(  "8   888
  888   888ooo888 `"Y88b.    888
  888 . 888    .o o.  )88b   888 .
  "888" `Y8bod8P' 8""888P'   "888"
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
rot13 :
grfg
rounded :
<BLANKLINE>
   _                   _
 _| |_  _____   ___  _| |_
(_   _)| ___ | /___)(_   _)
  | |_ | ____||___ |  | |_
   \__)|_____)(___/    \__)
<BLANKLINE>
<BLANKLINE>
rowancap :
 dMMMMMMP     dMMMMMP    .dMMMb  dMMMMMMP
   dMP       dMP        dMP" VP    dMP
  dMP       dMMMP       VMMMb     dMP
 dMP       dMP        dP .dMP    dMP
dMP       dMMMMMP     VMMMP"    dMP
<BLANKLINE>
<BLANKLINE>
rozzo :
  d8                   d8
 d88    ,e e,   dP"Y  d88
d88888 d88 88b C88b  d88888
 888   888   ,  Y88D  888
 888    "YeeP" d,dP   888
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
sblood :
 @@@@@@@ @@@@@@@@  @@@@@@ @@@@@@@
   @@!   @@!      !@@       @@!
   @!!   @!!!:!    !@@!!    @!!
   !!:   !!:          !:!   !!:
    :    : :: ::: ::.: :     :
<BLANKLINE>
<BLANKLINE>
script :
<BLANKLINE>
<BLANKLINE>
_|_  _   ,  _|_
 |  |/  / \_ |
 |_/|__/ \/  |_/
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
serifcap :
 ____  ___  ___  ____
(_  _)(  _)/ __)(_  _)
  )(   ) _)\__ \  )(
 (__) (___)(___/ (__)
<BLANKLINE>
shadow :
 |                |
 __|   _ \   __|  __|
 |     __/ \__ \  |
\__| \___| ____/ \__|
<BLANKLINE>
<BLANKLINE>
short :
|- _  _|-
|_(/__\|_
<BLANKLINE>
<BLANKLINE>
slant :
   __                  __
  / /_  ___    _____  / /_
 / __/ / _ \  / ___/ / __/
/ /_  /  __/ (__  ) / /_
\__/  \___/ /____/  \__/
<BLANKLINE>
<BLANKLINE>
slide :
 #|                #|
##HH|  #H|   #HH| ##HH|
 #|   ##HH| ##H|   #|
 #|   ##       H|  #|
 #H|   #HH| ##H|   #H|
<BLANKLINE>
<BLANKLINE>
slscript :
<BLANKLINE>
 _/_        _/_
 /   _  _   /
<__ </_/_)_<__
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
small :
 _             _
| |_  ___  ___| |_
|  _|/ -_)(_-<|  _|
 \__|\___|/__/ \__|
<BLANKLINE>
smisome1 :
    ___       ___       ___       ___
   /\  \     /\  \     /\  \     /\  \
   \:\  \   /::\  \   /::\  \    \:\  \
   /::\__\ /::\:\__\ /\:\:\__\   /::\__\
  /:/\/__/ \:\:\/  / \:\:\/__/  /:/\/__/
  \/__/     \:\/  /   \::/  /   \/__/
             \/__/     \/__/
<BLANKLINE>
smkeyboard :
 ____  ____  ____  ____
||t ||||e ||||s ||||t ||
||__||||__||||__||||__||
|/__\||/__\||/__\||/__\|
<BLANKLINE>
smscript :
<BLANKLINE>
_|_  _  ,  _|_
 |  |/ / \_ |
 |_/|_/ \/  |_/
<BLANKLINE>
<BLANKLINE>
smshadow :
 |               |
  _|   -_) (_-<   _|
\__| \___| ___/ \__|
<BLANKLINE>
<BLANKLINE>
smslant :
  __             __
 / /_ ___   ___ / /_
/ __// -_) (_-</ __/
\__/ \__/ /___/\__/
<BLANKLINE>
<BLANKLINE>
speed :
_____               _____
__  /______ __________  /_
_  __/_  _ \__  ___/_  __/
/ /_  /  __/_(__  ) / /_
\__/  \___/ /____/  \__/
<BLANKLINE>
<BLANKLINE>
stampatello :
.          .
|- ,-. ,-. |-
|  |-' `-. |
`' `-' `-' `'
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
standard :
 _               _
| |_   ___  ___ | |_
| __| / _ \/ __|| __|
| |_ |  __/\__ \| |_
 \__| \___||___/ \__|
<BLANKLINE>
<BLANKLINE>
starwars :
.___________. _______      _______..___________.
|           ||   ____|    /       ||           |
`---|  |----`|  |__      |   (----``---|  |----`
    |  |     |   __|      \   \        |  |
    |  |     |  |____ .----)   |       |  |
    |__|     |_______||_______/        |__|
<BLANKLINE>
<BLANKLINE>
stellar :
  `..                     `..
  `..                     `..
`.`. `.   `..     `.... `.`. `.
  `..   `.   `.. `..      `..
  `..  `..... `..  `...   `..
  `..  `.            `..  `..
   `..   `....   `.. `..   `..
<BLANKLINE>
<BLANKLINE>
stop :
<BLANKLINE>
 _                  _
| |_    ____   ___ | |_
|  _)  / _  ) /___)|  _)
| |__ ( (/ / |___ || |__
 \___) \____)(___/  \___)
<BLANKLINE>
<BLANKLINE>
straight :
<BLANKLINE>
|_  _  _ |_
|_ (- _) |_
<BLANKLINE>
<BLANKLINE>
swan :
<BLANKLINE>
<BLANKLINE>
 .            .
_|_          _|_
 |   .-. .--. |
 |  (.-' `--. |
 `-' `--'`--' `-'
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
tanja :
  t)                     t)
t)tTTT                 t)tTTT
  t)   e)EEEEE  s)SSSS   t)
  t)   e)EEEE  s)SSSS    t)
  t)   e)           s)   t)
  t)T   e)EEEE s)SSSS    t)T
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
tengwar :
             .dP'
           dP'
<BLANKLINE>
`Yb.d888b   'Yb   .d888b.  `Yb.d888b
 88'    8Y   88   8'   `Yb  88'    8Y
 88     8P   88   Yb.   88  88     8P
 88   ,dP   .8P       .dP   88   ,dP
 88                 .dP'    88
 88               .dP'      88
.8P                        .8P
<BLANKLINE>
thick :
 w               w
w8ww .d88b d88b w8ww
 8   8.dP' `Yb.  8
 Y8P `Y88P Y88P  Y8P
<BLANKLINE>
<BLANKLINE>
thin :
<BLANKLINE>
|              |
|--- ,---.,---.|---
|    |---'`---.|
`---'`---'`---'`---'
<BLANKLINE>
<BLANKLINE>
threepoint :
_|_ _  __|_
 | (/__\ |
<BLANKLINE>
<BLANKLINE>
tinker-toy :
 o           o
 |           |
-o- o-o o-o -o-
 |  |-'  \   |
 o  o-o o-o  o
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
tombstone :
 ___ __,  _, ___
  |  |_  (_   |
  |  |   , )  |
  ~  ~~~  ~   ~
<BLANKLINE>
<BLANKLINE>
trek :
  dBBBBBBP     dBBBP   .dBBBBP  dBBBBBBP
                       BP
   dBP       dBBP      `BBBBb    dBP
  dBP       dBP           dBP   dBP
 dBP       dBBBBP    dBBBBP'   dBP
<BLANKLINE>
<BLANKLINE>
twopoint :
_|_ _ __|_
 | }__\ |
<BLANKLINE>
univers :
<BLANKLINE>
<BLANKLINE>
  ,d                              ,d
  88                              88
MM88MMM   ,adPPYba,  ,adPPYba,  MM88MMM
  88     a8P_____88  I8[    ""    88
  88     8PP"""""""   `"Y8ba,     88
  88,    "8b,   ,aa  aa    ]8I    88,
  "Y888   `"Ybbd8"'  `"YbbdP"'    "Y888
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
usaflag :
 :::==== :::===== :::===  :::====
 :::==== :::      :::     :::====
   ===   ======    =====    ===
   ===   ===          ===   ===
   ===   ======== ======    ===
<BLANKLINE>
<BLANKLINE>
weird :
<BLANKLINE>
 /              /
(___  ___  ___ (___
|    |___)|___ |
|__  |__   __/ |__
<BLANKLINE>
<BLANKLINE>
>>> tprint("test",font = "block243")
<BLANKLINE>
  _|                            _|
_|_|_|_|    _|_|      _|_|_|  _|_|_|_|
  _|      _|_|_|_|  _|_|        _|
  _|      _|            _|_|    _|
    _|_|    _|_|_|  _|_|_|        _|_|
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
>>> art_list()
100$
[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]
******************************
3
ᕙ༼ ,,ԾܫԾ,, ༽ᕗ
******************************
5
ᕙ༼ ,,இܫஇ,, ༽ᕗ
******************************
airplane1
 ‛¯¯٭٭¯¯(▫▫)¯¯٭٭¯¯’
******************************
airplane2
✈
******************************
angry face
(⋟﹏⋞)
******************************
angry2
( ͠° ͟ʖ ͡°)﻿
******************************
ankush
︻デ┳═ー*----*
******************************
arrow
»»---------------------►
******************************
atish
(| - _ - |)
******************************
awesome
<:3 )~~~
******************************
bagel
nln >_< nln
******************************
bear
ʕ•ᴥ•ʔ
******************************
bee
¸.·´¯`·¸¸.·´¯`·.¸.-<\^}0=:
******************************
big eyes
⺌∅‿∅⺌
******************************
big nose
˚∆˚
******************************
bird
 (⌒▽⌒)﻿
******************************
birds
~(‾▿‾)~
******************************
boobs
(.)(.)
******************************
boom box
♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪
******************************
bullshit
|3ᵕᶦᶦᶳᶣᶨᶵ
******************************
bunny
(\_/)
******************************
butterfly
Ƹ̵̡Ӝ̵̨̄Ʒ
******************************
car race
|[●▪▪●]|
******************************
care crowd
(-(-_(-_-)_-)-)
******************************
cassette
|[●▪▪●]|
******************************
cat face
⦿⽘⦿
******************************
cat smile
≧◔◡◔≦﻿
******************************
cat1
=^..^=
******************************
cat2
龴ↀ◡ↀ龴
******************************
caterpillar
,/\,/\,/\,/\,/\,/\,o
******************************
chair
╦╣
******************************
cheer
  ^(¤o¤)^
******************************
chess
♞▀▄▀▄♝▀▄
******************************
chess pieces
♚ ♛ ♜ ♝ ♞ ♟ ♔ ♕ ♖ ♗ ♘ ♙
******************************
cigarette
(____((____________()~~~
******************************
coffee
c[_]
******************************
cry
 (╯︵╰,)
******************************
crying
Ỏ̷͖͈̞̩͎̻̫̫̜͉̠̫͕̭̭̫̫̹̗̹͈̼̠̖͍͚̥͈̮̼͕̠̤̯̻̥̬̗̼̳̤̳̬̪̹͚̞̼̠͕̼̠̦͚̫͔̯̹͉͉̘͎͕̼̣̝͙̱̟̹̩̟̳̦̭͉̮̖̭̣̣̞̙̗̜̺̭̻̥͚͙̝̦̲̱͉͖͉̰̦͎̫̣̼͎͍̠̮͓̹̹͉̤̰̗̙͕͇͔̱͕̭͈̳̗̭͔̘̖̺̮̜̠͖̘͓̳͕̟̠̱̫̤͓͔̘̰̲͙͍͇̙͎̣̼̗̖͙̯͉̠̟͈͍͕̪͓̝̩̦̖̹̼̠̘̮͚̟͉̺̜͍͓̯̳̱̻͕̣̳͉̻̭̭̱͍̪̩̭̺͕̺̼̥̪͖̦̟͎̻̰_Ỏ̷͖͈̞̩͎̻̫̫̜͉̠̫͕̭̭̫̫̹̗̹͈̼̠̖͍͚̥͈̮̼͕̠̤̯̻̥̬̗̼̳̤̳̬̪̹͚̞̼̠͕̼̠̦͚̫͔̯̹͉͉̘͎͕̼̣̝͙̱̟̹̩̟̳̦̭͉̮̖̭̣̣̞̙̗̜̺̭̻̥͚͙̝̦̲̱͉͖͉̰̦͎̫̣̼͎͍̠̮͓̹̹͉̤̰̗̙͕͇͔̱͕̭͈̳̗̭͔̘̖̺̮̜̠͖̘͓̳͕̟̠̱̫̤͓͔̘̰̲͙͍͇̙͎̣̼̗̖͙̯͉̠̟͈͍͕̪͓̝̩̦̖̹̼̠̘̮͚̟͉̺̜͍͓̯̳̱̻͕̣̳͉̻̭̭̱͍̪̩̭̺͕̺̼̥̪͖̦̟͎̻̰
******************************
cthulhu
^(;,;)^
******************************
cute cat
^⨀ᴥ⨀^
******************************
dagger
cxxx|;:;:;:;:;:;:;:;>
******************************
decorate
▂▃▅▇█▓▒░۩۞۩        ۩۞۩░▒▓█▇▅▃▂
******************************
dice
[: :]
******************************
dog
ˁ˚ᴥ˚ˀ
******************************
dummy
<-|-'_'-|->
******************************
elephant
°j°m
******************************
eye closed
 (╯_╰)
******************************
eyes
℃ↂ_ↂↃ
******************************
face
•|龴◡龴|•
******************************
finger1
╭∩╮(Ο_Ο)╭∩╮
******************************
finger2
┌∩┐(◣_◢)┌∩┐
******************************
fish swim
¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
******************************
fish1
><(((('>
******************************
fish2
><>
******************************
formula1 car
\ō͡≡o˞̶
******************************
fox
-^^,--,~
******************************
fu
(ಠ_ಠ)┌∩┐
******************************
fuck you
nlm (-_-) mln
******************************
ghost
‹’’›(Ͼ˳Ͽ)‹’’›
******************************
glasses
-@-@-
******************************
glasses2
ᒡ◯ᵔ◯ᒢ
******************************
guitar
c====(=#O| ) ~~ ♬·¯·♩¸¸♪·¯·♫¸
******************************
gun
︻╦╤─
******************************
hairstyle
⨌⨀_⨀⨌
******************************
hal
@_'-'
******************************
happy
 ۜ\(סּںסּَ` )/ۜ
******************************
happy2
⎦˚◡˚⎣
******************************
head shot
->~∑≥_≤)
******************************
headphone
d[-_-]b
******************************
heart1
»-(¯`·.·´¯)->
******************************
heart2
♡
******************************
help
٩(͡๏̯͡๏)۶
******************************
homer
(_8(|)
******************************
house
__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___
******************************
hug me
(っ◕‿◕)っ
******************************
human
•͡˘㇁•͡˘
******************************
hybrix
ʕʘ̅͜ʘ̅ʔ
******************************
inlove
(✿ ♥‿♥)
******************************
killer
(⌐■_■)--︻╦╤─ - - - (╥﹏╥)
******************************
king
-_-
******************************
kirby
(つ -‘ _ ‘- )つ
******************************
kiss
(o'3'o)
******************************
knife
)xxxxx[;;;;;;;;;>
******************************
koala
@( * O * )@
******************************
kokain
 ̿ ̿' ̿'\̵͇̿̿\з=(•̪●)=ε/̵͇̿̿/'̿''̿ ̿
******************************
linqan
:Q___
******************************
looking face
ô¿ô
******************************
love in my eye
(♥_♥)
******************************
love you
»-(¯`·.·´¯)-><-(¯`·.·´¯)-«
******************************
mango
) _ _ __/°°¬
******************************
message1
(¯`·._.·(¯`·._.·  ·._.·´¯)·._.·´¯)
******************************
message2
,.-~*´¨¯¨`*·~-.¸-(-,.-~*´¨¯¨`*·~-.¸
******************************
metal
\m/_(>_<)_\m/
******************************
mis mujeres
(-(-_(-_-)_-)-)
******************************
monkey
@('_')@
******************************
monster
٩(̾●̮̮̃̾•̃̾)۶
******************************
monster2
٩(- ̮̮̃-̃)۶
******************************
mouse
----{,_,">
******************************
nathan
♪└(￣◇￣)┐♪└(￣◇￣)┐♪└(￣◇￣)┐♪
******************************
needle
|==|iiii|>-----
******************************
nope
t(-_-t)
******************************
nose
\˚ㄥ˚\
******************************
old lady boobs
|\o/\o/|
******************************
owlkin
(ᾢȍˬȍ)ᾢ ļ ļ ļ ļ ļ
******************************
panda
ヽ(￣(ｴ)￣)ﾉ
******************************
perky
( ๏ Y ๏ )
******************************
pig1
^(*(oo)*)^
******************************
pig2
༼☉ɷ⊙༽
******************************
ping pong
( •_•)O*¯`·.¸.·´¯`°Q(•_• )
******************************
pirate
✌(◕‿-)✌
******************************
pistols1
¯¯̿̿¯̿̿'̿̿̿̿̿̿̿'̿̿'̿̿̿̿̿'̿̿̿)͇̿̿)̿̿̿̿ '̿̿̿̿̿̿\̵͇̿̿\=(•̪̀●́)=o/̵͇̿̿/'̿̿ ̿ ̿̿
******************************
pistols2
̿' ̿'\̵͇̿̿\з=(◕_◕)=ε/̵͇̿̿/'̿'̿ ̿
******************************
professor
"""⌐(ಠ۾ಠ)¬"""
******************************
rak
/⦿L⦿\
******************************
rare
┌ಠ_ಠ)┌∩┐ ᶠᶸᶜᵏ♥ᵧₒᵤ
******************************
real face
( ͡° ͜ʖ ͡°)﻿
******************************
religious
☪ ✡ † ☨ ✞ ✝ ☥ ☦ ☓ ♁ ☩
******************************
robot1
d[ o_0 ]b
******************************
robot2
 c[○┬●]כ
******************************
rock on
\,,/(^_^)\,,/
******************************
rocket
∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===>
******************************
rope
╚(▲_▲)╝
******************************
rose1
--------{---(@
******************************
rose2
@}}>-----
******************************
sad1
ε(´סּ︵סּ`)з
******************************
sad2
(✖╭╮✖)
******************************
sat
'(◣_◢)'
******************************
scissors
✄
******************************
singing
d(^o^)b¸¸♬·¯·♩¸¸♪·¯·♫¸¸
******************************
sleeping
(-.-)Zzz...
******************************
sleeping baby
[{-_-}] ZZZzz zz z...
******************************
snail
'-'_@_
******************************
sniperstars
✯╾━╤デ╦︻✯
******************************
sorreh bro
(◢_◣)
******************************
sparkling heart
-`ღ´-
******************************
sperm
~~o
******************************
star in my eyes
<*_*>
******************************
stars
✌⊂(✰‿✰)つ✌
******************************
stars2
⋆ ✢ ✣ ✤ ✥ ✦ ✧ ✩ ✪ ✫ ✬ ✭ ✮ ✯ ✰ ★
******************************
sword1
(===||:::::::::::::::>
******************************
sword2
▬▬ι═══════ﺤ    -═══════ι▬▬
******************************
sword3
ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>
******************************
sword4
 |O/////[{:;:;:;:;:;:;:;:;>
******************************
table flip
(╯°□°）╯︵ ┻━┻
******************************
teddy
ˁ(⦿ᴥ⦿)ˀ
******************************
tron
(\/)(;,,;)(\/)
******************************
trumpet
-=iii=<()
******************************
ukulele
{ o }==(::)
******************************
umadbro
¯\_(ツ)_/¯
******************************
up
(◔/‿\◔)
******************************
upsidedown
( ͜。 ͡ʖ ͜。)
******************************
waves
°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸
******************************
weather
☼ ☀ ☁ ☂ ☃ ☄ ☾ ☽ ❄ ☇ ☈ ⊙ ☉ ℃ ℉ ° ❅ ✺ ϟ
******************************
what?
ة_ة
******************************
woman
▓⚗_⚗▓
******************************
worm
_/\__/\__0>
******************************
yolo
Yᵒᵘ Oᶰˡʸ Lᶤᵛᵉ Oᶰᶜᵉ
******************************
zable
ಠ_ರೃ
******************************
zombie
'º_º'
******************************
>>> aprint(artname = "awesame")
<:3 )~~~
>>> help_func()
              _
  __ _  _ __ | |_
 / _` || '__|| __|
| (_| || |   | |_
 \__,_||_|    \__|
<BLANKLINE>
<BLANKLINE>
        _     ____
__   __/ |   | ___|
\ \ / /| |   |___ \
 \ V / | | _  ___) |
  \_/  |_|(_)|____/ 
<BLANKLINE>
<BLANKLINE>
ASCII art is also known as "computer text art".
It involves the smart placement of typed special characters or
letters to make a visual shape that is spread over multiple lines of text.
Art is a Python lib for text converting to ASCII ART fancy.
<BLANKLINE>
Webpage : http://art.shaghighi.ir
<BLANKLINE>
Help :
<BLANKLINE>
     - list --> (list of arts)
<BLANKLINE>
     - fonts --> (list of fonts)
<BLANKLINE>
     - test --> (run tests)
<BLANKLINE>
     - text 'yourtext' 'font(optional)' --> (text art) Example : 'python -m art text exampletext block'
<BLANKLINE>
     - shape 'shapename' --> (shape art) Example : 'python -m art shape butterfly'
<BLANKLINE>
     - save 'yourtext' 'font(optional)'  -->  Example : 'python -m art save exampletext block'
<BLANKLINE>
     - all 'yourtext'  -->  Example : 'python -m art all exampletext'
>>> tprint('طط')
<BLANKLINE>
>>> random.seed(3)
>>> Art = art("random")
>>> Text = text2art("test","random")
>>> random.seed(9)
>>> Text2 = text2art("test","random")
>>> Art2 =  art("random")
>>> len(Art)!=len(Art2)
True
>>> len(Text)!=len(Text2)
True
>>> Data=art('assdsds')
Traceback (most recent call last):
        ...
art.art.artError: Invalid art name
>>> art("coffee")
'c[_] '
>>> tprint("test 2")
 _               _     ____
| |_   ___  ___ | |_  |___ \
| __| / _ \/ __|| __|   __) |
| |_ |  __/\__ \| |_   / __/
 \__| \___||___/ \__| |_____|
<BLANKLINE>
<BLANKLINE>
>>> tprint("aasdasdال",chr_ignore=True)
                        _                  _
  __ _   __ _  ___   __| |  __ _  ___   __| |
 / _` | / _` |/ __| / _` | / _` |/ __| / _` |
| (_| || (_| |\__ \| (_| || (_| |\__ \| (_| |
 \__,_| \__,_||___/ \__,_| \__,_||___/ \__,_|
<BLANKLINE>
<BLANKLINE>
>>> tprint("$2","block")
<BLANKLINE>
 .----------------.
| .--------------. |
| |    _____     | |
| |   / ___ `.   | |
| |  |_/___) |   | |
| |   .'____.'   | |
| |  / /____     | |
| |  |_______|   | |
| |              | |
| '--------------' |
 '----------------'
<BLANKLINE>
>>> tprint("salam\t","lcd")
<BLANKLINE>
              |
   -   -      +    -    |- -
   \  | |     |   | |   | | |
   -   --     -    --
<BLANKLINE>
<BLANKLINE>
>>> text2art("test",font = 2)
Traceback (most recent call last):
        ...
art.art.artError: font should have str type
>>> art("love_you",number=2,text=2)
Traceback (most recent call last):
        ...
art.art.artError: text should have str type
>>> Data=tsave("test file\nk",filename="test")
Saved!
Filename: test.txt
>>> Data["Message"]
'OK'
>>> Data["Status"]
True
>>> Data=tsave("test file\nk",filename="test.bw")
Saved!
Filename: test.bw
>>> Data["Message"]
'OK'
>>> Data["Status"]
True
>>> Data=tsave("test art")
Saved!
Filename: art.txt
>>> Data["Message"]
'OK'
>>> Data["Status"]
True
>>> Data=tsave("test art2")
Saved!
Filename: art2.txt
>>> Data["Message"]
'OK'
>>> Data["Status"]
True
>>> Data=tsave("test art3",print_status=False)
>>> Data["Message"]
'OK'
>>> Data["Status"]
True
>>> file=open("test.txt","r")
>>> data = file.read()
>>> (len(data)==282) or (len(data)==294)
True
>>> file=open("art.txt","r")
>>> data = file.read()
>>> (len(data)==246) or (len(data)==252)
True
>>> file=open("art2.txt","r")
>>> data = file.read()
>>> (len(data)==288) or (len(data)==294)
True
>>> file.close()
>>> Data=text2art(222)
Traceback (most recent call last):
        ...
art.art.artError: text should have str type
>>> text2art("seسسس",font=DEFAULT_FONT,chr_ignore=False)
Traceback (most recent call last):
        ...
art.art.artError: س is invalid
>>> Data=tsave(22,font=DEFAULT_FONT,filename="art",chr_ignore=True,print_status=True)
>>> Data["Message"]
"'int' object has no attribute 'split'"
>>> Data["Status"]
False
>>> tprint(22,font=DEFAULT_FONT,chr_ignore=True)
Traceback (most recent call last):
        ...
art.art.artError: text should have str type
>>> art(22,number=1,text="")
Traceback (most recent call last):
        ...
art.art.artError: artname shoud have str type
>>> aprint("woman",number="22",text="")
Traceback (most recent call last):
        ...
art.art.artError: number should have int type
>>> aprint("love_you",number=1,text="")
»-(¯`·.·´¯)-><-(¯`·.·´¯)-«
>>> os.remove("art.txt")
>>> os.remove("art2.txt")
>>> os.remove("art3.txt")
>>> os.remove("test.bw")
>>> os.remove("test.txt")

'''
