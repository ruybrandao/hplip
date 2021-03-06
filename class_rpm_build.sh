#!/bin/sh

rpm_dir=rpm_temp/buildroot
etc_dir=/etc/hp/
etc_rules=/etc/udev/rules.d/
usr_bin=/usr/bin
usr_lib_cups_filter=/usr/lib/cups/filter/
usr_share_cups=/usr/share/cups/drv/hp/
usr_share_models=/usr/share/hplip/data/models/
usr_share_ppd=/usr/share/ppd/HP/
usr_share_hplip=/usr/share/hplip/
ppd_hpcups=./ppd/classppd/hpcups
ppd_ps=./ppd/classppd/ps

mkdir -p $rpm_dir
mkdir -p $rpm_dir$etc_dir
mkdir -p $rpm_dir$etc_rules
mkdir -p $rpm_dir$usr_bin
mkdir -p $rpm_dir$usr_lib_cups_filter
mkdir -p $rpm_dir$usr_share_cups
mkdir -p $rpm_dir$usr_share_models
mkdir -p $rpm_dir$usr_share_ppd

cp -f ./hplip.conf $rpm_dir$etc_dir
cp -f ./data/rules/56-hpmud.rules $rpm_dir$etc_rules
#cp -f ./locatedriver $rpm_dir$usr_bin/hp-locatedriver
cp -f ./locatedriver $rpm_dir$usr_share_hplip
cp -f ./hpcups $rpm_dir$usr_lib_cups_filter
cp -f ./hpps $rpm_dir$usr_lib_cups_filter
cp -f ./prnt/drv/hpcups.drv $rpm_dir$usr_share_cups
cp -f ./data/models/models.dat $rpm_dir$usr_share_models

cp -f $ppd_hpcups/*.gz $rpm_dir$usr_share_ppd
cp -f $ppd_ps/*.gz $rpm_dir$usr_share_ppd

#cp -f hplipclassdriver.spec ./rpm_temp 


echo "rpm_dir is created with specific files" 

