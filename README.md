# Poiler

This is my Python Boiler Plate for writing console apps.

### How To

1. Clone this repository.
2. Goto `config` directory rename `config.example.json` to `config.json`.
3. Update `config/config.json`
4. Add your arguments in `route/Router.py`
5. Add your controller in `controller/` Directory.
6. Add associations between routes and controller in `main.py`
6. In Console run python main.py --app

### Reason for the Repository.

I've been writing lot of Python CLI apps for different purposes, each time I've to manually copy paste the boiler plate and carry on. So I thought of creating a repository. Maybe someday someone else would find it useful. 

I've added helpful classes in `base/support/` directory which I hope you'll find useful.

1. [Collection (For Querying on List of Dictionary.)](https://github.com/rummykhan/poiler/blob/master/base/support/collection.py)</a>
2. [Command (For user interaction and priting.)](https://github.com/rummykhan/poiler/blob/master/base/support/command.py)
3. [Dict (Walking recursively over a Dictionary.)](https://github.com/rummykhan/poiler/blob/master/base/support/dict.py)
4. [Map (A Simple Dictionary To access Dictionary as Object e.g. `person.name`.)](https://github.com/rummykhan/poiler/blob/master/base/support/map.py)
5. [Str (Multiple String Helpers.)](https://github.com/rummykhan/poiler/blob/master/base/support/str.py)
6. [Time (A Complete Time Utility Inspired from Carbon.)](https://github.com/rummykhan/poiler/blob/master/base/support/time.py)

There is logger class for displaying log info on CLI, This logger class is somewhat similar to <a href="http://www.php-fig.org/psr/psr-3/">PSR-3 Logger</a>


### Easy Config
Now you can specify your configuration in a JSON File. See <a href="https://github.com/rummykhan/poiler/blob/master/config/config.example.json">config.example.json</a>

I've already included a <a href="https://github.com/rummykhan/poiler/blob/master/config/config.py">`Config Class`</a> in `config/` directory which will helps you to read JSON configuration files.

This `Config Class` expose a static method `get(path)`. Which is pretty intelligent to read your configuration recursively.

### Not a framework

This is not a python framework for writing console apps. There are already plenty of pretty amazing and popular framework outside.
e.g.
1. [Cement](http://builtoncement.com/)
2. [Clint](https://pypi.python.org/pypi/clint/)
3. [Click](http://click.pocoo.org/5/)
4. [Docopt](http://docopt.org/)
5. [Plac](https://pypi.python.org/pypi/plac)
6. [Cliff](https://docs.openstack.org/developer/cliff/)

### Inspired From Laravel

Since I've been coding in PHP/Laravel for more then one and half  years, So it's natural that you'll see glitters of Laravel Inside.


### Contact
[rehan_manzoor@outlook.com](mailto://rehan_manzoor@outlook.com)