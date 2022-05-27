import babilib
from multiprocessing import Pool

hosts_babild = ['shd01']
hosts_babies = [{'server':'shvmie10','efn':107}, {'server':'shvmie11','efn':108}, {'server':'shdia01','efn':99},{'server':'shvmif6','efn':110}]
hosts_mpv = ['shmpv03','shmpv07','shmpv09','shmpv12','shmpvs1','shmpvb3f','brmpv01']
#hosts_mpv = ['shmpv03']

def restart_babies_v1740():
	babilib.execarg('atcat02','((cd /home/daq/daqconfig/atcat02 && ./restartdaq_phys.sh >> log.txt &))')

def rst_babild(host):
	babilib.restart_babild(host)

def rst_babies(host):
	babilib.restart_babies(host['server'],host['efn'])

def rst_mpv(host):
	babilib.restart_mpvbabildes(host)

if __name__ == '__main__':
	#p1 = Pool(len(hosts_babild))
	#p1.map(rst_babild, hosts_babild)
	#p2 = Pool(len(hosts_babies))
	#p2.map(rst_babies, hosts_babies)
	#p3 = Pool(len(hosts_mpv))
	#p3.map(rst_mpv, hosts_mpv)
	for host in hosts_babild:
		babilib.restart_babild(host)
	for host in hosts_babies:
		babilib.restart_babies(host['server'],host['efn'])
	for host in hosts_mpv:
		babilib.restart_mpvbabildes(host)
	#restart_babies_v1740()
	