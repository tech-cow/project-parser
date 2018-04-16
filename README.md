<h3 style="text-align:center;font-weight: 300;" align="center">
  <img src="/img/banner.jpg" width="450px">
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/badge/downloads-0k-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/badge/build-passing-yellow.svg?style=flat-square">
</p>


> In order to showcase my github project on my portfolio, this script is intended to grab necessary data and export them as a JSON file using the Github REST API.

## External Libraries

Third Party libraries are used in this project

| Package           |   Description |
| ------------- |:-------------:|
| `pygithub`     |  Github RESTful API Python's Framwork  |

## Getting Started

The user needs to have Terminal/Bash installed, Python version in this project is 3.0+.

### Run

🐍 Python3

```bash
$ python3 parser.py
```

### Code Walkthrough

In `class Block`: Creating a Block data structure that takes a few args including index, timestamp, a random data that could be anything and most importantly, a previous hash that the newly created block can build upon.

```python
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """
        Function Explain.
        hash.update(arg) :Update the hash object with the string arg.
        hash.hexdigest(arg) : Return the digest of the strings passed to the
        update() method so far containing only hexadecimal digits.
        """
        sha = hasher.sha256()
        sha.update(str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash))
        return sha.hexdigest()
```







<!-- ## Demo -->
<!-- The blockchain application prints out each hash along with a relative index. -->

<!-- ![Demo](md_assets/demo.png) -->


## License

🌱 MIT 🌱

---

> ![home](http://yuzhoujr.com/emoji/home.svg) [yuzhoujr.com](http://www.yuzhoujr.com) &nbsp;&middot;&nbsp;
> ![github](http://yuzhoujr.com/emoji/github.svg)  [@yuzhoujr](https://github.com/yuzhoujr) &nbsp;&middot;&nbsp;
> ![linkedin](http://yuzhoujr.com/emoji/linkedin.svg)  [@yuzhoujr](https://linkedin.com/in/yuzhoujr)
