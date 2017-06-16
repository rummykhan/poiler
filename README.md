# Poiler

This is my Python Boiler Plate for writing console apps.

### How To

1. Clone this repository.
2. Goto `config` directory rename `config.example.json` to `config.json`.
3. Update `config/config.json`
4. In Console run python main.py --app

### Reason for the Repository.

I've been writing lot of Python CLI apps for different purposes, each time I've to manually copy paste the boiler plate and carry on. So I thought of creating a repository. Maybe someday someone else would find it useful. 

I've added helpful classes in `base/support/` directory which I hope you'll find useful.

1. <a href="https://github.com/rummykhan/poiler/blob/master/base/support/collection.py">Collection (For Querying on List of Dictionary.)</a>
2. <a href="https://github.com/rummykhan/poiler/blob/master/base/support/command.py">Command (For user interaction and priting.)</a>
3. <a href="https://github.com/rummykhan/poiler/blob/master/base/support/dict.py">Dict (Walking recursively over a Dictionary.)</a>
4. <a href="https://github.com/rummykhan/poiler/blob/master/base/support/map.py">Map (A Simple Dictionary To access Dictionary as Object e.g. `person.name`.)</a>
5. <a href="https://github.com/rummykhan/poiler/blob/master/base/support/str.py">Str (Multiple String Helpers.)</a>
6. <a href="https://github.com/rummykhan/poiler/blob/master/base/support/time.py">Time (A Complete Time Utility Inspired from Carbon.)</a>

There is logger class for displaying log info on CLI, This logger class is somewhat similar to <a href="http://www.php-fig.org/psr/psr-3/">PSR-3 Logger</a>


### Easy Config
Now you can specify your configuration in a JSON File. See <a href="https://github.com/rummykhan/poiler/blob/master/config/config.example.json">config.example.json</a>

I've already included a <a href="https://github.com/rummykhan/poiler/blob/master/config/config.py">`Config Class`</a> in `config/` directory which will helps you to read JSON configuration files.

This `Config Class` expose a static method `get(path)`. Which is pretty intelligent to read your configuration recursively.

### Not a framework

This is not a python framework for writing console apps. There are already plenty of pretty amazing and popular framework outside.
e.g.
1. <a href="http://builtoncement.com/">Cement</a>
2. <a href="https://pypi.python.org/pypi/clint/">Clint</a>
3. <a href="http://click.pocoo.org/5/">Click</a>
4. <a href="http://docopt.org/">Docopt</a>
5. <a href="https://pypi.python.org/pypi/plac">Plac</a>
6. <a href="https://docs.openstack.org/developer/cliff/">Cliff</a>

### Inspired From Laravel

Since I've been coding in PHP/Laravel for more then One and Half an Year, So it's natural that you'll see glitters of Laravel Inside.


### Contact
rehan_manzoor@outlook.com