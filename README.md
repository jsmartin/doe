Function:

Find all the pesky orphaned EBS volumes across your account and delete them.  Orphaned volumes are defined as those that have a status of "available" and have no tags.  If you have additional criteria, alter the conditional.

Usage:

	Usage: doe.py [options]
	
	Options:
	  -h, --help    show this help message and exit
	  -d, --delete  Delete orphaned instances
	  

Example Output	  
 
	doe.py --delete
	
	Zone: us-east-1
	Total: 547 Orphaned: 536
	
	Zone: us-west-2
	Total: 0 Orphaned: 0
	
	Zone: us-west-1
	Total: 0 Orphaned: 0
	
	Zone: eu-west-1
	Total: 0 Orphaned: 0
	
	Zone: eu-central-1
	Total: 0 Orphaned: 0
	
	Zone: ap-southeast-1
	Total: 0 Orphaned: 0
	
	Zone: ap-southeast-2
	Total: 0 Orphaned: 0
	
	Zone: ap-northeast-1
	Total: 0 Orphaned: 0
	
	Zone: sa-east-1
	Total: 0 Orphaned: 0


	Deleting EBS orphan vol-0bb2ff4e RegionInfo:us-east-1