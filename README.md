# elit-sdk-python

This repository is the elit SDK for python language. Your NLP tools implemented the abstract class and method of this SDK can be hosted on [elit.cloud](https://elit.cloud).

## Get Started

The minimum required version of python is python 3.  

### Install

```bash
pip install elitsdk
```

### Example Usage:

```python
from elitsdk.sdk import ElitSDK


class Example(ElitSDK):
    def __init__(self):
        super()
    
    def decode(self, input_data, *args, **kwargs):
        pass
     
    def load_model(self, model_root):
        pass
```

