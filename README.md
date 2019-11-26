# Emmett-Haml

Emmett-Haml is an extension for the [Emmett framework](http://github.com/emmett-framework/emmett) providing an Haml like syntax for templates. This is not a template engine but a compiler which converts haml files to html Renoir templates.

## Installation

You can install Emmett-Haml using pip:

    pip install emmett-haml

And add it to your Emmett application:

```python
from emmett_haml import Haml

app.use_extension(Haml)
```

## License

Emmett-Haml is released under BSD license. Check the LICENSE file for more details.
