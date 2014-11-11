#! /usr/bin/env python

import boto.ec2
from optparse import OptionParser
import sys


def get_volumes(conn):
    orphaned = []
    if not conn:
        return [], 0
    volumes = conn.get_all_volumes()
    for vol in volumes:
        if vol.status == "available" and vol.tags == {} :
            orphaned.append(vol)

    return orphaned, len(volumes)


parser = OptionParser()
parser.add_option("-d", "--delete",
                  action="store_true", dest="delete", default=False,
                  help="Delete orphaned instances")

(options, args) = parser.parse_args()


zones= [ "us-east-1", "us-west-2", "us-west-1", "eu-west-1", "eu-central-1", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "sa-east-1"]

orphaned_space_total = 0
total_orphaned = []
total_vols = 0

for zone in zones:
    print "\nZone:", zone
    conn = boto.ec2.connect_to_region(zone)
    (zone_orphaned, zone_total_vols) = get_volumes(conn)
    print "Total:", zone_total_vols, "Orphaned:", len(zone_orphaned)
    total_orphaned += zone_orphaned
    total_vols += zone_total_vols


for vol in total_orphaned:
    orphaned_space_total += vol.size

print "\n\nTotal Volumes:", total_vols
print "Total Orphaned:", len(total_orphaned)
print "Orphaned Space:", orphaned_space_total, " GB"

if options.delete:
    print "\n"
    for vol in total_orphaned:
        print "Deleting EBS orphan", vol.id, vol.region
        vol.delete()
