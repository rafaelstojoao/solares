# -*- coding: utf-8 -*-
"""
======================================
Searching and downloading from the VSO
======================================

How to download data from the VSO with Fido.
"""
import astropy.units as u
from sunpy.net import Fido, attrs as a

###############################################################################
# `Fido <sunpy.net.fido_factory.UnifiedDownloaderFactory>` is the primary
# interface to search for and download data and
# will search the VSO when appropriate. The following example searches for all
# SOHO/EIT images between the times defined below by defining
# a timerange (`~sunpy.net.attrs.Time`) and
# the instrument (`~sunpy.net.attrs.Instrument`).
attrs_time = a.Time('2020/02/01 00:10', '2020/02/01 00:11')
result = Fido.search(attrs_time, a.Instrument('aia'))
downloaded_files = Fido.fetch(result)
downloaded_files = Fido.fetch(result, path='Data/res.txt')
###############################################################################
# Let's inspect the results.
print(result)

###############################################################################
# The following shows how to download the results. If we
# don't provide a path it will download the file into the sunpy data directory.
# The output provides the path of the downloaded files.

##downloaded_files = Fido.fetch(result)
##print(downloaded_files)

###############################################################################
# More complicated queries can be constructed by using relational operators.
# For example, it is possible to query two wavelengths at the same time with
# the OR operator (|).
##result = Fido.search(a.Time('2012/03/04 00:00', '2012/03/04 00:02'),
  ##                   a.Instrument('aia'),
    ##                 a.Wavelength(171*u.angstrom) | a.Wavelength(94*u.angstrom))
##print(result)

