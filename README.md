# Nairobi Arch Linux User Registry

A registry of [Arch Linux](https://www.archlinux.org/) users in Nairobi, Kenya.  Written in Django cuz:

`┬─┬ ノ( ゜-゜ノ)`

## Try it
It's easiest if you use Python's virtualenv (with [wrapper extensions](https://bitbucket.org/dhellmann/virtualenvwrapper)):

*Create and prepare a virtual env*:

```
mkvirtualenv -p `which python2` archlinuxke
pip install django
```

*Clone the repo*:

```
git clone https://github.com/nairobilug/archregistrynbo.git
```

*Run it*:

```
cd archregistrynbo
python manage.py runserver
```

*Bob's your uncle*:
http://localhost:8000
