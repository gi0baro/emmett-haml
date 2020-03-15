# Emmett-HAML

Emmett-HAML is an extension for the [Emmett framework](https://github.com/emmett-framework/emmett) providing an HAML like syntax for templates. This is not a template engine but a compiler which converts HAML files to HTML Renoir templates.

## Installation

You can install Emmett-HAML using pip:

    pip install emmett-haml

And add it to your Emmett application:

```python
from emmett_haml import Haml

app.use_extension(Haml)
```

## License

Emmett-HAML is released under BSD license. Check the LICENSE file for more details.
