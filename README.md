### Setup Guidelines
---

##### For Vagrant Users
-----
If you use Vagrantfile in this repository, please follow the instructions below:

1. Make sure the following version of Vagrant and Virtual Box was installed.

| Tables        | Link           |Version           |
| ------------- |:-------------:|:-------------:| 
| Vagrant      | https://www.vagrantup.com/downloads.html | 2.2.6 | 
| Virtualbox      | https://www.virtualbox.org/wiki/Download_Old_Builds_6_0      | 6.0.16 |

2. After running `vagrant up`, make sure the version `python` and `sqlite3` was updated:
 
```sh
$ vagrant up
$ vagrant ssh
# python version : 3.6
$ python --version
# sqlite3 version : 3.29.0
$ sqlite3 --version
```
If the version was not updated, run `vagrant provision`.

3. Lastly, the latest version of sqlite3 was correctly loaded in python:

```sh
$ python
>>> import sqlite3
>>> sqlite3.sqlite_version
#do not use sqlite3.version!!
```

If the version was not updated, load `~/.bashshrc` by running `source ~/.bashshrc` after accessing varant through `vagrant ssh`.

##### For Every User
-----
You can run the app by `python manage.py runserver`:

```bash
cd path/to/root/directory
python manage.py runserver 0:8000
```

Access to http://192.168.33.11:8000/ and check if the app is running successfully.