#
#
#
# VSO Keyword Lookup : INSTRUMENT
# Known Instruments
#
# This list contains the common name of current (and possibly in development) instruments that VSO can search on. More information about each instrument may be found within the VSO Registry. User Interface programmers should note that some names may be encoded as UTF-8.
#
# 512-CHANNEL MAGNETOGRAPH
#     512-channel Magnetograph
# 60-FT SHG
#     60-foot Tower Spectroheliograph
# AIA
#     Atmospheric Imaging Assembly
# BCS
#     Bragg Crystal Spectrometer
# BIG BEAR
#     Big Bear Solar Observatory, California TON and GONG+ sites
# CDS
#     Coronal Diagnostic Spectrometer
# CELIAS
#     Charge, Element, and Isotope Analysis System
# CERRO TOLOLO
#     Cerro Tololo, Chile GONG+ site
# CFDT1
#     Cartesian Full-Disk Telescope No.1
# CFDT2
#     Cartesian Full-Disk Telescope No.2
# CHP
#     Chromospheric Helium-I Imaging Photometer
# CHROTEL
#     Chromospheric Telescope
# CLIMSO
#     Christian Latouche IMageur SOlaire
# COSTEP
#     Comprehensive Suprathermal and Energetic Particle Analyzer
# CP
#     Coronagraph/Polarimeter
# DPM
#     Digital Prominence Monitor
# EIS
#     EUV Imaging Spectrometer
# EIT
#     Extreme ultraviolet Imaging Telescope
# EL TEIDE
#     Canary Islands GONG+ site
# ERNE
#     Energetic and Relativistic Nuclei and Electron experiment
# EVE
#     Extreme Ultraviolet Variability Experiment
# FOXSI
#     Focusing Optics X-ray Solar Imager
# GOLF
#     Global Oscillations at Low Frequencies
# HI-C
#     High Resolution Coronal Imager (193 A)
# HI-C21
#     High Resolution Coronal Imager 2.1 (172 A)
# HMI
#     Helioseismic and Magnetic Imager
# HXECLIPSE
#     UCAR HAO Historical Eclipse Archive
# HXT
#     Hard X-Ray Telescope
# IMPACT
#     In-situ Measurements of Particles and CME Transients
# IRIS
#     Interface Region Imaging Spectrograph
# ISOON
#     Improved Solar Observing Optical Network
# KHPI
#     Kanzelhöhe Hα Patrol Instrument
# LASCO
#     Large Angle and Spectrometric Coronagraph
# LEARMONTH
#     Australian GONG+ site
# LONGWAVE-LOBE-06
#     Full longwave EUV observation of Sun with EUNIS (2006 flight)
# LONGWAVE-LOBE-07
#     Full longwave EUV observation of Sun with EUNIS (2007 flight)
# LONGWAVE-SLIT-06
#     Full longwave EUV observation of Sun with EUNIS (trimmed/2006 flight)
# LONGWAVE-SLIT-07
#     Full longwave EUV observation of Sun with EUNIS (trimmed/2007 flight)
# LYRA
#     LYman alpha RAdiometer
# MAUNA LOA
#     Hawai'ian GONG+ site
# MDI
#     Michelson Doppler Imager
# MK3
#     Mk. III coronagraph
# MK4
#     Mk. IV coronagraph
# MOF/60
#     Mt. Wilson 60-Foot Tower Telescope
# MOTH
#     Magneto Optical filters at Two Heights
# O-SPAN
#     O-SPAN (formerly known as ISOON)
# OVSA
#     Owens Valley Solar Array
# PHOENIX
#     PHOENIX detector on flight #3 of FOXSI
# PLASTIC
#     PLasma And SupraThermal Ion Composition
# PSPT
#     Precision Solar Photometric Telescope
# RHESSI
#     Reuven Ramaty High Energy Solar Spectroscopic Imager
# SECCHI
#     Sun Earth Connection Coronal and Heliospheric Investigation
# SHORTWAVE-LOBE-06
#     Shortwave EUV observation of Sun with EUNIS (2006 flight)
# SHORTWAVE-LOBE-07
#     Shortwave EUV observation of Sun with EUNIS (2007 flight)
# SHORTWAVE-SLIT-06
#     Shortwave EUV observation of Sun with EUNIS (trimmed/2006 flight)
# SHORTWAVE-SLIT-07
#     Shortwave EUV observation of Sun with EUNIS (trimmed/2007 flight)
# SJ
#     Slit-Jaw
# SOLAR FTS SPECTROMETER
#     Solar FTS Spectrometer
# SOT
#     Solar Optical Telescope
# SP1
#     Spectropolarimeter1
# SP2
#     Spectropolarimeter2
# SPECTROHELIOGRAPH
#     SpectroHeliograph
# SPECTROMAGNETOGRAPH
#     SpectroMagnetograph
# SUMER
#     Solar Ultraviolet Measurements of Emitted Radiation
# SWAN
#     Solar Wind Anisotropies
# SWAP
#     Sun Watcher using Active pixel system detector and image Processing
# SWAVES
#     STEREO/WAVES
# SXI-0
#     Solar X-ray Imager
# SXT
#     Soft X-Ray Telescope
# TENERIFE
#     Canary Islands TON site
# TRACE
#     Transition Region And Coronal Explorer
# UDAIPUR
#     Indian GONG+ site
# UVCS
#     Ultraviolet Coronagraph Spectrometer
# VAULT-1999
#     Very High Angular Resolution Ultraviolet Telescope (1999 flight)
# VAULT-2002
#     Very High Angular Resolution Ultraviolet Telescope (2002 flight)
# VAULT-2014
#     Very High Angular Resolution Ultraviolet Telescope (2014 flight)
# VIRGO
#     Variability of Solar Irradiance and Gravity Oscillations
# VSM
#     Vector SpecroMagnetograph
# WBS
#     Wide Band Spectrometer
# WISPR
#     Wide-Field Imager for Solar Probe Plus
# XRT
#     X-Ray Telescope
#
# Help us improve VSO: Tell us what features you would like to see.
#
# Other Comments? Then please contact us.
# VSO @ Home | NSO | Stanford
# Valid XHTML 1.1! Automatically Generated at :Fri Mar 6 10:57:26 2020
