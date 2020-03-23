#!/usr/bin/env python3

import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--weights', action="store", dest='WEIGHTS', default=os.environ.get('PREDIX_WEIGHTS'), help='Path to weights file')
parser.add_argument('--dosages', action="store", dest='DOSAGES', default=os.environ.get('PREDIX_DOSAGES'), help='Path to dosage directory')
parser.add_argument('--samples', action="store", dest='SAMPLES', default=os.environ.get('PREDIX_SAMPLES'), help='Path to samples file')
parser.add_argument('--output_prefix', action="store", dest='OUTPUT_PREFIX', default=os.environ.get('PREDIX_OUTPUT'), help='File prefix for output files')

args = parser.parse_args()

if args.WEIGHTS and args.DOSAGES and args.SAMPLES and args.OUTPUT_PREFIX:
    subprocess.call(
    ['./PrediXcan.py',
    '--predict',
    '--weights',
    args.WEIGHTS,
    '--dosages',
    args.DOSAGES,
    '--samples',
    args.SAMPLES,
    '--output_prefix',
    args.OUTPUT_PREFIX])
else:
    print(str(args.WEIGHTS) + '\n' + str(args.DOSAGES) + '\n' + str(args.SAMPLES) + '\n' + str(args.OUTPUT_PREFIX))
