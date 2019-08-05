# pptxcom
Python library for creating, editing, and controlling Microsoft's PowerPoint presentation software. At the moment this repository will contain a collection of classes, functions, and constants to accomplish various tasks in PowerPoint using Python. The future library will begin evolving from those pieces of code over time.

## Getting Started
### Installing
`pip install git+https://github.com/leakydata/pptxcom`

#### Grab an active PowerPoint application instance and create an object from it:
```Python
import pptxcom as pt
PPT = pt.active_app()
```

#### Grab an active PowerPoint application instance and create a presentation object from it:
```Python
import pptxcom as pt
Pres = pt.active_pres()
```

#### Open an existing PowerPoint presentation and create an object from it:
```Python
import pptxcom as pt
Pres = pt.open_pres(r'C:\path\to\file.pptx') 
```

## Built With
* [pywin32](https://github.com/mhammond/pywin32) - Python for Windows (pywin32) Extensions

## Authors
* Nathan Jones

## Contributing
Please read [CONTRIBUTING.md](https://github.com/leakydata/pptxcom/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](https://github.com/leakydata/pptxcom/blob/master/LICENSE) file for details

## Acknowledgements
* Thank you to [Mark Hammond](https://github.com/mhammond) for his work on the [pywin32](https://github.com/mhammond/pywin32) module.
* Thank you to anybody whose code I've used.
