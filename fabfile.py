from __future__ import with_statement
from fabric.api import *
import time

packages = {
    'pip':[
        'python-dateutil==1.5',
        'feedparser==5.1',
        'raven==1.4.6',
        'pyyaml',
        '-U distribute',
        'nltk',
        'numpy',
    ],
	    'apt-get':[
        'python-dev',
        'python-memcache',
    ]
}


def package_setup():
    for p in packages['pip']:
        local('pip install %s' % p) 

def _update_deployment_timestamp():
    import fileinput
    for line in fileinput.input('settings.py', inplace=1):
        if line.startswith('DEPLOYMENT_TIMESTAMP'):
            print 'DEPLOYMENT_TIMESTAMP = %i \n' % int(time.time()),
        else:
            print line,

def runcommand():
#    with settings(warn_only=True):
#        run('rm /usr/share/nltk_data -r')
#    run('mkdir /usr/share/nltk_data')
#    run("python -c \"import nltk;nltk.download('brown', download_dir='/usr/share/nltk_data')\"")
    pass

def prod():
    env.hosts = ['root@ml.prod.corporate.01']

def deploy(install_packages=False):
    if install_packages:
        for package in packages['apt-get']:
            run('apt-get install %s' % package)
        for package in packages['pip']:
            run('pip install %s' % package)

    with cd('/usr/local/metaLayer-metalayerdotcom/metalayerdotcom'):
        run("git pull")
        run("git submodule init && git submodule update")
        run("git status")
    with settings(warn_only=True):
        run("service apache2 restart")

def git():
    _update_deployment_timestamp()
    for dir in ['.']: #'compressor', 'chargifyapi', 'metalayercore'
        with settings(warn_only=True):
            local('cd /home/griff/code/metaLayer/metalayerdotcom/%s && git add --all && git commit' % dir)
            local('cd /home/griff/code/metaLayer/metalayerdotcom/%s && git push' % dir)
